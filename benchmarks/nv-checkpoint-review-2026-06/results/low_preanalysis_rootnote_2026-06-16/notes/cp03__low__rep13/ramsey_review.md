# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Prior short-tau design note: `evidence/e017.md`.
- New terminal Ramsey data and bridge metadata:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
  - `measurement/m002.json`: bridge job spec.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json`: terminal bridge status.
  - `measurement/m005.json`: run control.
- Generated local analysis artifacts:
  - `ramsey_analysis_summary.json`
  - `ramsey_m001_review.png`

## Calculations or scripts run

- Ran an inline Python analysis over `measurement/m001.json`.
- Parsed the raw export as `ExperimentData` shape `1 x 2 x 41` and `ExperimentDataEachAvg` shape `1 x 12 x 2 x 41`.
- Used the scan grid from the export: tau `48 ns..1968 ns`, 41 points, 48 ns spacing, 12 averages, 90000 repetitions per average.
- Computed raw reference and signal traces, per-point SEM across stored averages, signal/reference ratio, and signal divided by a linear fitted reference baseline.
- Performed least-squares sine/cosine screens with constant plus linear baseline at:
  - programmed Ramsey carrier: `1.000 MHz`
  - expected nearby 13C sidebands from project model: `0.615 MHz` and `1.385 MHz`
  - exploratory dense frequency grid: `0.2..3.0 MHz`
- Computed simple average-to-average mean readout drift checks using robust z-scores.

Key numeric checks:

- Terminal run completed safely; final bridge count text was `35.122 kcps`, no abort, no stop request.
- Raw signal mean/range: `44.655 kcps`, range `40.698..47.197 kcps` (`6.499 kcps` span).
- Raw reference mean/range: `48.573 kcps`, range `47.568..49.744 kcps` (`2.176 kcps` span).
- Median raw-signal SEM across averages: `1.138 kcps`; max SEM `1.405 kcps`.
- Median ratio SEM: `0.0127`.
- Simple stored-average mean drift check flagged no averages by the robust-z threshold, but average means still show notable common-mode variation: signal averages range roughly `37.47..51.21 kcps`, reference averages `42.02..55.19 kcps`.
- LS amplitudes:
  - `1.000 MHz`: raw signal `1.282 kcps`, ratio `0.0274`.
  - `0.615 MHz`: raw signal `1.103 kcps`, ratio `0.0243`.
  - `1.385 MHz`: raw signal `1.220 kcps`, ratio `0.0271`.
- The largest exploratory combined LS screen landed at the low-frequency search boundary, `0.200 MHz`, with raw amplitude `5.904 kcps` and ratio amplitude `0.1183`. Every per-average ratio screen also preferred the same `0.200 MHz` boundary, indicating a slow envelope/baseline component rather than a resolved Ramsey carrier or sideband.

## Plausible interpretation

The short-tau/high-SNR diagnostic did what it was designed to test: it concentrated shots in the first `~2 us` and avoided tau zero. It shows a real-looking low-frequency/early-time structure in the raw signal and ratio views, larger than the SEM-scale target-frequency components.

However, this structure does not cleanly support the programmed Ramsey phase ramp. The `1.0 MHz` carrier amplitude is only about `1.1x` the median raw-signal SEM and is comparable to the target sideband amplitudes. The strongest screen is pinned to `0.2 MHz`, the lower edge of the exploratory range, and not to `1.0 MHz` or the expected `0.615/1.385 MHz` sidebands. This is more consistent with a slow envelope, baseline evolution, or short-window artifact than with a clean oscillatory Ramsey signal.

Given the two prior non-claim-grade Ramsey datasets and this short-tau result, r03 still has good alignment/pODMR support, but Ramsey on this route has not produced claim-grade T2star or 13C evidence.

## Claims that are not yet supported

- No supported numeric T2star claim from this short-tau run.
- No supported nearby 13C claim from FFT/LS sidebands.
- No supported statement that the `0.2 MHz` boundary feature is a physical coupling or true Ramsey beat.
- No supported claim that the microwave frequency is wrong solely from this Ramsey data; the fine weak-pi pODMR still supports the grid center used for this run.
- No supported claim that more blind Ramsey averaging on the same route will solve the issue.

## Recommended next action

Do not run another blind Ramsey repeat on r03. Treat the r03 Ramsey/T2star/13C branch as unsupported under the current Ramsey route unless an alternate diagnostic is chosen.

The next useful action is to switch protocol or calibration target rather than accumulate more of the same data. Recommended choice: run a short, targeted protocol review and design an alternate coherence diagnostic, preferably Hahn echo/CPMG `N=1` baseline on the same accepted r03 after a fresh track/count check and, if needed, a quick weak-pi pODMR recenter. Use that to separate true dephasing from Ramsey-route/readout/baseline artifacts before attempting any further 13C spectroscopy.
