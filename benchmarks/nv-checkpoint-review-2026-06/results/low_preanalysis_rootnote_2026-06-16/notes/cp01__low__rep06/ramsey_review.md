# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`.
- Completed Ramsey job contract/status/control: `measurement/m002.json`, `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`.
- Raw Ramsey savedexperiment export: `measurement/m001.json`.
- Scratch outputs created here: `analyze_ramsey.py`, `scratch/ramsey_analysis_summary.json`, `scratch/ramsey_traces_and_fits.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed `ExperimentData` shape `(1, 2, 31)` and `ExperimentDataEachAvg` shape `(1, 4, 2, 31)`.
- Confirmed scan parameters: tau `0..6 us`, step `0.2 us`, 31 points, 4 averages, 50000 repetitions, snake scan order, data saved in tau order.
- Confirmed Ramsey parameters from variables: `mw_freq = 3.876 GHz`, `det = 1.5 MHz`, `length_pi_pulse = 52 ns`, `mod_depth = 1`.
- Checked signal, reference, and signal/reference traces with linear-detrended Hann FFTs and simple Gaussian-decay cosine fits.
- Checked per-average signal/reference consistency against the final averaged ratio.

## Plausible interpretation

- The Ramsey run completed and is analyzable as a first scout on accepted candidate `image145844_reimage_r03`.
- The averaged signal/reference ratio has visible structure with peak-to-peak ratio contrast `0.1586`, about `14.7%` of its mean.
- A free damped-cosine fit to signal/reference gives `T2* ~ 3.55 us` and frequency `~1.68 MHz`, but the fit quality is weak (`R2 ~ 0.20`). A signal-only fit gives `T2* ~ 3.21 us`, frequency `~1.70 MHz`, also weak (`R2 ~ 0.26`).
- FFT peaks are normalization-sensitive: signal peaks near `1.96 MHz`, reference has a strong low-frequency feature near `0.215 MHz`, and signal/reference peaks near `0.925 MHz`. This argues that the current run contains oscillatory content but does not isolate a stable Ramsey carrier/sideband interpretation.
- Per-average ratio traces are not identical but are not random either: correlations with the final ratio are about `0.42..0.71`. Per-average channel means vary noticeably, consistent with drift/common-mode changes affecting the first scout.

## Claims that are not yet supported

- No well-supported `T2*` value should be claimed from this run. The numerical fit values above are descriptive only because fit residuals remain large and model quality is poor.
- No well-supported nearby `13C` conclusion should be claimed. The expected project-scale sideband separation was about `0.385 MHz`, but the observed FFT features depend strongly on readout normalization and do not provide a robust carrier-plus-sideband pattern.
- This run should not be used to reject r03 as the aligned NV. The prior pODMR evidence still supports r03; this Ramsey result is better treated as a noisy/drift-affected first scout than as invalidating spectroscopy.

## Recommended next action

Repeat or extend Ramsey on r03 with stronger claim-grade controls rather than making a T2*/13C claim now. Use the same weak-pi-supported `mw_freq = 3.876 GHz`, but prioritize higher SNR and drift control: repeat under stable counts, keep per-average tracking, and consider a longer tau span or more points only if the runtime/advisory cap allows. The decision point after the next run should be whether the same carrier/sideband peaks recur consistently in raw signal and reference-normalized traces and across averages.
