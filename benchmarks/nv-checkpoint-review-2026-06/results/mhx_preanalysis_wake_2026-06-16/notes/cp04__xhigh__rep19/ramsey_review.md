# Ramsey Det-Shift Review

## Files/Data Used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New measurement: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` status, `measurement/m005.json` control.
- Prior comparison/model context: `evidence/e008.json` prior det=1.0 MHz short-tau terminal review, `evidence/e019.json` det-shift model/advisory.
- Generated locally: `analyze_ramsey_detshift.py`, `ramsey_detshift_analysis.json`, `ramsey_detshift_review.png`.

## Calculations/Scripts Run

- Ran `python analyze_ramsey_detshift.py`.
- Verified raw axis contract: `ExperimentDataEachAvg` is `[scan, avg, readout, point]`; averaging per-average readouts reproduces `ExperimentData`.
- Readout basis from saved `ramsey.xml`/metadata: `full_experiment=0`, readout 1 is reference and readout 2 is Ramsey signal.
- Terminal/run checks: job `nv23_ramsey_20260514_015423_auto_ramsey` completed, `12 x 90000` shots per tau, final count `44.796 kcps`, monitor `last_error=''`, `stop_requested=false`.
- Grid: `tau = 0.048..1.968 us`, 41 points, 48 ns step; FFT bin spacing `0.508 MHz`, nominal span resolution `0.521 MHz`, Nyquist `10.42 MHz`.
- Noise/structure: median per-point SEM `0.711 kcps` signal and `0.0126` ratio; first `0.75 us` peak-to-peak `6.46 kcps` signal and `0.134` ratio. Per-average signal/reference means are strongly common-mode correlated (`r = 0.90`).
- Main LS frequency screens:
  - All-tau point-wise ratio top: `1.623 MHz`, amplitude `0.02547`, residual R2 improvement `0.430`.
  - Raw signal top: `0.882 MHz`, amplitude `1.533 kcps`, residual R2 improvement `0.577`.
  - Signal over fitted reference line top: `0.882 MHz`, amplitude `0.03193`, residual R2 improvement `0.576`.
  - With `tau <= 0.2 us` excluded, tops shift to `0.746 MHz` ratio and `0.806 MHz` raw/signal-over-refline.
- Target checks:
  - Programmed `1.500 MHz` carrier: ratio amplitude `0.02399`, raw amplitude `1.128 kcps`.
  - Prior-feature det-tracking carrier `1.692 MHz`: ratio amplitude `0.02505`, raw amplitude `1.225 kcps`.
  - Fixed prior `1.192 MHz` artifact-control: ratio amplitude only `0.00511`, raw amplitude `0.474 kcps`.
  - Programmed sidebands `1.115/1.885 MHz`: ratio amplitudes `0.0108/0.0173`.
  - Det-tracking sidebands `1.307/2.077 MHz`: ratio amplitudes `0.0095/0.0061`.
- Descriptive damped-sinusoid fits are not promoted: raw/signal-over-refline prefer about `0.818 MHz`, `T2* ~0.717 us`; point-wise ratio prefers about `0.678 MHz`, `T2* ~0.469 us`.
- `ramsey_detshift_review.png` was generated and verified as a valid PNG by PIL; the local image-viewer tool could not open it due to an access error.

## Plausible Interpretation

The det-shift run is terminal and analyzable, with no hard run/control anomaly in the provided snapshot. It does not simply reproduce the prior fixed `~1.192 MHz` ratio component, which argues against blindly promoting that earlier line as a stable fixed feature.

However, the run still does not support a clean physical Ramsey carrier model. The key problem is readout/view disagreement: point-wise ratio favors `~1.62 MHz`, while raw signal and fitted-reference-line normalization favor `~0.88 MHz`; excluding early tau points shifts the preferred frequencies again. The data are plausibly dominated by a short-time transient and/or common-mode/reference/baseline structure rather than a stable carrier plus sidebands.

## Claims Not Yet Supported

- No numeric `T2*` is supported from this measurement.
- No nearby `13C` conclusion is supported.
- A carrier at the programmed `1.500 MHz` is not supported as claim-grade.
- A det-tracking carrier at `~1.692 MHz` is not supported as claim-grade.
- The `~0.88 MHz` raw/signal-over-refline feature should not be claimed physical; it is view- and window-sensitive and overlaps earlier non-claim-grade behavior.
- A scan-order-aware MATLAB drift result for this terminal run is not present in the neutral snapshot; only the saved snake order and per-average common-mode checks were available here.

## Recommended Next Action

Stop blind Ramsey repeats on r03. Make a branch decision: either move to an alternate coherence/13C protocol with a fresh quantitative model and signal-resolvability check, or close the r03 Ramsey/T2star/13C branch as unsupported under the current Ramsey route. If continuing experimentally, do not fit/promote `T2*` until raw/readout-aware signal presence is established under the alternate protocol.
