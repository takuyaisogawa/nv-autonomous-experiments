# Ramsey Review

## Files/data used

- `project/brief.md`, `project/state.md`, `project/advice.md`: project objective, accepted r03 context, prior Ramsey/pODMR conclusions, and requested evidence boundaries.
- `md/memory.md`, `md/knowledge.md`: local NV analysis policy, especially raw/readout-aware review and fit-after-signal-presence guidance.
- `context.json`: checkpoint context and recent evidence summary.
- `measurement/m001.json`: terminal savedexperiment raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- `measurement/m002.json`: submitted Ramsey job spec.
- `measurement/m003.json`: terminal bridge result.
- `measurement/m004.json`, `measurement/m005.json`: final status/control provenance.

## Calculations or scripts run

- Parsed `measurement/m001.json` with local Python/numpy.
- Verified `ExperimentDataEachAvg` axis contract by checking that averaging the 20 stored averages reconstructs `ExperimentData`: `true`.
- Confirmed terminal settings from metadata/result: `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`, `tau = 0.048..8.048 us` in 41 points (`0.2 us` step), `20 x 50000` shots, final counts `43.433 kcps`.
- Computed raw readout curves, point-wise `signal/reference`, and signal normalized by a linear fitted reference.
- Computed per-point SEM across 20 stored averages.
- Ran least-squares sinusoid screens with intercept plus linear baseline from `0.25..2.45 MHz` for raw signal, point-wise ratio, and fitted-reference ratio.
- Checked target amplitudes at carrier `1.5 MHz`, expected 13C sidebands `1.115/1.885 MHz`, old `1.192 MHz` control, and prior det-shift top `1.623 MHz`.
- Ran a windowed FFT check after linear detrending.
- Ran rough average-to-average drift checks from stored-average means.
- Wrote scratch outputs `ramsey_analysis_summary.json` and `ramsey_review_plot.png`.

## Plausible interpretation

- The run completed cleanly and is analyzable: bridge status is completed, no stop was requested, saved data exist, final counts are healthy, and the stored-average axis contract is internally consistent.
- Raw signal peak-to-peak is `6.27 kcps`, but the median signal SEM is `0.85 kcps`; the relevant sinusoidal target amplitudes are much smaller than the full apparent point-to-point range.
- The strongest combined LS screen is near `2.27 MHz` in all three views: raw signal amplitude `0.818 kcps`, point-wise ratio amplitude `0.01845`, fitted-reference ratio amplitude `0.01677`.
- The programmed `1.5 MHz` carrier is present only weakly/moderately: raw amplitude `0.705 kcps`, point-wise ratio amplitude `0.01575`, fitted-reference ratio amplitude `0.01447`. It is not the top component and is near the measured SEM scale.
- Expected 13C sidebands are not supported: low sideband `1.115 MHz` is weak (`0.145 kcps` raw, `0.00278` point ratio), and high sideband `1.885 MHz` is also not dominant (`0.261 kcps` raw, `0.00962` point ratio).
- FFT peaks include bins near the carrier region (`1.463/1.585 MHz`) and near `2.317 MHz`, consistent with broad exploratory power but not a clean carrier/sideband model.
- Per-average screens remain mixed. For raw signal, only 3/20 averages have top frequency within `0.15 MHz` of `1.5 MHz`, 7/20 near `2.27 MHz`, 2/20 near each expected sideband region. Point-wise ratio gives 5/20 near `1.5 MHz`, 4/20 near `2.27 MHz`, and weak sideband consistency.
- Rough average-mean drift is not a hard anomaly: first five signal-average means `46.27 kcps`, last five `44.77 kcps` (`-3.2%`), with no rough MAD-flagged averages. Average-to-average common-mode scatter is still substantial.
- Descriptive damped fits are not claim-grade. A free raw-top fit lands near `2.282 MHz`, `T2star ~1.80 us`, `R2 ~0.65`; a carrier-initialized fit moves to `1.77 MHz`, `T2star ~0.22 us`, `R2 ~0.56`. These fits are useful diagnostics only because signal presence at a stable physical carrier/sideband model is not established.

## Claims that are not yet supported

- Do not claim a numerical `T2star` from this Ramsey run.
- Do not claim a nearby 13C coupling or sideband splitting from this run.
- Do not claim that the strongest `~2.27 MHz` component is a physical Ramsey carrier or nuclear-spin feature; it is an empirical spectral component without sufficient per-average or model consistency.
- Do not promote the old `~1.192 MHz` feature; it remains weak here (`0.110 kcps` raw, `0.00194` point ratio).
- Do not treat the refreshed pODMR center as invalidated by this Ramsey alone; the Ramsey data show weak/mixed coherent contrast, not a clean spectroscopy contradiction.

## Recommended next action

This 1.0e6-shot refreshed-center long-span Ramsey still does not support a stable carrier/sideband model. Avoid another blind long-span Ramsey repeat on r03. The next action should be to switch strategy: either run an alternate coherence protocol that first establishes robust coherent contrast under current conditions (for example a Hahn/CPMG-N=1 style baseline before any 13C-sensitive dynamical-decoupling scan), or close the r03 Ramsey branch with the supported conclusion that T2star and nearby-13C claims are unsupported under the tested Ramsey conditions.
