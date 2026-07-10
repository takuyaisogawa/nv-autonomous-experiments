# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New terminal Ramsey measurement:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
  - `measurement/m002.json`: submitted job spec.
  - `measurement/m003.json`: completed bridge result.
  - `measurement/m004.json`: final run status.
  - `measurement/m005.json`: final run control state.
- Prior comparison/model context:
  - `evidence/e008.json`: terminal det=1.0 MHz short-tau Ramsey review.
  - `evidence/e019.json`: det=1.5 MHz shift-check model plan and target frequencies.
  - `evidence/e021.json`: verified experiment intent.
- Generated local analysis artifacts: `analyze_current_ramsey.py`, `ramsey_review_analysis.json`, `ramsey_review_plot.png`.

## Calculations or scripts run

- Ran `python analyze_current_ramsey.py`.
- Verified raw-export axis contract: `ExperimentData` shape `[1,2,41]`; `ExperimentDataEachAvg` shape `[1,12,2,41]`; averaging the per-average axis reproduces combined readouts.
- Reconstructed tau grid: 48 ns to 1.968 us, 41 points, 48 ns step; Nyquist about 10.42 MHz; nominal `1/span` resolution about 0.521 MHz.
- Checked terminal health: run completed, 12 averages x 90000 repetitions = 1.08e6 shots per tau, final counts 44.796 kcps, stop not requested, monitor error empty.
- Ran local scan-order-aware drift heuristic using `ScanOrderEachAvg` snake order. No averages were flagged; max common-mode drop was 0.040 and max worst-readout drop was 0.053, below the 0.15 threshold used by the project drift checks.
- Computed raw signal, reference, point-wise ratio, and signal divided by fitted reference-line views.
- Computed SEM across stored averages: median signal SEM 0.711 kcps; median ratio SEM 0.0126.
- Ran linear-detrended FFT and least-squares component screens at:
  - programmed carrier 1.500 MHz,
  - programmed 13C sidebands 1.115 and 1.885 MHz,
  - det-tracking carrier predicted from prior 1.192 MHz feature: 1.692 MHz,
  - det-tracking sidebands 1.307 and 2.077 MHz,
  - previous artifact/control frequency 1.192 MHz.
- Ran descriptive damped-sinusoid grid fits only as diagnostics.

## Plausible interpretation

- The measurement is valid/analyzable as a completed terminal Ramsey dataset; there is no hard bridge anomaly, no stop request, and no local drift flag.
- The det-shift check gives partial evidence that the old fixed 1.192 MHz feature is not simply repeated: its ratio LS amplitude fell to 0.0051, while the strongest point-wise ratio screen moved to 1.623 MHz with ratio amplitude 0.0255.
- The moved ratio component is in the broad det-tracking/programmed-carrier band: 1.623 MHz lies between the programmed 1.500 MHz carrier and the prior-feature-tracking prediction of 1.692 MHz. With a 1.92 us span, these are not cleanly separated by FFT resolution.
- The evidence is still mixed across readout views. Raw signal and signal/fitted-reference-line screens peak near 0.882 MHz, not near 1.5-1.7 MHz. Per-average top frequencies are also inconsistent.
- The best cautious reading is: the det change affected the observed normalized Ramsey structure, arguing against a purely fixed 1.192 MHz artifact, but the current data still do not establish a clean physical Ramsey carrier model.

## Claims that are not yet supported

- Do not claim a numerical T2star from this run. The descriptive grid fits are model-sensitive and disagree by view: ratio fit near 0.678 MHz with `T2star ~0.47 us`; raw-signal fit near 0.818 MHz with `T2star ~0.72 us`. These are diagnostics, not physical estimates.
- Do not claim nearby 13C coupling. The programmed sideband ratio amplitudes are 0.0108 at 1.115 MHz and 0.0173 at 1.885 MHz; det-tracking sideband amplitudes are 0.0095 at 1.307 MHz and 0.0061 at 2.077 MHz. None is dominant or consistently supported across raw/readout-aware views.
- Do not claim that the physical carrier is exactly 1.623 MHz or exactly det-tracking. The ratio view supports a shifted component, but raw signal and fitted-reference-line normalization do not.
- Do not use point-wise normalization alone as signal-presence evidence.

## Recommended next action

- Do not run another blind Ramsey repeat under the same protocol. First do a bridge-free branch synthesis of all r03 Ramsey datasets, explicitly separating:
  - supported aligned-NV / pODMR evidence,
  - unsupported T2star,
  - unsupported 13C,
  - the limited det-shift evidence that the old 1.192 MHz feature is not fixed.
- If the project continues experimentally, move to an alternate targeted protocol or control path rather than more same-style Ramsey accumulation. The next design should require raw-signal/readout-aware carrier evidence before any T2star fit, and should treat 13C only after a supported carrier/sideband model appears.
