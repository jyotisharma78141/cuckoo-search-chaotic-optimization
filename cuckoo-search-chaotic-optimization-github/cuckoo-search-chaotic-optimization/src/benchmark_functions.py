import numpy as np


def michalewicz(x, m=10):
    x = np.asarray(x)
    i = np.arange(1, len(x) + 1)
    return -np.sum(np.sin(x) * np.sin(i * x**2 / np.pi) ** (2 * m))


def sphere(x):
    x = np.asarray(x)
    return np.sum(x**2)


def rastrigin(x):
    x = np.asarray(x)
    n = len(x)
    return 10 * n + np.sum(x**2 - 10 * np.cos(2 * np.pi * x))


def ackley(x):
    x = np.asarray(x)
    n = len(x)
    s1 = np.sum(x**2)
    s2 = np.sum(np.cos(2 * np.pi * x))
    return -20 * np.exp(-0.2 * np.sqrt(s1 / n)) - np.exp(s2 / n) + 20 + np.e


def griewank(x):
    x = np.asarray(x)
    i = np.arange(1, len(x) + 1)
    return np.sum(x**2) / 4000 - np.prod(np.cos(x / np.sqrt(i))) + 1


BENCHMARKS = {
    "Michalewicz-2D": (michalewicz, 2, 0.0, np.pi),
    "Sphere-10D": (sphere, 10, -5.12, 5.12),
    "Rastrigin-10D": (rastrigin, 10, -5.12, 5.12),
    "Ackley-10D": (ackley, 10, -32.768, 32.768),
    "Griewank-10D": (griewank, 10, -600.0, 600.0),
}
