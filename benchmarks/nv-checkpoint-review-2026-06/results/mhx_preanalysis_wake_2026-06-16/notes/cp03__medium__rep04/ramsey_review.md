# Ramsey Review: r03 Short-Tau High-SNR Diagnostic

## Files/data used

- `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json` for project context and prior decisions.
- `measurement/m001.json`: terminal raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
- `measurement/m002.json`: job spec for the short-tau Ramsey diagnostic.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal bridge result, status, and control for `nv23_ramsey_20260513_230331_auto_ramsey`.
- `evidence/e017.md` for the design/start note of this short-tau diagnostic.
- Prior context in `project/state.md` for comparison with the two earlier non-claim-grade Ramsey runs.

## Calculations or scripts run

- Ran local Python parsing of `measurement/m001.json`.
- Wrote scratch outputs:
  - `ramsey_analysis_summary.json`
  - `ramsey_shorttau_analysis.png`
- Checks performed:
  - Confirmed scan metadata: `tau = 48 ns..1.968 us`, 41 points, 48 ns step, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, 12 averages x 90000 repetitions = `1.08e6` shots per tau point.
  - Used readout 1 as reference and readout 2 as Ramsey signal, consistent with prior project protocol basis for `ramsey.xml` with `full_experiment=0`.
  - Compared raw readouts, point-wise ratio, and signal normalized to a fitted reference line.
  - Fitted linear-baseline-plus-sinusoid least-squares screens at 1.0 MHz, expected 13C sideband positions near 0.615 and 1.385 MHz, and the prior exploratory 0.884 MHz feature.
  - Ran a frequency screen over 0.1..5.0 MHz and an FFT check after linear detrending.
  - Checked per-average 1 MHz amplitude/phase consistency.
  - Computed a direct scan-order common-mode trend check from `ScanOrderEachAvg`.

## Quantitative findings

- Terminal run completed safely with no stop request or monitor error; final count text was `35.122 kcps`, above the 20 kcps execution threshold but lower than the previous `44.184 kcps` final count.
- Raw reference readout is comparatively stable: mean `48.573 kcps`, tau std `0.456 kcps`, peak-to-peak `2.176 kcps`.
- Raw Ramsey signal has much larger tau structure: mean `44.655 kcps`, tau std `1.574 kcps`, peak-to-peak `6.499 kcps`, from `40.698 kcps` at 48 ns to `47.197 kcps` at 1.344 us.
- Median across-average SEM is about `1.14 kcps` for the signal and `0.0127` for the ratio, so the full raw signal excursion is several SEM and larger than the reference variation.
- Least-squares at the programmed 1.0 MHz carrier:
  - raw signal amplitude `1.28 kcps`, residual R2 improvement `0.377`;
  - point-wise ratio amplitude `0.0274`, R2 improvement `0.355`;
  - signal/fitted-reference-line amplitude `0.0264`, R2 improvement `0.378`.
- Per-average signal/fitted-reference-line 1 MHz amplitudes are present in all 12 averages (`0.014..0.040` ratio units). Most phases cluster near `-pi`; averages 10 and 12 are weaker/outlying but not contradictory enough to erase the combined signal.
- Direct common-mode scan-order check did not show a hard count-collapse pattern: no average exceeded a 15% negative common-mode drop; the worst negative trend was average 10 at about `-6.0%`, while average 7 rose about `+11.7%`.
- The broad frequency screen on signal/fitted-reference-line peaks near `1.187 MHz` with amplitude `0.0346` and R2 improvement `0.681`; this is stronger than the fixed 1.0 MHz component but is not enough to claim a shifted carrier because the window is only 1.92 us and model parameters are highly correlated.
- FFT resolution is coarse for 13C interpretation: bin spacing is about `0.508 MHz`. The largest FFT bin in normalized views is `1.524 MHz`, close to the high-sideband region but also compatible with leakage/windowing from the short, decaying, non-sinusoidal trace.
- A simple grid fit at fixed 1.0 MHz with exponential envelope prefers very short apparent decay times (`~0.16..0.18 us` depending on view), but this is not claim-grade because the fit is front-loaded, sensitive to baseline/phase, and the acquisition spans fewer than two programmed carrier periods.

## Plausible interpretation

- This short-tau/high-SNR diagnostic supports the presence of an early-time Ramsey-like modulation on accepted r03. The earlier 8 us/non-claim-grade runs likely diluted or obscured the useful signal by spending most samples after the contrast had strongly decayed and by including baseline/artifact structure.
- The data are consistent with a short T2star failure mode, plausibly sub-microsecond and possibly a few tenths of a microsecond, but the present dataset should be treated as a signal-presence diagnostic rather than a precise T2star measurement.
- The 0.884 MHz feature from the first scout is not supported here; its fixed-frequency LS amplitude is much smaller than the 1 MHz and 1.18 MHz screens.

## Claims not yet supported

- No precise numeric T2star claim is supported from this run.
- No nearby 13C conclusion is supported. The short 1.92 us span gives poor sideband resolution, and the apparent 1.5 MHz FFT/bin strength cannot be separated from windowing, leakage, or model mismatch.
- No claim is supported that the carrier is truly shifted from 1.0 MHz to 1.187 MHz; that peak comes from an exploratory short-window screen with correlated baseline/phase/decay parameters.
- No claim is supported that r03 lacks a Ramsey signal. This run argues the opposite: a real early-time modulation is present.

## Recommended next action

Run a non-blind parameter-extraction Ramsey on r03 designed around the newly observed short early-time signal, not another 8 us blind repeat. A good next diagnostic is a shorter-window, higher-carrier Ramsey, e.g. det around `3 MHz` with dense 24-48 ns tau sampling over roughly the first `1 us`, maintaining high shots per point and even averages. The goal should be to pack several carrier cycles inside the likely short T2star envelope so T2star, phase, and baseline are less degenerate. Defer 13C sideband claims until a carrier/decay model is stable; if that succeeds, follow with a longer or dedicated spectroscopy measurement for 13C.
