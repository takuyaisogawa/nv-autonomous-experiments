# Ramsey det-shift review

## Files/data used

- Project context: `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New measurement files:
  - `measurement/m001.json`: terminal savedexperiment raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
  - `measurement/m002.json`: submitted job spec.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json`: terminal status.
  - `measurement/m005.json`: control state.
- Generated local analysis artifacts: `analyze_ramsey.py`, `ramsey_analysis.json`, `ramsey_detshift_review.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Verified raw-export axis contract: `ExperimentDataEachAvg` is `[scan, avg, readout, point]`; averaging the per-average readout axis reproduces `ExperimentData`.
- Used readout 1 as reference and readout 2 as Ramsey signal, consistent with the project context for `ramsey.xml` / `full_experiment=0`.
- Checked terminal metadata:
  - completed `true`
  - final counts `44.796 kcps`
  - `12` averages x `90000` repetitions = `1.08e6` shots per tau point
  - tau `0.048..1.968 us`, `41` points, `48 ns` step
  - `mw_freq = 3.8759 GHz`, `det = 1.5 MHz`
  - stop requested `false`, monitor last error empty
- Quantitative screens:
  - FFT bin spacing about `0.508 MHz`; Nyquist about `10.417 MHz`.
  - Median per-point SEM across stored averages: signal `0.711 kcps`, ratio `0.0126`.
  - Full signal peak-to-peak, dominated by early tau, is `6.46 kcps`; full ratio peak-to-peak is `0.134`.
  - Least-squares fixed-frequency screens used a linear baseline plus sine/cosine quadratures.
  - Target checks in the ratio view:
    - prior fixed component `1.192 MHz`: amplitude `0.00511`, raw-signal amplitude `0.474 kcps`
    - programmed carrier `1.500 MHz`: amplitude `0.02399`, raw-signal amplitude `1.128 kcps`
    - prior feature if det-tracking `1.692 MHz`: amplitude `0.02505`, raw-signal amplitude `1.225 kcps`
    - expected 13C sidebands `1.115/1.885 MHz`: ratio amplitudes `0.01076/0.01732`
  - All-tau ratio LS screen peaks near `1.623 MHz` with amplitude `0.02547`.
  - Repeating the ratio LS screen after dropping `tau <= 0.2 us` moves the top component to about `0.746 MHz`.
  - Per-average top frequencies are inconsistent: examples include `1.938`, `1.543`, `0.870`, `0.886`, `1.751`, `0.792`, `0.897`, `1.201`, `0.799`, `1.662`, `0.250`, and `1.712 MHz`.
  - Descriptive damped-grid fits were run only as diagnostics. Ratio view preferred about `0.684 MHz`, `T2* ~0.482 us`; raw-signal view preferred about `0.818 MHz`, `T2* ~0.721 us`. These disagree with the all-tau LS top and are not promoted.

## Plausible interpretation

The det-shift diagnostic is terminal and analyzable. Compared with the previous short-tau det=1.0 MHz run whose empirical component was near `1.192 MHz`, the new all-tau screen has moved upward to `~1.62 MHz`, and the programmed-carrier/det-tracking target amplitudes are larger than the old fixed `1.192 MHz` component. That is suggestive that at least part of the short-tau structure is sensitive to the programmed detuning.

However, the evidence is not claim-grade. The dominant component depends strongly on early tau points: skipping `tau <= 0.2 us` moves the top screen to `~0.746 MHz`. Stored averages do not agree on a common frequency, and the descriptive damped fits choose still different frequencies. The data look like an early-time transient plus baseline/readout effects with possible weak det-sensitive Ramsey content, not a clean carrier-plus-sideband model.

## Claims that are not yet supported

- No well-supported numeric `T2*` is established from this run.
- No well-supported nearby `13C` conclusion is established.
- The `~1.62 MHz` all-tau component should not be claimed as a physical Ramsey carrier.
- The `1.115/1.885 MHz` target sidebands should not be claimed as resolved 13C sidebands.
- The descriptive `T2* ~0.5..0.7 us` fits should not be used downstream as physical parameters.

## Recommended next action

Stop doing blind Ramsey repeats on this r03 branch. Do a bridge-free synthesis across all r03 Ramsey datasets, then choose one of two paths:

1. If the project still needs an active T2*/13C attempt on this same NV, switch to a targeted alternate protocol or calibration that suppresses/identifies the short-tau transient before fitting T2*.
2. If the objective allows branch closeout, record r03 as an aligned NV with Ramsey/T2*/13C unsupported under the tested conditions, and move to a supported negative/unsupported conclusion or a new candidate/protocol decision.
