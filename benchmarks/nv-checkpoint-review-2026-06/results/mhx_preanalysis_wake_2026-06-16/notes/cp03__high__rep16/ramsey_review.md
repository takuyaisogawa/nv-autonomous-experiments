# Ramsey Review: short-tau r03 diagnostic

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`.
- Prior Ramsey/design context: `evidence/e003.json` (terminal det=1.0 MHz, 8 us Ramsey review), `evidence/e009.json` (short-tau diagnostic intent/model), `evidence/e017.md` (short-tau start note).
- New terminal measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control.

## Calculations or scripts run

- Created and ran `analyze_ramsey_shorttau.py`.
- Outputs: `ramsey_shorttau_analysis.json` and `ramsey_shorttau_review.png`.
- Checks performed:
  - Parsed readouts using prior `ramsey.xml/full_experiment=0` convention: channel 0 reference, channel 1 Ramsey signal.
  - Verified terminal run metadata: job `nv23_ramsey_20260513_230331_auto_ramsey`, `auto__ramsey`, `mw_freq=3.8759 GHz`, `det=1.0 MHz`, `tau=48 ns..1.968 us`, 41 points, `12 x 90000` repetitions, completed, no stop request, monitor error empty.
  - Verified scan-order mode is snake and stored data are in tau order.
  - Computed signal/reference ratio, per-point SEM across 12 stored averages, fixed-frequency linear least-squares components, exploratory frequency screen, FFT sanity check, per-average screens, and phase consistency.

## Quantitative results

- Combined raw signal mean `44.655 kcps`; reference mean `48.573 kcps`; ratio mean `0.91946`.
- Median per-point SEM: signal `1.138 kcps`, ratio `0.01271`.
- Signal peak-to-peak: `5.69 kcps` in the first `0.75 us`, `6.50 kcps` over the full short window. Ratio peak-to-peak: `0.1108` in the first `0.75 us`, `0.1433` full-window.
- Fixed-frequency LS components on ratio:
  - Expected low 13C sideband `0.6154 MHz`: amplitude `0.02428`, baseline-residual improvement `0.311`.
  - Programmed carrier `1.000 MHz`: amplitude `0.02741`, improvement `0.355`; raw-signal amplitude `1.282 kcps`.
  - Expected high 13C sideband `1.3846 MHz`: amplitude `0.02715`, improvement `0.345`.
  - Prior 8 us top component `1.178 MHz`: amplitude `0.03617`, improvement `0.654`; raw-signal amplitude `1.678 kcps`.
- Exploratory ratio screen peaks near `1.19 MHz` (`1.192 MHz`, amplitude `0.03631`, improvement `0.656`).
- Per-average fixed-frequency phase is repeatable:
  - `1.178 MHz` phase resultant length `0.968`.
  - `1.192 MHz` phase resultant length `0.967`.
  - `1.000 MHz` phase resultant length `0.948`.
- FFT bin spacing is coarse at `0.508 MHz`; strongest ratio FFT bins are `0.508 MHz` and `1.016 MHz`. This short-window FFT is not a high-resolution 13C sideband test.
- A free decaying-cosine fit to ratio preferred about `1.198 MHz`, but the fitted decay was poorly constrained: `T2* ~6.29 us` with `~9.61 us` standard error. Do not promote this as a T2* value.

## Plausible interpretation

- This short-tau/high-SNR diagnostic does show a real-looking early-time Ramsey oscillatory component on accepted r03. The strongest combined component is near `1.18..1.19 MHz`, and its phase is consistent across stored averages.
- The result is stronger than the prior det=1.0 MHz, 8 us run because the same approximate `1.178 MHz` component is now visible in the short-tau trace with much larger residual improvement.
- A plausible physical reading is that the Ramsey detuning is offset from the nominal programmed `1.0 MHz` by roughly `0.18..0.20 MHz`, possibly from residual resonance-center error or local shift. This is an inference, not yet a demonstrated det-following model.
- The data argue against the specific failure mode that there is no early-time Ramsey signal at this shot budget. They do not yet give a stable envelope or sideband pattern.

## Claims not yet supported

- No claim-grade numeric `T2*`: the short span and free decaying-cosine fit leave the decay time underconstrained.
- No nearby `13C` conclusion: the target sidebands at `0.615` and `1.385 MHz` are not dominant over the `1.18..1.19 MHz` component, and the short-window FFT resolution is too coarse to resolve sidebands cleanly.
- Do not claim the programmed `1.0 MHz` carrier model is fully validated: a 1.0 MHz component is present, but the best combined fit is consistently higher near `1.19 MHz`.
- Do not claim that per-average count changes are absent. Average signal/reference means vary substantially common-mode; ratio normalization is usable, but this remains provenance for cautious interpretation.

## Recommended next action

Run a targeted detuning clarification before any T2* or 13C closeout: use r03 and test whether the observed Ramsey frequency follows the programmed detuning/frequency setting, for example with two short-tau Ramsey checks at deliberately shifted `mw_freq` or `det` around the current `3.8759 GHz` basis. If the `~1.19 MHz` feature follows as a Ramsey carrier, then run a longer/high-SNR Ramsey designed around that calibrated carrier to fit T2* and only then revisit 13C sidebands. If it does not follow, treat the r03 Ramsey/13C branch as unsupported under current conditions rather than repeating blind long-window scans.
