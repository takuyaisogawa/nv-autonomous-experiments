# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New Ramsey terminal data and metadata:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
  - `measurement/m002.json`: submitted Ramsey job spec.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json` and `measurement/m005.json`: terminal status/control provenance.
- Recent planning/provenance evidence: `evidence/e022.json`, `evidence/e023.json`, `evidence/e024.json`.
- Local outputs created here: `analyze_ramsey.py`, `ramsey_analysis.json`, `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed combined raw data with shape `[1, 2, 41]` and per-average data with shape `[1, 20, 2, 41]`.
- Confirmed Ramsey grid: tau `48 ns..8.048 us`, 41 points, `dt = 200 ns`, span `8.0 us`, nominal frequency resolution `125 kHz`, Nyquist `2.5 MHz`.
- Reviewed raw signal, point-wise `signal/reference`, and signal normalized by a fitted reference line.
- Ran least-squares sinusoid screens from `0.125..2.45 MHz`, including explicit target amplitudes at the programmed carrier `1.5 MHz`, expected 13C sidebands `1.115/1.885 MHz`, previous det-shift feature `1.623 MHz`, and previous det=1.0 diagnostic feature `1.192 MHz`.
- Ran the same LS screen after skipping the first 4 tau points.
- Ran windowed FFT checks and per-average LS screens.
- Ran a descriptive grid fit of point-wise ratio to a damped sinusoid; this is recorded only as descriptive because signal assignment is not supported.

## Quantitative checks

- Terminal run completed cleanly: bridge status `completed`, no abort/stop, final counts `43.433 kcps`, `20 x 50000` shots, saved data present.
- Mean readouts: reference `48.79 kcps`, signal `44.67 kcps`, mean point-wise ratio `0.9156`.
- Per-point uncertainty scale: median signal SEM `0.850 kcps`; median ratio SEM `0.0116`; fitted-reference ratio SEM estimate `0.0174`.
- Common-mode average variation is nontrivial: average signal mean range `37.38..50.37 kcps`, reference mean range `41.74..54.90 kcps`, signal CV `7.1%`, reference CV `6.7%`, ratio mean range `0.891..0.959`.
- Combined LS screens:
  - Raw signal top: `2.272 MHz`, amplitude `0.818 kcps`; carrier `1.5 MHz` amplitude `0.705 kcps`; sidebands `1.115/1.885 MHz` amplitudes `0.146/0.261 kcps`.
  - Point-wise ratio top: `2.270 MHz`, amplitude `0.01845`; carrier amplitude `0.01575`; sidebands `0.00277/0.00961`.
  - Fitted-reference ratio top: `2.272 MHz`, amplitude `0.01678`; carrier amplitude `0.01447`; sidebands `0.00299/0.00536`.
- Skip-first4 LS screens still top near `2.27 MHz`, but amplitudes shrink: point-wise ratio top `0.01417`, carrier `0.01231`, sidebands `0.00068/0.00528`.
- FFT checks are method-dependent: raw and fitted-reference views top near `2.317 MHz`, while point-wise ratio FFT top is near `1.463 MHz`.
- Per-average ratio screens are mixed: only `4/20` averages have top frequency within `0.15 MHz` of `1.5 MHz`; `4/20` are near `2.27 MHz`; `3/20` are near either expected 13C sideband.
- Descriptive damped-sinusoid grid fit on point-wise ratio gives `f = 2.275 MHz`, `T2star = 2.57 us`, amplitude `0.0553`, `R2 = 0.56`; this fit is not promoted because the frequency is not the planned carrier/sideband model and per-average/method consistency is weak.

## Plausible interpretation

The refreshed-center long-span Ramsey completed safely and contains analyzable oscillatory structure. The strongest combined LS feature is around `2.27 MHz` in raw, point-wise ratio, and fitted-reference normalization, while the FFT view partly conflicts by putting point-wise normalization near the programmed `1.5 MHz` carrier. The carrier-sized response is present but not dominant, is near the per-point uncertainty scale in raw units, and does not appear consistently as the top per-average component.

The expected 13C sideband pattern is not supported. The lower sideband near `1.115 MHz` is weak in all combined views, and the upper sideband near `1.885 MHz` is not consistent enough across views or averages to claim a coupling model.

This is useful evidence that simply adding more shots at the refreshed pODMR center did not resolve the Ramsey/T2star/13C ambiguity. It does not invalidate r03 as an aligned NV; it limits what can be claimed from Ramsey under the current protocol/settings.

## Claims that are not yet supported

- No supported numeric `T2star` claim from this dataset.
- No supported nearby `13C` coupling/sideband claim.
- Do not claim the `2.27 MHz` feature is physical without a control showing it tracks programmed detuning or microwave frequency.
- Do not claim the programmed `1.5 MHz` carrier is cleanly recovered; it is present but not dominant or per-average consistent.
- Do not claim sub-grid pODMR resonance precision beyond the prior grid-supported `3.8765 GHz` calibration.

## Recommended next action

Do not run another blind long-span Ramsey repeat. The next action should be a targeted control that decides whether the observed Ramsey frequency tracks the programmed detuning/microwave setting. A compact two-condition Ramsey diagnostic is the most direct: keep the same r03 target and refreshed pODMR basis, but deliberately shift `det` or `mw_freq` enough that a real Ramsey carrier should move predictably while fixed analysis/apparatus artifacts should not. If that control remains mixed, record a supported "Ramsey/T2star and 13C not resolved under current conditions" conclusion for r03 and pivot to an alternate protocol rather than continuing Ramsey repeats.
