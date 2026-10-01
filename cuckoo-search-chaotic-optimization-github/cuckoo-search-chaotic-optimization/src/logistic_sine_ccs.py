import math
import numpy as np


def levy_flight(beta=1.5, dim=2, rng=None):
    rng = np.random.default_rng() if rng is None else rng
    numerator = math.gamma(1 + beta) * math.sin(math.pi * beta / 2)
    denominator = (
        math.gamma((1 + beta) / 2)
        * beta
        * 2 ** ((beta - 1) / 2)
    )
    sigma = (numerator / denominator) ** (1 / beta)
    u = rng.normal(0, sigma, dim)
    v = rng.normal(0, 1, dim)
    return u / (np.abs(v) ** (1 / beta))


def logistic_sine_map(x, r=0.86):
    return (
        r * x * (1.0 - x)
        + ((4.0 - r) / 4.0) * math.sin(math.pi * x)
    ) % 1.0


def ls_ccs(
    obj_func,
    n=25,
    dim=2,
    lb=0.0,
    ub=np.pi,
    pa=0.25,
    max_iter=300,
    beta=1.5,
    seed=0.3,
    elitism_keep=2,
    r=0.86,
    random_seed=42,
):
    """Logistic-Sine Chaotic Cuckoo Search (LS-CCS).

    The structure follows the documented project pseudocode:
    chaotic initialization, dynamic chaotic step size, Lévy flights,
    chaotic abandonment, and elitism.
    """
    rng = np.random.default_rng(random_seed)

    cv = seed
    nests = np.zeros((n, dim))
    for i in range(n):
        for d in range(dim):
            cv = logistic_sine_map(cv, r)
            nests[i, d] = lb + (ub - lb) * cv

    fitness = np.array([obj_func(x) for x in nests])
    best_idx = np.argmin(fitness)
    best_nest = nests[best_idx].copy()
    best_fitness = float(fitness[best_idx])

    ca = seed
    convergence = []

    for _ in range(max_iter):
        ca = logistic_sine_map(ca, r)
        alpha = 2.0 * ca

        elite_indices = np.argsort(fitness)[:elitism_keep]
        elite_nests = nests[elite_indices].copy()
        elite_fitness = fitness[elite_indices].copy()

        for i in range(n):
            step = levy_flight(beta, dim, rng)
            new_nest = np.clip(
                nests[i] + alpha * step,
                lb,
                ub,
            )
            j = rng.integers(0, n)
            new_fitness = obj_func(new_nest)

            if new_fitness < fitness[j]:
                nests[j] = new_nest
                fitness[j] = new_fitness

        n_abandon = max(1, int(pa * n))
        worst_indices = np.argsort(fitness)[-n_abandon:]

        for idx in worst_indices:
            for d in range(dim):
                cv = logistic_sine_map(cv, r)
                nests[idx, d] = lb + (ub - lb) * cv
            fitness[idx] = obj_func(nests[idx])

        for k in range(elitism_keep):
            worst_pos = np.argmax(fitness)
            if elite_fitness[k] < fitness[worst_pos]:
                nests[worst_pos] = elite_nests[k]
                fitness[worst_pos] = elite_fitness[k]

        best_idx = np.argmin(fitness)
        if fitness[best_idx] < best_fitness:
            best_fitness = float(fitness[best_idx])
            best_nest = nests[best_idx].copy()

        convergence.append(best_fitness)

    return best_nest, best_fitness, convergence


if __name__ == "__main__":
    from benchmark_functions import michalewicz

    best, fitness, convergence = ls_ccs(michalewicz)
    print("Best position:", best)
    print("Best fitness:", fitness)
