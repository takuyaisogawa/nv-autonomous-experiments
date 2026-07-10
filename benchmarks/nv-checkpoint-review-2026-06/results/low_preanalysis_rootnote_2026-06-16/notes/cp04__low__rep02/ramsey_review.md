# Ramsey Review: det=1.5 MHz short-tau shift check

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, plus targeted searches through `md/`, `evidence/`, and `measurement/`.
- New terminal measurement data:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
  - `measurement/m002.json`: submitted job/spec for `nv23_ramsey_20260514_015423_auto_ramsey`.
  - `measurement/m003.json`: completed bridge result/status.
  - `measurement/m004.json`: terminal run status.
  - `measurement/m005.json`: run-control state.
- Scratch outputs created:
  - `scratch/ramsey_det1p5_analysis_summary.json`
  - `scratch/ramsey_det1p5_trace.png`
  - `scratch/ramsey_det1p5_frequency_screen.png`

## Calculations or scripts run

- Used inline local Python to inspect JSON structures and analyze the raw export.
- Extracted combined and per-average readouts from `ExperimentData` and `ExperimentDataEachAvg`.
- Treated readout 0 as Ramsey signal and readout 1 as reference/post-Ramsey readout; checked both raw signal and signal/reference ratio.
- Computed per-point SEM from the 12 stored averages.
- Ran weighted linear least-squares frequency screens of the form `offset + slope*tau + a*cos(2*pi*f*tau) + b*sin(2*pi*f*tau)` over 0.2..4.5 MHz.
- Explicitly checked the prespecified frequencies from the project plan:
  - programmed det: 1.500 MHz
  - det-tracking prediction from prior ~1.192 MHz component: ~1.692 MHz
  - prior empirical component: ~1.192 MHz
  - expected 13C sideband checks: ~1.307 MHz and ~2.076 MHz
- Ran descriptive damped-sinusoid fits only as diagnostics, not as claim support.

Key numeric checks:

- Run completed: `2026-05-14T01:54:36` to `2026-05-14T04:15:00`; savedexperiment `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
- Scan: tau `0.048..1.968 us`, 41 points; `det = 1.5 MHz`; `mw_freq = 3.8759 GHz`; 12 averages x 90000 repetitions.
- Final count text from bridge result: `44.796 kcps`.
- Combined signal mean: `48.084 kcps`; reference mean: `44.269 kcps`.
- Median per-point SEM from average-to-average scatter: signal `0.745 kcps`, ratio `0.0146`.
- Raw-signal peak-to-peak across tau: `2.40 kcps`; ratio peak-to-peak: `0.163`, indicating appreciable reference/normalization structure.
- Frequency screen:
  - The largest ratio component in the broad screen is at the low-frequency boundary, `0.200 MHz`, with ratio amplitude `0.327`; all per-average ratio screens also selected this low-frequency boundary. This is more consistent with baseline/reference structure than a resolved MHz Ramsey carrier.
  - At programmed `1.500 MHz`: ratio amplitude `0.0251` with formal LS SNR `4.43`, but raw-signal amplitude only `0.027 kcps`, far below the signal SEM.
  - At det-tracking prediction `1.692 MHz`: ratio amplitude `0.0265` with formal LS SNR `4.70`, but raw-signal amplitude only `0.085 kcps`, also far below the signal SEM.
  - At prior empirical `1.192 MHz`: ratio amplitude `0.0086`, formal SNR `1.22`; no support for persistence at the old frequency.
  - 13C sideband checks: lower `1.307 MHz` ratio SNR `1.79`; upper `2.076 MHz` ratio SNR `0.83`; neither is claim-grade.
- Descriptive damped-sinusoid fits around the programmed/det-tracking window converged near `1.574 MHz` with short apparent decay around `0.57 us`, but this is not promoted because the apparent oscillation is ratio-dominated and not supported in the raw signal.

## Plausible interpretation

- The det-shift run argues against simply promoting the previous `~1.192 MHz` feature as a stable physical Ramsey component: the `1.192 MHz` check is weak in this run.
- The new ratio screen has modest components near the programmed/det-shifted MHz region, but they are not mirrored by a raw-signal oscillation of comparable significance. The ratio behavior is likely affected by reference/baseline structure.
- The data remain analyzable and the run completed cleanly, but the evidence does not yet support a clean programmed-carrier Ramsey model.
- Under current conditions on r03, the Ramsey evidence is still non-claim-grade for both T2star and nearby 13C coupling.

## Claims that are not yet supported

- Do not claim a numeric T2star from this run.
- Do not claim detected nearby 13C sidebands from this run.
- Do not claim that the prior `~1.19 MHz` feature is a physical Ramsey carrier.
- Do not claim that the `~1.57..1.69 MHz` ratio feature is a clean det-tracking Ramsey carrier without raw-signal support.
- Do not claim that the refined pODMR center alone explains the Ramsey frequency mismatch.

## Recommended next action

Stop blind Ramsey repeats on r03 under this same protocol. The targeted det-shift check did not produce a raw/readout-aware carrier or 13C-sideband model. The next action should be to choose a non-Ramsey or modified validation path before branch closeout, for example:

- run an alternate coherence/readout protocol less sensitive to the reference-normalization artifact, or
- perform a deliberately short diagnostic focused on raw-signal contrast/calibration rather than extracting T2star, or
- close r03 Ramsey/13C as unsupported under current measurement conditions and move to a new aligned NV candidate if the project requires a supported T2star/13C conclusion.
