# Ramsey Review

## Files/data used

- `project/state.md`, `project/brief.md`, and `project/advice.md` for the project objective and prior decision state.
- `evidence/e007.json` for the second-Ramsey model: accepted r03, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, expected 13C sidebands near `0.615/1.385 MHz`, and readout roles (`readout1` reference, `readout2` Ramsey signal).
- `measurement/m001.json` for the new raw Ramsey export: `ramsey.xml`, `tau = 0..8 us`, 41 points, 8 stored averages.
- `measurement/m002.json` and `measurement/m003.json` for the executed job settings and terminal result: `8 x 50000` repetitions, final counts `44.184 kcps`, no abort, safe shutdown OK.
- `measurement/m004.json` and `measurement/m005.json` for terminal bridge status/control.

## Calculations or scripts run

- Added and ran `python analyze_ramsey.py`.
- Outputs generated: `ramsey_analysis_summary.json` and `ramsey_diagnostics.png`.
- Checks performed:
  - Combined raw readouts, point-wise `signal/ref`, and fitted-reference-line normalization.
  - Stored-average mean/ref checks for drift/common-mode movement.
  - Linear-detrended least-squares sinusoid checks at `1.000 MHz`, expected 13C sidebands `0.615423/1.384577 MHz`, and prior scout component `0.884 MHz`.
  - Windowed FFT peak search on raw signal and normalized views.
  - Fixed-`1.0 MHz` exponentially decaying cosine fit to raw signal as a descriptive stress test, not as a claim source.

Key numerical results:

- Combined readouts: reference mean `49.31 kcps`, Ramsey signal mean `44.58 kcps`, signal range `39.31..47.03 kcps`.
- Stored-average signal means vary strongly: `48.44, 43.44, 41.20, 49.98, 45.73, 41.38, 36.20, 50.27 kcps`; reference means move similarly, so common-mode drift/focus/count variation is material.
- Exact-frequency least-squares on raw signal is weak:
  - `1.000 MHz`: amplitude `0.276 kcps`, detrended `R2 = 0.024`.
  - `0.615423 MHz`: amplitude `0.464 kcps`, detrended `R2 = 0.067`.
  - `1.384577 MHz`: amplitude `0.263 kcps`, detrended `R2 = 0.022`.
  - `0.884 MHz`: amplitude `0.286 kcps`, detrended `R2 = 0.026`.
- Normalized views also do not promote the target frequencies: exact `1.000 MHz` explains only about `2.4..5.0%` of detrended variance, and the lower 13C-sideband check about `6.7..6.9%`.
- FFT peaks are not clean claim-grade target peaks. The largest raw/normalized peaks sit near `1.10..1.22 MHz`, with other comparable structure near `0.49/0.61/1.34 MHz`; finite-bin leakage and drift make this exploratory only.
- Fixed-`1 MHz` exponential-cosine fit returns `R2 = 0.517`, but pushes `T2star` to the lower bound `0.2 us` with amplitude `-8.0 +/- 5.4 kcps`; this is not a trustworthy T2star extraction.

## Plausible interpretation

- The measurement completed and is analyzable, but it is not claim-grade for T2star or 13C.
- There is weak oscillatory spectral content in the neighborhood of the programmed detuned carrier bins, but the exact `1.0 MHz` component is small and per-average phases/amplitudes are not consistent enough to support a Ramsey-carrier claim.
- The prior scout's non-claim-grade `~0.884 MHz` component is not reproduced as a clear fixed feature. The det-shift diagnostic therefore weakly disfavors treating that prior component as a stable physical Ramsey frequency, but does not by itself establish a clean det-following carrier.
- Large stored-average common-mode movement is a likely contributor to the ambiguous FFT/fit behavior.

## Claims that are not yet supported

- No supported `T2star` value from this data. The descriptive fixed-carrier fit is boundary-driven and should not be used.
- No supported nearby-13C conclusion. The `0.615/1.385 MHz` sideband checks are weak and not independently consistent.
- No supported sub-grid resonance refinement beyond the prior fine-pODMR grid-supported `3.8759 GHz`.
- No supported claim that r03 lacks 13C coupling; the current Ramsey data is too ambiguous to distinguish weak coupling from measurement/drift limitations.

## Recommended next action

Do not blindly repeat the same long Ramsey. First stabilize or diagnose the Ramsey contrast: retrack/check counts and run a shorter focused Ramsey validation around the expected carrier with reduced per-average window, or run a Ramsey frequency/detuning diagnostic that can confirm a phase-ramp-following carrier before spending another high-shot 13C/T2star acquisition. Only fit T2star or evaluate 13C sidebands after a raw/readout-aware carrier is clearly present.
