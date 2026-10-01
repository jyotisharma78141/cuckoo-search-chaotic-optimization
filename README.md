# Cuckoo Search Optimization with Chaotic Logistic Maps

**MSc Computer Science Major Project — Jyoti Sharma**  
Central University of Rajasthan, 2026

## Overview

This repository contains a Python implementation and experimental study of three
continuous optimization algorithms developed for the MSc major project:

1. **Standard Cuckoo Search (CS)** — baseline method using Lévy flights.
2. **Chaotic Cuckoo Search (CCS)** — replaces the fixed step-size with a Logistic-map-driven
   chaotic value and uses chaotic initialization/abandonment with elitism.
3. **Logistic-Sine Chaotic Cuckoo Search (LS-CCS)** — proposed extension using a
   hybrid Logistic-Sine chaotic map.

The implementation evaluates the algorithms on standard numerical benchmark functions
and on the classical constrained compression-spring design problem.

## Project structure

```text
cuckoo-search-chaotic-optimization/
├── README.md
├── requirements.txt
├── LICENSE
├── src/
│   ├── cuckoo_search.py
│   ├── chaotic_cuckoo_search.py
│   ├── logistic_sine_ccs.py
│   └── benchmark_functions.py
├── experiments/
│   └── run_benchmarks.py
├── results/
│   └── README.md
└── docs/
    └── project_notes.md
```

## Algorithms

| Algorithm | Initialization | Step size | Abandonment | Elitism |
|---|---|---|---|---|
| CS | Uniform random | Fixed | Uniform random | No |
| CCS | Logistic map | Dynamic chaotic | Logistic map | Top-2 |
| LS-CCS | Logistic-Sine map | Dynamic chaotic | Logistic-Sine map | Top-2 |

## Parameters used in the project

- Number of nests: **25**
- Maximum iterations: **300** for benchmark functions
- Maximum iterations: **500** for compression-spring experiments
- Abandonment probability: **0.25**
- Lévy index: **1.5**
- Elitism: **2**
- Logistic-map parameter: **4.0**
- Logistic-Sine parameter: **0.86**
- Independent runs: **20**

## Benchmark functions

- Michalewicz (2D), bounds `[0, π]`, known minimum ≈ `-1.8013`
- Sphere (10D), bounds `[-5.12, 5.12]`
- Rastrigin (10D), bounds `[-5.12, 5.12]`
- Ackley (10D), bounds `[-32.768, 32.768]`
- Griewank (10D), bounds `[-600, 600]`

## Running the code

Create a virtual environment if desired, then install dependencies:

```bash
pip install -r requirements.txt
```

Run a small benchmark demonstration:

```bash
python experiments/run_benchmarks.py
```

The script prints the best solution and fitness for each algorithm/function pair.

## Reported project results

The MSc report reports the following 20-run results:

### Michalewicz (2D)

| Metric | CS | CCS | LS-CCS |
|---|---:|---:|---:|
| Best | -1.801271 | -1.801303 | -1.801303 |
| Mean | -1.797651 | -1.801300 | -1.801299 |
| Worst | -1.787254 | -1.801257 | -1.801249 |
| Std Dev | 0.003994 | 0.000010 | 0.000012 |

### Sphere (10D)

| Metric | CS | CCS | LS-CCS |
|---|---:|---:|---:|
| Best | 0.773308 | 0.000672 | 0.000443 |
| Mean | 1.409149 | 0.004356 | 0.003953 |
| Worst | 2.200852 | 0.009662 | 0.012570 |
| Std Dev | 0.390191 | 0.002796 | 0.003568 |

### Other benchmark best values

| Function | CS | CCS | LS-CCS |
|---|---:|---:|---:|
| Rastrigin | 38.23 | 21.65 | 16.28 |
| Ackley | 2.53 | 0.137 | 0.098 |
| Griewank | 0.256 | 0.133 | 0.126 |

### Compression spring

The report gives a literature benchmark of approximately `0.012665` and reports:

| Metric | CS | CCS | LS-CCS |
|---|---:|---:|---:|
| Best | 0.012813 | 0.012727 | 0.012829 |
| Mean | 0.015646 | 0.014018 | 0.014404 |
| Std Dev | 0.005896 | 0.001754 | 0.001462 |

**Important:** these tables are the results reported in the MSc project report. The repository code is a clean, reproducible reconstruction of the documented algorithms; running it again may produce different stochastic results.

## Academic context

This project was completed as an MSc Computer Science major project under the guidance
of **Prof. Mamta Rani** at the Central University of Rajasthan.

The implementation follows the project report's documented methodology and parameters.
It is intended for academic learning, reproducibility, and further research.

## References

- Yang, X.-S., & Deb, S. (2009). Cuckoo Search via Lévy Flights.
- Mantegna, R. N. (1994). Fast, accurate algorithm for numerical simulation of Lévy stable stochastic processes.
- Demir, F. B., Tuncer, T., & Kocamaz, A. F. (2020). A Logistic Chaotic Map-based Optimization Algorithm for Numerical Functions and Engineering Design Problems.

## Author

**Jyoti Sharma**  
MSc Computer Science  
Central University of Rajasthan
