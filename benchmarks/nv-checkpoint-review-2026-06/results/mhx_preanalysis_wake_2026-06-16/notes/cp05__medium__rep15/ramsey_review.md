# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New terminal Ramsey data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` submitted job, `measurement/m003.json` terminal result, `measurement/m004.json` final status, `measurement/m005.json` control state.
- Planning/calibration context: `evidence/e014.json` refreshed-center Ramsey design and targets; `evidence/e001.json` preceding weak-pi pODMR refresh selecting `mw_freq = 3.8765 GHz`.
- Scratch outputs created here: `analyze_ramsey_review.py`, `ramsey_review_analysis.json`, `ramsey_review_plot.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey_review.py`.
- Axis contract check passed: `ExperimentDataEachAvg` shape `[20, 2, 41]`; averaging across the 20 stored averages reproduced `ExperimentData` to numerical precision (`max_abs_sig_mean_delta = 7.1e-15 kcps`).
- Scan: `tau = 48 ns..8.048 us`, `41` points, `200 ns` step, `20 x 50000 = 1.0e6` shots per tau point. Readout basis from `ramsey.xml`/metadata: readout 1 is `mS=0` reference, readout 2 is Ramsey signal.
- Terminal health: completed safely, final counts `43.433 kcps`, stop not requested.
- Drift check from snake acquisition order found no flagged averages. Largest negative common-mode slope was average 8, about `-6.4%`, below the `15%` drop threshold.
- Combined raw signal statistics: mean signal `44.67 kcps`, median per-point signal SEM `0.85 kcps`, raw signal peak-to-peak `6.27 kcps`. Point-wise ratio median SEM was `0.0116`.
- Least-squares sinusoid screens with offset/slope terms:
  - Programmed carrier `1.5 MHz`: raw amplitude `0.705 kcps`, point-wise ratio amplitude `0.0157`; rough coefficient-level significance about `2.5 sigma`.
  - Expected 13C sidebands from the project model, `1.115 MHz` and `1.885 MHz`: raw amplitudes `0.145/0.261 kcps`; ratio amplitudes `0.0028/0.0096`. These are weak and not symmetric.
  - Prior fixed-control frequency `1.192 MHz`: raw amplitude `0.110 kcps`, ratio amplitude `0.0019`; weak in this run.
  - Unconstrained LS screen top was off-model near `2.27 MHz` in raw, point-wise ratio, and reference-line-normalized views; skipping the first four tau points did not remove this top feature.
- FFT check on the point-wise ratio placed large bins near the carrier region (`1.463/1.585 MHz`) but also near high frequencies (`2.317/2.195 MHz`). This supports only weak carrier-like content, not a clean model.
- Per-average frequency screens were mixed: raw top frequencies ranged broadly from about `0.2 MHz` to `2.29 MHz`; only some averages had carrier-near tops. Carrier phase/coherence was better than sidebands but still not enough to promote a physical T2star/13C model.

## Plausible interpretation

- The acquisition itself is usable: terminal metadata, raw export, readout axis, shot count, and drift checks do not show a hard anomaly.
- The refreshed center probably improved carrier-like evidence compared with the earlier fixed-control concern: the old `~1.192 MHz` artifact-control target is weak, and FFT bins include the `1.5 MHz` carrier region.
- However, the Ramsey contrast is small relative to point-wise scatter and to the project expectation. The carrier is a weak component (`0.705 kcps` raw amplitude, below the `0.85 kcps` median per-point SEM; ratio amplitude only `0.0157`), and the strongest empirical screen is not at the programmed carrier or the expected 13C sidebands.
- The sideband evidence does not match a nearby-13C Ramsey model: the low sideband is nearly absent, the high sideband is weak, and per-average frequency/phase behavior is mixed.
- Best current interpretation: this is another analyzable but non-claim-grade Ramsey dataset on accepted r03. It provides useful evidence against a simple fixed `1.192 MHz` artifact explanation, but it still does not establish a clean carrier/decay envelope or sideband pattern.

## Claims not yet supported

- No numeric `T2*` is supported from this run. A fit would be descriptive only because raw/readout-aware signal presence and decay shape are not clean enough.
- No nearby `13C` claim is supported. The expected `1.115/1.885 MHz` sidebands are not consistent or strong enough.
- Do not claim sub-grid microwave resonance precision beyond the preceding pODMR refresh basis (`3.8765 GHz`, several-100-kHz uncertainty).
- Do not claim the off-model `~2.27 MHz` screen top is physical; it is an empirical feature requiring a targeted diagnostic if it matters.

## Recommended next action

Do not run another blind long-span Ramsey repeat on r03 under the same basic conditions. Treat the Ramsey/T2star/13C branch as non-claim-grade under current Ramsey conditions and either close that conclusion explicitly, or switch to a deliberately different diagnostic/protocol after fresh tracking and frequency calibration. If continuing toward a 13C conclusion, the next experiment should be an alternate, model-specific sequence rather than more Ramsey averaging.
