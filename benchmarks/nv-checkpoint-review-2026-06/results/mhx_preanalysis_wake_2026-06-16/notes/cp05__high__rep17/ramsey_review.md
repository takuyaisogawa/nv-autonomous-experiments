# Ramsey Review

## Files/Data Used

- Project context: `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New Ramsey terminal data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` submit spec, `measurement/m003.json` terminal result, `measurement/m004.json` status, `measurement/m005.json` control.
- Relevant prior/design context: `evidence/e014.json` refreshed-center Ramsey model/advisory; `evidence/e015.json` advisory/validation output; earlier `evidence/` files for the pODMR refresh and job-start context.
- Generated local artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_diagnostic.png`.

## Calculations/Scripts Run

- Ran `python analyze_ramsey.py` after setting Matplotlib to the noninteractive `Agg` backend. The first run reached numeric output but failed while creating a plot because Tk was unavailable; the final rerun completed and wrote `ramsey_analysis_summary.json` and `ramsey_diagnostic.png`.
- Verified the raw export axis contract: `ExperimentDataEachAvg` averaged over the average axis reproduces `ExperimentData` with max absolute difference `1.42e-14`, consistent with `[scan, avg, readout, point]`.
- Confirmed measurement parameters from terminal metadata: completed job `nv23_ramsey_20260514_055148_auto_ramsey`, final counts `43.433 kcps`, `tau = 0.048..8.048 us`, 41 points, 20 averages x 50000 reps, snake scan order.
- Treated readout 1 as reference and readout 2 as Ramsey signal per the provided protocol context. Median signal/reference were `44.804/48.881 kcps`; median signal SEM across averages was `0.850 kcps`; median ratio SEM was `0.0116`.
- Least-squares sinusoid screens used constant + linear baseline plus sine/cosine terms. Targets were the programmed carrier `1.5 MHz`, expected 13C sidebands `1.115/1.885 MHz`, old short-tau control `1.192 MHz`, and prior det-shift top `1.623 MHz`.
- Full-span target amplitudes:
  - Raw signal carrier: `0.705 kcps`, only `0.83x` median signal SEM.
  - Ratio carrier: `0.01575`, about `1.36x` median ratio SEM.
  - Raw sidebands: `0.145 kcps` at `1.115 MHz`, `0.261 kcps` at `1.885 MHz`.
  - Ratio sidebands: `0.00278` at `1.115 MHz`, `0.00962` at `1.885 MHz`.
- Exploratory full-span screens found the strongest component near `2.27 MHz` in raw, point-wise ratio, and signal-over-reference-line views, not at the planned carrier or 13C sidebands.
- Skip-first-four-points check did not rescue the interpretation: ratio carrier fell to `0.01231`; sidebands were `0.00067` and `0.00527`; the top normalized screen remained near `2.266 MHz`.
- Per-average ratio screens were scattered: top frequencies included `0.125`, `0.430`, `0.545`, `0.700`, `0.855`, `0.990`, `1.535`, `1.575`, `1.680`, `1.895`, `1.930`, `2.055`, `2.115`, `2.140`, `2.250`, `2.260`, and `2.340 MHz`. This is not a stable carrier/sideband pattern.
- Simple scan-order/common-mode drift check: signal-average means spanned `37.38..50.37 kcps`, reference-average means spanned `41.74..54.90 kcps`, with strong reference-signal common-mode correlation `0.970`. Max robust mean z score was `2.28`, so this is provenance rather than a hard anomaly in this local check.

## Plausible Interpretation

- The job completed safely and produced analyzable raw Ramsey data with no stop request or terminal bridge error.
- The refreshed-center Ramsey did not produce a clean, dominant programmed carrier at `1.5 MHz`. The carrier-like fitted component is small compared with per-point uncertainty in raw kcps and only modest in normalized units.
- The expected 13C sideband pair at about `1.115/1.885 MHz` is not coherently supported: the lower sideband is especially weak, the upper sideband is not dominant, and per-average screens do not repeat a carrier-plus-sidebands structure.
- The persistent strongest full/skip spectral screen near `2.27 MHz` may reflect residual apparatus/analysis/baseline structure, alias-sensitive spectral leakage, or a real but currently unassigned oscillatory component. It is not enough by itself to assign a T2star or 13C coupling because it does not match the programmed detuning or expected sideband model and is not per-average stable.
- The strong common-mode reference/signal average-to-average variation suggests normalization is useful as provenance, but it also reinforces the need not to promote weak normalization-only spectral features.

## Claims Not Yet Supported

- No supported numeric T2star from this Ramsey run. A decay fit would be descriptive only because raw/readout-aware carrier signal presence is not established.
- No supported nearby 13C conclusion from this run. The expected sidebands are not consistently present or dominant.
- No supported claim that the `2.27 MHz` component is physical. It is an empirical feature requiring a targeted control or alternate protocol before interpretation.
- No supported claim that simply accumulating more identical long-span Ramsey averages will solve the issue; this was already a higher-shot refreshed-center test and remains non-claim-grade.

## Recommended Next Action

Do not run another blind long-span Ramsey repeat on r03. The project now has several analyzable but non-claim-grade Ramsey datasets, including this refreshed-center high-shot run. The next action should be to switch protocol/diagnostic: either run an alternate coherence baseline such as Hahn echo/CPMG N=1 to establish whether a coherent electron-spin signal is recoverable under current conditions, or perform a targeted Ramsey control specifically designed around the empirical `~2.27 MHz` feature before any physical assignment. Keep the final r03 T2star/13C status as unsupported under current Ramsey evidence until such a control or alternate protocol changes the signal-presence picture.
