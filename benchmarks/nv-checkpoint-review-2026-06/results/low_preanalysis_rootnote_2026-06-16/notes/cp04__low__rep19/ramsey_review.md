# Ramsey Review: det=1.5 MHz short-tau shift check

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, with Ramsey/NV-specific checks from `md/memory.md` and `md/knowledge.md`.
- New measurement data:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
  - `measurement/m002.json`: submitted execute spec for `nv23_ramsey_20260514_015423_auto_ramsey`.
  - `measurement/m003.json`: terminal result, completed 2026-05-14 04:15:00.
  - `measurement/m004.json`, `measurement/m005.json`: run status/control.
- Scratch outputs created here:
  - `ramsey_analysis_summary.txt`
  - `ramsey_det1p5_shiftcheck_analysis.png`

## Calculations or scripts run

- Inspected JSON structure with Python. The raw export has `ExperimentDataEachAvg` shape `[1, 12, 2, 41]`, matching the project warning that this Ramsey export should be interpreted as `[scan, avg, readout, point]`.
- Confirmed run parameters from the export/spec: `tau = 48 ns..1.968 us`, 41 points, 48 ns step, 12 averages, 90000 repetitions, `mw_freq = 3.8759 GHz`, `det = 1.5 MHz`, snake scan order saved in tau order.
- Computed combined raw signal, reference, and signal/reference ratio; per-point SEM across the 12 averages; FFT of linearly detrended/windowed ratio; and least-squares sinusoid screens using `constant + linear trend + cos/sin`.
- Frequency checks included:
  - programmed det: `1.500 MHz`
  - det-tracking test from prior empirical `~1.192 MHz` at det=1.0: `~1.692 MHz`
  - expected 13C sideband positions around that det-tracking carrier: `~1.307 MHz` and `~2.076 MHz`
  - prior fixed-feature control: `1.192 MHz`

Key numeric results:

- Sampling: span `1.920 us`, Nyquist `10.417 MHz`, FFT bin spacing `0.508 MHz`.
- Combined raw signal: mean `48.084 kcps`, median per-point SEM `0.745 kcps`, peak-to-peak `2.400 kcps`.
- Combined signal/reference ratio: mean `1.087164`, median per-point SEM `0.014637`, peak-to-peak `0.163171`.
- Target-frequency least-squares amplitudes:
  - `1.500 MHz`: ratio amp `0.028573` (`1.95x` median ratio SEM), raw amp `0.037 kcps` (`0.05x` raw SEM).
  - `1.692 MHz`: ratio amp `0.029756` (`2.03x` median ratio SEM), raw amp `0.099 kcps` (`0.13x` raw SEM).
  - `1.307 MHz`: ratio amp `0.011252` (`0.77x` median ratio SEM), raw amp `0.222 kcps` (`0.30x` raw SEM).
  - `2.076 MHz`: ratio amp `0.006808` (`0.47x` median ratio SEM), raw amp `0.174 kcps` (`0.23x` raw SEM).
  - `1.192 MHz`: ratio amp `0.005944` (`0.41x` median ratio SEM), raw amp `0.294 kcps` (`0.39x` raw SEM).
- The strongest ratio LS screen over `0.2..2.8 MHz` was at the lower boundary, `0.200 MHz`, consistent with slow baseline structure rather than a Ramsey carrier. Per-average ratio best frequencies were inconsistent: `1.960, 1.515, 0.870, 0.890, 1.765, 0.600, 0.890, 1.165, 0.600, 1.665, 0.600, 1.735 MHz`.
- Detrended/windowed ratio FFT had a bin at `1.524 MHz`, but this is not supported by the raw-signal LS amplitude and is not stable across averages.

## Plausible interpretation

- The det=1.5 MHz shift-check weakens the hypothesis that the earlier `~1.192 MHz` feature is a fixed, reproducible spectral feature: at `1.192 MHz` the combined ratio amplitude is only `0.41x` median ratio SEM, and per-average screens are not stable there.
- The run does not provide a clean positive det-tracking result either. Ratio-only fits near `1.5..1.692 MHz` are modest, but the corresponding raw-signal amplitudes are far below raw SEM and per-average frequencies disagree. That is not enough to promote a Ramsey carrier or a T2star fit.
- The most likely reading is still "analyzable but non-claim-grade Ramsey data under current conditions": baseline/readout-normalization structure and average-to-average variation can create weak ratio spectral features without a coherent raw Ramsey oscillation.

## Claims not yet supported

- No supported numeric `T2star` for r03.
- No supported nearby `13C` conclusion from Ramsey/FFT sidebands.
- No supported claim that the observed ratio features are the programmed `1.5 MHz` Ramsey carrier.
- No supported claim that the prior `~1.192 MHz` feature det-tracked to `~1.692 MHz`.
- No supported claim that the 13C sidebands at `~1.307 MHz` or `~2.076 MHz` are present.

## Recommended next action

Do not run another blind Ramsey repeat on r03. This det-shift diagnostic was the planned non-blind check, and it remains non-claim-grade. The next project decision should be either:

1. switch to a deliberately different protocol/diagnostic for T2star or 13C support after fresh resonance/tracking checks, or
2. close the r03 Ramsey branch as unsupported for T2star/13C under the present Ramsey conditions and move to a new aligned candidate or alternate measurement strategy.
