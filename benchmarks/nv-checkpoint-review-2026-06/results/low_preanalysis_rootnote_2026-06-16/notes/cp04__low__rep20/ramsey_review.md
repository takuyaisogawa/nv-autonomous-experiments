# Ramsey Review: det=1.5 MHz Short-Tau Shift Check

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New measurement: `measurement/m001.json` raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
- New run metadata: `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control.
- Prior context from project state: accepted r03 at `mw_freq = 3.8759 GHz`; prior short-tau det=1.0 MHz run had strongest empirical ratio component near `1.192 MHz` but no supported T2star/13C claim.
- Local scratch outputs created: `ramsey_review_analysis.json`, `ramsey_review_plot.png`.

## Calculations or scripts run

- Parsed `measurement/m001.json` with Python/NumPy.
- Verified `ExperimentDataEachAvg` axis contract as `[scan, avg, readout, point]` by checking mean per-average reference/signal reproduces `ExperimentData`.
- Confirmed scan/run settings from local files: `tau = 48 ns..1.968 us`, 41 points, `dt = 48 ns`, `det = 1.5 MHz`, `12 averages x 90000 repetitions`, final counts `44.796 kcps`, scan order `snake`, tracking `Per average`.
- Computed raw signal/reference, signal/reference ratio, signal normalized by fitted reference line, per-point SEM, FFT of linear-detrended residuals, least-squares sinusoid screens from `0.25..2.25 MHz`, and targeted least-squares amplitudes at:
  - programmed carrier `1.500 MHz`
  - det-tracking prediction from prior `1.192 -> 1.692 MHz`
  - expected 13C sidebands `1.307 MHz` and `2.076 MHz`
  - prior fixed component `1.192 MHz`
- Simple robust per-average drift sanity found no average-mean outliers in reference, signal, or ratio.

## Plausible interpretation

- The det-shift run is analyzable and not obviously failed. Counts recovered to `44.796 kcps`; no stop was requested; the raw export has 12 stored averages.
- The previous fixed `~1.192 MHz` feature is not reproduced as a dominant ratio feature in this det=1.5 MHz run. Its all-tau ratio LS amplitude is only `0.0051`, with low baseline-residual improvement (`0.017`), much weaker than the 1.5-1.7 MHz content.
- The all-tau ratio LS screen is strongest near `1.623 MHz` with amplitude `0.0255` in ratio and residual improvement `0.430`. The det-tracking target `1.692 MHz` is close but lower (`0.0250`, improvement `0.411`), and the programmed `1.500 MHz` carrier is also visible (`0.0240`, improvement `0.359`).
- FFT of the ratio residual is coarse because the window is only `1.92 us`; the largest ratio FFT bin is `1.524 MHz` with amplitude `0.0246`.
- Raw signal and fitted-reference normalization prefer a different exploratory component near `0.882 MHz`, while ratio prefers `1.623 MHz`. This readout-view disagreement prevents a clean physical Ramsey carrier assignment.
- Per-average ratio frequency screens are inconsistent, with individual averages preferring frequencies from about `0.25` to `1.94 MHz`; this is weak repeatability evidence for any single frequency.
- The 13C sideband targets are not compelling: ratio amplitudes are `0.0095` at `1.307 MHz` and `0.0062` at `2.076 MHz`, both with low residual improvement and much weaker than the main exploratory components.
- Net: the det-shift result argues against simply promoting the old fixed `1.192 MHz` feature, but it still does not establish a clean det-following Ramsey carrier/sideband model.

## Claims that are not yet supported

- Do not claim a numeric T2star from this run. The carrier identity is not secure across raw/readout-aware views, so a decay fit would be descriptive rather than physical.
- Do not claim nearby 13C coupling from the Ramsey FFT/LS screens. The expected sidebands are weak and not dominant.
- Do not claim the dominant component is definitively the programmed `1.5 MHz` carrier or a shifted `1.692 MHz` carrier. The evidence is suggestive but not coherent enough across signal, ratio, reference-line normalization, and per-average screens.
- Do not reopen r01/r02 or weaken the r03 alignment conclusion from this Ramsey result; this run tests r03 Ramsey interpretation, not pODMR alignment.

## Recommended next action

Avoid another blind Ramsey repeat on the same settings. The current branch has now produced several analyzable but non-claim-grade Ramsey datasets. The next scientific action should be a deliberate branch decision: either switch to an alternate protocol better suited to separating true electron coherence from readout/baseline artifacts, such as a Hahn/CPMG-style T2 baseline or another calibrated sequence after protocol inspection, or close the r03 Ramsey/13C branch as unsupported under the current Ramsey conditions while preserving the supported r03 alignment claim.
