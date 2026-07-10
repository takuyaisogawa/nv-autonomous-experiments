# Ramsey Review

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/advice.md`, `project/state.md`, and signal/drift guidance from `md/memory.md` and `md/knowledge.md`.
- Ramsey measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` terminal status, `measurement/m005.json` control state.
- Prior Ramsey setup context: `evidence/e009.json` job artifact, `evidence/e010.json` running status, `evidence/e011.json` batch state. Prior r03 acceptance came from the project state and weak-pi pODMR context summarized there.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Script outputs: `ramsey_analysis_summary.json` and `ramsey_analysis.png`.
- Parsed the raw export as 2 readout traces x 31 tau points, with 4 averages x 50000 repetitions, `tau = 0..6 us` in `0.2 us` steps, snake scan order, `mw_freq = 3.876 GHz`, and programmed `det = 1.5 MHz`.
- Treated readout 1 as reference-like and readout 2 as signal-like, matching the project readout convention and raw levels.
- Computed signal/reference ratio, per-point SEM across averages, forward/reverse average agreement under snake order, acquisition-order slopes, FFT of the linearly detrended ratio, and descriptive sinusoid/damped-cosine fits.

Key numerical checks:

- Terminal Ramsey completed, but final count text was `38.249 kcps`, down from the immediate pre-Ramsey weak-pi context of `43.890 kcps` by `12.9%`.
- Saved scan position was `[117.279, 117.294, 115.535] um`, offset from fresh tracked `[117.314436, 117.761644, 115.141679] um` by `[-0.035, -0.468, +0.393] um`.
- Aggregate readouts: reference mean `45.318 kcps`, signal mean `42.098 kcps`. Ratio mean `0.9292`, range `0.8591..0.9946`, peak-to-peak `0.1355`; median ratio SEM across averages `0.0256`.
- Per-average ratio means were stable-ish (`0.9347, 0.9298, 0.9199, 0.9377`), but forward averages 1+3 and reverse averages 2+4 had weak tau-order agreement (`corr = 0.126`, RMS ratio difference `0.0592`), so tau-dependent structure is not robust across scan direction.
- FFT of detrended ratio had top bins at `0.968, 0.323, 0.806, 1.613, 1.935, 1.290 MHz`. The expected `1.5 MHz` carrier is split between nearby bins and is not isolated; the `~1.115/1.885 MHz` 13C sideband bins are not uniquely distinguished from unrelated comparable peaks.
- A fixed `1.5 MHz` sinusoid plus line gave amplitude `-0.0094 +/- 0.0048` in ratio units, `R2 = 0.0067`, reduced chi2 `2.45`, no improvement over the linear null (`R2 = 0.0077`, reduced chi2 `2.41`).
- A free damped cosine gave a descriptive `T2* = 2.74 +/- 1.33 us` at `1.681 MHz`, but only `R2 = 0.173` and reduced chi2 `1.97`; this is not claim-grade and should not be promoted as a T2* estimate.

## Plausible interpretation

The Ramsey job completed and contains real readout variation, but this first scout is non-claim-grade. The raw signal/reference trace has modulation above the median per-point SEM, yet the modulation is not cleanly locked to the programmed `1.5 MHz` Ramsey carrier, and forward/reverse snake averages do not reproduce the tau dependence well. The count drop, saved-position shift, and average-to-average readout changes make drift/common-mode variation a plausible contributor.

r03 remains the best aligned candidate from the previous pODMR evidence; this Ramsey does not invalidate that alignment. It only says this particular Ramsey acquisition is too ambiguous for T2* or 13C conclusions.

## Claims not yet supported

- No well-supported T2* value is established from this measurement.
- No well-supported nearby `13C` coupling or sideband conclusion is established.
- The free damped-cosine fit should not be used as a physical T2* claim.
- The FFT peaks should not be interpreted as `13C` evidence, and the absence of clean peaks should not be interpreted as evidence of no nearby `13C`.
- This Ramsey does not prove r03 is a bad NV or that the pODMR resonance was wrong.

## Recommended next action

Do not make T2* or `13C` claims yet. Continue targeted work on r03 with a drift-aware Ramsey repeat after a fresh TrackCenter/count check. Preserve roughly the same total shots but shorten the untracked per-average window by reducing repetitions per average and increasing the even average count, for example evaluate an advisory for `8 x 25000` or `10 x 20000` rather than `4 x 50000`. Keep the tau span sufficient for the `1.5 MHz +/- ~0.385 MHz` FFT check unless the advisory forces a smaller scan. If the repeat still lacks a clean carrier, stop repeating Ramsey blindly and first re-check the weak-pi pODMR center or Ramsey detuning/sequence behavior.
