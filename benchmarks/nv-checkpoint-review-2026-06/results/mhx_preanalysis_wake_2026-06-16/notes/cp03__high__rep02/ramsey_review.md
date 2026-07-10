# Ramsey Review: short-tau/high-SNR r03 diagnostic

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`, plus prior Ramsey/design context in `evidence/e003.json` and `evidence/e017.md`.
- New terminal measurement data:
  - `measurement/m001.json`: raw savedexperiment export for `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
  - `measurement/m002.json`: bridge job spec for `nv23_ramsey_20260513_230331_auto_ramsey`.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json`: terminal bridge status.
  - `measurement/m005.json`: run control.
- Scratch artifact created: `ramsey_shorttau_review.png`.

## Calculations or scripts run

- Used inline Python/NumPy to inspect JSON schemas, data shapes, run metadata, and terminal status.
- Treated trace 1 as reference and trace 2 as Ramsey signal, following the prior project Ramsey review convention. The new raw export has `ExperimentData` shape `1 x 2 x 41` and `ExperimentDataEachAvg` shape `1 x 12 x 2 x 41`.
- Confirmed run settings from data/spec: `tau = 48 ns..1.968 us`, 41 points, `dt = 48 ns`, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `12 x 90000` shots per tau point.
- Completion/status checks: bridge status `completed`, no error message, no stop request, safe shutdown ok. Terminal final count text was `Final = 35.122 kcps`, above the job's `20 kcps` minimum but lower than the pre-run/latest-context value.
- Raw/readout summary:
  - Reference mean over tau `48.573 kcps`, std over tau `0.456 kcps`.
  - Signal mean over tau `44.655 kcps`, std over tau `1.574 kcps`.
  - Signal/reference ratio mean `0.9195`, std over tau `0.0348`, min/max `0.8396..0.9829`.
  - Median per-point SEM from stored averages: signal `1.138 kcps`, ratio `0.0127`.
- Drift/provenance checks:
  - Per-average reference means ranged `42.016..55.188 kcps`; signal means ranged `37.474..51.213 kcps`; ratio means ranged `0.893..0.956`.
  - Intra-average reference first/second-half differences in scan order were at most about `2.1 kcps`; no hard acquisition anomaly, but common-mode count drift is real provenance.
- Least-squares sinusoid screens used a linear baseline plus sine/cosine terms:
  - At programmed carrier `1.000 MHz`: ratio amplitude `0.0274`, raw-signal amplitude `1.282 kcps`, baseline residual improvement `0.355` for ratio and `0.377` for raw signal.
  - Blind combined-ratio screen peaks broadly near `1.192 MHz`: ratio amplitude `0.0363`, residual improvement `0.656`.
  - Expected 13C sideband targets are not distinguishable in this short window: low sideband `0.615 MHz` ratio amplitude `0.0243`, high sideband `1.385 MHz` ratio amplitude `0.0271`.
  - Prior non-claim feature `0.884 MHz` is weak here: ratio amplitude `0.0126`, residual improvement `0.071`.
- FFT check on linear-detrended ratio has coarse bin spacing `0.508 MHz`; largest bins below 2.5 MHz are `0.508 MHz` amplitude `0.0300` and `1.016 MHz` amplitude `0.0280`. This is useful as a sanity check only, not frequency-resolution evidence.
- Damped-cosine fits were exploratory:
  - Free-frequency ratio fit found about `1.198 MHz`, initial amplitude `0.0417`, `T2* ~ 6.3 us`, but the `T2*` uncertainty was larger than the fitted value and the scan spans only `1.92 us`.
  - Fixed-`1 MHz` damped fit was unstable, with an inflated early amplitude and `T2* ~ 0.16 us`; do not use it as a physical T2* result.

## Plausible interpretation

- This short-tau/high-SNR run is qualitatively stronger than the prior two Ramsey attempts. It supports a real short-time Ramsey response on accepted r03: the programmed `1 MHz` component is now above the median per-point SEM and much larger than in the prior 8 us run (`0.0274` ratio amplitude here versus prior `0.00916`; `1.282 kcps` raw signal here versus prior `0.277 kcps`).
- The data argue against the strict failure mode "no visible Ramsey carrier at early tau" and against an extremely short signal that disappears before roughly `2 us`.
- The best blind frequency is broad and shifted toward `~1.19 MHz`, while the FFT resolution is coarse because the deliberate span is short. Treat the frequency offset as diagnostic, not as a precise physical frequency.
- The run is compatible with r03 remaining the aligned target and with short-tau Ramsey contrast being present under higher-SNR/no-tau0 conditions.

## Claims not yet supported

- No numeric `T2*` claim is supported. The scan is too short to constrain decay, and damped-cosine fits are model-dependent/unstable.
- No nearby `13C` claim is supported. The `0.615 MHz` and `1.385 MHz` sideband screens are comparable to the carrier under this short-span model, and FFT resolution is too coarse to separate them cleanly.
- Do not claim the blind `~1.19 MHz` screen peak as a calibrated detuning or coupling. It may reflect short-window fitting ambiguity, baseline/envelope structure, or a real detuning shift, but this run alone does not decide.
- Do not claim the final count drop as a target loss. Counts stayed above threshold and the ratio signal is present, but average-to-average common-mode drift should be carried forward as provenance.

## Recommended next action

Run an advisory-checked medium-window Ramsey on the same r03 that keeps the successful changes from this diagnostic: no `tau=0`, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, high total shots, and even averages. Extend the span enough to constrain decay and improve sideband resolution, for example about `48 ns..6 us` with `~96 ns` spacing, while reducing repetitions per average and increasing averages or splitting jobs so the per-average tracking window stays under the active cap. Use that run first to establish a stable carrier/decay and only then evaluate a numeric `T2*` and 13C sidebands.
