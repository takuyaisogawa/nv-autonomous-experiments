# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `context.json`, `md/memory.md`, `md/knowledge.md`.
- Prior evidence: especially `evidence/e003.json` for the terminal 8 us det=1.0 MHz Ramsey review, `evidence/e006.json` for the short-tau design/model, and `evidence/e017.md` for the short-tau job-start note.
- New measurement: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control.

## Calculations or scripts run

- Added and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis_results.json` and `ramsey_shorttau_review.png`.
- Confirmed terminal run: `nv23_ramsey_20260513_230331_auto_ramsey`, completed `2026-05-14T01:23:47`, savedexperiment `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`, no stop request, final counts `35.122 kcps`.
- Measurement settings from raw/job metadata: `tau = 48 ns..1.968 us`, 41 points, `48 ns` spacing, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `12 x 90000` repetitions, two readouts, snake order, saved in tau order.
- Sampling checks: Nyquist `10.42 MHz`; nominal frequency resolution from the short span is only `0.521 MHz`, so this run can test early-time carrier visibility but is not a high-resolution 13C sideband measurement.
- Readout-aware checks:
  - Raw signal mean `44.65 kcps`, raw reference mean `48.57 kcps`.
  - Median per-point SEM across stored averages: signal `1.14 kcps`, reference `1.12 kcps`.
  - Raw signal span across tau `6.50 kcps`, but average-to-average means have large common-mode variation: reference range `26.8%` of median and signal range `30.8%`; late-three average means are about `14%` below early-three means in both channels.
- Target least-squares amplitudes:
  - Carrier `1.000 MHz`: raw signal `1.26 kcps` after linear detrending, ratio amplitude `0.0274`, reference-line-normalized amplitude `0.0264`.
  - Expected low 13C sideband near `0.615 MHz`: raw signal `1.10 kcps`, ratio `0.0243`, reference-line-normalized `0.0227`.
  - Expected high 13C sideband near `1.385 MHz`: raw signal `1.21 kcps`, ratio `0.0271`, reference-line-normalized `0.0251`.
- Exploratory frequency screen was restricted to frequencies with at least about one cycle over the short window. The strongest combined components are near `1.20 MHz`:
  - Raw signal detrended top: `1.205 MHz`, amplitude `1.69 kcps`.
  - Ratio detrended top: `1.207 MHz`, amplitude `0.0364`.
  - Reference-line-normalized top: `1.205 MHz`, amplitude `0.0347`.
  - Per-average top frequencies are mixed: many averages choose `~1.15..1.29 MHz`, while several choose the lowest resolvable bin `0.521 MHz`; carrier amplitudes per average are `0.65..2.04 kcps`.

## Plausible interpretation

- The run completed and returned analyzable short-tau Ramsey data. There is no hard bridge/abort anomaly in the available measurement files.
- The short-tau/high-SNR diagnostic improves on the earlier 8 us data in the sense that a weak resolvable component around `~1.2 MHz` appears again in combined raw, ratio, and reference-line-normalized views. This is plausibly the same non-claim-grade feature previously seen near `1.178 MHz` in the det=1.0 MHz 8 us review.
- The result still does not support a clean programmed-carrier model. The explicit `1.0 MHz` carrier amplitude is only about the median signal SEM and is not dominant over the expected 13C sideband checks. The strongest combined component is offset to `~1.2 MHz`, and the short span makes frequency assignment coarse.
- The large common-mode stored-average changes mean the tau-shape cannot be treated as a precise decay envelope without stronger carrier evidence. A T2star fit would be model-driven rather than data-supported.

## Claims that are not yet supported

- No supported numeric `T2star` value from this Ramsey dataset.
- No supported nearby `13C` conclusion from this dataset.
- No supported assignment of the `~1.2 MHz` feature to the programmed Ramsey carrier, a physical detuning, a 13C sideband, or an artifact.
- No claim that the aligned r03 candidate is invalidated; the prior pODMR alignment evidence still stands in the provided project context.

## Recommended next action

Do not run another blind Ramsey repeat on r03. Treat the r03 Ramsey/T2star/13C branch as unresolved under the current Ramsey conditions. If continuing r03, use a non-blind diagnostic that changes the question: first inspect/verify the `auto__ramsey` phase/frequency convention and then run a controlled detuning/frequency diagnostic or switch to an alternate protocol such as echo/CPMG for coherence/13C evidence. Defer any T2star fit or 13C claim until a raw/readout-aware carrier or sideband model is actually supported.
