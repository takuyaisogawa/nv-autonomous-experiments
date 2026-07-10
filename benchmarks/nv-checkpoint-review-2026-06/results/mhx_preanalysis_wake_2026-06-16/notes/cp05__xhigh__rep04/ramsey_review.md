# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`.
- Prior planning context: `evidence/e014.json` for the refreshed-center Ramsey model/advisory and target frequencies.
- New terminal measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` run control.
- Local analysis artifacts created here: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis_plot.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey.py`.
- Verified raw axis contract: `ExperimentData` shape is `[1,2,41]`, `ExperimentDataEachAvg` shape is `[1,20,2,41]`; the stored-average mean matches the combined reference and signal traces.
- Confirmed scan settings: `ramsey.xml`, `mw_freq=3.8765 GHz`, `det=1.5 MHz`, `tau=0.048..8.048 us`, `0.2 us` step, `41` points, `20 x 50000` shots, snake order.
- Terminal health checks: job completed, final counts `43.433 kcps`, safe shutdown true, no abort, no stop request, monitor `last_error=""`.
- Robust common-mode average check flagged no averages at `abs(z)>3.5`, but average-level brightness span was not small: reference mean span `27.2%`, signal mean span `29.1%`.
- Weighted sinusoid least-squares screens with linear baseline, plus FFT and subset checks:
  - Full span top component is near `2.268 MHz` in raw signal, point-wise ratio, and fitted-reference-line normalization.
  - Full span target amplitudes: carrier `1.5 MHz` is `0.713 kcps` raw / `0.0148` ratio / `0.0146` refline-normalized; low 13C sideband `1.115 MHz` is weak (`0.116 kcps` raw / `0.0036` ratio / `0.0024` refline); high sideband `1.885 MHz` is smaller than the full-span top and not paired with the low sideband.
  - Skipping the first 4 tau points moves raw and refline-normalized tops to about `1.520 MHz`, but point-wise ratio still tops near `2.263 MHz`.
  - Direction split is not stable: odd/forward averages top near `2.28 MHz`, while even/reverse averages top near `1.51 MHz`.

## Plausible interpretation

The measurement completed cleanly and is analyzable. The combined data contain real oscillatory structure above pure numerical noise, and the skip-transient raw/refline view has a carrier-like component near the programmed `1.5 MHz` detuning. However, the result is still not a clean Ramsey/T2star dataset: the full-span dominant component is near `2.27 MHz`, the first few tau points strongly affect the screen, and the frequency preference changes with snake scan direction. That pattern is more consistent with mixed physical Ramsey response plus scan-order/transient/baseline sensitivity than with a single robust carrier/decay model.

The refreshed pODMR center did not convert the r03 Ramsey branch into a claim-grade carrier/sideband result. The data are useful evidence that same-protocol Ramsey repeats are unlikely to resolve the objective by simple shot accumulation.

## Claims not yet supported

- No numeric T2star should be promoted from this run.
- No nearby 13C claim is supported: the expected low/high sidebands at about `1.115/1.885 MHz` are not a consistent paired feature across views, skip-transient handling, and average subsets.
- Do not claim the `2.268 MHz` full-span component as a physical Ramsey frequency; it is scan-direction/transient sensitive.
- Do not claim sub-grid or fully solved microwave-center precision from the prior pODMR refresh based on this Ramsey outcome.

## Recommended next action

Stop doing blind same-protocol Ramsey repeats on r03. The next project action should be a deliberate alternate diagnostic: design a scan-order-insensitive or randomized/phase-cycled Ramsey check with shorter per-average windows, or switch to an alternate protocol for T2star/13C evidence. If that is not available, record the current r03 Ramsey/T2star/13C state as unsupported under these conditions rather than fitting a T2star from this dataset.
