# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json`.
- Prior project evidence used for the expected model and frequency context: `evidence/e006.md`, `evidence/e007.json`, and `evidence/e013.md`.
- New completed Ramsey measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, and `measurement/m005.json` control record.
- Generated local artifacts: `ramsey_analysis.py`, `ramsey_analysis_results.json`, and `ramsey_review_plot.png`.

## Calculations or scripts run

- Ran `python ramsey_analysis.py`.
- Confirmed the executed Ramsey settings from the saved scan variable values and job spec: `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `tau = 0..8 us`, `41` points, `8` averages, `50000` repetitions, snake order. The embedded XML text contains older defaults, but the executed variable list matches the job spec.
- Treated readout 1 as the pre-Ramsey reference and readout 2 as the post-Ramsey signal, based on the `full_experiment=0` Ramsey XML path in `measurement/m001.json`.
- Calculated raw readout traces, combined signal/reference, per-average signal/reference, SEM across stored averages, a local average-level count-drift proxy, FFT spectra, weighted fixed-frequency sine fits, shifted-sideband checks around the observed carrier, and weighted grid-profile damped Ramsey fits.

## Quantitative checks

- Terminal result completed with final counts `44.184 kcps`.
- Per-average reference means ranged from `40.47` to `55.53 kcps`; average 7 was more than `15%` below the median reference mean. Per-average normalization was therefore more informative than raw combined counts alone.
- Mean per-average signal/reference ratio ranged from `0.803` to `0.970`; median ratio SEM across tau points was `0.0187`.
- The `tau=0` ratio point was the lowest point, so fits were checked both with and without it.
- Mean-ratio FFT top components were near `1.098 MHz` and `1.220 MHz` using all tau points; excluding `tau=0`, the largest bins were near `1.125 MHz`, `1.250 MHz`, and `1.000 MHz`.
- Weighted fixed-sine checks excluding `tau=0`:
  - programmed `1.000 MHz` carrier: ratio amplitude `0.0074`, `R2 = 0.052`;
  - strongest exploratory `1.220 MHz` bin: ratio amplitude `0.0161`, `R2 = 0.242`;
  - expected 13C sidebands at `0.615/1.385 MHz`: amplitudes `0.0134/0.0117`, `R2 = 0.138/0.106`;
  - prior scout `0.884 MHz` component: amplitude `0.0094`, `R2 = 0.081`.
- If the observed carrier is taken as `1.16..1.18 MHz`, shifted sidebands at carrier `+/- 0.3846 MHz` are weak: for a `1.18 MHz` carrier, low/high shifted-sideband fits have amplitudes `0.0038/0.0061` and `R2 = 0.013/0.031`.
- Damped grid-profile fits to the mean per-average ratio excluding `tau=0` prefer a carrier near `1.18 MHz`, with rough `T2star` values of `6.8 us` for a Gaussian envelope and `5.4 us` for an exponential envelope. The profile is broad: Gaussian `Delta chi2 <= 2.71` spans `4.3..17 us`, and exponential spans `2.1..32 us`; looser intervals can run to the upper grid bound.

## Plausible interpretation

The Ramsey data are analyzable and contain weak Ramsey-like oscillatory content, but it is not a clean claim-grade measurement. The dominant exploratory component is closer to `1.16..1.22 MHz` than to the programmed `1.0 MHz` carrier. That could be residual microwave detuning, a shifted carrier from center drift, finite-window leakage, or sensitivity to the early-time point. The prior non-claim-grade `~0.884 MHz` component is not dominant in this det-shifted run.

A rough `T2star` scale of several microseconds, plausibly around `5..7 us`, is consistent with the best damped-profile fits after excluding `tau=0`, but the value is model- and inclusion-sensitive and should remain provisional.

There is no supported resolved 13C sideband pattern in this dataset. Neither the planned `0.615/1.385 MHz` sidebands nor sidebands shifted around the observed carrier form a strong, symmetric, claim-grade pair.

## Claims not yet supported

- A well-supported numeric `T2star` value.
- A nearby 13C coupling claim.
- A definitive no-13C conclusion; this run supports "no resolved 13C sidebands seen here," not physical absence.
- Exact assignment of the `1.16..1.22 MHz` feature as the true Ramsey carrier.
- Physical interpretation of the `tau=0` point.

## Recommended next action

Do not make a T2star or 13C claim from this run. First resolve the carrier mismatch on r03: perform a fresh fine weak-pi pODMR/current-center check or a compact Ramsey detuning diagnostic designed to test whether the `1.16..1.22 MHz` component follows microwave detuning/programmed `det`. For the next T2star attempt, avoid relying on `tau=0` and only fit/report `T2star` after the carrier frequency and phase are reproducible; then repeat with enough SNR/span to test sidebands relative to the confirmed carrier.
