# Benchmarks and evaluation

Named benchmark datasets, test cohorts, benchmark studies, and metric toolkits solve different evaluation problems.

## MP-20

**Type:** Training / validation / test dataset

[2022 CSP113](https://arxiv.org/abs/2110.06197)

[Versioned release / code](https://github.com/txie-93/cdvae/tree/f857f598d6f6cca5dc1ea0582d228f12dcc2c2ea/data/mp_20)

Up to 20 atoms per cell; use the released split, preprocessing and matcher. Canonical split sizes are 27,136 / 9,047 / 9,046.

## MPTS-52

**Type:** Chronological training / validation / test dataset

[2024 MatbenchGenmetrics2024](https://doi.org/10.21105/joss.05618) · [2023 CSP128](https://arxiv.org/abs/2309.04475)

[Versioned release / code](https://github.com/jiaor17/DiffCSP/tree/7121d159826efa2ba9500bf299250d96da37f146/data/mpts_52)

Up to 52 atoms per cell, not 52 test structures. Sometimes mistyped MPST-52. Preserve the chronological split.

[Original Data Url](https://figshare.com/articles/dataset/Materials_Project_Time_Split_Data/19991516)

[Framework Url](https://github.com/sparks-baird/matbench-genmetrics)

## CSPBench

**Type:** Cross-method benchmark study

[2026 CSP180](https://doi.org/10.1002/aidi.70162)

[Versioned release / code](https://github.com/usccolumbia/cspbenchmark/tree/6e2eee244f434e2010fa4f9d3a08e2c054242a47)

180-target study; the DFT-based baseline comparison uses a separate 23-target subset.

## T180

**Type:** Versioned test cohort

[2026 CSP185](https://arxiv.org/abs/2609.26502v1)

[Versioned release / code](https://github.com/usccolumbia/benchmark_deep_csp/tree/320b7289e70b61f9d8d51d7fe7dae3e074f75522/data/testsets/v3.1/T180)

180 targets in v3.1. Integer atom counts of the geometric primitive cell are supplied. Use the reference and query manifests; do not assume identity with the historical CSPBench cohort.

## T46

**Type:** Versioned test cohort

[2026 CSP185](https://arxiv.org/abs/2609.26502v1)

[Versioned release / code](https://github.com/usccolumbia/benchmark_deep_csp/tree/320b7289e70b61f9d8d51d7fe7dae3e074f75522/data/testsets/v3.1/T46)

46 targets in v3.1. Keep its own denominator and primitive-cell-count query manifest.

## CSPMetrics / CSPBenchMetrics

**Type:** Evaluation metric package

[2024 CSPMetrics2024](https://doi.org/10.1016/j.commatsci.2024.112802)

[Versioned release / code](https://github.com/usccolumbia/CSPBenchMetrics)

Complementary geometry, graph, fingerprint, diffraction and energy comparisons. This is a toolkit, not a single fixed benchmark cohort.

## Comparison checklist

Record the exact split or cohort manifest, supplied cell counts/symmetry, number of candidates, matcher and tolerances, relaxation and ranking model, compute budget, failed targets, and training exposure. Keep structure recovery, space-group agreement, energy ranking, and physical stability as separate measurements.

Other benchmark and dataset links, including molecular blind tests, are retained in the [dataset index](datasets.md) and individual [software profiles](software.md).
