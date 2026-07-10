# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json`.
- Measurement data: `measurement/m001.json` raw savedexperiment export; `measurement/m002.json` job spec; `measurement/m003.json` terminal result; `measurement/m004.json` run status; `measurement/m005.json` run control.
- Prior local context used quantitatively: `evidence/e014.json` refreshed-center Ramsey model/plan, including targets at carrier `1.5 MHz` and 13C sidebands `1.115/1.885 MHz` from `f13C = 384.8 kHz`.
- Created local scratch outputs: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, and `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Validated raw array contract: `ExperimentData` shape `[2,41]`, `ExperimentDataEachAvg` shape `[20,2,41]`; mean of per-average readouts reproduced combined readouts to `~1e-14 kcps`.
- Confirmed scan: `tau = 0.048..8.048 us`, `0.2 us` step, 41 points; `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`, `20 x 50000 = 1.0e6` shots per tau.
- Terminal health: completed, final counts `43.433 kcps`, safe shutdown ok, not aborted, no stop request.
- Drift/noise checks: no average exceeded the local `15%` common-mode drop flag; median signal SEM `0.850 kcps`; median fitted-reference-line normalized SEM `0.00937`.
- Least-squares frequency screens used `offset + linear trend + cos/sin(f)` on raw signal, point-wise ratio, and fitted-reference-line normalization, over full data and skipping first 4 tau points. FFT checks were also run after linear detrending.
- Main fitted-reference-line normalized checks:
  - Broad screen top: `~2.271 MHz`, amplitude `0.01678` full span and `0.01139` after skip-first-4.
  - Programmed carrier `1.5 MHz`: amplitude `0.01447` full span and `0.01049` after skip-first-4; raw-signal amplitude `0.705 kcps` full and `0.512 kcps` after skip-first-4.
  - Planned 13C sidebands: `1.115 MHz` amplitude `0.00298` full / `0.00025` skip; `1.885 MHz` amplitude `0.00536` full / `0.00255` skip.
  - Exploratory `det + 2*f13C ~= 2.270 MHz`: amplitude `0.01677` full / `0.01138` skip, with per-average phase coherence `R = 0.878`; paired `det - 2*f13C ~= 0.730 MHz` was weak, amplitude `0.00381` full / `0.00324` skip and phase coherence `R = 0.317`.
- Descriptive damped-sinusoid grid checks were not stable: full-span fits preferred the shortest allowed `T2star = 0.25 us` boundary near `1.74..1.8 MHz`; skip-first-4 fits preferred `~1.53 MHz` with `T2star ~2.8 us` exponential or `~4.0 us` Gaussian.

## Plausible interpretation

The run is healthy and analyzable. Compared with earlier non-claim-grade Ramsey runs, this refreshed-center, higher-shot dataset now contains modest carrier-compatible oscillatory content near `1.5 MHz`; the carrier phase is fairly consistent across averages (`R = 0.829` in the normalized view). However, the carrier amplitude is small, roughly comparable to per-point SEM, and it is not the dominant broad-screen component.

The strongest combined component is near `2.27 MHz`. Its proximity to `det + 2*f13C` is a useful hypothesis generator, especially because prior det-shift context had a skip-transient feature near the rough lower partner region. But in this dataset the lower `det - 2*f13C` partner is weak, the predeclared first-order sidebands at `det +/- f13C` are weak, and the decay fit is sensitive to early tau points. Treat this as a possible coupled-spin or analysis/artifact lead, not a 13C conclusion.

## Claims that are not yet supported

- A numerical T2star value is not supported. Full-span and skip-transient decay fits disagree and the full-span optimum is boundary-dominated.
- A nearby 13C claim is not supported. The planned first-order sidebands are weak and inconsistent, and the exploratory `2.27 MHz` feature lacks a mirrored/control confirmation.
- The refreshed pODMR center has not by itself solved the Ramsey/T2star problem; it improved carrier-like evidence but did not produce a clean carrier-plus-decay model.
- The `2.27 MHz` component should not be assigned to a physical coupling yet.

## Recommended next action

Avoid another blind repeat. Use this result to design a targeted Ramsey diagnostic that predeclares carrier, `det +/- f13C`, and `det +/- 2*f13C` targets and tests whether the `2.27 MHz` feature shifts with programmed detuning. A good next measurement would keep the refreshed NV/frequency workflow, use an alternate detuning such as `1.25 MHz` with an 8 us span and similar shot budget if drift allows, and require the carrier/sideband pattern to move by the detuning change while fixed apparatus features do not. Recalibrate weak-pi pODMR first if the frequency calibration is stale.
