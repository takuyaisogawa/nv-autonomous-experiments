# Ramsey Review

## Files/Data Used

- Project context: `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New Ramsey data and run metadata:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
  - `measurement/m002.json`: execute contract for `nv23_ramsey_20260514_055148_auto_ramsey`.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json`, `measurement/m005.json`: terminal status/control.
- Generated during this review: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `analysis_output.txt`, `ramsey_review_plot.png`.

## Calculations/Scripts Run

- Ran `python analyze_ramsey.py`.
- Confirmed data shape and axis contract from the export:
  - `ExperimentData`: `[1, 2, 41]`.
  - `ExperimentDataEachAvg`: `[1, 20, 2, 41]`, interpreted as `[scan, avg, readout, tau]`.
  - Averaging the 20 per-average curves reconstructs `ExperimentData` with max absolute difference `1.42e-14`, so the per-average axis use is internally consistent.
- Run parameters from local files:
  - `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`.
  - `tau = 0.048..8.048 us`, `41` points, `0.2 us` step.
  - `20 x 50000` repetitions, or `1.0e6` shots per tau point.
  - Terminal result completed; `stop_requested = false`; run summary final count detail `43.433 kcps`.
- Quantitative checks:
  - Combined signal mean `44.670 kcps`; signal span `6.269 kcps`.
  - Median signal SEM across stored averages `0.850 kcps`.
  - Combined signal/reference ratio mean `0.9156`; ratio span `0.1206`.
  - Median ratio SEM `0.0116`.
  - Linear-detrended least-squares sinusoid screens were run on raw signal and signal/reference ratio.
  - Target amplitudes in ratio units:
    - carrier `1.500 MHz`: amplitude `0.01575`, `R2 = 0.253`.
    - expected low 13C sideband `1.1152 MHz`: amplitude `0.00278`, `R2 = 0.008`.
    - expected high 13C sideband `1.8848 MHz`: amplitude `0.00962`, `R2 = 0.096`.
    - prior short-tau `1.192 MHz` control: amplitude `0.00194`, `R2 = 0.004`.
    - prior det-shift full-span `1.623 MHz` control: amplitude `0.00801`, `R2 = 0.068`.
  - Target amplitudes in raw signal units:
    - carrier `1.500 MHz`: amplitude `0.705 kcps`, `R2 = 0.250`.
    - expected low 13C sideband `1.1152 MHz`: amplitude `0.145 kcps`, `R2 = 0.011`.
    - expected high 13C sideband `1.8848 MHz`: amplitude `0.261 kcps`, `R2 = 0.035`.
  - Frequency screen:
    - The largest formal screen response is at the Nyquist edge, about `2.499..2.501 MHz`, with low `R2`; this is not a credible physical assignment.
    - Excluding the Nyquist-edge artifact qualitatively, the carrier neighborhood is one of the stronger non-edge components: full-span ratio screen has a local/top component near `1.516 MHz` with amplitude `0.01623`; after skipping the first four tau points, near `1.515 MHz` with amplitude `0.01255`.
    - Other non-edge responses near `2.27 MHz`, `2.19 MHz`, and `1.596 MHz` remain comparable in scale, so the spectrum is not uniquely carrier/sideband-like.
  - Simple average-level drift/provenance check:
    - Average signal means span `37.38..50.37 kcps`, but forward-vs-reverse snake means differ by only `-0.378 kcps`.

## Plausible Interpretation

- The refreshed-center long-span Ramsey completed safely and produced analyzable data at the intended frequency and tau grid.
- Compared with earlier r03 Ramsey attempts, the programmed `1.5 MHz` carrier is more plausible here: the full-span and skip-first-4 screens both retain a non-edge component close to `1.5 MHz`, and the old fixed `1.192 MHz` control is weak.
- However, the observed carrier-scale raw amplitude is only `0.705 kcps`, below the median per-point signal SEM of `0.850 kcps`, and the ratio amplitude `0.01575` is only modestly above the ratio SEM `0.0116`. This is weak evidence for a carrier-like Ramsey oscillation, not enough to promote a fitted T2star.
- The expected 13C sidebands at `1.1152 MHz` and `1.8848 MHz` are not supported as a consistent pair. The high sideband target has a small response, while the low sideband is essentially absent.
- The Nyquist-edge response is best treated as a sampling/analysis artifact because it sits at the `0.2 us` sampling Nyquist limit and has poor explanatory value.

## Claims Not Yet Supported

- No well-supported numeric T2star value is established from this measurement.
- No well-supported nearby 13C coupling/sideband conclusion is established.
- The data do not support claiming a clean carrier-plus-13C-sideband model.
- The non-edge `~1.5 MHz` component should not yet be treated as a robust physical Ramsey carrier without additional confirmation, because its amplitude is near the measured uncertainty and other non-edge frequencies remain comparable.
- Do not infer sub-grid precision from the refreshed weak-pi pODMR center; it remains a grid-supported calibration at `3.8765 GHz` with several-100-kHz uncertainty from the project context.

## Recommended Next Action

- Do not run another blind long Ramsey repeat under the same conditions.
- Use this as weak positive det-tracking/carrier-region evidence and move to a targeted protocol change that can produce a more decisive coherence conclusion. The most direct next experiment is a Hahn echo / `auto__cpmg` with `N = 1` on r03 after confirming current tracking and, if needed, refreshing weak-pi pODMR. This should test whether the weak Ramsey contrast is being limited by fast inhomogeneous dephasing or by Ramsey protocol/drive artifacts.
- If the project must close the Ramsey branch before more hardware work, record the current state as: aligned r03 established; Ramsey data are analyzable and show weak carrier-region evidence after refreshed-center calibration; T2star and 13C remain unsupported under current Ramsey conditions.
