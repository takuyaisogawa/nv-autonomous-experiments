# Ramsey Review: short-tau r03 diagnostic

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New completed Ramsey data: `measurement/m001.json` raw savedexperiment export; `measurement/m002.json` job spec; `measurement/m003.json` terminal bridge result; `measurement/m004.json` status; `measurement/m005.json` control.
- Prior comparison/design evidence: `evidence/e003.json` terminal second 8 us Ramsey review, `evidence/e006.json` short-tau quantitative plan, `evidence/e009.json` verified intent/model, `evidence/e017.md` start note.
- Scratch outputs created here: `analyze_ramsey_shorttau.py`, `ramsey_shorttau_analysis.json`, `ramsey_shorttau_overview.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey_shorttau.py`.
- Confirmed terminal run: job `nv23_ramsey_20260513_230331_auto_ramsey`, completed `2026-05-14T01:23:47`, savedexperiment `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`, final count `35.122 kcps`, above the `20 kcps` gate.
- Confirmed settings: `auto__ramsey`, `mw_freq=3.8759 GHz`, programmed `det=1.0 MHz`, `tau=48 ns..1.968 us`, `41` points, `12 x 90000` repetitions, `1.08e6` shots per tau point. Active XML path has `full_experiment=0`, so readout 1 is the reference and readout 2 is the Ramsey signal.
- Raw/readout stats: reference mean `48.573 kcps`, signal mean `44.655 kcps`, signal peak-to-peak over tau `6.499 kcps`, ratio peak-to-peak `0.1433`. Median SEM across stored averages is `1.138 kcps` for raw signal and `0.0127` for signal/reference ratio.
- Least-squares screen used a linear baseline plus sine/cosine component. The strongest combined ratio component is near `1.192 MHz` with amplitude `0.0363` ratio units and baseline-residual R2 improvement `0.656`; the raw-signal screen peaks near `1.187 MHz` with amplitude `1.68 kcps` and R2 improvement `0.681`.
- Target checks:
  - Programmed `1.0 MHz`: ratio amplitude `0.0274`, raw-signal amplitude `1.28 kcps`, R2 improvement about `0.35..0.38`.
  - Prior 8 us top component `1.178 MHz`: ratio amplitude `0.0362`, raw-signal amplitude `1.68 kcps`, R2 improvement about `0.65..0.68`.
  - Expected sideband targets from the plan, `0.615 MHz` and `1.385 MHz`, are not favored over the `~1.18..1.20 MHz` component.
- Bootstrap over the 12 stored averages, resampling averages 500 times, found top ratio frequency median `1.195 MHz` with 16-84% range `1.180..1.210 MHz`; top ratio amplitude median `0.0364` with 16-84% range `0.0333..0.0395`; `97.8%` of bootstrap top frequencies fell in `1.1..1.3 MHz` and `0%` in `0.9..1.1 MHz`.
- Forward/reverse snake averages both show the same feature: forward ratio amplitude at `1.187 MHz` is `0.0385`, reverse is `0.0345`. First-half/last-half averages also retain it, though last-half amplitude is lower (`0.0409` vs `0.0321`).
- A scratch nonlinear fit check was run before the script was finalized. Free-frequency decaying fits preferred about `1.18..1.21 MHz` with model-dependent envelope times around a few us; fixed-`1 MHz` decays forced very short apparent T2* and large amplitudes. I am not promoting those fits as claims because the result is strongly model-dependent over only a `1.92 us` span.

## Plausible interpretation

- This new short-tau/high-SNR run does support a measurable Ramsey-like short-window feature on accepted r03. That is a meaningful change from the previous two long-window Ramsey reviews, where the features were too weak or inconsistent for a claim.
- The most plausible current reading is not a clean programmed-`1.0 MHz` Ramsey carrier. The strongest and most robust component is near `1.18..1.20 MHz`, matching the prior 8 us review's largest exploratory component (`1.178 MHz`) but now with better SEM and average-resampling support.
- The feature is visible in raw signal, point-wise ratio, and fitted-reference-line normalization, and it survives forward/reverse snake grouping. That argues against a simple monotonic acquisition-order ramp as the whole explanation.
- There was substantial average-to-average common-mode count variation: per-average signal means span `37.47..51.21 kcps` and reference means span `42.02..55.19 kcps`. Treat this as drift/count provenance. Ratio normalization helps but does not make the result automatically claim-grade.
- The frequency mismatch may mean the effective resonance/detuning shifted after the fine pODMR, or that the short-window shape is being fit by a nearby sinusoid due to baseline/sequence transients. A fresh resonance check is needed before assigning the component physically.

## Claims not yet supported

- No well-supported numeric T2* should be claimed from this dataset alone.
- No nearby-13C coupling or 13C absence conclusion is supported by this short-span scan. The span gives only about `0.52 MHz` nominal frequency resolution and was designed as a carrier/early-time diagnostic, not a sideband-resolved 13C measurement.
- Do not claim the observed feature is exactly the programmed `1.0 MHz` carrier. The bootstrap and LS screens favor `~1.195 MHz`.
- Do not claim the `3.8759 GHz` pODMR center was still current during this late Ramsey run, or that it shifted by exactly `~0.18..0.20 MHz`, without a fresh pODMR/resonance check.
- Do not treat the previous "no T2*/13C claim" as evidence that r03 has no Ramsey response. This run now shows a repeatable short-tau Ramsey-like feature, but not yet a final parameter.

## Recommended next action

Run a fresh weak-pi/fine pODMR or equivalent resonance check on r03 before another Ramsey. If it shows a resonance shift consistent with the `~1.18..1.20 MHz` effective Ramsey component, plan the next Ramsey from that fresh center with a model that can support a T2* fit and, only after the carrier/decay is established, a longer/higher-resolution 13C sideband check. Avoid another blind repeat of either prior Ramsey condition.
