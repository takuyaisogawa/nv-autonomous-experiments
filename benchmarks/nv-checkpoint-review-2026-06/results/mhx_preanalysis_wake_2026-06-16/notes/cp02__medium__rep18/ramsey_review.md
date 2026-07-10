# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json`.
- Prior/follow-up evidence: `evidence/e001.json` through `evidence/e013.md`, especially the fine weak-pi pODMR review selecting `mw_freq = 3.8759 GHz`, and the second Ramsey model expecting `det = 1.0 MHz` with possible 13C sidebands near `0.615/1.385 MHz`.
- New Ramsey data/metadata:
  - `measurement/m001.json`: terminal savedexperiment raw export for `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
  - `measurement/m002.json`: submitted job spec.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json`: terminal status.
  - `measurement/m005.json`: run control.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis_summary.json` and `ramsey_review_plot.png`.
- Parsed raw export as `ExperimentData` shape `[2, 41]` and `ExperimentDataEachAvg` shape `[8, 2, 41]`; treated trace 1 as reference and trace 2 as Ramsey signal.
- Confirmed scan: `tau = 0..8 us`, `dt = 0.2 us`, 41 points, 8 averages x 50000 repetitions, final count `44.184 kcps`.
- Checked raw reference, raw signal, signal/reference, scan-order-aware per-average common-mode drift proxy, FFT bins, least-squares sinusoid amplitudes at `0.615`, `0.884`, `1.0`, and `1.385 MHz`, and exploratory damped-cosine fits.

## Quantitative checks

- Readout levels: reference mean/std `49.31/0.87`; signal mean/std `44.58/1.34`; signal/reference mean/std `0.904/0.029`.
- Per-average common-mode brightness varied substantially. Drop-score proxy was largest for average 2 at `0.039`, with averages 7 and 8 at `0.012` and `0.005`; other averages showed positive acquisition-order slope rather than drop.
- Per-average signal residuals correlated with the combined residual at `0.36..0.66`, but pairwise residual agreement was modest: median `0.21`, range `-0.05..0.47`.
- FFT:
  - Raw signal top bins were `1.220 MHz` amp `0.797`, `1.098 MHz` amp `0.764`, and `0.488 MHz` amp `0.640`.
  - Signal/reference top bins were `1.098 MHz` amp `0.0211`, `1.220 MHz` amp `0.0188`, and `0.976 MHz` amp `0.0133`.
  - Target-bin amplitudes in signal/reference were `0.0076` at `0.615 MHz`, `0.0066` at prior `0.884 MHz`, `0.0133` at `1.0 MHz`, and `0.0066` at `1.385 MHz`.
- Least-squares sinusoid checks against fixed target frequencies were weak:
  - Signal/reference at `1.0 MHz`: amp `0.00916`, z `1.39`, R2 `0.053`.
  - Signal/reference at `0.615 MHz`: amp `0.0111`, z `1.68`, R2 `0.074`.
  - Signal/reference at `1.385 MHz`: amp `0.00843`, z `1.28`, R2 `0.046`.
  - Prior `0.884 MHz` did not recur strongly: amp `0.00742`, z `1.10`, R2 `0.035`.
- Exploratory free-frequency damped fits to signal/reference preferred about `1.17..1.19 MHz`, but T2* was not stable: including all points gave `T2* ~2.28 us`, while skipping initial points gave `~4.2..5.7 us`; R2 stayed only `0.35..0.49`.
- Terminal status `measurement/m004.json` reports a later expected per-average tracking window of about `630 s`, whereas the pre-enqueue project state cited `~555 s` under a `600 s` cap. The run completed safely, but future Ramsey repeats should shorten the per-average window.

## Plausible interpretation

- This is analyzable Ramsey data on the accepted r03 branch, and the run completed safely with good final counts.
- The det-shift diagnostic is partially useful: the old non-claim-grade `~0.884 MHz` component is not the dominant feature in this run, arguing against treating that prior peak as a stable physical carrier.
- There is weak carrier-like content around `1.1..1.2 MHz` in normalized views. That could be compatible with a Ramsey oscillation near the programmed `1.0 MHz` detuning plus a modest residual microwave-frequency offset, but the exact `1.0 MHz` fixed-frequency test is not strong.
- The expected 13C sideband locations near `0.615` and `1.385 MHz` are not isolated above comparable FFT/background structure.
- The decay envelope is not robust enough to claim T2*: fitted T2* depends strongly on inclusion of early tau points and on model choice.

## Claims not yet supported

- No well-supported numeric T2* claim.
- No well-supported nearby 13C conclusion.
- No supported claim that the Ramsey carrier is exactly the programmed `1.0 MHz`.
- No supported claim that the `1.17..1.19 MHz` exploratory fit frequency is physical rather than residual detuning, drift/reference structure, or analysis sensitivity.
- No supported coupling/Hamiltonian extraction from this Ramsey data.

## Recommended next action

- Do not make a final T2* or 13C claim from this run.
- Before another long Ramsey repeat, use the current data as a frequency diagnostic: plan a shorter per-average Ramsey follow-up that centers analysis around the observed `~1.18 MHz` carrier-like feature, keeps the tau span sufficient for sideband resolution, and reduces points/repetitions enough to keep the per-average tracking window below the active cap.
- A practical next experiment is a bounded Ramsey repeat on r03 with the same fine-pODMR `mw_freq` unless a fresh weak-pi pODMR is first run, but with reduced per-average runtime and enough averages for drift/SEM checks. If the carrier-like feature does not become phase-consistent and the sidebands remain absent, close the Ramsey/13C branch conservatively as no supported 13C evidence from this NV under current conditions.
