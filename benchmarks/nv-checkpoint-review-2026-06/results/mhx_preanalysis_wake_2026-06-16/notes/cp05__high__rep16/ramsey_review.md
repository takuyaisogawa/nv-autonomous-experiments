# Ramsey Review

## Files/data used

- `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`, and `md/knowledge.md` for objective, prior r03 selection, and the required Ramsey review criteria.
- `context.json` for checkpoint notes: the measurement directory contains the terminal data for `nv23_ramsey_20260514_055148_auto_ramsey`.
- `measurement/m001.json`: terminal savedexperiment raw export, `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- `measurement/m002.json`: submitted job spec. Key settings: `mw_freq=3.8765 GHz`, `det=1.5 MHz`, `tau=48 ns..8.048 us`, 41 points, 20 averages, 50000 repetitions.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal result/status/control. Run completed, final counts `43.433 kcps`, no monitor error, no stop request, safe shutdown ok.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Wrote `ramsey_analysis_summary.json` and `ramsey_analysis.png`.
- Verified raw array contract: `ExperimentDataEachAvg` averaged over 20 averages reproduces `ExperimentData`; readout 1 treated as reference and readout 2 as Ramsey signal, consistent with prior local analysis convention.
- Constructed tau axis from export: `48 ns` start, `200 ns` step, `8.048 us` stop, nominal frequency resolution `125 kHz`, Nyquist `2.5 MHz`.
- Checked three views: raw signal, point-wise signal/reference, and signal divided by a fitted reference line.
- Least-squares sinusoid screens used a constant plus linear baseline and scanned `0.2..2.4 MHz`; target checks included carrier `1.500 MHz`, expected 13C sidebands `1.115/1.885 MHz`, prior det-shift top `1.623 MHz`, and old artifact-control `1.192 MHz`.
- Repeated the same checks after skipping the first four tau points.
- Computed per-point SEM from stored averages and per-average dominant ratio frequencies.

## Plausible interpretation

- The run is terminal and analyzable, with no hard bridge/control anomaly in the provided files.
- The programmed carrier is visible only weakly. Full-span carrier amplitudes are `0.705 kcps` raw and `0.0157` in point-wise ratio, versus median SEM of `0.850 kcps` raw signal and `0.0116` ratio. After skipping the first four tau points, carrier ratio amplitude drops to `0.0123`.
- The strongest full-span LS component is near `2.27 MHz` in raw signal, point-wise ratio, and fitted-reference-line normalization. It remains near `2.266 MHz` in the skip-first-4 ratio screen. This is not the programmed `1.5 MHz` carrier, the expected 13C sidebands, the prior `1.623 MHz` det-shift top, or the old `1.192 MHz` control.
- FFT checks are mixed: the ratio FFT top is near the carrier (`~1.517 MHz` full span, `~1.508 MHz` skip-first-4), but the raw and fitted-reference-line FFT tops are not consistently carrier-like. This supports at most a weak carrier-like component, not a robust Ramsey model.
- Expected 13C sideband amplitudes are not coherent: point-wise ratio LS amplitudes are `0.00277` at `1.115 MHz` and `0.00961` at `1.885 MHz`, both below the main carrier/top-screen scale and without per-average support.
- Per-average dominant ratio frequencies are scattered. Within one nominal `125 kHz` bin, only `5/20` averages are near `1.500 MHz`, `1/20` near `1.115 MHz`, and `2/20` near `1.885 MHz`. This is not enough to promote a carrier/sideband/T2star model.

## Claims that are not yet supported

- No supported numeric `T2star` can be claimed from this run. The carrier/decay signal presence is not strong enough relative to SEM and per-average inconsistency.
- No supported nearby `13C` coupling claim can be made. The expected sidebands are weak and inconsistent.
- The `~2.27 MHz` LS maximum should not be interpreted as a physical Ramsey frequency without a control, because it is not predicted by the measurement plan and is close enough to the noise/SEM scale to be a screening artifact.
- A definitive negative `13C` conclusion for r03 is not established by this single run; only the statement that this Ramsey dataset does not show claim-grade sidebands is supported.

## Recommended next action

Avoid another blind repeat of the same long-span Ramsey. The next useful action is an alternate/control diagnostic: verify the current pi/2 pulse calibration at the refreshed center, then run a compact phase-cycled or detuning-sign Ramsey control that should force a clean carrier response if the sequence/readout path is healthy. If that diagnostic still fails to produce a consistent carrier in raw and reference-line-normalized views, record r03 as having unsupported T2star/13C under the current Ramsey route and decide whether to switch protocol or move to another aligned NV candidate.
