# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New completed Ramsey: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` status, `measurement/m005.json` control.
- Comparison/control: prior short-tau det=1.0 MHz raw/review context from `evidence/e006.json`, `evidence/e008.json`, `evidence/e010.json`, and `evidence/e011.json`; det-shift model/intent from `evidence/e019.json` and `evidence/e021.json`.

## Calculations or scripts run

- Created and ran `ramsey_analysis.py`.
- Outputs: `ramsey_analysis_results.json` and `ramsey_detshift_review.png`.
- Checks performed:
  - Verified raw axis contract: averaging `ExperimentDataEachAvg` over the average axis reconstructs `ExperimentData` with max absolute difference `1.4e-14` for both prior and new runs.
  - Used readout 1 as reference and readout 2 as Ramsey signal per project context/metadata; inspected raw signal, pointwise signal/reference ratio, and signal divided by a fitted reference line.
  - Computed per-point SEM from 12 stored averages, linear-baseline residual peak-to-peak values, FFT bin checks, and linear-baseline least-squares sinusoid screens from 0.25 to 2.5 MHz.
  - Compared target frequencies: programmed carrier `1.5 MHz`, programmed 13C sidebands `1.115/1.885 MHz`, det-tracking carrier prediction `1.692 MHz`, det-tracking 13C sidebands `1.307/2.077 MHz`, and fixed artifact-control `1.192 MHz`.

## Plausible interpretation

- The new run completed cleanly enough to analyze: `auto__ramsey`, `tau = 0.048..1.968 us` in 41 points, 12 averages x 90000 repetitions (`1.08e6` shots/tau), final counts `44.796 kcps`, stop not requested, safe shutdown OK.
- The prior det=1.0 MHz short-tau run had its strongest combined ratio component at `1.192 MHz` with ratio amplitude `0.0363` and raw-signal amplitude `1.68 kcps`.
- In the new det=1.5 MHz run, the pointwise ratio screen maximum moves upward to about `1.623 MHz` with ratio amplitude `0.0255`, and the target `1.692 MHz` det-tracking carrier is nearly comparable (`0.0250`). The fixed `1.192 MHz` ratio component is weak (`0.0051`), so the old ratio feature did not remain fixed in the same view.
- However, raw/readout-aware evidence is mixed rather than claim-grade. The raw-signal and fitted-reference-line-normalized views prefer about `0.882 MHz`, not the programmed `1.5 MHz` carrier or the `1.692 MHz` det-tracking prediction. The reference readout itself has structure near `0.924 MHz`, so the ratio-only shift is not enough to promote a physical Ramsey carrier.
- The target signal sizes are modest relative to noise: new median SEM is `0.711 kcps` in raw signal and `0.0126` in ratio; the top raw-signal component is `1.53 kcps`, and the top ratio component is `0.0255`. The nominal independent frequency resolution over the short tau span is only about `0.521 MHz` (`0.508 MHz` FFT bin spacing), so kHz-level screen maxima are not precise frequency estimates.

## Claims not yet supported

- No well-supported numeric T2star claim from this Ramsey run or the combined r03 Ramsey branch.
- No supported nearby 13C claim: programmed sidebands and det-tracking sidebands are not dominant or raw/readout-consistent.
- No supported claim that the `1.623/1.692 MHz` ratio feature is a clean physical Ramsey carrier; it is ratio-view evidence only and conflicts with the raw-signal/fitted-reference-line views.
- No supported claim that the old `1.192 MHz` feature was simply a fixed artifact in every view; it is suppressed in the new ratio view, but the raw-signal behavior remains ambiguous.

## Recommended next action

Do not run another blind Ramsey repeat on r03. Treat the r03 aligned-NV spectroscopy as supported, but the Ramsey/T2star/13C branch as still unsupported under current Ramsey conditions. Next, either switch to an alternate protocol that can establish coherence/13C with a more robust readout model, or close this r03 Ramsey branch as non-claim-grade with a supported negative/unsupported conclusion under these conditions.
