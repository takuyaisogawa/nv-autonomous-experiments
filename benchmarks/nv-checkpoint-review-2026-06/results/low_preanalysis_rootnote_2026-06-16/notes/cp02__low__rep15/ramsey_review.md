# Ramsey review: second det=1.0 MHz r03 follow-up

## Files/data used

- `project/state.md`, `project/brief.md`, and `project/advice.md` for the project objective, prior candidate decisions, and expected Ramsey checks.
- `measurement/m002.json` for the executed job contract: accepted `image145844_reimage_r03`, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `tau = 0..8 us`, 41 points, `8 x 50000` repetitions.
- `measurement/m003.json` and `measurement/m004.json` for terminal status/provenance: job completed, savedexperiment `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`, elapsed 5256 s, no terminal status warnings in `m004`.
- `measurement/m001.json` for the raw savedexperiment export: `ExperimentData`, `ExperimentDataEachAvg`, errors, and snake scan order.
- `md/knowledge.md` / `md/memory.md` were searched for Ramsey/T2star/13C guardrails and prior context.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis_summary.json` and `ramsey_analysis_plot.png`.
- Checks performed:
  - Built `tau` from `0..8 us`, 41 points, `dt = 0.2 us`; nominal FFT resolution is `125 kHz`, with the discrete `rfft` grid at about `121.95 kHz` spacing for 41 samples.
  - Reviewed raw signal/reference ranges: signal `46.95..51.24 kcps`, reference `39.31..47.03 kcps`.
  - Computed signal/reference contrast and a first-order reference-line-normalized signal. Peak-to-peak contrast was `19.6%` for point-wise ratio but only `7.0%` for reference-line normalization, so denominator/reference structure materially affects apparent contrast.
  - Ran FFT on detrended mean-normalized signal/reference. Largest exploratory FFT amplitudes were near `1.098 MHz` (`2.30%`), `1.220 MHz` (`2.04%`), and `0.976 MHz` (`1.48%`).
  - Ran least-squares sinusoid checks with offset+slope at target frequencies:
    - Programmed `1.000 MHz`: amplitude `1.08%`, residual RMS `3.19%`; per-average amplitudes `0.48..2.70%`.
    - Expected low 13C sideband `0.615 MHz`: amplitude `1.22%`, nearest FFT amplitude `0.78%`; per-average amplitudes `0.87..5.05%`.
    - Expected high 13C sideband `1.385 MHz`: amplitude `0.97%`, nearest FFT amplitude `0.72%`; per-average amplitudes `0.50..3.60%`.
    - Prior scout component `0.884 MHz`: amplitude `0.86%`, nearest FFT amplitude `0.74%`.
  - Per-average mean signal varied `40.47..55.53 kcps`, reference `36.20..50.27 kcps`; mean ratio varied less (`1.084..1.128`). Forward/reverse snake-direction mean-ratio offset was small at `0.73%`.

## Plausible interpretation

- The second Ramsey is analyzable and shows weak spectral weight close to the programmed `1.0 MHz` detuning. This is more compatible with a real Ramsey phase-ramp response than the first scout's non-claim-grade `~0.884 MHz` feature, because the prior `0.884 MHz` component is not a dominant component here.
- The data still do not support a robust T2star extraction. The apparent oscillation amplitude is small compared with residual structure, and the trace is sensitive to readout normalization.
- The expected 13C sidebands near `0.615 MHz` and `1.385 MHz` are not convincingly resolved. The low-sideband least-squares amplitude is comparable to the carrier check, but the FFT amplitude at the nearest bin is not prominent and per-average amplitudes are inconsistent.
- The large common-mode per-average count swings argue for caution, although the signal/reference ratio and snake-direction check do not show a simple acquisition-direction drift failure.

## Claims not yet supported

- No well-supported numerical T2star value is established from this run.
- No well-supported nearby 13C coupling conclusion is established.
- Do not claim resolved 13C sidebands at `0.615/1.385 MHz`.
- Do not claim the refined pODMR center has sub-grid precision beyond the prior grid-supported `3.8759 GHz`.
- Do not treat the large point-wise ratio peak-to-peak contrast alone as Ramsey contrast; it is reference-denominator sensitive.

## Recommended next action

Before another blind repeat, run a targeted Ramsey confirmation on the same accepted r03 with a deliberately different detuning that remains inside the same sampling limits, preferably `det = 0.5 MHz` over `0..8 us` with the same or higher averages. The key decision criterion should be whether the main spectral feature follows the programmed detuning while the prior `0.884 MHz` feature stays absent. If it follows detuning with per-average phase consistency, then fit T2star on the combined and per-average traces; if not, pause Ramsey repeats and re-check frequency calibration/readout normalization before making T2star or 13C claims.
