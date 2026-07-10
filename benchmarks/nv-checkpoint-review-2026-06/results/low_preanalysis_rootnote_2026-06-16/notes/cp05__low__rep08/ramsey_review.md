# Ramsey Review

## Files/data used

- `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`: project context and required Ramsey interpretation gates.
- `measurement/m001.json`: terminal raw savedexperiment export for `nv23_ramsey_20260514_055148_auto_ramsey`.
- `measurement/m002.json`: submitted measurement spec.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal result/status/control provenance.
- Prior evidence context in `evidence/` was searched for the intended targets and prior Ramsey conclusions.

## Calculations or scripts run

- Ran local Python scratch analysis from PowerShell against `measurement/m001.json`.
- Parsed `ExperimentData` and `ExperimentDataEachAvg` as two readout channels over 41 tau points and 20 averages.
- Checked raw signal, point-wise signal/reference ratio, and signal divided by a fitted linear reference.
- Performed linear-baseline sinusoid least-squares screens at:
  - programmed carrier: `1.5 MHz`
  - expected 13C sidebands: `1.115 MHz`, `1.885 MHz`
  - prior controls: `1.192 MHz`, `1.623 MHz`
- Performed exploratory frequency screens from `0.125..2.4 MHz`, including a skip-first-4-points check.
- Checked per-average ratio frequency screens and simple average-to-average brightness/ratio drift summaries.
- Wrote local artifacts:
  - `ramsey_analysis_summary.json`
  - `ramsey_review_trace.png`
  - `ramsey_review_ratio.png`

## Plausible interpretation

- The run completed cleanly: `20 x 50000` shots, `tau = 0.048..8.048 us` in 41 points, snake scan order, terminal final counts `43.433 kcps`, no abort/stop/error in the terminal bridge status.
- Combined raw signal peak-to-peak is `6.27 kcps`, but median per-point signal SEM across averages is `0.85 kcps`; the visible structure is not enough by itself to claim a Ramsey model.
- The programmed carrier is present weakly but not decisively:
  - raw signal LS amplitude at `1.5 MHz`: `0.705 kcps`, below the median raw SEM (`0.850 kcps`)
  - signal/reference LS amplitude at `1.5 MHz`: `0.01575`, about `1.36x` the median ratio SEM (`0.01161`)
  - fitted-reference-normalized LS amplitude at `1.5 MHz`: `0.01447`
- The strongest combined exploratory screen is near `2.27 MHz` in all combined views, not at the programmed `1.5 MHz` carrier or expected `1.115/1.885 MHz` sidebands. Skip-first-4-points screens still favor about `2.27 MHz`.
- Sideband support is weak and asymmetric:
  - ratio LS amplitude at `1.115 MHz`: `0.00277`
  - ratio LS amplitude at `1.885 MHz`: `0.00961`
  - neither sideband pair is cleanly promoted over the carrier/top-screen ambiguity.
- Per-average ratio screens are mixed, with top frequencies spread from the low search edge to above `2 MHz`; median top frequency is about `1.56 MHz` with a wide IQR (`0.82..2.07 MHz`). This argues against a stable, claim-grade carrier/sideband model.
- Simple drift summaries show average-to-average brightness movement, but the normalized ratio mean varies less than raw brightness. This is provenance to keep in mind, not enough here to rescue or invalidate a T2star/13C claim.

## Claims that are not yet supported

- Do not claim a numeric `T2star` from this run.
- Do not claim resolved nearby `13C` coupling from this run.
- Do not claim that the `2.27 MHz` exploratory top is a physical Ramsey frequency without additional detuning-controlled evidence.
- Do not claim that the refreshed pODMR center fully fixed the prior Ramsey ambiguity; this long-span/high-shot run remains non-claim-grade.

## Recommended next action

Stop blind Ramsey repeats on r03 under the same conditions. The best next action is a decision point: either switch to an alternate protocol designed to establish dephasing/coupling more robustly under these conditions, or record a supported negative/unsupported r03 Ramsey/13C conclusion for the current setup and move to another candidate/strategy.
