# Non-LLM pODMR Signal-Processing Baselines

The baselines use the released raw pODMR exports and the same 96 gold-labeled cases.
Readout 1 is treated as reference and readout 2 as signal.  The main contrast
feature is `1 - signal/reference`, so a pODMR dip appears as a positive local
feature.  Fixed-threshold baselines are not fitted to the labels.  The threshold
sweep is reported separately as a diagnostic for how much separation is present
in this dataset.

## Fixed baselines

| Classifier | TP | TN | FP | FN | Accuracy | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|---:|
| contrast_depth_ge_0p132 | 24 | 72 | 0 | 0 | 100.0% | 0.0% | 0.0% |
| contrast_depth_ge_0p10 | 24 | 69 | 3 | 0 | 96.9% | 4.2% | 0.0% |
| detrended_depth_snr | 23 | 72 | 0 | 1 | 99.0% | 0.0% | 4.2% |
| avg_consistent_depth_snr | 8 | 70 | 2 | 16 | 81.2% | 2.8% | 66.7% |
| lorentzian_bic_depth | 22 | 70 | 2 | 2 | 95.8% | 2.8% | 8.3% |
| gaussian_bic_depth | 22 | 71 | 1 | 2 | 96.9% | 1.4% | 8.3% |

## Contrast-depth separation

The contrast-depth feature alone fully separates this dataset.  The largest
resonance-absent contrast depth is `0.126740947`, and the smallest
resonance-present contrast depth is `0.154093098`.  Therefore any threshold
larger than `0.126740947` and no larger than `0.154093098` gives 24 TP, 72 TN,
0 FP, and 0 FN when the rule is `present` if `depth >= threshold`.

## Threshold sweep diagnostics

| Feature | Selection | Threshold | TP | TN | FP | FN | Accuracy | FPR | FNR |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| depth | best_accuracy | 0.128 | 24 | 72 | 0 | 0 | 100.0% | 0.0% | 0.0% |
| depth | zero_fn_min_fp | 0.154 | 24 | 72 | 0 | 0 | 100.0% | 0.0% | 0.0% |
| detrended_snr | best_accuracy | 2.9 | 21 | 70 | 2 | 3 | 94.8% | 2.8% | 12.5% |
| detrended_snr | zero_fn_min_fp | 2.1 | 24 | 47 | 25 | 0 | 74.0% | 34.7% | 0.0% |
| gaussian_delta_bic | best_accuracy | 4 | 24 | 70 | 2 | 0 | 97.9% | 2.8% | 0.0% |
| gaussian_delta_bic | zero_fn_min_fp | 4 | 24 | 70 | 2 | 0 | 97.9% | 2.8% | 0.0% |
| lorentzian_delta_bic | best_accuracy | 3.5 | 24 | 70 | 2 | 0 | 97.9% | 2.8% | 0.0% |
| lorentzian_delta_bic | zero_fn_min_fp | 3.5 | 24 | 70 | 2 | 0 | 97.9% | 2.8% | 0.0% |

## Interpretation

A simple contrast-depth threshold is already very strong on this benchmark.
This means the pODMR classification task is not evidence that an LLM is a
better detector than conventional signal processing.  Instead, it supports a
narrower claim: when the agent is asked to calculate the expected signal, its
judgment moves toward the same physical comparison that a simple signal
baseline exploits.
