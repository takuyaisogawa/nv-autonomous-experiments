# Ramsey Review

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`.
- New det-shift Ramsey data: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` status, `measurement/m005.json` control.
- Prior comparison data: `evidence/e006.json` previous det=1.0 MHz short-tau raw export, `evidence/e008.json` previous terminal review, `evidence/e019.json` det-shift model/plan.
- Generated local artifacts: `analyze_ramsey.py`, `ramsey_analysis_output.json`, `ramsey_analysis.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey.py`.
- Verified `ExperimentDataEachAvg` axis contract by averaging stored averages back to `ExperimentData` for both current and prior raw exports.
- Used readout1 as reference and readout2 as Ramsey signal, following the project protocol basis for `ramsey.xml` with `full_experiment=0`.
- Checked scan-order drift from `ScanOrderEachAvg` in acquisition order. No averages flagged; max common-mode drop score was `0.0397`, below the `0.15` threshold.
- Current run completed cleanly: `12 x 90000` repetitions, `1.08e6` shots/tau point, tau `0.048..1.968 us` in 41 points, final counts `44.796 kcps`, stop request false, monitor error empty.
- Current median SEM: signal `0.711 kcps`, ratio `0.0126`. Early `0.75 us` peak-to-peak: signal `6.46 kcps`, ratio `0.134`.
- Least-squares frequency screen:
  - Prior det=1.0 MHz top ratio component recomputed at `1.192 MHz`.
  - Current det=1.5 MHz top point-wise-ratio component is `1.623 MHz`, amplitude `0.02547`.
  - Expected det-tracking target from prior top is `1.692 MHz`; current top is `0.069 MHz` away, within the short-window FFT bin spacing of `0.508 MHz`.
  - Fixed prior-artifact control at `1.192 MHz` is weak in the current ratio view: amplitude `0.00511`, about `0.40x` median ratio SEM.
  - Programmed carrier `1.5 MHz` and det-tracking target `1.692 MHz` are similar in ratio amplitude: `0.02399` and `0.02505`, about `1.9..2.0x` median ratio SEM.
- Raw/readout-aware conflict:
  - Raw signal top component is near `0.882 MHz`, amplitude `1.533 kcps`.
  - Signal divided by fitted reference line is also dominated near `0.882 MHz`.
  - Per-average ratio top frequencies are scattered (`0.25..1.94 MHz`), not a stable repeat-by-repeat carrier.
- Expected 13C sideband checks are not dominant:
  - Programmed sidebands: `1.115 MHz` amp `0.01076`, `1.885 MHz` amp `0.01732`.
  - Det-tracking sidebands: `1.307 MHz` amp `0.00953`, `2.077 MHz` amp `0.00614`.

## Plausible interpretation

The det-shift run is analyzable and useful. The point-wise ratio component moved upward from the prior `1.192 MHz` toward the expected det-tracking region (`1.623 MHz` observed versus `1.692 MHz` predicted), and the fixed `1.192 MHz` component largely disappeared. That argues against a simple fixed-frequency artifact explanation.

However, the raw signal and fitted-reference-line-normalized signal are dominated by a different component near `0.882 MHz`, and the stored-average screens are inconsistent. Because the project rules treat raw/readout-aware evidence as primary and point-wise normalization as secondary, this is only a ratio-view det-shift hint, not a claim-grade Ramsey carrier.

## Claims not yet supported

- No numeric `T2*` is supported from this Ramsey set.
- No nearby `13C` coupling conclusion is supported.
- The `1.623 MHz` ratio feature is not yet established as the physical Ramsey carrier.
- The `0.882 MHz` raw-signal feature is not yet assigned to a physical source.
- The current data do not support closing the whole objective with a positive T2*/13C result; they only support that repeated short-tau Ramsey under this route remains model-ambiguous.

## Recommended next action

Stop blind Ramsey repeats on r03 under the same route. Do a bridge-free synthesis of all r03 Ramsey datasets, then choose an alternate/control protocol that can separate readout/protocol transients from spin dephasing, such as a Hahn-echo/CPMG baseline or a Ramsey systematic control with phase/sign/readout checks. Fit or claim `T2*` only after raw/readout-aware evidence supports a physical carrier and decay model.
