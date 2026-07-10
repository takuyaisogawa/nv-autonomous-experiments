# Ramsey Review: det=1.5 MHz short-tau shift check

## Files/data used

- Project context: `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New completed Ramsey data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control.
- Prior comparison data: `evidence/e006.json` prior det=1.0 MHz short-tau terminal raw export, `evidence/e007.json` prior drift review, `evidence/e008.json` prior terminal review, `evidence/e009.py` prior review script pattern, `evidence/e019.json`/`e021.json` det-shift model and verified intent.

## Calculations/scripts run

- Created and ran `analyze_ramsey_detshift.py`.
- Outputs: `ramsey_detshift_analysis.json` and `ramsey_detshift_analysis.png`.
- Checks performed:
  - Verified `ExperimentDataEachAvg` axis contract as `[scan, avg, readout, point]` by reconstructing combined `ExperimentData`.
  - Used readout 1 as reference and readout 2 as Ramsey signal, consistent with the saved `ramsey.xml` path and `full_experiment=0`.
  - Computed raw signal/reference curves, point-wise ratio, signal over fitted reference line, SEM across 12 stored averages, FFT residual bins, least-squares sinusoid screens against a linear baseline, per-average frequency screens, and a local scan-order drift proxy from `ScanOrderEachAvg`.

Key numeric checks:

- Run completed: `auto__ramsey`, `mw_freq=3.8759 GHz`, `det=1.5 MHz`, tau `0.048..1.968 us` in 41 points, `12 x 90000 = 1.08e6` shots/tau, final counts `44.796 kcps`, `stop_requested=false`, monitor error empty.
- Sampling: tau step `48 ns`, Nyquist `10.42 MHz`, FFT bin spacing `0.508 MHz`, nominal `1/span` resolution `0.521 MHz`.
- Median per-point SEM: signal `0.711 kcps`, ratio `0.0126`.
- Drift proxy: no averages flagged.
- All-tau point-wise ratio screen top: `1.623 MHz`, ratio LS amplitude `0.02547`, residual R2 improvement `0.430`.
- Skip-first-point ratio top: `1.650 MHz`; skip `tau <= 0.2 us` ratio top moves to `0.746 MHz`, so the early-time segment remains influential.
- Raw signal screen top: `0.882 MHz`, amplitude `1.533 kcps`; signal/fitted-reference-line top also `0.882 MHz`; raw reference top `0.924 MHz`.
- Target amplitudes in the all-tau ratio fit:
  - prior fixed artifact control `1.192 MHz`: `0.00511` ratio, `0.474 kcps` raw signal.
  - programmed carrier `1.500 MHz`: `0.02399` ratio, `1.128 kcps` raw signal.
  - det-tracking prior top `1.692 MHz`: `0.02505` ratio, `1.225 kcps` raw signal.
  - det-tracking sidebands `1.307/2.077 MHz`: `0.00953/0.00614` ratio.
  - programmed sidebands `1.115/1.885 MHz`: `0.01076/0.01732` ratio.
- Per-average ratio tops are inconsistent: examples include `1.543`, `0.870`, `0.886`, `1.751`, `0.792`, `1.201`, `1.662`, and `1.712 MHz`; one average is dominated by a low-frequency boundary component.

## Plausible interpretation

The run is terminal and analyzable. It gives some evidence against a simple fixed `~1.192 MHz` artifact, because the all-tau ratio amplitude at `1.192 MHz` is small while the all-tau ratio screen is strongest near the programmed/det-shift target region (`1.5..1.7 MHz`).

That is not enough to claim a Ramsey carrier. The strongest frequency depends on the readout view: point-wise ratio prefers `~1.62 MHz`, but raw signal and signal over fitted reference line prefer `~0.882 MHz`, with the reference itself showing `~0.924 MHz` structure. The result is also early-time sensitive, since skipping `tau <= 0.2 us` moves the ratio screen to `~0.746 MHz`. The frequency spacing/resolution means `1.5 MHz` and `1.692 MHz` are not cleanly separable by FFT, and the LS screen should be treated as exploratory.

## Claims not yet supported

- No numeric T2star is supported. A descriptive damped fit can be made, but it follows view-dependent transient structure rather than a supported physical carrier/decay model.
- No nearby `13C` conclusion is supported. Neither the programmed sidebands nor the det-tracking sidebands are dominant and consistent across raw/readout-aware views.
- The project still supports r03 as an aligned NV from pODMR evidence, but the Ramsey branch remains non-claim-grade for T2star/13C under the current analysis.

## Recommended next action

Do not run another blind same-style Ramsey repeat. First do a short branch synthesis across all Ramsey datasets and decide whether to close r03 Ramsey/T2star/13C as unsupported under current conditions or run a targeted control/alternate protocol. If another Ramsey-family control is chosen, the success criterion should be raw-signal or fitted-reference-line carrier tracking across det settings, not point-wise-ratio-only structure.
