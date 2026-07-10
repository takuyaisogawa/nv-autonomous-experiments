# Ramsey Review: det=1.5 MHz Short-Tau Shift Check

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New completed Ramsey run: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control.
- Comparison/context evidence: `evidence/e008.json` prior terminal det=1.0 MHz short-tau review, `evidence/e019.json` det-shift model/plan.
- New local artifacts created: `analyze_ramsey_detshift.py`, `ramsey_detshift_analysis.json`, `ramsey_detshift_review.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey_detshift.py`.
- Verified `ExperimentDataEachAvg` axis contract as `[scan, avg, readout, point]` by averaging per-average readouts back to `ExperimentData`.
- Used readout1 as reference and readout2 as Ramsey signal for `ramsey.xml` with `full_experiment=0`.
- Reconstructed tau grid: `0.048..1.968 us`, 41 points, `48 ns` step, 12 averages x 90000 repetitions = `1.08e6` shots/tau point.
- Ran local scan-order common-mode drift check using `ScanOrderEachAvg` snake order; no averages flagged.
- Calculated raw signal/reference statistics, per-point SEM, linear-detrended FFT, least-squares sinusoid screens, target-frequency amplitudes, per-average frequency screens, and a descriptive damped-sinusoid grid fit.
- Checked generated figure dimensions with PIL: `1650 x 1800` RGBA.

## Quantitative checks

- Run status: completed, final counts `44.796 kcps`, stop requested `false`, monitor error empty.
- Median per-point SEM: signal `0.711 kcps`, ratio `0.01262`.
- Frequency resolution is coarse for precise assignment: FFT bin spacing `0.508 MHz`, nominal `1/span = 0.521 MHz`, Nyquist `10.42 MHz`.
- Combined ratio LS screen top: `1.623 MHz`, ratio amplitude `0.02547`, raw-signal amplitude `1.252 kcps`, R2 improvement `0.430`.
- Programmed carrier `1.500 MHz`: ratio amplitude `0.02399`, raw-signal amplitude `1.128 kcps`.
- Predicted det-tracking carrier from previous `1.192 MHz` feature: `1.692 MHz`, ratio amplitude `0.02505`, raw-signal amplitude `1.225 kcps`.
- Previous artifact-control frequency `1.192 MHz`: weak in this run, ratio amplitude `0.00511`, raw-signal amplitude `0.474 kcps`.
- 13C sideband targets are not dominant:
  - Programmed low/high sidebands `1.115/1.885 MHz`: ratio amplitudes `0.01076/0.01732`.
  - Det-tracking low/high sidebands `1.307/2.077 MHz`: ratio amplitudes `0.00953/0.00614`.
- Per-average frequency screens are inconsistent; top per-average frequencies scatter across low-frequency, carrier-band, and edge-like components.
- Descriptive damped-sinusoid ratio fit prefers `0.678 MHz`, `T2* ~0.469 us`, but this is not promoted because carrier assignment failed and the fit is model-sensitive over the short window.

## Plausible interpretation

The new det=1.5 MHz Ramsey run is terminal and analyzable, with no local drift flag. The previous fixed `~1.192 MHz` feature is not strong in the combined data. The main response moved into the broad `1.5..1.7 MHz` carrier band, so the data are coarsely det-responsive.

However, the short tau span only gives about `0.52 MHz` frequency resolution, the LS amplitudes at `1.5`, `1.623`, and `1.692 MHz` are similar, and the per-average frequency screens do not agree. This supports "not simply the old fixed 1.192 MHz component" more than it supports a clean Ramsey carrier. The data still do not justify a numeric T2star or nearby-13C assignment.

## Claims not yet supported

- A precise Ramsey carrier frequency from this run.
- A well-supported numeric T2star for r03.
- A nearby 13C conclusion or sideband model.
- A claim that the prior `~1.192 MHz` feature was definitively a fixed apparatus artifact; it is disfavored in the combined det-shift data, but the mechanism remains unresolved.
- A physical interpretation based on the descriptive damped-sinusoid fit.

## Recommended next action

Do not run another blind Ramsey repeat on r03 under the same `auto__ramsey` conditions. Treat the current Ramsey/T2star/13C branch as unsupported under this protocol unless an alternate, hypothesis-driven check is chosen. The next useful action is a protocol/calibration diagnostic or alternate T2-family measurement designed to separate pulse-sequence/baseline transient behavior from true free precession before any T2star or 13C claim.
