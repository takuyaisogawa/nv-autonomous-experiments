# Ramsey Review

## Files/Data Used

- New completed Ramsey det-shift run:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`
  - `measurement/m002.json`: executed job spec
  - `measurement/m003.json`: terminal bridge result
  - `measurement/m004.json`: terminal bridge status
  - `measurement/m005.json`: bridge control state
- Prior comparison/control:
  - `evidence/e006.json`: terminal raw export for prior det=1.0 MHz short-tau Ramsey
  - `evidence/e008.json`: prior terminal review summary
  - `evidence/e019.json`: det-shift model/target plan
- Project context:
  - `project/brief.md`, `project/state.md`, `project/advice.md`
  - `md/memory.md`, `md/knowledge.md`, `context.json`

## Calculations/Scripts Run

- Created and ran `analyze_ramsey_detshift.py`.
- Outputs:
  - `ramsey_detshift_analysis.json`
  - `ramsey_detshift_review.png`
- Checks performed:
  - Verified `ExperimentDataEachAvg` axis contract by averaging per-average readouts back to `ExperimentData`.
  - Computed raw reference, raw signal, point-wise signal/reference ratio, and signal normalized by a fitted reference line.
  - Computed per-point SEM from stored averages.
  - Ran linear-baseline plus sinusoid least-squares frequency screens from 0.25 to 2.5 MHz.
  - Checked FFT bins after linear detrending; bin spacing is coarse at about 0.508 MHz, with nominal span resolution about 0.521 MHz.
  - Ran a local scan-order common-mode drift approximation using `Scan.ScanOrderEachAvg`.
  - Verified the generated PNG opens as a 1980 x 1260 RGBA image.

## Quantitative Results

- New run completed normally:
  - job `nv23_ramsey_20260514_015423_auto_ramsey`
  - det = 1.5 MHz, `mw_freq = 3.8759 GHz`
  - tau = 48 ns to 1.968 us, 41 points, 48 ns step
  - 12 averages x 90000 repetitions = 1.08e6 shots per tau point
  - final counts 44.796 kcps, no monitor error, no stop request, safe shutdown true
- Local drift check:
  - scan order mode `snake`
  - no flagged averages
  - maximum local common-mode drop score about 0.040, below the 0.15 threshold used in the project drift convention
- Noise/scale:
  - median raw-signal SEM: 0.711 kcps
  - median ratio SEM: 0.0126
  - early 0.75 us peak-to-peak: 6.46 kcps raw signal, 0.134 ratio
- Det-shift comparison:
  - prior terminal det=1.0 MHz ratio-screen top: 1.192 MHz, ratio amplitude 0.0363
  - new det=1.5 MHz point-wise ratio-screen top: 1.623 MHz, ratio amplitude 0.0255, linear-baseline residual R2 improvement 0.430
  - expected det-tracking target from prior top: about 1.692 MHz; new amplitude there is 0.0250 ratio with R2 improvement 0.411
  - old 1.192 MHz artifact-control point is weak in the new ratio view: amplitude 0.0051, R2 improvement 0.017
- Raw/readout-aware caveat:
  - new raw signal is dominated by about 0.882 MHz, amplitude 1.53 kcps, R2 improvement 0.577
  - fitted-reference-line normalization is also dominated by about 0.882 MHz, amplitude 0.0319, R2 improvement 0.576
  - reference readout has its own structure near about 0.924 MHz, amplitude 0.405 kcps, R2 improvement 0.292
  - per-average top frequencies are scattered, not a clean repeatability check
- 13C target checks in the new run:
  - programmed sidebands at about 1.115 and 1.885 MHz are not dominant
  - det-tracking sidebands at about 1.307 and 2.077 MHz are also not dominant

## Plausible Interpretation

The new data weakly argue that the earlier 1.19 MHz point-wise ratio feature was not simply a fixed-frequency artifact: the ratio-screen maximum moved upward when det was changed from 1.0 to 1.5 MHz, landing within about 0.069 MHz of the planned det-tracking target. However, this is not claim-grade evidence for a physical Ramsey carrier because the raw signal and fitted-reference-line view do not share that dominant frequency; they are instead dominated by a first-scout-like component near 0.88 MHz. The reference readout also has measurable frequency structure, so point-wise ratio evidence is especially vulnerable to denominator/reference artifacts.

This run is therefore analyzable and useful as a diagnostic, but it does not yet provide a clean carrier/sideband model. The most conservative interpretation is mixed evidence: there may be det-dependent phase content in the ratio channel, but baseline/reference/transient effects still dominate the raw/readout-aware interpretation.

## Claims Not Yet Supported

- No well-supported numeric T2star is established from this run.
- No nearby 13C coupling conclusion is established.
- Do not claim a clean det-tracking Ramsey carrier from the ratio view alone.
- Do not assign the 0.882 MHz raw-signal feature, the 1.623 MHz ratio feature, or any sideband target to a physical spin transition without further protocol evidence.
- The aligned-r03 pODMR conclusion remains supported by earlier spectroscopy, but this Ramsey run does not complete the T2star/13C objective.

## Recommended Next Action

Do not run another blind same-style Ramsey repeat. Treat the current Ramsey branch as non-claim-grade and move to a targeted alternate protocol/readout diagnostic before any T2star fit: specifically, use a design that suppresses or separates point-wise reference artifacts and early-tau transients, then require a carrier that is present in raw signal and fitted-reference-line normalization before fitting T2star or interpreting 13C sidebands. If that is not available or remains mixed, close r03 Ramsey/T2star/13C as unsupported under current conditions rather than accumulating more equivalent Ramsey data.
