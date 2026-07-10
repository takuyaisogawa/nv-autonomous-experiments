# Ramsey Review

## Files/data used

- `project/state.md`, `project/brief.md`, `project/advice.md`: current project context and prior Ramsey/pODMR conclusions.
- `md/memory.md`, `md/knowledge.md`: local project rules for raw/readout-aware NV/Ramsey interpretation.
- `measurement/m001.json`: terminal raw export for `1DExp-seq-ramsey-vary-tau-2026-05-13-230350`.
- `measurement/m002.json`, `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: job spec, terminal result/status/control for `nv23_ramsey_20260513_230331_auto_ramsey`.
- Prior local evidence summaries in `evidence/`, especially the earlier det=1.0 MHz 8 us Ramsey terminal review and project state.
- Generated local scratch outputs: `ramsey_analysis_summary.json` and `ramsey_shorttau_review.png`.

## Calculations or scripts run

- Inspected the measurement JSON structure with Python and confirmed combined readouts plus `ExperimentDataEachAvg`.
- Corrected `ExperimentDataEachAvg` interpretation to shape `[average, readout, tau_point]`; readout 1 is the mS=0 reference and readout 2 is Ramsey signal under `full_experiment=0`.
- Ran Python least-squares sinusoid screens using intercept + linear trend + sine/cosine terms at:
  - programmed carrier: 1.000 MHz
  - nominal 13C sidebands from prior plan: 0.615 MHz and 1.385 MHz
  - prior non-claim feature: 0.884 MHz
- Ran a frequency scan from 0.25 to 2.5 MHz, per-average frequency screens, split-half 1 MHz checks, per-point SEM from the 12 averages, and average-mean drift checks.
- Saved corrected numeric summary to `ramsey_analysis_summary.json`; saved a raw/readout and frequency-screen plot to `ramsey_shorttau_review.png`.

Key numbers:

- Run completed cleanly: 41 tau points from 0.048 to 1.968 us, 12 averages x 90000 repetitions, final counts 35.122 kcps.
- Combined raw signal range: 6.50 kcps; combined reference range: 2.18 kcps.
- Median signal SEM across averages: 1.14 kcps; median reference SEM: 1.12 kcps.
- LS amplitude at 1.000 MHz: 1.28 kcps raw signal, normalized amplitude 0.0264; this is only about 1.1x the median signal SEM.
- LS amplitudes at 0.615/1.385 MHz: 1.10/1.22 kcps raw signal, also near the SEM scale.
- LS amplitude at prior 0.884 MHz feature: 0.58 kcps, weaker than the carrier and sideband checks.
- Frequency screen is dominated by the low-frequency edge near 0.25 MHz, consistent with residual slow baseline/early-time shape rather than a clean programmed Ramsey carrier.
- Per-average signal means range from 37.47 to 51.21 kcps, about 30.8% of the median; reference means range about 26.8%. The late averages are substantially dimmer, so common-mode drift/tracking changes remain important provenance.
- A descriptive fixed-1 MHz damped-cosine fit can produce `T2* ~0.38 us` with amplitude `~5.1 kcps`, but this is not promoted because the carrier amplitude from linear LS is SEM-scale and the run has strong per-average baseline variation.

## Plausible interpretation

The short-tau/high-SNR run did improve the nominal per-point precision and contains analyzable early-time structure, but it still does not cleanly recover a robust programmed 1.0 MHz Ramsey carrier or the expected 13C sideband pattern. The strongest quantitative feature is slow/edge-of-window structure and average-to-average baseline motion, not a stable carrier-following oscillation. The prior 0.884 MHz exploratory feature is not strengthened by this run.

This supports the existing project caution: r03 remains a valid aligned NV candidate from pODMR, but Ramsey/T2* and nearby-13C conclusions are still not claim-grade under the current protocol. Very short dephasing is possible, but the present data do not isolate it from baseline/drift and readout-shape effects well enough to report a numeric T2*.

## Claims not yet supported

- No supported numeric T2* value from this dataset.
- No supported nearby 13C claim from the 0.615/1.385 MHz sideband checks.
- No supported claim that the 0.884 MHz feature seen in an earlier scout is physical.
- No supported claim that simply increasing Ramsey averages or repeating the same det=1.0 MHz Ramsey will resolve the branch.
- No sub-grid refinement of the pODMR center beyond the prior grid-supported `mw_freq_hz = 3.8759e9`.

## Recommended next action

Do not run another blind Ramsey repeat on r03. Close the current Ramsey/T2*/13C claim as unsupported under this protocol, or switch to a different diagnostic that directly tests the failure mode before further long acquisitions. The most defensible next experimental action is a calibration/control step rather than another Ramsey accumulation: re-check the r03 resonance/Rabi pulse calibration and then, if still pursuing coherence, use an alternate protocol or phase-control diagnostic designed to separate carrier visibility from baseline drift and readout-shape artifacts.
