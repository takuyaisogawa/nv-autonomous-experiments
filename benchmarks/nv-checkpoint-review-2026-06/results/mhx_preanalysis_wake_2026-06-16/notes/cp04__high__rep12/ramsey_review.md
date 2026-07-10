# Ramsey Review: r03 det-shift short-tau run

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`.
- New completed Ramsey measurement:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
  - `measurement/m002.json`: submitted job spec, `mw_freq = 3.8759 GHz`, `det = 1.5 MHz`, `tau = 48 ns..1.968 us`, 41 points, `12 x 90000`.
  - `measurement/m003.json`: terminal bridge result, completed `2026-05-14T04:15:00`, final counts `44.796 kcps`.
  - `measurement/m004.json`, `measurement/m005.json`: terminal status/control, `stop_requested = false`.
- Prior comparison data:
  - `evidence/e006.json`: terminal det=1.0 MHz short-tau Ramsey raw export.
  - `evidence/e008.json`: terminal det=1.0 MHz short-tau review, prior ratio-screen top near `1.192 MHz`.

## Calculations/scripts run

- Created and ran `analyze_ramsey_detshift.py`.
- Outputs:
  - `ramsey_detshift_analysis.json`
  - `ramsey_detshift_review.png`
- Checks performed:
  - Parsed readouts as reference then Ramsey signal from `ramsey.xml`/`full_experiment=0` sequence structure.
  - Computed raw Ramsey signal, point-wise signal/reference ratio, and signal normalized by a fitted reference line.
  - Estimated per-point SEM across 12 stored averages.
  - Ran a scan-order-aware common-mode drift check using snake acquisition order; no averages flagged.
  - Ran linear-baseline plus sinusoid least-squares screens from `0.3..3.0 MHz`.
  - Checked target frequencies: programmed `1.5 MHz`, prior component `1.192 MHz`, det-tracking prediction `1.692 MHz`, shifted 13C sidebands `1.307/2.077 MHz`, and programmed-det sidebands `1.115/1.885 MHz`.
  - Ran FFT residual checks; bin spacing is coarse at `0.508 MHz`, so FFT is only a visual sanity check.

## Quantitative results

- Acquisition quality:
  - `12 x 90000 = 1.08e6` shots per tau point.
  - Raw reference mean `48.08 kcps`; raw Ramsey-signal mean `44.27 kcps`.
  - Median raw-signal SEM `0.711 kcps`; median ratio SEM `0.0126`.
  - Early `tau <= 0.75 us` transient remains large: signal peak-to-peak `6.46 kcps`, ratio peak-to-peak `0.134`.
  - Drift check flagged `[]`.
- Frequency screens:
  - Ratio view top LS component: `1.623 MHz`, ratio amplitude `0.02547`, baseline-residual R2 improvement `0.430`.
  - Det-tracking prediction `1.692 MHz`: ratio amplitude `0.02505`, R2 improvement `0.411`; raw-signal amplitude `1.225 kcps`, R2 improvement `0.427`.
  - Programmed carrier `1.5 MHz`: ratio amplitude `0.02399`, R2 improvement `0.359`; raw-signal amplitude `1.128 kcps`, R2 improvement `0.345`.
  - Prior empirical `1.192 MHz`: weak in this run, ratio amplitude `0.00511`, R2 improvement `0.017`.
  - Raw signal and reference-line-normalized signal instead peak near `0.882 MHz` with raw amplitude `1.533 kcps` and sig/refline amplitude `0.03193`.
  - Per-average ratio-screen top frequencies are inconsistent: `1.938, 1.543, 0.870, 0.886, 1.751, 0.792, 0.897, 1.201, 0.799, 1.662, 0.300, 1.712 MHz`.
- 13C sideband checks:
  - Shifted sidebands around `1.692 MHz`: `1.307 MHz` ratio amplitude `0.00953`, R2 `0.056`; `2.077 MHz` ratio amplitude `0.00614`, R2 `0.023`.
  - Programmed-det sidebands around `1.5 MHz`: `1.115 MHz` ratio amplitude `0.01076`, R2 `0.077`; `1.885 MHz` ratio amplitude `0.01732`, R2 `0.184`.
  - None are dominant or cross-view consistent.

## Plausible interpretation

The run is terminal and analyzable, with no hard execution anomaly and no drift-flagged averages. The ratio view moved upward from the prior det=1.0 MHz short-tau result: the previous `1.192 MHz` feature is weak here, and the ratio screen now peaks broadly near `1.623 MHz`, with the `1.692 MHz` det-tracking prediction only slightly weaker. That is qualitatively in the det-shift direction.

However, this is not claim-grade Ramsey evidence. The raw signal and reference-line-normalized views prefer `~0.882 MHz`, not the ratio top. The short tau span gives only `~0.52 MHz` nominal frequency resolution, making `1.5`, `1.623`, and `1.692 MHz` hard to separate cleanly. Stored-average frequency screens are not consistent. The large early-time transient remains comparable to or larger than the fitted components.

Best current interpretation: r03 remains an accepted aligned NV, but the Ramsey route has not yet produced a robust carrier/decay model. The det-shift result weakens the fixed `1.192 MHz` artifact hypothesis, but it does not establish a clean det-following Ramsey carrier or 13C sideband structure.

## Claims not yet supported

- Do not claim a numeric `T2star` from this run.
- Do not claim nearby `13C` coupling from this run.
- Do not claim that the programmed `1.5 MHz` carrier is cleanly resolved.
- Do not claim that the `1.692 MHz` det-tracking hypothesis is established; it is only partially suggested in the ratio view.
- Do not treat normalization-only structure as signal presence without raw/readout-aware agreement.

## Recommended next action

Do not run another blind Ramsey repeat on r03. Do a short bridge-free branch synthesis across all four r03 Ramsey datasets, then either close the Ramsey/T2star/13C branch as unsupported under the current Ramsey protocol or design an alternate targeted protocol with a clearer success criterion. If continuing experimentally, the next protocol should be chosen to avoid the current ambiguity between early-time transient, normalization behavior, and true Ramsey carrier response.
