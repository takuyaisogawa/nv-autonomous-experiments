# Ramsey Review: short-tau high-SNR r03 diagnostic

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/advice.md`, `project/state.md`.
- Prior knowledge/state: `md/memory.md`, `md/knowledge.md` by targeted search only.
- New measurement:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
  - `measurement/m002.json`: submitted job contract.
  - `measurement/m003.json`: terminal result.
  - `measurement/m004.json`: terminal status.
  - `measurement/m005.json`: run control.
- Scratch artifacts generated here:
  - `analyze_ramsey.py`
  - `ramsey_analysis_summary.json`
  - `ramsey_shorttau_overview.png`
  - `ramsey_shorttau_ls_spectrum.png`

## Calculations or scripts run

- Parsed `measurement/m001.json` with Python/numpy.
- Verified acquisition settings: `tau = 0.048..1.968 us`, 41 points, `dt = 48 ns`, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, 12 averages, 90000 repetitions per tau point.
- Checked terminal metadata: job `nv23_ramsey_20260513_230331_auto_ramsey` completed, no stop request, no monitor error, safe shutdown ok, final count text `35.122 kcps`.
- Built raw signal, reference, signal/reference ratio, and signal divided by a fitted reference line.
- Estimated per-point SEM across stored averages:
  - raw signal median SEM `1.12 kcps`
  - ratio median SEM `0.0151`
  - fitted-reference-line normalized median SEM `0.0109`
- Checked average-to-average common-mode behavior:
  - mean signal per average spans `42.016..55.188 kcps` (`27.1%` relative span)
  - mean reference per average spans `37.474..51.213 kcps`
  - average index correlation is negative for both signal (`r = -0.66`) and reference (`r = -0.61`)
  - signal and reference move together, so this is mainly provenance/common-mode drift, but it makes simple ratio features denominator-sensitive.
- Least-squares screened sinusoidal amplitudes with offset+slope at target frequencies:
  - raw signal amplitudes: `1.000 MHz = 0.213 kcps`, `0.615 MHz = 0.175 kcps`, `1.385 MHz = 0.149 kcps`
  - simple ratio amplitudes: `1.000 MHz = 0.0327`, `0.615 MHz = 0.0292`, `1.385 MHz = 0.0317`
  - fitted-reference-line normalized amplitudes: `1.000 MHz = 0.00475`, `0.615 MHz = 0.00401`, `1.385 MHz = 0.00334`
- FFT/detrended checks show bins near `1.016 MHz` and `1.524 MHz`, but amplitudes are not stable across normalization choices and the raw/line-normalized target amplitudes are below the measured per-point SEM scale.
- A descriptive damped 1 MHz fit to the simple ratio finds an apparent very short `T2* ~0.16 us`, but this depends on the reference-denominator trend and is not supported by raw signal or fitted-reference-line normalization.

## Plausible interpretation

The short-tau/high-SNR Ramsey diagnostic completed and is analyzable, but it does not provide claim-grade Ramsey contrast. The raw signal is nearly flat at the programmed 1 MHz carrier scale: the raw 1 MHz LS amplitude is only `0.213 kcps`, well below the `1.12 kcps` median per-point SEM. Conservative fitted-reference-line normalization likewise gives a 1 MHz amplitude of only `0.00475`, below the `0.0109` median SEM. The simple signal/reference ratio shows larger apparent low-frequency and target-frequency structure, but this is plausibly driven by reference-channel curvature and common-mode count drift rather than a robust NV Ramsey oscillation.

This result weakens the "hidden by long-window averaging only" explanation for the prior non-claim-grade Ramsey runs. If the r03 Ramsey carrier were clean and only very short-lived, this 48 ns..1.968 us, 1.08e6-shot-per-point acquisition should have made early-time carrier contrast more evident in raw or conservative normalized data.

## Claims not yet supported

- No supported numeric `T2*` for r03.
- No supported nearby `13C` coupling conclusion.
- No supported claim that the apparent ratio-only short-decay fit is physical.
- No supported promotion of any exploratory component near the carrier, the expected `13C` sidebands (`~0.615/1.385 MHz`), or the earlier non-claim-grade features.
- No supported conclusion that r03 is unsuitable as an aligned NV for all purposes; the pODMR alignment evidence remains separate. The unsupported part is Ramsey/T2*/13C under these conditions.

## Recommended next action

Do not run another blind Ramsey repeat on r03. Treat the Ramsey/T2*/13C branch as unsupported under the current Ramsey protocol unless an alternate diagnostic is explicitly designed to isolate the failure mode. The next useful action is to choose between:

1. an alternate protocol/check for Ramsey contrast generation and readout normalization, using controls that can separate sequence/normalization artifacts from true dephasing; or
2. closing r03 with "aligned NV found, but no supported T2*/13C conclusion from available Ramsey data" and moving to a different aligned candidate/search path if the project requires a supported T2*/13C result.
