# Ramsey review: r03 det=1.0 MHz, 8 us, 8 averages

## Files/data used

- `project/state.md`, `project/brief.md`, `project/advice.md`: project context, accepted r03 candidate, prior pODMR/Ramsey conclusions, and required claim posture.
- `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- `measurement/m002.json`, `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: job contract/result/status/control context for `nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg`.
- `evidence/e013.md` and related evidence summaries as prior context for the fine pODMR and second Ramsey launch.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Output artifacts:
  - `ramsey_analysis_summary.json`
  - `ramsey_review_plot.png`
- Parsed `measurement/m001.json` as 8 averages, 2 readout channels, 41 tau points from 0 to 8 us with 0.2 us spacing, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, and `50000` repetitions per average.
- Treated channel 0 as the brighter reference/readout line and channel 1 as signal. Reviewed raw signal/reference ratio and a simple reference-line normalization.
- FFT check used the mean-subtracted reference-line-normalized trace with a Hann window. Nominal FFT bin spacing from the sampled record is about 0.122 MHz.
- Least-squares checks fit offset + linear trend + sinusoid at diagnostic frequencies: expected lower 13C sideband 0.615 MHz, prior scout feature 0.884 MHz, programmed carrier 1.0 MHz, and expected upper 13C sideband 1.385 MHz.

Key quantitative results:

- Combined signal/reference ratio mean: `0.9042`; peak-to-peak ratio variation: `0.1696`.
- Reference-line-normalized peak-to-peak variation: `0.1759`.
- Strongest exploratory FFT bins:
  - `1.098 MHz`, amplitude `0.00919`
  - `1.220 MHz`, amplitude `0.00910`
  - `0.488 MHz`, amplitude `0.00681`
  - `0.976 MHz`, amplitude `0.00448`
  - `0.610 MHz`, amplitude `0.00424`
  - `1.341 MHz`, amplitude `0.00384`
- Least-squares sinusoid amplitudes versus residual RMS:
  - `0.615 MHz`: amplitude `0.01110`, residual RMS `0.02738`, amp/RMS `0.41`
  - `0.884 MHz`: amplitude `0.00609`, residual RMS `0.02812`, amp/RMS `0.22`
  - `1.000 MHz`: amplitude `0.00714`, residual RMS `0.02799`, amp/RMS `0.26`
  - `1.385 MHz`: amplitude `0.00665`, residual RMS `0.02805`, amp/RMS `0.24`
- Per-average fitted 1.0 MHz amplitudes are inconsistent: amplitude/RMS ranges from about `0.05` to `0.41`.
- Per-average fitted 0.884 MHz amplitudes are also inconsistent: amplitude/RMS ranges from about `0.15` to `0.49`.
- Common-mode readout changed substantially across averages: mean reference span about `30.5%`, mean signal span about `31.6%`; ratio mean span is smaller, about `3.9%`.

## Plausible interpretation

- The experiment completed and returned analyzable Ramsey-like data on the accepted r03 NV.
- The det-shifted run does not provide a clean, claim-grade Ramsey carrier. There is some spectral weight near the programmed 1.0 MHz region, but the largest FFT bins are offset to roughly 1.10 to 1.22 MHz, and direct least-squares amplitude at 1.0 MHz is small compared with residual scatter.
- The prior scout's non-claim-grade `~0.884 MHz` component does not reappear as a dominant component here, which weakens the case that it was a stable physical carrier.
- The expected 13C sideband regions near `0.615 MHz` and `1.385 MHz` show only weak bins/fits and are not internally convincing. The lower sideband bin at about `0.610 MHz` is visible but not strong enough relative to residuals and per-average inconsistency.
- The large common-mode changes between averages mean raw counts drifted or tracking/readout conditions changed, although ratio normalization reduces much of that. This should be treated as provenance caution, not a standalone 13C/T2star result.

## Claims that are not yet supported

- A well-supported T2star value is not supported by this run.
- A well-supported nearby 13C conclusion is not supported by this run.
- A precise Ramsey carrier frequency is not supported. The programmed 1.0 MHz carrier is not cleanly recovered with strong per-average consistency.
- The `~1.10-1.22 MHz` FFT content should not be claimed as physical without repeatability or a better-controlled follow-up.
- The prior `~0.884 MHz` scout feature should not be claimed as physical.

## Recommended next action

Do not repeat the same long Ramsey blindly. First run a short diagnostic Ramsey on r03 after rechecking/refreshing tracking and pODMR center, with a cleaner carrier-validation goal: use the same `mw_freq = 3.8759 GHz` basis unless pODMR has shifted, choose one detuning, and collect enough averages to compare per-average phase/amplitude consistency before fitting T2star. If the next diagnostic still fails to recover a stable programmed carrier, close the r03 Ramsey branch as non-claim-grade for T2star/13C or switch sequence/normalization strategy rather than accumulating more identical data.
