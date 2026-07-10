# Short-Tau Ramsey Review

## Files/data used

- Project context: `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New Ramsey measurement:
  - `measurement/m001.json`: terminal raw export for `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
  - `measurement/m002.json`: submitted job spec, `auto__ramsey`, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `tau = 48 ns..1.968 us`, 41 points, `12 x 90000` repetitions.
  - `measurement/m003.json`: terminal bridge result, completed at `2026-05-14T01:23:47`, no error code.
  - `measurement/m004.json`: terminal status, completed, elapsed `8402 s`.
  - `measurement/m005.json`: control file, `stop_requested = false`.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis_summary.json`, `ramsey_analysis_stdout.json`, `ramsey_shorttau_diagnostic.png`.
- Checks performed:
  - Loaded raw two-readout data and 12 stored averages.
  - Used readout 1 as reference and readout 2 as signal, consistent with the prior Ramsey review convention.
  - Computed raw signal, point-wise `signal/reference`, and signal normalized by a fitted reference line.
  - Estimated repeatability from stored-average scatter.
  - Screened target frequencies with least-squares sinusoid plus offset/slope: `0.615 MHz`, `1.000 MHz`, `1.385 MHz`.
  - Ran Hann-window detrended FFT screens.
  - Ran stacked per-average common-sinusoid fits with per-average offset/slope terms.
  - Ran a forced diagnostic `1.0 MHz` damped-cosine fit; this is not used as a claim.

## Quantitative results

- Acquisition grid: 41 points, `tau = 0.048..1.968 us`, step `48 ns`, total `1.08e6` shots per tau point.
- Mean levels: signal `44.65 kcps`, reference `48.57 kcps`.
- Raw signal peak-to-peak over tau: `6.50 kcps`.
- Conservative median SEM from stored-average scatter: signal `1.14 kcps`, ratio `0.0127`.
- Stored-average common-mode signal movement is not negligible: averages `2, 5, 8, 10, 11` exceed `5%` from the median mean signal. Ratio-average offsets are smaller but still present.
- Target single-frequency LS amplitudes on the combined trace:
  - `0.615 MHz`: raw `1.10 kcps`, ratio `0.0243`.
  - `1.000 MHz`: raw `1.28 kcps`, ratio `0.0274`.
  - `1.385 MHz`: raw `1.22 kcps`, ratio `0.0271`.
- Stacked per-average common-sinusoid fits find repeatable phase/coherent components at all three target frequencies:
  - `0.615 MHz`: raw `1.10 +/- 0.12 kcps`, ratio `0.0243 +/- 0.0029`.
  - `1.000 MHz`: raw `1.28 +/- 0.12 kcps`, ratio `0.0272 +/- 0.0031`.
  - `1.385 MHz`: raw `1.22 +/- 0.13 kcps`, ratio `0.0272 +/- 0.0031`.
- FFT top bins are coarse because the window is only `1.92 us`; strongest raw/ratio bins are near `1.524 MHz`, then `1.016 MHz`, then `0.508 MHz`.
- Forced `1.0 MHz` damped-cosine diagnostic returns `T2star ~0.184 us`, amplitude `8.22 kcps`, RMS `0.944 kcps`. This is model-leveraged by the earliest points and by the short window, so it is a diagnostic hypothesis, not a supported fitted result.

## Plausible interpretation

- The short-tau/high-SNR run is more informative than the earlier long-window Ramsey scans. It shows a repeatable early-time Ramsey-like shape in raw signal and normalized ratio, and a `1 MHz` component is plausible.
- The data are consistent with a very short dephasing time, roughly sub-microsecond and possibly a few `0.1 us`, which would explain why the earlier `0..6 us` and `0..8 us` scans did not produce a clean carrier/sideband model.
- The short window intentionally improves early-time sensitivity but sacrifices frequency selectivity. Over `1.92 us`, the carrier and expected 13C sideband frequencies are not cleanly separable; all three target frequencies fit with comparable amplitudes.
- The stored-average common-mode movement argues for caution. The oscillatory component survives per-average offset/slope handling, but drift/baseline structure remains an important provenance issue.

## Claims not yet supported

- No claim-grade numeric `T2star` is supported from this dataset alone.
- No nearby-13C claim is supported. The `0.615 MHz` and `1.385 MHz` sideband tests are not distinguishable enough from the `1.0 MHz` carrier response on this short window.
- The forced `T2star ~0.184 us` fit should not be promoted as a result without a detuning/phase control or a better constrained model.
- This dataset does not establish whether the early-time response is purely NV Ramsey dephasing, a drift/baseline-correlated artifact, or a mixture.

## Recommended next action

Do not run another blind long-window Ramsey repeat. Run a targeted short-tau control that changes the programmed Ramsey detuning or phase while keeping the high-SNR short-window strategy, then require the oscillation to follow that programmed change before fitting and reporting `T2star`. If that control fails or remains ambiguous, close the r03 Ramsey/T2star branch as unsupported under current Ramsey conditions and move the 13C question to an alternate protocol such as echo/CPMG/XY8 rather than Ramsey sidebands.
