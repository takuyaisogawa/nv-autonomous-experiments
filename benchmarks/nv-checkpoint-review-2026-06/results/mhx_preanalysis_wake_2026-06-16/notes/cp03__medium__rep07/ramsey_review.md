# Ramsey review: short-tau high-SNR r03 diagnostic

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, and `evidence/e017.md`.
- New measurement artifacts: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job plan, `measurement/m003.json` terminal result, `measurement/m004.json` final status, and `measurement/m005.json` control state.
- Scratch outputs created here: `analyze_ramsey.py`, `ramsey_analysis.json`, and `ramsey_analysis.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey.py`.
- Parsed `measurement/m001.json` as a 41-point Ramsey scan with tau `0.048..1.968 us` in `48 ns` steps, `12` stored averages, `90000` repetitions per average, and two raw readout channels.
- Computed combined readouts, per-average SEM, readout ratio `readout1/readout0`, FFT amplitudes after linear detrending, least-squares sinusoid-plus-linear-baseline screens, and target fits at:
  - programmed carrier: `1.000 MHz`
  - expected low 13C sideband: `0.615423 MHz`
  - expected high 13C sideband: `1.384577 MHz`
- Did simple scan-order diagnostics using `ScanOrderEachAvg` snake ordering by comparing first-half vs second-half common-mode counts within each average.

## Quantitative checks

- Measurement completed normally: `measurement/m003.json` status is `completed`; `measurement/m004.json` state is `completed`; no stop was requested in `measurement/m005.json`.
- Combined means: readout0 `48.57 kcps`, readout1 `44.65 kcps`.
- Median exported channel errors are `1.46 kcps` and `1.40 kcps`; median SEM across stored averages is `1.12 kcps`, `1.14 kcps`, and `0.0127` for the `readout1/readout0` ratio.
- Ratio peak-to-peak over the tau scan is `0.143`, so the short-window data are not flat at the combined-average level.
- For `readout1/readout0`, least-squares target amplitudes are:
  - `1.000 MHz`: amplitude `0.0274`, baseline residual improvement `0.355`
  - `0.615423 MHz`: amplitude `0.0243`, improvement `0.311`
  - `1.384577 MHz`: amplitude `0.0271`, improvement `0.345`
- The strongest combined ratio least-squares screen is near `1.192 MHz`, amplitude `0.0363`, improvement `0.656`, not exactly at the programmed carrier or either expected 13C sideband.
- The strongest ratio FFT bin is `1.524 MHz` with amplitude `0.0287`; the nearest programmed-carrier bin `1.016 MHz` has amplitude `0.0222`. The finite `1.92 us` window gives broad/ambiguous frequency discrimination.
- Per-average ratio screens are not cleanly locked to one frequency. Several averages prefer low-frequency edge/baseline-like components around the `0.2 MHz` lower scan bound; others prefer about `1.13..1.29 MHz`; one prefers `2.10 MHz`. The `1.0 MHz` target is present in each average but with variable amplitude.
- Scan-order first-half/second-half common-mode shifts range from about `-1.42` to `+2.91 kcps`; this is not a hard failure by itself, but it is comparable to the raw oscillation scale and should remain part of the uncertainty budget.

## Plausible interpretation

This short-tau/high-SNR run is better than the two prior long-window Ramsey attempts for detecting early-time structure: it shows a visible combined-average oscillatory component in the raw lower-count readout and in the readout ratio. A Ramsey-like early-time signal on r03 is therefore plausible.

The frequency assignment is not yet clean. The programmed `1.0 MHz` carrier is present, but the best combined least-squares screen is nearer `1.19 MHz`, and the FFT peak lands on a broad bin near `1.52 MHz`. The short window, linear-baseline covariance, scan-order/common-mode movement, and mixed per-average preferred frequencies mean this dataset should be treated as evidence for possible early-time Ramsey contrast, not as a calibrated frequency or decay result.

## Claims not yet supported

- No numeric T2star should be claimed from this dataset. The window covers less than two programmed-carrier cycles and does not establish a robust decay envelope independent of baseline and frequency choice.
- No nearby 13C claim is supported. The expected sideband frequencies are not uniquely dominant, and the high-sideband target is hard to distinguish from the broad combined feature in this short window.
- The previous non-claim-grade long-window Ramsey features are still not validated as physical sidebands or carrier response.
- This run does not invalidate the r03 alignment conclusion; that remains supported by the earlier pODMR evidence in `project/state.md`.

## Recommended next action

Do not make another blind long-window Ramsey repeat. The next useful step is a targeted confirmation of frequency assignment: run a same-short-window, high-SNR Ramsey diagnostic with a deliberately changed programmed detuning, or a phase-cycled/quadrature Ramsey if available, and require the observed early-time component to follow the programmed detuning before fitting T2star. Only after detuning-following carrier evidence is established should a longer or denser follow-up be used for T2star envelope and 13C-sideband claims.
