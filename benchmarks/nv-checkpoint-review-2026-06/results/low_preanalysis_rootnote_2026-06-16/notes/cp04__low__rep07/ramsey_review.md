# Ramsey Review: r03 det=1.5 MHz short-tau shift check

## Files/data used
- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`, `md/knowledge.md`.
- New measurement: `measurement/m001.json` raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`; `measurement/m002.json` job spec; `measurement/m003.json` terminal result; `measurement/m004.json` run status; `measurement/m005.json` control.
- Prior comparison context: `evidence/e008.json` and `evidence/e019.json` for the det=1.0 MHz short-tau result and the det-shift plan.
- Derived local outputs: `analysis/ramsey_det1p5_review_summary.json`, `analysis/ramsey_det1p5_review.png`.

## Calculations or scripts run
- Used inline Python to parse `measurement/m001.json`, inspect `ExperimentData` and `ExperimentDataEachAvg`, and compute:
  - tau grid: 41 points, 48 ns to 1.968 us, 48 ns step, Nyquist 10.42 MHz.
  - acquisition: 12 averages x 90000 repetitions, final counts 44.796 kcps.
  - readout means: signal 44.27 kcps, reference 48.08 kcps; median signal SEM 0.71 kcps; median signal/reference SEM 0.0126.
  - least-squares sinusoid screens versus linear/quadratic baselines on raw signal and signal/reference ratio.
  - per-average target-band peak checks and per-average mean count checks.
- Plotted raw readouts, normalized signal, LS frequency screen, and per-average means in `analysis/ramsey_det1p5_review.png`.

## Plausible interpretation
- The new det=1.5 MHz run completed safely and is analyzable. It used the intended accepted r03 NV, `mw_freq = 3.8759 GHz`, `det = 1.5 MHz`, same short-tau window as the prior det=1.0 MHz diagnostic, and no stop request/error is recorded.
- The previous fixed empirical component near 1.192 MHz is not reproduced strongly: signal/reference LS amplitude at 1.192 MHz is only about 0.0045-0.0051, compared with about 0.0363 in the prior det=1.0 MHz terminal review.
- The most relevant target-band structure is near the det-tracking expectation. Around 1.692 MHz the signal/reference LS amplitude is about 0.025-0.026 and raw-signal amplitude about 1.22-1.29 kcps. This is close to the predicted shifted version of the old 1.192 MHz component and larger than the old fixed 1.192 MHz response in this run.
- The programmed 1.5 MHz carrier is similar but slightly weaker: signal/reference LS amplitude about 0.024 and raw-signal amplitude about 1.13 kcps. Local target-band peaks cluster around 1.55-1.66 MHz depending on baseline model.
- The expected 13C sideband positions are not supported: lower sideband near 1.307 MHz has weak ratio amplitude about 0.009-0.011, and upper sideband near 2.076 MHz is about 0.006.
- There is substantial slow baseline/common-mode structure. Low-frequency components below about 0.6 MHz dominate the broad LS screen, and per-average means vary noticeably, including a low-count average 7. The target-band feature is therefore suggestive but not robust enough to promote a fitted T2star.

## Claims not yet supported
- No supported numeric T2star from this run. A damped Ramsey fit would be model-dependent because the target-band oscillation is small and baseline-sensitive.
- No supported nearby 13C claim. The expected sidebands around the det-tracking carrier are not resolved with consistent amplitude or per-average support.
- Do not claim that the 1.66-1.69 MHz feature is definitively the physical Ramsey carrier. It argues against a fixed 1.192 MHz artifact, but per-average peak locations are mixed and slow baseline content is strong.
- Do not claim r03 has failed as an NV candidate; spectroscopy already supports r03 alignment. The unsupported part remains Ramsey/T2star/13C under the present protocol/conditions.

## Recommended next action
- Stop blind Ramsey repeats on this branch. The det-shift result partially supports det tracking but still does not meet claim-grade T2star/13C criteria.
- Next choose an alternate protocol or a targeted control that attacks the baseline/early-transient problem, such as a phase-cycled Ramsey/alternate readout normalization route if available, or move to a different T2-family protocol appropriate for obtaining a defensible coherence bound. If no such protocol is available now, close this branch as: aligned r03 found, T2star and 13C not supported under current Ramsey conditions.
