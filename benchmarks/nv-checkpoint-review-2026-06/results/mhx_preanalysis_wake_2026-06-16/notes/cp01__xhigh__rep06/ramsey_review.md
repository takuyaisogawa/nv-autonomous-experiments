# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`, and relevant Ramsey/FFT guidance in `md/knowledge.md`.
- Prior Ramsey planning/provenance: `evidence/e005.json`, `evidence/e007.json`, `evidence/e009.json`, `evidence/e010.json`, `evidence/e011.json`.
- New completed Ramsey data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` execute spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control.
- Scratch artifacts generated here: `ramsey_analysis_summary.json` and `ramsey_review_plot.png`.

## Calculations or scripts run

- Ran inline Python/NumPy/SciPy checks on `measurement/m001.json`.
- Verified raw data shape: `ExperimentData` is `(1, 2, 31)` and `ExperimentDataEachAvg` is `(1, 4, 2, 31)`. The saved average exactly matches the mean of the four stored averages.
- Inspected the saved `ramsey.xml` text. With `full_experiment=0`, readout 1 is the ms=0 reference and readout 2 is the Ramsey signal, so the main observable used was signal/reference.
- Scan/acquisition: tau `0..6 us`, 31 points, `dt=0.2 us`, rFFT bin spacing `161.3 kHz` by sampled-grid convention, Nyquist `2.5 MHz`, 4 averages x 50000 repetitions, snake order, tracking per average.
- Drift/count checks:
  - Terminal result completed normally, final count `38.249 kcps`, about `12.9%` below the preceding weak-pODMR final count `43.890 kcps`, but above the `20 kcps` gate.
  - Saved final position `[117.279, 117.294, 115.535] um` is about `0.61 um` from the fresh r03 track position recorded in the job metadata.
  - Mean readout counts: reference `45.318 kcps`, signal `42.098 kcps`.
  - Mean signal/reference ratio `0.9292`, peak-to-peak `0.1355`, median per-point SEM from stored averages `0.0256`.
  - Per-average total count normalization to average 1: `[1.000, 0.938, 0.995, 0.960]`; per-average mean ratios were `[0.9347, 0.9298, 0.9199, 0.9377]`.
  - Scan-order drift check showed average 2 reference counts trending down in acquisition order (`p=0.022`), but ratio means were comparatively stable and the even snake order helps cancel first-order drift.
- Frequency/fitting checks on signal/reference:
  - A fixed `1.5 MHz` sinusoid, the programmed Ramsey detuning, had ratio amplitude `0.0058` and did not improve over a line baseline (`F p=0.81`; BIC worse than baseline).
  - Best free sinusoid was near `0.949 MHz` with ratio amplitude `0.0249`, but BIC was essentially tied with the line baseline (`Delta BIC = +0.22`, where positive is worse for the sinusoid model as counted here).
  - Descriptive damped fits found `~0.94 MHz` carriers with `T ~2.4 us` for exponential envelope and `T ~3.2 us` for Gaussian envelope, but these are not claim-grade because the expected carrier is absent and the model has enough freedom to chase the noisy low-frequency structure.
  - Resampling the four averages gave an unstable free-frequency distribution, roughly bimodal from `~0.86` to `~1.67 MHz`; fixed-1.5-MHz amplitude remained small.
- FFT checks:
  - Hann-windowed, line-detrended ratio FFT top bins were `0.968 MHz` (`0.0236` amplitude), `0.806 MHz` (`0.0213`), `0.323 MHz` (`0.0206`), and `1.935 MHz` (`0.0201`).
  - Expected carrier nearest bin to `1.5 MHz` was `1.452 MHz` with only `0.0116` amplitude.
  - Expected 13C sideband bins for `det +/- 0.385 MHz` were near `1.129 MHz` (`0.0124`) and `1.935 MHz` (`0.0201`), but there is no robust carrier-plus-symmetric-sideband pattern.

## Plausible interpretation

The Ramsey run completed and produced analyzable readouts. There is weak Ramsey-like modulation in the normalized trace, with the strongest time/FFT evidence around `0.94..0.97 MHz`, not at the programmed `1.5 MHz` carrier. A plausible physical interpretation is that the resonance/phase basis shifted by roughly several hundred kHz during the run, or that the Ramsey phase-ramp behavior plus residual detuning did not produce the expected carrier. Count drift and scan-order effects are present but not catastrophic after normalization.

Treat the `T ~2..3 us` damped-fit result only as a follow-up hypothesis. The data quality and carrier mismatch do not support promoting it to the project T2star conclusion.

## Claims not yet supported

- No well-supported numeric T2star claim is supported by this scout.
- No well-supported nearby-13C claim is supported. The `1.935 MHz` FFT bin is compatible with the planned upper sideband location, but the expected carrier is weak and the lower sideband is not comparably supported.
- The Ramsey result does not invalidate the prior r03 alignment claim; it mainly says the first Ramsey scout is non-claim-grade.
- Do not claim a sequence bug from this single scout. The saved sequence and job metadata match the intended `tau` Ramsey route, but the carrier mismatch should be checked by recalibration/repeat before blaming control logic.

## Recommended next action

Do a short r03 recentering step before repeating Ramsey: TrackCenter/count check plus a fine weak-pi pODMR around the current `3.876 GHz` basis, wide enough to catch an inferred `~0.5 MHz` center shift. If r03 remains trackable and the resonance is clear, repeat Ramsey with the updated center and an advisory-checked grid that keeps the carrier and possible `~0.385 MHz` 13C sidebands below Nyquist. Favor more independent averages or a cleaner current-center repeat over a blind same-settings repeat; keep per-average tracking-window guidance explicit.
