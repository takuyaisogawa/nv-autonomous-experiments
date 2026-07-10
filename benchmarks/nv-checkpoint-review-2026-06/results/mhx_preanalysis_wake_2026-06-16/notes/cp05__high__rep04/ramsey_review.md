# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`.
- Measurement files: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` status, `measurement/m005.json` control.
- Model/planning context: `evidence/e014.json`.
- Scratch outputs created here: `analyze_ramsey_m001.py`, `ramsey_review_analysis.json`, `ramsey_review_plot.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey_m001.py`.
- Verified raw axis contract: `ExperimentData` shape `[1,2,41]`; `ExperimentDataEachAvg` shape `[1,20,2,41]`; mean of the 20 stored averages reproduces `ExperimentData` to `1.4e-14 kcps`.
- Confirmed terminal run parameters from local files: `auto__ramsey`, tau `48 ns..8.048 us` in 41 points, `mw_freq=3.8765 GHz`, `det=1.5 MHz`, `20 x 50000` shots, final counts `43.433 kcps`, no stop request.
- Used readout role from local model note: readout 1 reference, readout 2 Ramsey signal.
- Computed raw signal, pointwise signal/reference, and signal/fitted-reference-line views.
- Computed SEM across stored averages: median raw signal SEM `0.850 kcps`; median ratio SEM `0.0116`.
- Ran acquisition-order common-mode drift proxy using `ScanOrderInfo` snake order; no stored average had a common-mode drop larger than 15%.
- Ran LS sinusoid frequency screens and Hann-window FFT checks for full data and after skipping the first 4 tau points.

## Plausible interpretation

- The data are analyzable and have no hard terminal/run anomaly in the local files.
- A weak carrier-consistent component is present near the programmed detuning:
  - LS raw full-span top peaks include `2.271 MHz` at `0.818 kcps` and `1.515 MHz` at `0.723 kcps`; the exact `1.500 MHz` target is `0.705 kcps`.
  - LS raw skip-first-4 peaks include `2.271 MHz` at `0.555 kcps` and `1.517 MHz` at `0.525 kcps`; exact `1.500 MHz` target is `0.512 kcps`.
  - FFT raw full-span nearest carrier bin `1.463 MHz` has `0.529 kcps`; skip-first-4 nearest carrier bin `1.486 MHz` has `0.514 kcps`.
- Normalized views are qualitatively similar: carrier-near power is present, but a `~2.27 MHz` component remains comparable or larger.
- The old fixed `~1.192 MHz` control is weak in the combined views, so this run is not simply reproducing that earlier fixed feature.
- Expected 13C sideband targets are not supported as a coherent pair. In LS raw full-span, low/high sideband amplitudes are only `0.146/0.261 kcps`; skip-first-4 they drop to `0.012/0.124 kcps`. Normalized views also do not show a stable sideband-pair pattern.
- Per-average raw frequency screens are mixed: only a few stored averages top near the programmed carrier, while many top at low-frequency, `~2.2 MHz`, or other frequencies. This weakens any physical assignment from the combined spectrum alone.
- A forced descriptive carrier-envelope grid fit chooses about `T2star = 1.0 us`, amplitude `3.82 kcps`, RMS residual `0.69 kcps`, but this is dominated by early-time structure and is not promoted.

## Claims not yet supported

- No claim-grade numeric T2star is supported from this run.
- No nearby 13C claim is supported; the expected sidebands around `1.115 MHz` and `1.885 MHz` are not consistent across full/skip and raw/normalized checks.
- The competing `~2.27 MHz` feature is not assigned to NV physics; it could be analysis/systematic/transient-related without more evidence.
- The forced carrier-envelope fit is not evidence for a final T2star value.

## Recommended next action

Do not run another blind Ramsey repeat on this branch. Treat the refreshed-center Ramsey as weak carrier evidence but non-claim-grade for T2star/13C, then choose an alternate diagnostic/protocol or close the r03 Ramsey branch with an explicit unsupported T2star and unsupported nearby-13C conclusion under the measured conditions.
