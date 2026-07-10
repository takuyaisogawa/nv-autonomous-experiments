# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New terminal Ramsey data: `measurement/m001.json` raw export for `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
- New run metadata: `measurement/m002.json` job spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` terminal status, `measurement/m005.json` run control.
- Prior comparison/context: `evidence/e002.json` drift-analysis method, `evidence/e003.json` terminal 8 us det=1.0 MHz Ramsey review, `evidence/e006.json`/`evidence/e009.json` short-tau model and success criteria, `evidence/e017.md` short-tau design/start note.

## Calculations or scripts run

- Added and ran `python analyze_ramsey_shorttau.py`.
- Outputs: `ramsey_shorttau_analysis.json` and `ramsey_shorttau_review.png`.
- Checks performed in the script:
  - Parsed the exported Ramsey scan and confirmed readout roles from `ramsey.xml` with `full_experiment=0`: readout 1 is the true mS=0 reference; readout 2 is the Ramsey signal.
  - Computed raw reference/signal, point-wise signal/reference ratio, and signal normalized to a fitted reference line.
  - Computed per-point SEM across 12 stored averages, average-to-average means, and scan-order-aware drift scores from the saved snake order.
  - Ran linear-baseline-plus-sinusoid least-squares checks at 1.0 MHz, expected 13C sidebands 0.615423 and 1.384577 MHz, prior scout 0.884361 MHz, and prior second-run top 1.178 MHz.
  - Ran FFT checks on linearly detrended traces, broad frequency screens, fixed/free-frequency damped Ramsey fits, per-average carrier screens, and 1000x average-resampling bootstrap screens.

## Plausible interpretation

- The run completed with analyzable data: 48 ns to 1.968 us, 41 points, 12 averages x 90000 repetitions, total 1.08e6 shots per tau point. Terminal final counts were 35.122 kcps, above the 20 kcps gate but lower than earlier r03 counts.
- No scan-order drift flags were found by the local reproduction of the prior drift method. Average means drift across the run, especially lower averages 10-11, but this is provenance rather than a hard anomaly.
- The short-tau data show weak early-time Ramsey-like structure. The programmed 1.0 MHz component is much larger than in the prior 8 us det=1.0 MHz run: ratio LS amplitude 0.0274 and raw-signal amplitude 1.28 kcps here, versus prior 0.00916 ratio and 0.277 kcps.
- The 1.0 MHz component is still not dominant. The strongest combined undamped screen is near 1.192 MHz with ratio amplitude 0.0363 and R2 improvement 0.656. Bootstrap resampling puts the top frequency at 1.18-1.21 MHz (16/50/84 percentiles) and puts 98.3% of top frequencies in 1.12-1.25 MHz, with 0% in 0.95-1.05 MHz.
- FFT resolution is coarse for 13C interpretation in this short window: bin spacing is 0.508 MHz. The largest detrended ratio FFT bins are 0.508 MHz and 1.016 MHz, so FFT alone cannot resolve carrier/sideband structure here.
- Fixed-1.0 MHz damped fits return very short apparent T2star values, about 0.16 us on ratio and 0.18 us on raw signal, but require large first-tau amplitudes and are not unique. Free-frequency damped fits near 1.195-1.200 MHz fit better and return T2star values longer than the short scan window, so the fitted decay is not stable enough to promote.

## Claims that are not yet supported

- No well-supported numeric T2star should be claimed from this run. In particular, the fixed-carrier ~0.16-0.18 us fit is a model-dependent diagnostic, not a result.
- No nearby 13C claim is supported. The expected sidebands are not dominant or separated by the short-window FFT, and the dominant screen is not the programmed carrier or either expected sideband.
- The physical origin of the recurring ~1.18-1.20 MHz feature is not established. It could be actual detuning from a shifted resonance, a control/systematic feature, or a non-simple Ramsey response; the current data do not distinguish these.
- The data also do not support declaring the carrier definitively absent. There is weak, phase-coherent early-time 1.0 MHz content, but it is not clean enough for T2star extraction.

## Recommended next action

Do not run another blind Ramsey repeat and do not promote a T2star/13C result from this file. The next bridge-touching step should be a fresh weak-pi pODMR center check around the `3.8759 GHz` working point, because a roughly 0.18-0.20 MHz resonance offset could make a programmed 1.0 MHz Ramsey detuning appear near the recurring 1.18-1.20 MHz component. If the center check explains the offset, update `mw_freq` and rerun a controlled Ramsey; if it does not, use a deliberate det-shift/phase-control Ramsey or alternate protocol and require the feature to follow the programmed detuning before fitting T2star.
