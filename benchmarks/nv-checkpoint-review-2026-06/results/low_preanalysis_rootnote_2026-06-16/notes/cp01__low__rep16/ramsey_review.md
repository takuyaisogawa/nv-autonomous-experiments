# Ramsey review: r03 first T2star/13C scout

## Files/data used

- `project/brief.md`, `project/advice.md`, and `project/state.md` for objective, current r03 status, and prior claim boundaries.
- `measurement/m002.json`, `measurement/m003.json`, `measurement/m004.json`, and `measurement/m005.json` for the Ramsey job plan/status/control/result metadata.
- `measurement/m001.json` for the raw saved-experiment export from `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
- Generated local analysis artifacts: `ramsey_analysis_summary.json`, `ramsey_trace_fit.png`, and `ramsey_fft.png`.

## Calculations or scripts run

- Parsed the raw export with Python from `measurement/m001.json`.
- Built tau as 31 evenly spaced points over `0..6 us`, step `0.2 us`.
- Used channel 0 as the signal readout and channel 1 as the reference readout; inspected raw channels, `signal/reference`, and `(signal-reference)/(signal+reference)`.
- Fit the mean normalized `signal/reference` trace to `c + a*cos(2*pi*f*t + phi)*exp(-t/T)` with bounded nonlinear least squares.
- Refit each stored average separately with the same model.
- Ran Hann-window FFT checks on signal, reference, normalized ratio, and contrast.
- Saved summary values to `ramsey_analysis_summary.json`; saved plots to `ramsey_trace_fit.png` and `ramsey_fft.png`.

Key quantitative results:

- Job completed without bridge abort; saved artifact run id is `1DExp-seq-ramsey-vary-tau-2026-05-13-185521`.
- Final count text was `38.249 kcps`, down from the pre-Ramsey weak-pODMR/fresh context of about `43.890 kcps`.
- Mean readouts over the final averaged trace were `45.318 kcps` signal and `42.098 kcps` reference.
- Mean per-average signal/reference ratios were stable at `1.0745`, `1.0792`, `1.0911`, `1.0713`, but channel means varied by average, consistent with non-negligible common-mode changes.
- Mean-trace damped-cosine fit on normalized `signal/reference`: `f = 0.947 MHz`, `T2star = 2.29 us`, amplitude `0.0746`, `R2 = 0.435`.
- Approximate 1-sigma fit errors from the covariance were `0.035 MHz` on frequency and `1.11 us` on T2star, but these are descriptive because residual structure and per-average inconsistency dominate the uncertainty.
- Per-average fits did not agree cleanly: average frequencies were about `0.930`, `0.515`, `0.957`, and `0.897 MHz`; two averages hit the upper T bound (`50 us`), while averages 1 and 4 gave `5.75 us` and `2.07 us`.
- FFT bin spacing from the actual 31-point DFT is `161.29 kHz`. The strongest Hann-window normalized-ratio bins were `0.968`, `0.323`, `0.161`, `0.806`, `1.935`, `1.774`, `0.645`, and `1.613 MHz`.
- The planned detuning was `1.5 MHz`; the expected 13C sideband scale from the project model was about `0.385 MHz`, implying sideband checks near `1.115` and `1.885 MHz` if the carrier had appeared at `1.5 MHz`.

## Plausible interpretation

- The Ramsey run produced a real-looking oscillatory component, but it is not clean enough for a final T2star claim. The most plausible descriptive component in the normalized trace is near `0.95 MHz` with a few-microsecond decay.
- The observed carrier-like frequency is substantially below the requested `det = 1.5 MHz`. That could reflect mw frequency offset from the true resonance, sequence/IQ behavior, or analysis/readout complications, but the local files do not distinguish those causes.
- The lower final counts and per-average channel variation make drift/count changes a material caveat, even though the averaged ratio is not catastrophically unstable.
- The FFT supports "there is spectral content near 1 MHz" more strongly than it supports the planned detuning model.
- 13C evidence is not claim-grade. Bins near the expected `det +/- 0.385 MHz` positions are not isolated from nearby noisy peaks and the carrier itself is not at the planned `1.5 MHz`, so sideband interpretation would be premature.

## Claims that are not yet supported

- A well-supported T2star value for r03 is not yet established.
- A nearby 13C coupling conclusion is not yet established.
- The Ramsey fit value `T2star ~2.3 us` should not be presented as final; it is a descriptive fit to a noisy scout trace with weak R2 and inconsistent per-average behavior.
- The FFT does not support a resolved 13C sideband claim.
- This run does not invalidate the prior r03 alignment conclusion from strong-pi and weak-pi pODMR; it only leaves T2star/13C unresolved.

## Recommended next action

Run a targeted Ramsey follow-up on r03 after a fresh track/quick resonance check, using the observed `~0.95 MHz` Ramsey frequency to choose a better-resolved acquisition. Prefer a longer time span and/or more points only if the per-average tracking window remains within the drift cap; otherwise keep the time span modest but improve SNR/repeatability. The follow-up should explicitly test whether the carrier is reproducible near `0.95 MHz` and only then evaluate sidebands relative to the observed carrier.
