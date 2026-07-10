# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`.
- New terminal measurement: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` result, `measurement/m004.json` status, `measurement/m005.json` control.
- Prior/project comparison context: `evidence/e008.json` terminal det=1.0 MHz short-tau Ramsey review, `evidence/e019.json` det-shift model plan, `evidence/e021.json` verified det-shift intent.
- Scratch outputs created here: `ramsey_analysis.py`, `ramsey_analysis_summary.json`, `ramsey_review_plot.png`.

## Calculations/scripts run

- Ran `python ramsey_analysis.py`.
- Parsed raw readouts as readout1 reference and readout2 Ramsey signal per project protocol context. Verified `ExperimentDataEachAvg` averages back to `ExperimentData`.
- Rebuilt tau grid: 0.048 to 1.968 us, 41 points, 48 ns step; 12 averages x 90000 reps = 1.08e6 shots per tau.
- Ran scan-order-aware drift check using `ScanOrderEachAvg` snake order. No averages flagged; max common-mode drop was 3.97%, max worst-trace drop was 5.35%, below the 15% screen threshold.
- Ran linear-detrended least-squares frequency screens from 0.25 to 2.4 MHz, target checks, nearest-bin FFT checks, per-average screens, and diagnostic damped-sinusoid grid fits.

## Plausible interpretation

- The run completed cleanly: status completed, finished 2026-05-14T04:15:00, final counts 44.796 kcps, safe shutdown true, monitor error empty, stop requested false.
- The old fixed-frequency 1.192 MHz control is not dominant in this det=1.5 MHz run: ratio LS amplitude 0.00511, only 0.40x the median ratio SEM.
- The all-tau ratio screen has its top near 1.623 MHz with ratio amplitude 0.02547 and R2 improvement 0.430. This is broadly in the programmed/det-shifted band: programmed 1.5 MHz amplitude 0.02399, and prior-top det-tracking prediction 1.692 MHz amplitude 0.02505.
- This is weakly consistent with a det-shifted Ramsey-like component, but not claim-grade. The component is smaller than the prior det=1.0 MHz top amplitude 0.03631, the short 1.92 us window cannot cleanly distinguish 1.5 from 1.692 MHz, and the nearest FFT bin spacing is about 0.508 MHz.
- Early-time sensitivity remains a problem. Removing tau <= 0.2 us moves the top ratio screen to about 0.746 MHz, away from the carrier band. Per-average top frequencies scatter broadly, so the combined feature is not stable enough to promote.

## Claims not yet supported

- A numeric T2star value is not supported. The diagnostic damped fits prefer low-frequency/short-decay shapes, likely dominated by the early-time transient, and should not be promoted.
- Nearby 13C coupling is not supported. Programmed 13C sideband amplitudes are weak/non-dominant: 1.115 MHz amplitude 0.01076 and 1.885 MHz amplitude 0.01732; det-tracking sideband candidates are also weak.
- Exact carrier assignment is not supported: the data do not distinguish programmed 1.5 MHz from the 1.692 MHz det-tracking prediction with enough confidence.
- A clean physical Ramsey model is not supported yet, even though the fixed 1.192 MHz artifact/control hypothesis is weakened for this run.

## Recommended next action

Stop blind Ramsey repeats on r03. Do a branch decision: either switch to an alternate coherence/spectroscopy protocol or explicit artifact-control protocol that addresses the short-tau transient/low-contrast ambiguity, or close the r03 Ramsey/T2star/13C branch as unsupported under current conditions.
