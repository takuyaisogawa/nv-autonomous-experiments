# Ramsey Review: short-tau r03 diagnostic

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, and `md/memory.md`.
- New Ramsey data: `measurement/m001.json`, raw export for `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
- Run metadata: `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status/control snapshot, `measurement/m005.json` control snapshot.
- Prior comparison context from state/evidence: earlier r03 Ramsey runs at detuning 1.5 MHz and 1.0 MHz over longer windows were analyzable but non-claim-grade; fine weak-pi pODMR supported `mw_freq = 3.8759 GHz`.

## Calculations or scripts run

- Used local Python to parse `measurement/m001.json`, extract `tau`, `ExperimentData`, and `ExperimentDataEachAvg`.
- Confirmed acquisition parameters from raw export/terminal metadata:
  - `tau = 48 ns..1.968 us`, 41 points, 48 ns step.
  - `12 averages x 90000 repetitions`, signal/reference traces, snake scan, tracking per average.
  - `mw_freq = 3.8759 GHz`, programmed detuning `1.0 MHz`.
  - Terminal run completed normally; final text count `35.122 kcps`.
- Created scratch outputs under `scratch_ramsey_analysis/`:
  - `summary.json`
  - `model_compare.json`
  - `ramsey_shorttau_review.png`
  - `ramsey_shorttau_per_avg.png`
- Quantitative checks performed:
  - Raw signal peak-to-peak over tau: `6.50 kcps`; median per-point SEM across stored averages: `1.14 kcps`.
  - Ratio peak-to-peak: `0.143`; median ratio SEM: `0.0127`.
  - Average-to-average mean count drift is large: reference mean relative span `26.8%`, signal mean relative span `30.8%`.
  - Fixed-frequency least-squares amplitudes on raw signal:
    - `1.000 MHz` carrier: `1.28 kcps`, ratio amplitude `0.0274`.
    - Expected 13C sideband positions from prior model, `0.615 MHz` and `1.385 MHz`: `1.10 kcps` and `1.22 kcps`, ratio amplitudes `0.0243` and `0.0271`.
  - Detrended FFT has coarse bin spacing about `0.508 MHz`; strongest bins were `1.524 MHz`, `1.016 MHz`, and `0.508 MHz`, so FFT alone cannot resolve the carrier from nearby short-window structure/sidebands.
  - Model comparison on raw signal using per-point SEM:
    - Linear baseline: reduced chi-square `2.06`, AIC `84.24`.
    - Linear + fixed `1 MHz` sinusoid: reduced chi-square `1.28`, AIC `55.39`.
    - Linear + fixed `1 MHz` exponentially damped sinusoid: reduced chi-square `0.875`, AIC `41.50`, fitted decay constant `T2star = 0.279 us`, fitted amplitude `-5.10 kcps`.
  - Same model comparison on point-wise signal/reference ratio improves with damped 1 MHz term but remains overdispersed: reduced chi-square `3.41`, fitted decay constant `0.161 us`.
  - Per-average damped 1 MHz raw fits are not tightly consistent: fitted decay constants span about `0.068..2.21 us`, with many fits in the `0.15..0.49 us` range and phase/amplitude instability.

## Plausible interpretation

- This short-tau/high-SNR run is qualitatively different from the prior long-window Ramsey attempts: the raw signal contains a visible early-time structure with effect size several times the stored-average SEM.
- The programmed `1 MHz` detuning is now a plausible part of the signal: adding a fixed `1 MHz` term substantially improves the raw-signal model, and a damped `1 MHz` term fits the combined raw signal with a short decay time.
- The most defensible physical interpretation is that r03 may have a very short Ramsey dephasing time, order `0.2..0.4 us`, which was mostly washed out in the earlier longer-window scans.
- The data still have substantial common-mode/count drift between stored averages, and the normalized/per-average fits are not stable enough to promote a precise T2star value.
- The 13C interpretation is not supported. The targeted `0.615 MHz` and `1.385 MHz` sideband amplitudes are comparable to the carrier-screen amplitude and are not resolved by the coarse short-window FFT. No clean triplet/sideband model follows from this dataset.

## Claims that are not yet supported

- Do not claim a precise T2star from this run. A reasonable working estimate is only "very short, likely order `0.2..0.4 us` if the Ramsey-like interpretation is correct."
- Do not claim a nearby 13C coupling or absence of 13C. The short window and drift do not support a resolved sideband conclusion.
- Do not claim that the previous non-claim-grade `~0.884 MHz` or `~1.178 MHz` features were physical. This run favors short-time carrier-like behavior but does not reconcile all prior frequency screens.
- Do not claim that reference normalization validates the fit. The raw signal is the strongest evidence; normalized views remain noisy/overdispersed.

## Recommended next action

- Stop blind long-window Ramsey repeats on r03.
- Run a targeted confirmation designed for the short-T2star hypothesis: repeat short-tau Ramsey with the same `mw_freq = 3.8759 GHz` and `det = 1.0 MHz`, but use a phase/control comparison if available, or at minimum acquire a matched detuning-control pair such as `+1.0 MHz` and `-1.0 MHz` over `~0.05..1.5 us` with high shots and balanced averages. The confirmation criterion should be phase/frequency inversion or reproducible early-time carrier decay, not just another unconstrained fit.
- If that confirmation reproduces the early damped carrier, report T2star as a short-time Ramsey estimate with uncertainty from repeat/control consistency. If it does not, close r03 Ramsey/T2star as unsupported under current conditions and switch to an alternate dephasing protocol or candidate.
