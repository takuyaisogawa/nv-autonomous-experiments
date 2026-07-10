# Ramsey Review

## Files/data used

- Project context: `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`.
- New Ramsey export/result files: `measurement/m001.json` through `measurement/m005.json`.
- Main data file reviewed: `measurement/m001.json`, exported from `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- Job context: `measurement/m002.json` and `measurement/m003.json` identify `nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg`, `auto__ramsey`, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `tau = 0..8 us`, 41 points, 8 averages x 50000 repetitions.
- Run status/control: `measurement/m004.json`, `measurement/m005.json`; run completed, no stop requested. Terminal final count was `44.184 kcps`.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis_summary.txt` and `ramsey_review_plot.png`.
- Checks performed:
  - Parsed combined readouts and `ExperimentDataEachAvg`.
  - Treated readout 1 as reference and readout 2 as Ramsey signal, while also checking signal/reference ratio.
  - Confirmed scan grid: 41 tau points, `0..8 us`, `dt = 0.2 us`; FFT bin spacing is about `125 kHz`, Nyquist about `2.5 MHz`.
  - Detrended linearly and ran Hann-window FFT summaries for signal, reference, and ratio.
  - Least-squares fits with constant + linear trend + fixed sine/cosine at `0.884 MHz` prior component, expected low 13C sideband `0.615 MHz`, programmed carrier `1.000 MHz`, and expected high 13C sideband `1.385 MHz`.
  - Per-average signal FFT/fixed-frequency amplitude checks and average-mean drift check.

## Plausible interpretation

- The measurement is analyzable and completed normally, but it is not claim-grade for T2star or 13C.
- Combined signal has spectral weight near the programmed-detuning region: top signal FFT bins are `1.220 MHz` and `1.098 MHz`; ratio FFT also peaks at `1.098 MHz` and `1.220 MHz`, with a smaller `0.976 MHz` component. This is more compatible with a weak Ramsey response near the `1.0 MHz` detuning than the prior scout's fixed `~0.884 MHz` feature, but it is not clean.
- Targeted fixed-frequency fits are weak. For the signal channel, the `1.000 MHz` carrier fit has amplitude `0.277 kcps`, RMS residual `1.24 kcps`, and `R2 = 0.115`. For the ratio, the carrier amplitude is `0.00916` with `R2 = 0.053`. These are too low to support a quantitative T2star fit.
- Candidate 13C-sideband bins are present only as weak, ambiguous spectral content: signal FFT includes `0.610 MHz` and `1.341 MHz`, close to expected `0.615/1.385 MHz`, but fixed-frequency fits explain little variance (`R2 ~ 0.156` low sideband in signal; `R2 ~ 0.113` high sideband in signal; ratio fits lower).
- Stored averages disagree strongly. Signal average means range from `36.2` to `50.27 kcps` with CV `11.1%`; per-average dominant FFT frequencies are inconsistent (`0.122`, `0.488`, `0.244`, `1.707`, `1.220`, `0.366 MHz`, etc.). This points to drift/baseline variation and/or low SNR dominating the combined trace.
- The run status expected-runtime record reports per-average/tracking-window estimates of about `629.8 s`, above the usual `600 s` nighttime planning cap, even though earlier project state expected the run to be under cap. That does not invalidate completed data, but it is relevant provenance for baseline instability.

## Claims that are not yet supported

- No supported numeric T2star value from this Ramsey.
- No supported 13C coupling/conclusion from the FFT or sideband amplitudes.
- No supported claim that the prior `~0.884 MHz` scout component was a real physical carrier; this run weakly shifts spectral weight toward the programmed `1.0 MHz` region, but the evidence is not decisive.
- No supported claim of a clean Ramsey carrier at exactly `1.0 MHz`; the largest combined bins are offset and broad within the available 125 kHz resolution.

## Recommended next action

Before another long Ramsey, re-check the r03 weak-pi resonance/track health and redesign the Ramsey acquisition to reduce per-average untracked time below the active cap. If continuing this branch, use the same `det = 1.0 MHz`, `0..8 us`, 41-point grid for comparability, but split shots into shorter per-average windows, for example lower repetitions per average with more averages, then repeat only if the advisory confirms the tracking window is comfortably below cap. The decision criterion should be a reproducible carrier in raw signal and ratio near the programmed detuning with per-average consistency before attempting a T2star decay fit or 13C sideband claim.
