# Ramsey Review

## Files/data used

- `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`, and `md/knowledge.md` for project objective, prior r03 resonance evidence, and Ramsey interpretation rules.
- `measurement/m002.json` and `evidence/e010.json` for the submitted second Ramsey contract: `auto__ramsey`, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `tau = 0..8 us`, 41 points, `8 x 50000` repetitions.
- `measurement/m003.json`, `measurement/m004.json`, and `measurement/m005.json` for terminal bridge status/control: completed, final counts `44.184 kcps`, no stop request, safe shutdown ok.
- `measurement/m001.json` for exported savedexperiment raw data: `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`, readout1 reference and readout2 Ramsey signal, snake order, per-average tracking.
- `evidence/e007.json` for the pre-run model: expected carrier at `1.0 MHz`, possible 13C sidebands at `0.615423 MHz` and `1.384577 MHz`, prior scout component to check near `0.884 MHz`, and expected raw oscillation scale of order `2-6 kcps` if the Ramsey signal is comparable to the scout/bounded by pODMR contrast.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs created: `ramsey_analysis_summary.txt` and `ramsey_analysis.png`.
- Checks performed:
  - Parsed combined and per-average readouts from `measurement/m001.json`; shapes were combined `(2, 41)` and per-average `(8, 2, 41)`.
  - Reconstructed the tau grid as `0..8 us`, `dt = 0.2 us`, nominal FFT resolution `125 kHz`, Nyquist `2.5 MHz`.
  - Reviewed raw signal, point-wise signal/reference, and signal normalized to a fitted reference line.
  - Detrended each view and inspected FFT bins.
  - Least-squares screened fixed frequencies at `1.0 MHz`, `0.615423 MHz`, `1.384577 MHz`, and `0.884 MHz`, using offset + linear trend + sine/cosine terms.
  - Checked per-average target-frequency amplitudes and simple scan-order first-half/second-half common-mode shifts.
  - Tried a constrained 1.0 MHz exponentially decaying cosine fit only as a diagnostic; it collapsed to the lower T2* bound and was not used as a claim.

Key numerical results:

- Combined signal mean/range: mean `44.580 kcps`, range `39.308..47.029 kcps`, peak-to-peak `7.721 kcps`.
- Per-average signal means varied strongly: `[48.437, 43.441, 41.201, 49.977, 45.726, 41.383, 36.203, 50.272] kcps`; reference means tracked similar common-mode variation.
- Raw-signal FFT top bins after linear detrending: `0.488 MHz` amplitude `0.862 kcps`, `1.220 MHz` amplitude `0.751 kcps`, `0.122 MHz` amplitude `0.550 kcps`, `1.098 MHz` amplitude `0.541 kcps`, `0.610 MHz` amplitude `0.484 kcps`.
- Fixed-frequency raw-signal least-squares amplitudes were small compared with residuals:
  - `1.0 MHz`: amplitude `0.277 kcps`, residual RMS `1.243 kcps`, amp/resid `0.223`.
  - `0.615423 MHz`: amplitude `0.475 kcps`, residual RMS `1.214 kcps`, amp/resid `0.392`.
  - `1.384577 MHz`: amplitude `0.263 kcps`, residual RMS `1.244 kcps`, amp/resid `0.211`.
  - `0.884 MHz`: amplitude `0.286 kcps`, residual RMS `1.242 kcps`, amp/resid `0.230`.
- Normalized views also did not produce a strong target-frequency result; target amp/resid values stayed below about `0.40`.
- Per-average strongest target frequency was inconsistent: averages 1-3 favored `0.884 MHz`, averages 4 and 7 favored `1.0 MHz`, averages 5-6 favored the lower sideband, and average 8 favored the upper sideband.

## Plausible interpretation

The run completed successfully and produced analyzable Ramsey data, but the data do not support a robust Ramsey carrier at the programmed `1.0 MHz`. The expected `1.0 MHz` component is weak in raw and normalized views, and the fixed-frequency amplitude is far below both the residual scatter and the pre-run expected raw oscillation scale. The largest combined FFT bins are not cleanly at the programmed carrier or the predicted 13C sidebands, and the stored averages disagree on which target frequency is strongest.

The most plausible interpretation is that this second Ramsey follow-up is still non-claim-grade. It weakens the idea that the first scout's `~0.884 MHz` component was a stable physical carrier, because the combined second run also does not support a clean fixed `0.884 MHz` line. The observed structure is more consistent with weak/noisy oscillatory content plus common-mode drift or baseline variation than with a clean Ramsey signal suitable for T2* or 13C extraction.

## Claims that are not yet supported

- No supported numeric T2star value can be claimed from this measurement. The diagnostic 1.0 MHz decaying-cosine fit is fit-only evidence and hits the lower T2* bound.
- No supported nearby 13C conclusion can be claimed. The lower-sideband fixed-frequency amplitude is the largest of the target checks in the combined raw data, but it is still only `0.475 kcps` against `1.214 kcps` residual RMS and is not consistent across averages.
- The programmed `1.0 MHz` Ramsey carrier is not established.
- The prior `~0.884 MHz` scout component is not established as a stable physical feature.
- The fine weak-pi pODMR center at `3.8759 GHz` remains supported as a frequency calibration input, but this Ramsey run does not prove that it yields a claim-grade T2* signal under the present sequence/settings.

## Recommended next action

Do not fit or report T2star/13C from this run. Treat the second Ramsey as a completed negative diagnostic on r03 under `auto__ramsey` at `det = 1.0 MHz`.

Before another T2star attempt, run a bridge-free route/protocol and data-shape review focused on why `auto__ramsey` is not yielding a clear carrier despite supported pODMR resonance: re-check the active Ramsey XML/manifest timing and phase-ramp semantics, compare the two Ramsey raw exports side by side, and decide whether the next physical measurement should be a shorter/high-contrast Ramsey diagnostic, a phase/readout-control Ramsey variant, or a branch closure/no-13C conclusion for r03 rather than another blind repeat.
