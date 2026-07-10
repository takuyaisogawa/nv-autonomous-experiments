# Ramsey Review: Refreshed-Center r03 Long-Span Run

## Files/data used

- `project/state.md`, `project/brief.md`, `project/advice.md`, `context.json`: project objective, prior r03 acceptance, prior non-claim-grade Ramsey history, and planned terminal review criteria.
- `measurement/m001.json`: terminal savedexperiment raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- `measurement/m002.json`: executed job spec for `nv23_ramsey_20260514_055148_auto_ramsey`.
- `measurement/m003.json`: terminal bridge result; run completed, final counts `43.433 kcps`, safe shutdown true, no error code.
- `measurement/m004.json`, `measurement/m005.json`: terminal status/control; completed, no stop request.
- `evidence/e014.json`: pre-run model and frequency targets: carrier `1.500 MHz`, expected 13C sidebands `1.115 MHz` and `1.885 MHz`, 41 tau points from `48 ns` to `8.048 us`, `20 x 50000` shots.

## Calculations/scripts run

- Created and ran `analyze_ramsey_m005.py`.
- Outputs: `ramsey_analysis_m005.json` and `ramsey_analysis_m005.png`.
- Checks performed:
  - Verified `ExperimentDataEachAvg` axis contract as `[scan, avg, readout, point]` by reproducing combined `ExperimentData`.
  - Extracted readout 1 as reference and readout 2 as signal, then reviewed raw signal, `signal/ref`, and signal normalized to a fitted reference line.
  - Computed per-point SEM across 20 stored averages: median signal SEM `0.850 kcps`, median `signal/ref` SEM `0.0116`.
  - Ran least-squares sinusoid screens from `0.2..2.45 MHz` for full data and after skipping first 4 tau points.
  - Checked target amplitudes at carrier, expected sidebands, prior det-shift top, prior skip-transient top, and prior short-tau empirical top.
  - Ran FFT checks on detrended combined views.
  - Ran bootstrap consistency checks over the 20 stored averages for target sinusoid coefficients.
  - Ran a descriptive damped-sinusoid grid screen; this was not used as a claim-grade fit.
  - Ran a local scan-order-aware drift advisory using `ScanOrderEachAvg`; per-average mean counts varied, but first/second-half acquisition-order ratio shifts were modest: median `0.0135`, max `0.0403`, none above `0.05`.

## Quantitative result

- Acquisition health is acceptable: completed, `20 x 50000 = 1.0e6` shots per tau point, final counts `43.433 kcps`, no stop/error, snake scan order, axis contract verified.
- Combined full-span `signal/ref` LS screen is strongest near `2.270 MHz` with amplitude `0.01845`; after skipping first 4 tau points it remains near `2.266 MHz` with amplitude `0.01418`.
- Programmed carrier `1.500 MHz` is present but not dominant:
  - `signal/ref` full-span amplitude `0.01575`;
  - raw-signal full-span amplitude `0.705 kcps`, below the median per-point signal SEM `0.850 kcps`;
  - bootstrap over stored averages gives carrier `signal/ref` amplitude median about `0.0163` with 95% interval `0.0118..0.0209`.
- Expected 13C sidebands are not a supported pair:
  - low sideband `1.115 MHz`: `signal/ref` amplitude `0.00278`, bootstrap coefficient intervals include zero;
  - high sideband `1.885 MHz`: `signal/ref` amplitude `0.00962`, weak/isolated and not accompanied by the low sideband.
- FFT of `signal/ref` has coarse high bins near `1.463`, `1.585`, `2.317`, and `2.195 MHz`; it does not uniquely support the carrier/sideband model.
- Per-average frequency screens are mixed rather than clustered at one physical target.
- Descriptive damped grid on `signal/ref` prefers about `2.275 MHz` and `T2star ~2.5 us`; fixed-carrier `1.5 MHz` gives a worse descriptive fit with `T2star ~2.1 us`. Because the frequency assignment is not clean, neither value should be promoted.

## Plausible interpretation

The data contain weak Ramsey-like oscillatory content, and the programmed carrier band is more credible than in some earlier null-looking runs because the carrier projection is coherent across stored averages. However, the dominant combined LS feature is still not the planned carrier or the expected 13C sidebands, the FFT view is not unique, and per-average screens remain inconsistent. This looks like a weak/mixed Ramsey response with residual drift/transient or analysis-sensitive spectral structure, not a clean carrier-decay/13C-sideband measurement.

This refreshed-center run is useful evidence that simply adding shots at the refreshed pODMR center does not produce a claim-grade Ramsey/13C spectrum under the current protocol.

## Claims not yet supported

- No numeric T2star claim is supported.
- No nearby 13C claim is supported.
- The `2.27 MHz` component should not be assigned to a physical transition/coupling from this dataset alone.
- The isolated high-sideband-sized component near `1.885 MHz` is not enough for a 13C conclusion without the expected paired/consistent sideband evidence.
- The weak `1.5 MHz` carrier projection is not enough by itself to promote a decay fit.

## Recommended next action

Do not run another blind long Ramsey repeat on r03. Record the Ramsey branch as non-claim-grade under the current conditions. If the project must continue beyond this conclusion, switch to an alternate targeted protocol rather than more accumulation: refresh/confirm the resonance only if needed, then use a more robust coherence or 13C-sensitive sequence such as Hahn/CPMG/XY8-style follow-up, with a pre-run model for the expected signal and a clear claim criterion. If no alternate protocol is pursued, the supported conclusion is that r03 remains an aligned NV, but current Ramsey data do not support T2star or 13C extraction.
