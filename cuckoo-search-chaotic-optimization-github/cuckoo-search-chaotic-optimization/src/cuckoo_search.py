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
    sigma_u = (numerator / denominator) ** (1 / beta)

    u = rng.normal(0, sigma_u, dim)
    v = rng.normal(0, 1, dim)

    return u / (np.abs(v) ** (1 / beta))


def cuckoo_search(
    obj_func,
    n=25,
    dim=2,
    lb=0.0,
    ub=np.pi,
    pa=0.25,
    max_iter=300,
    alpha=1.0,
    beta=1.5,
    seed=42,
):
    """Standard Cuckoo Search based on the project methodology.

    Returns:
        best_nest, best_fitness, convergence
    """
    rng = np.random.default_rng(seed)
    nests = rng.uniform(lb, ub, size=(n, dim))
    fitness = np.array([obj_func(x) for x in nests])

    best_idx = np.argmin(fitness)
    best_nest = nests[best_idx].copy()
    best_fitness = float(fitness[best_idx])
    convergence = []

    for _ in range(max_iter):
        # Lévy-flight solution generation
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

        # Abandon a fraction of nests and create new random nests
        n_abandon = max(1, int(pa * n))
        worst_indices = np.argsort(fitness)[-n_abandon:]

        for idx in worst_indices:
            nests[idx] = rng.uniform(lb, ub, dim)
            fitness[idx] = obj_func(nests[idx])

        best_idx = np.argmin(fitness)
        if fitness[best_idx] < best_fitness:
            best_fitness = float(fitness[best_idx])
            best_nest = nests[best_idx].copy()

        convergence.append(best_fitness)

    return best_nest, best_fitness, convergence


if __name__ == "__main__":
    from benchmark_functions import michalewicz

    best, fitness, convergence = cuckoo_search(michalewicz)
    print("Best position:", best)
    print("Best fitness:", fitness)
