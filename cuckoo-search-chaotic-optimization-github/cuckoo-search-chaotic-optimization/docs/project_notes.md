# Project Notes

## Source basis

The implementation in this repository was reconstructed from the author's MSc major
project report, *Optimization using Cuckoo Search Algorithm with Chaotic Logistic Maps*.

The report documents three systems:

- Standard Cuckoo Search (CS)
- Chaotic Cuckoo Search (CCS) with Logistic Map
- Logistic-Sine Chaotic Cuckoo Search (LS-CCS)

The report specifies Python, NumPy, Matplotlib and SciPy as the main software stack.

## Important reproducibility note

The report's appendix code is embedded in a PDF and some mathematical/code characters
are altered by PDF text extraction. The repository therefore contains a cleaned,
executable reconstruction of the documented algorithms rather than claiming byte-for-byte
reproduction of the PDF appendix.

## Documented experimental settings

n = 25
pa = 0.25
beta = 1.5
elitism_keep = 2
max_iter = 300 (500 for spring)
Logistic r = 4.0
Logistic-Sine r = 0.86
20 independent runs

## Reported findings

The report documents strong convergence behavior for the chaotic variants on several
unconstrained benchmark functions. It also reports that the compression-spring result
does not have the same ordering as the unconstrained benchmarks: CCS has the reported
best and mean values, while LS-CCS has the lowest reported standard deviation.

These statements describe the project's reported results; they should not be presented
as a universal claim that one optimization algorithm is always superior.
