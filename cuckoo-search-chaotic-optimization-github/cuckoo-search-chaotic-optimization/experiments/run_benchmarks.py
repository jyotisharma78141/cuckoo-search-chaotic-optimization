import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from benchmark_functions import BENCHMARKS
from cuckoo_search import cuckoo_search
from chaotic_cuckoo_search import chaotic_cuckoo_search
from logistic_sine_ccs import ls_ccs


ALGORITHMS = {
    "CS": cuckoo_search,
    "CCS": chaotic_cuckoo_search,
    "LS-CCS": ls_ccs,
}


def main():
    print("=" * 72)
    print("Cuckoo Search — benchmark demonstration")
    print("=" * 72)

    for function_name, (func, dim, lb, ub) in BENCHMARKS.items():
        print(f"\n{function_name}")
        print("-" * 72)

        for name, algorithm in ALGORITHMS.items():
            best, fitness, _ = algorithm(
                func,
                dim=dim,
                lb=lb,
                ub=ub,
                max_iter=300,
                **({"seed": 42} if name == "CS" else {"random_seed": 42}),
            )
            print(f"{name:6s} fitness = {fitness:.8f}  position = {np.round(best, 5)}")


if __name__ == "__main__":
    main()
