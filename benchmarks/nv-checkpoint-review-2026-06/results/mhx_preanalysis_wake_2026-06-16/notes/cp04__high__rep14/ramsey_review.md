# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New terminal measurement: `measurement/m001.json` raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`; `measurement/m002.json` job spec; `measurement/m003.json` bridge result; `measurement/m004.json` status; `measurement/m005.json` control.
- Prior comparison context: especially `evidence/e008.json` terminal det=1.0 MHz short-tau Ramsey review and `evidence/e019.json` / `evidence/e021.json` det-shift model plan and success criteria.

## Calculations or scripts run

- Created and ran `analyze_ramsey_detshift.py`.
- Outputs: `ramsey_detshift_analysis.json` and `ramsey_detshift_review.png`.
- Checks performed:
  - Verified `ExperimentDataEachAvg` axis contract by averaging per-average readouts back to `ExperimentData`.
  - Used readout 1 as reference and readout 2 as Ramsey signal, consistent with the saved `ramsey.xml` / `full_experiment=0` project context.
  - Computed raw signal/reference traces, point-wise ratio, signal divided by fitted reference line, SEM across 12 stored averages, scan-order-aware common-mode drift summary, FFT bins, least-squares sinusoid screens, target-frequency amplitudes, per-average screens, and descriptive damped-sinusoid grid fits.

## Key quantitative results

- Run completed: `nv23_ramsey_20260514_015423_auto_ramsey`, state `completed`, finished `2026-05-14T04:15:00`, final counts `44.796 kcps`, monitor `last_error` empty, `stop_requested=false`.
- Acquisition: `tau = 0.048..1.968 us`, 41 points, 48 ns spacing, `det = 1.5 MHz`, `mw_freq = 3.8759 GHz`, 12 averages x 90000 repetitions = `1.08e6` shots per tau point.
- Drift/common-mode check: local scan-order-aware summary flagged no averages; scan order was snake.
- Noise/variation: median raw-signal SEM `0.711 kcps`; median ratio SEM `0.0126`. Signal residual peak-to-peak after linear baseline was `6.29 kcps`; ratio residual peak-to-peak was `0.133`.
- Ratio LS screen:
  - strongest all-tau component near `1.623 MHz`, ratio amplitude `0.0255`, raw-signal amplitude `1.25 kcps`.
  - programmed `1.5 MHz` carrier: ratio amplitude `0.0240`, raw amplitude `1.13 kcps`.
  - det-tracking prediction from prior `1.192 + 0.5 = 1.692 MHz`: ratio amplitude `0.0250`, raw amplitude `1.22 kcps`.
  - old fixed `1.192 MHz` component: ratio amplitude only `0.0051`, raw amplitude `0.474 kcps`.
- Sideband checks for `det=1.5 MHz` and `f13C ~= 0.3846 MHz`:
  - low sideband `1.115 MHz`: ratio amplitude `0.0108`.
  - high sideband `1.885 MHz`: ratio amplitude `0.0173`.
  - neither is dominant or consistent enough for a 13C claim.
- Caveats:
  - raw signal LS screen is strongest near `0.882 MHz`, not near 1.5-1.7 MHz.
  - after skipping `tau <= 0.2 us`, the ratio LS screen shifts toward `~0.746 MHz`.
  - per-average top frequencies are inconsistent.
  - descriptive damped fits prefer short apparent decay and sub-carrier frequencies (`ratio`: `0.678 MHz`, `T2* ~0.47 us`; raw signal: `0.818 MHz`, `T2* ~0.72 us`), so they are not promoted as physical T2star.

## Plausible interpretation

The det-shift measurement is valid, terminal, and analyzable. It argues against the old `~1.192 MHz` feature being a fixed artifact because that component is strongly suppressed in the det=1.5 MHz run. The combined ratio view is suggestive of partial det tracking: the strongest component is near `1.623 MHz`, close to the `~1.692 MHz` prediction within the coarse `~0.52 MHz` nominal frequency resolution of the 1.92 us span.

However, the evidence is not clean enough to assign a physical Ramsey carrier or extract T2star. Raw signal and normalized views disagree on the dominant frequency, early-time transient behavior remains important, and stored averages do not show a stable single-frequency picture.

## Claims not yet supported

- No well-supported numeric T2star for r03 from this Ramsey branch.
- No supported nearby 13C coupling conclusion.
- No supported claim that the `1.623 MHz` ratio component is definitively the physical Ramsey carrier.
- No supported sideband model around the det=1.5 MHz carrier.

## Recommended next action

Do not run another blind Ramsey repeat. Perform a bridge-free synthesis of all four r03 Ramsey datasets, then choose between:

1. a targeted alternate protocol that is less sensitive to the early-time transient / readout-normalization ambiguity, such as a Hahn-echo or CPMG baseline route if available under the project safety gates; or
2. a supported branch conclusion that r03 is aligned by pODMR but T2star and 13C remain unsupported under the current Ramsey conditions.
