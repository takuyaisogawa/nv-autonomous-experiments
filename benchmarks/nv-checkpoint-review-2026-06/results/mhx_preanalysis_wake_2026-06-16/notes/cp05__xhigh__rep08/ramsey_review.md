# Ramsey Review

## Files/Data Used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`, `md/knowledge.md`.
- New Ramsey measurement: `measurement/m001.json` through `measurement/m005.json`.
- Terminal job: `nv23_ramsey_20260514_055148_auto_ramsey`, completed `2026-05-14T09:28:25`, savedexperiment path recorded as `<MATLAB_23C_ROOT>\savedexperiments\NV1\1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- Measurement settings from the local files: `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`, `tau = 0.048..8.048 us`, 41 points, 20 averages x 50000 repetitions = `1.0e6` shots per tau point.

## Calculations/Scripts Run

- Created and ran `ramsey_analysis.py`.
- Outputs: `ramsey_analysis_summary.json` and `ramsey_analysis_plot.png`.
- Checks performed:
  - Verified raw export axis contract: `ExperimentDataEachAvg` mean reproduces `ExperimentData`; shape is `(1, 20, 2, 41)` for per-average data.
  - Treated readout 1 as the bright reference and readout 2 as Ramsey signal based on `full_experiment = 0` in the sequence metadata.
  - Checked terminal status/result: completed, final counts `43.433 kcps`, no monitor error, `stop_requested = false`.
  - Computed raw signal, point-wise signal/reference, and signal normalized to a fitted reference line.
  - Computed per-point SEM across stored averages: median signal SEM `0.850 kcps`, median ratio SEM `0.0116`.
  - Ran least-squares sinusoid screens from `0.2..2.4 MHz` and FFT screens, both full-span and after skipping the first 4 tau points.
  - Checked project-target frequencies: carrier `1.5 MHz`, expected 13C sidebands `1.115/1.885 MHz`, prior controls/features `1.192`, `1.623`, and `0.884 MHz`.
  - Bootstrapped stored averages to estimate whether the top frequency is robust.

## Plausible Interpretation

- The measurement is analyzable and has no copied terminal hard anomaly.
- There is a weak carrier-like component near the programmed `1.5 MHz` detuning:
  - Point-wise ratio LS amplitude at `1.5 MHz`: `0.01575` full-span, `0.01231` after skipping the first 4 tau points.
  - Raw-signal LS amplitude at `1.5 MHz`: `0.705 kcps` full-span, `0.512 kcps` after skipping first 4 tau points.
  - FFT bins also show power near `1.46..1.59 MHz`, especially after skipping the first 4 tau points.
- This is not claim-grade because the largest LS component is instead near `2.27 MHz` in raw, ratio, and fitted-reference-normalized views:
  - Ratio LS top: `2.270 MHz` full-span, `2.266 MHz` skip-first-4.
  - Bootstrap top-frequency probability favors `2.27 MHz` over `1.5 MHz`: for ratio, `P(top within 0.15 MHz of 2.27) = 0.710` full-span and `0.608` skip-first-4; for `1.5 MHz`, `0.276` and `0.334`.
- The first few tau points are structured: signal starts `[40.57, 46.84, 43.16, 44.01] kcps`, while the last four points are near `[44.80, 44.92, 44.80, 44.82] kcps`. This early-time structure materially affects the screens.
- Expected 13C sidebands are not supported:
  - Ratio LS amplitude at `1.115 MHz`: `0.00277` full-span, `0.00068` skip-first-4.
  - Ratio LS amplitude at `1.885 MHz`: `0.00961` full-span, `0.00528` skip-first-4.
  - Per-average top frequencies are mixed; only 1 of 20 ratio averages top near `1.115 MHz` and 2 of 20 top near `1.885 MHz`.

## Claims Not Yet Supported

- A numerical `T2star` value from this Ramsey measurement.
- A clean programmed-carrier Ramsey decay at `1.5 MHz`.
- Resolved nearby 13C sidebands at the expected `1.115/1.885 MHz` positions.
- A physical assignment of the dominant `~2.27 MHz` LS component.
- A definitive universal absence of nearby 13C coupling; the defensible conclusion is narrower: this refreshed-center Ramsey dataset is non-claim-grade for 13C under the current conditions.

## Recommended Next Action

Do not run another identical Ramsey repeat. Record this refreshed-center long-span Ramsey as non-claim-grade for both T2star and 13C. If the project still needs a stronger conclusion on r03, switch to an alternate protocol with better spectral discrimination after fresh tracking/frequency checks; otherwise close r03 with an unsupported/negative conclusion under the current Ramsey conditions.
