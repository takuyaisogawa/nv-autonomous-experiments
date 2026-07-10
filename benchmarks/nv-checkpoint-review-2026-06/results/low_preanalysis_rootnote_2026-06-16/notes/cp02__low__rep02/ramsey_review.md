# Ramsey Review: r03 det=1.0 MHz follow-up

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`.
- Measurement contract/control/status/result: `measurement/m002.json`, `measurement/m005.json`, `measurement/m004.json`, `measurement/m003.json`.
- Raw savedexperiment export: `measurement/m001.json`, from `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- Local analysis outputs created: `analysis/ramsey_det1p0_analysis_summary.json`, `analysis/ramsey_det1p0_trace.png`, `analysis/ramsey_det1p0_fft.png`.

## Calculations or scripts run

- Ran local Python inspection of `measurement/m001.json`:
  - extracted combined signal/reference arrays and 8 stored averages;
  - formed median-normalized `signal/reference` fractional trace;
  - checked snake scan-order common-mode first-half vs second-half changes per average;
  - computed Hann-window FFT of the combined normalized trace;
  - ran linear least-squares sinusoid checks at expected frequencies: `0.615`, `1.000`, `1.385 MHz`, plus prior scout feature `0.884 MHz`;
  - ran an exploratory damped-cosine fit only as a descriptive check, not as claim evidence.

Key numeric checks:

- Run completed cleanly: `8 x 50000`, `tau = 0..8 us`, 41 points, `dt = 0.2 us`, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, final counts `44.184 kcps`.
- Combined `signal/reference` fractional range after median normalization: `-6.9%` to `+12.8%`.
- FFT nominal bin spacing from the finite trace is `~121.95 kHz`. Strongest FFT bins were near `1.098 MHz`, `1.220 MHz`, and `0.976 MHz`; the expected sideband-near bin at `0.610 MHz` was present but smaller.
- Least-squares amplitudes on the combined normalized trace:
  - `0.615 MHz`: `1.22%` amplitude, residual RMS `3.18%`;
  - `0.884 MHz`: `0.86%` amplitude, residual RMS `3.23%`;
  - `1.000 MHz`: `1.09%` amplitude, residual RMS `3.20%`;
  - `1.385 MHz`: `0.97%` amplitude, residual RMS `3.22%`.
- Per-average 1.0 MHz amplitudes varied from `0.47%` to `2.72%`, with inconsistent quadrature signs/phases.
- Common-mode scan-order changes were modest to moderate across averages, about `-1.25%` to `+5.65%`; not a simple hard failure, but enough to keep drift/readout variation in the uncertainty budget.
- Exploratory damped-cosine fit found `f ~1.20 MHz`, `T2* ~0.94 us`, `R2 ~0.50`; this is not robust enough to use as a T2star claim.

## Plausible interpretation

- The det-shift diagnostic is partially encouraging: unlike the first Ramsey scout, the largest FFT content is now clustered around the programmed `1.0 MHz` carrier region rather than staying at the prior `~0.884 MHz` feature.
- However, the carrier is weak in direct least-squares checks and not stable across stored averages. The combined trace likely contains a real but low-SNR Ramsey component mixed with readout/reference fluctuations and per-average variation.
- There is no persuasive 13C sideband evidence. The expected sidebands near `0.615` and `1.385 MHz` are not stronger or more consistent than the carrier/prior-feature checks.

## Claims that are not yet supported

- Do not claim a well-supported T2star. The descriptive fit is low-quality and per-average consistency is insufficient.
- Do not claim resolved 13C coupling. Expected sidebands are not clearly distinguished from noise/fluctuation levels.
- Do not claim a precise Ramsey frequency beyond saying the FFT power moved near the detuned carrier region in this run.
- Do not use the exploratory `T2* ~0.94 us` fit as a project conclusion.

## Recommended next action

Do not immediately repeat the same 8 us Ramsey unchanged. First make a targeted diagnostic decision: either run a higher-SNR shorter-window Ramsey centered on the carrier, for example `tau = 0..4 us` with denser sampling and more averages/repetitions if runtime permits, or run a control Ramsey with a different detuning to verify that the carrier peak tracks `det`. Only fit T2star after the carrier is reproducible in per-average traces; only evaluate 13C after the carrier itself is claim-grade.
