# Ramsey Review: short-tau/high-SNR r03 diagnostic

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, and `evidence/e017.md`.
- New terminal measurement: `measurement/m001.json` raw export from `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
- Bridge/job metadata: `measurement/m002.json`, `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`.
- Prior comparison context came only from the provided snapshot: especially the previous non-claim-grade Ramsey summaries embedded in `project/state.md` and prior terminal-review evidence.

## Calculations or scripts run

- Created and ran `analyze_ramsey_shorttau.py`.
- Outputs: `ramsey_shorttau_analysis.json` and `ramsey_shorttau_review.png`.
- Measurement settings verified from JSON:
  - `tau = 0.048..1.968 us`, `41` points, `48 ns` step.
  - `mw_freq = 3.8759 GHz`, programmed Ramsey `det = 1.0 MHz`.
  - `12 averages x 90000 repetitions = 1.08e6 shots/tau`.
  - Scan order mode `snake`; terminal job status completed, final-count text `35.122 kcps`, no error message.
- Numeric checks performed:
  - Raw reference/signal and signal/reference summaries.
  - Per-point SEM from the 12 stored averages.
  - Scan-order-aware common-mode drift check using `ScanOrderEachAvg`; no averages exceeded the 15% drop flag threshold.
  - Least-squares sinusoid tests against a linear baseline at `1.000 MHz`, expected 13C sideband positions `0.615 MHz` and `1.385 MHz`, and prior exploratory `0.884 MHz`.
  - Dense least-squares frequency screen and descriptive FFT screen.
  - Diagnostic model fits: line, fixed `1.0 MHz` tone, free-frequency tone, and free-frequency exponentially decaying tone.

## Plausible interpretation

- This short-tau scan is better evidence for early-time Ramsey-like structure than the prior long-window scans, but it still does not cleanly support a T2star or 13C claim.
- Combined raw/readout-aware numbers:
  - Mean reference `48.573 kcps`; mean Ramsey signal `44.655 kcps`.
  - Ratio mean `0.9195`; ratio tau-standard-deviation `0.0348`; median ratio SEM `0.0127`.
  - Raw-signal median point SEM `1.14 kcps`; raw-signal linear-residual peak-to-peak `5.25 kcps`.
- Targeted LS amplitudes:
  - Programmed `1.0 MHz`: ratio amplitude `0.0274`, raw-signal amplitude `1.28 kcps`, R2 improvement vs linear `0.355` in ratio.
  - Expected low 13C sideband `0.615 MHz`: ratio amplitude `0.0243`, R2 improvement `0.311`.
  - Expected high 13C sideband `1.385 MHz`: ratio amplitude `0.0271`, R2 improvement `0.345`.
  - Prior `0.884 MHz` feature: weaker, ratio amplitude `0.0126`, R2 improvement `0.070`.
- The combined dense LS screen peaks at about `1.192 MHz` with ratio amplitude `0.0363` and R2 improvement `0.656`; skipping the first tau point leaves the top near `1.203 MHz`.
- Fit comparison on the combined ratio:
  - Linear RSS `0.04161`.
  - Fixed `1.0 MHz` cosine RSS `0.02685`, AIC `-292.6`.
  - Free-frequency cosine RSS `0.01431`, AIC `-316.4`, frequency `1.192 MHz`.
  - Free-frequency exponential cosine gave `T ~ 6.3 us`, but over a `1.92 us` span it did not improve AIC over the undamped free cosine, so that decay time is not claim-grade.
- The most plausible working interpretation is a weak early-time Ramsey oscillation with an apparent beat closer to `1.19 MHz` than the programmed `1.0 MHz`. Ordinary Ramsey physics would make that consistent with a residual microwave-frequency/transition-frequency offset or related phase calibration issue, but the current evidence is not enough to choose among detuning, multi-component response, normalization artifacts, or remaining average-to-average instability.

## Claims not yet supported

- No supported numeric T2star yet. A free decay fit is underconstrained by this short span and is not justified by model comparison.
- No supported nearby 13C conclusion. The short window has only about `0.52 MHz` nominal resolution, the expected sideband targets have LS amplitudes comparable to the carrier target, and the dominant combined component is not at either expected sideband.
- No supported claim that the programmed `1.0 MHz` carrier is cleanly recovered. It is present as a weak model component, but the stronger combined component is near `1.19 MHz`.
- No supported claim that the previous `~0.884 MHz` scout feature is reproducible; it is weaker in this diagnostic.

## Recommended next action

Do not run another blind long-window Ramsey repeat. Run a targeted detuning/frequency-follow-up on r03 before any T2star or 13C extraction: either a short-tau Ramsey detuning series or microwave-frequency offset series designed to test whether the observed beat follows the programmed det with an approximately constant offset near `+0.19 MHz`. If that produces a stable carrier model across averages, then acquire a claim-grade decay scan around the corrected condition; if it does not, close the r03 Ramsey/13C branch as unsupported under the current protocol and consider an alternate protocol.
