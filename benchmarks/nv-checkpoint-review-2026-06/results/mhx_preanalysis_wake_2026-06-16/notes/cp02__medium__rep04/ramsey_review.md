# Ramsey Review

## Files/data used

- `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md` for objective, prior r03 pODMR/Ramsey context, and local analysis rules.
- `evidence/e013.md` for the fine-pODMR basis and second-Ramsey plan.
- `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- `measurement/m002.json` through `measurement/m005.json`: job contract, terminal result, status, and control for `nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg`.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis_summary.json` and `ramsey_review_plot.png`.
- Parsed `ExperimentData` shape `[1, 2, 41]` and `ExperimentDataEachAvg` shape `[1, 8, 2, 41]`.
- Confirmed scan settings: `tau = 0..8 us`, 41 points, `dt = 0.2 us`, Nyquist `2.5 MHz`, FFT bin spacing `0.12195 MHz`, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `8 x 50000` repetitions.
- Checked raw signal, point-wise `signal/reference`, and signal normalized by a fitted reference line.
- Ran Hann FFTs after linear detrending and least-squares sinusoid checks at:
  - prior component: `0.884 MHz`
  - expected 13C sidebands: `0.6155 MHz` and `1.3845 MHz`
  - programmed carrier: `1.0 MHz`
- Ran a descriptive damped-cosine fit only as a sanity check, not as claim evidence.

## Plausible interpretation

- The run completed cleanly: terminal result reports `completed`, final counts `44.184 kcps`, no stop request, and saved data present.
- The combined raw signal has substantial variation (`39.31..47.03 kcps`, peak-to-peak `7.72 kcps`), but the spectral content is not well aligned with the planned physics check.
- FFT peaks are view-dependent:
  - raw signal top peaks: `1.2195 MHz`, `0.4878 MHz`, `2.1951 MHz`
  - point-wise ratio top peaks: `1.0976 MHz`, `0.4878 MHz`, `1.7073 MHz`
  - reference-line-normalized top peaks: `1.2195 MHz`, `0.4878 MHz`, `2.1951 MHz`
- Direct least-squares amplitudes at the planned frequencies are weak in the combined data:
  - raw signal: carrier `1.0 MHz` is `0.277 +/- 0.287 kcps` (`~0.96 sigma`, `R2 ~ 0.024`)
  - raw lower sideband `0.6155 MHz` is `0.475 +/- 0.287 kcps` (`~1.65 sigma`, `R2 ~ 0.069`)
  - raw upper sideband `1.3845 MHz` is `0.262 +/- 0.287 kcps` (`~0.92 sigma`, `R2 ~ 0.022`)
  - prior `0.884 MHz` component is `0.286 +/- 0.286 kcps` (`~1.00 sigma`, `R2 ~ 0.026`)
- Normalized views do not rescue the carrier or sidebands; the line-normalized carrier is `~0.96 sigma`, lower sideband `~1.65 sigma`, upper sideband `~0.92 sigma`.
- Per-average means vary strongly: signal average means span `36.20..50.27 kcps` (`14.07 kcps` span). This is large compared with the target sub-kcps LS amplitudes and makes drift/common-mode behavior important provenance.
- The descriptive damped-cosine fit is not reliable for T2star: it lands at the imposed lower bound `T2* = 0.2 us`, has large frequency uncertainty (`1.323 +/- 0.536 MHz`), and should not be promoted.
- Best interpretation: this second Ramsey is analyzable but non-claim-grade. It does not support a programmed `1.0 MHz` Ramsey carrier, does not support 13C sidebands near `0.615/1.385 MHz`, and does not support the prior `~0.884 MHz` component as a stable physical line. The data are more consistent with weak/inconsistent oscillatory content plus drift/baseline effects or a Ramsey/readout/phase-ramp issue than with a clean T2star/13C measurement.

## Claims that are not yet supported

- No supported T2star value from this run.
- No supported nearby-13C conclusion from this run.
- No supported claim that the prior `~0.884 MHz` feature is physical.
- No supported claim that the det-shifted Ramsey carrier follows the programmed `det = 1.0 MHz`.
- No claim of sub-grid pODMR center precision beyond the prior grid-supported `3.8759 GHz` basis.

## Recommended next action

Do not blindly repeat the same 0..8 us, 41-point Ramsey. Treat the r03 pODMR alignment as still supported, but treat the Ramsey/T2star route as unresolved. The next experiment should be diagnostic: either verify the Ramsey phase-ramp/readout behavior on a known-good/control condition, or run a shorter, denser low-tau Ramsey diagnostic designed to test whether coherence is decaying before the current 0.2 us sampling can robustly establish the carrier. Only return to a longer T2star/13C acquisition after a clear Ramsey carrier is recovered.
