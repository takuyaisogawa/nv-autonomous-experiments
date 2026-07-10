# Ramsey Review: r03 det=1.5 MHz short-tau shift check

## Files/data used

- `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`: project objective, accepted r03 context, prior Ramsey conclusions, and planned det-shift test.
- `measurement/m001.json`: terminal raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
- `measurement/m002.json`: submitted job spec for `nv23_ramsey_20260514_015423_auto_ramsey`.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal result/status/control.
- `evidence/e008.json`: prior terminal short-tau `det=1.0 MHz` review used for the comparison point.
- Generated locally: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_det1p5_review.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey.py`.
- Verified `ExperimentDataEachAvg` axis contract by averaging 12 per-average readout traces back to `ExperimentData`.
- Used raw readout roles from the prior project context: readout 1 as reference, readout 2 as Ramsey signal; computed raw signal, reference, signal/reference ratio, and signal/reference-line normalization.
- Checked acquisition metadata: completed job, `mw_freq = 3.8759 GHz`, `det = 1.5 MHz`, `tau = 48 ns..1.968 us`, 41 points, 12 averages x 90000 repetitions, final count text `44.796 kcps`.
- Computed point SEM across averages: median signal SEM `0.711 kcps`, median ratio SEM `0.0126`.
- Computed FFT/LS frequency screens from `0.25..2.5 MHz`, including all tau, skip-first-point, and skip-`tau <= 0.2 us` masks.
- Checked targets:
  - programmed carrier `1.5 MHz`: ratio LS amplitude `0.0240`, residual-R2 improvement `0.359`, signal amplitude `1.13 kcps`.
  - det-tracking prediction from prior `1.192 + 0.5 = 1.692 MHz`: ratio LS amplitude `0.0250`, residual-R2 improvement `0.411`, signal amplitude `1.22 kcps`.
  - prior fixed `1.192 MHz` component: ratio LS amplitude `0.00511`, residual-R2 improvement `0.0167`.
  - expected 13C sidebands near `1.307 MHz` and `2.076 MHz`: ratio amplitudes `0.00949` and `0.00616`, weak and not paired convincingly.
- Screen results:
  - ratio all-tau top component near `1.623 MHz`, ratio amplitude `0.0255`, residual-R2 improvement `0.430`.
  - ratio skip-first top near `1.650 MHz`.
  - ratio skip-`tau <= 0.2 us` top near `0.746 MHz`.
  - raw signal and signal/reference-line normalization top near `0.882 MHz`.
- Per-average top-frequency screen was inconsistent: individual best frequencies were spread across about `0.25..1.94 MHz`, though several averages retain moderate amplitude at `1.5..1.692 MHz`.
- Simple robust average-mean drift screen flagged no average; signal means ranged `39.64..46.92 kcps`, ratio means `0.8897..0.9536`.
- Descriptive damped-ratio grid fit selected `0.678 MHz`, `T2* ~0.47 us`, with improved BIC versus a linear baseline. This fit is not promoted because it is not tied to the programmed carrier or det-tracking target and is mask/readout sensitive.

## Plausible interpretation

- The det-shift run is analyzable and shows oscillatory/transient structure above the median point noise.
- The old fixed `~1.192 MHz` feature is not reproduced strongly in the new ratio data. This argues against simply treating the prior `~1.192 MHz` component as a stable fixed artifact.
- The new all-tau ratio component near `1.62 MHz` lies between the programmed `1.5 MHz` carrier and the prior-component det-tracking prediction `1.692 MHz`. With only a `1.92 us` tau span, nominal frequency resolution is about `0.52 MHz`, so this run cannot cleanly distinguish those frequencies.
- However, the result is not claim-grade: the preferred frequency depends strongly on analysis mask and readout treatment, and per-average frequency screens are inconsistent. The data may include an early-time transient, imperfect normalization/common-mode effects, or a real short-lived Ramsey response that is not isolated cleanly by this protocol.

## Claims that are not yet supported

- Do not claim a numeric T2*. The descriptive `~0.47 us` fit is model-dependent and selects a frequency that is not the planned carrier/det-tracking component.
- Do not claim nearby 13C coupling. The expected sidebands near `1.307 MHz` and `2.076 MHz` are weak and do not form a robust sideband pair.
- Do not claim that the Ramsey carrier is cleanly observed at exactly `1.5 MHz` or `1.692 MHz`. The all-tau ratio peak is near that band, but resolution and mask/readout dependence prevent a hard carrier assignment.
- Do not claim the prior `~1.192 MHz` feature was definitively physical. The det shift weakens a fixed-artifact explanation, but does not establish a clean det-following physical model.

## Recommended next action

Stop blind Ramsey repeats on r03 under this protocol. The most useful next step is a branch decision: either move to an alternate T2*/frequency-domain protocol or close the r03 Ramsey branch with a supported negative/unsupported conclusion under current conditions. If another measurement is justified, it should be a non-blind control designed to separate early-time transient/readout normalization from Ramsey phase evolution, not another same-grid accumulation.
