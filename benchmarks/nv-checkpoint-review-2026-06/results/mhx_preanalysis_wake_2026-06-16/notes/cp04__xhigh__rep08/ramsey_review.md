# Ramsey Review: r03 det-shift short-tau run

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New Ramsey measurement: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control.
- Prior comparison/model context: `evidence/e008.json` prior det=1.0 MHz short-tau terminal review, `evidence/e019.json` det=1.5 MHz shift-check model plan, plus nearby bridge/batch metadata in `evidence/e020.json`-`e030.json`.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis_summary.json` and `ramsey_analysis.png`.
- Checks performed:
  - Verified per-average raw-export axis contract: `ExperimentDataEachAvg` behaves as `[avg, readout, tau point]` and reconstructs combined `ExperimentData`.
  - Used readout1 as reference and readout2 as Ramsey signal per project context for `ramsey.xml` with `full_experiment=0`.
  - Computed raw signal/reference, point-wise signal/reference, signal over fitted reference line, per-point SEM from 12 stored averages, FFT bins, least-squares sinusoid screens, target-frequency amplitudes, per-average top-frequency screens, odd/even-average screens, early-time cutoff sensitivity, and descriptive damped-sinusoid grid fits.

## Key quantitative results

- Run completed safely: `nv23_ramsey_20260514_015423_auto_ramsey`, final counts `44.796 kcps`, no stop request, no monitor error, safe shutdown OK.
- Measurement settings: `mw_freq = 3.8759 GHz`, `det = 1.5 MHz`, `tau = 48 ns..1.968 us`, 41 points, 12 averages x 90000 repetitions = `1.08e6` shots per tau point.
- Noise/shape scale: median raw-signal SEM `0.711 kcps`; median ratio SEM `0.0126`. Raw signal linear-residual peak-to-peak `6.29 kcps`; first 0.75 us raw-signal peak-to-peak `6.46 kcps`; first 0.75 us ratio peak-to-peak `0.134`.
- Prior det=1.0 MHz short-tau run had top ratio component `1.192 MHz` with ratio amplitude `0.0363`.
- New point-wise ratio screen top is near `1.623 MHz`, amplitude `0.0255`, about `2.0x` median ratio SEM. This is shifted by `+0.431 MHz` from the prior `1.192 MHz`, near but not exactly the expected `+0.5 MHz` det shift; it is `69 kHz` below the predicted `1.692 MHz` tracking carrier.
- Target ratio amplitudes: programmed `1.5 MHz` carrier `0.0240`; predicted det-tracking `1.692 MHz` carrier `0.0250`; old fixed `1.192 MHz` control only `0.0051`.
- Raw/readout-aware caveat: raw signal and fitted-reference-line normalization are instead dominated near `0.882 MHz` (`1.53 kcps` raw amplitude; fitted-reference-line amplitude `0.0319`). The reference channel also has sub-MHz structure near `0.924 MHz`.
- Early-cutoff robustness is poor: after skipping early tau, the top frequency changes substantially (`~0.70-0.78 MHz` after skipping 0.2-0.3 us, `~1.09 MHz` after skipping 0.5 us, `~1.43-1.45 MHz` after skipping 0.75 us).
- Per-average consistency is weak: individual ratio-screen tops scatter across `0.25`, `0.79-0.895`, `1.20`, `1.545-1.75`, and `1.94 MHz`; odd/even average group tops differ (`0.850 MHz` vs `1.601 MHz`).
- 13C target checks are weak: programmed sidebands at `1.115/1.885 MHz` have ratio amplitudes `0.0108/0.0173`; det-tracking sidebands at `1.307/2.077 MHz` have ratio amplitudes `0.0095/0.0061`. None dominate across readout-aware views.

## Plausible interpretation

The new det=1.5 MHz run gives a useful diagnostic: the old `1.192 MHz` point-wise-ratio component does not remain strong at the fixed old frequency, and the combined ratio screen moves toward the expected det-shifted region. That weakly argues against a purely fixed `1.192 MHz` artifact.

However, this is still not claim-grade Ramsey physics. The carrier-like feature is only about `2x` the ratio SEM, raw signal/fitted-reference views prefer a sub-MHz component, the result is sensitive to early-time points, and stored averages do not agree on a dominant frequency. A plausible explanation is a mixture of real phase evolution with early-time/baseline/readout transients, but the present data do not isolate a stable physical carrier.

## Claims not yet supported

- No numeric T2star is supported from this run.
- No nearby 13C conclusion is supported.
- The `1.623 MHz` ratio-screen feature is not yet a confirmed Ramsey carrier.
- The descriptive damped-sinusoid fits are not supported physical parameter estimates; they are transient/model diagnostics only.
- The data do not justify another blind same-style Ramsey repeat as the next step.

## Recommended next action

Record this det-shift run as analyzable but non-claim-grade evidence. Do not claim T2star or 13C from r03 Ramsey data yet. Next, stop repeating the same Ramsey pattern and choose a targeted alternate route: either close the r03 Ramsey/T2star/13C branch as unsupported under current Ramsey conditions, or run an alternate protocol designed to separate real spin coherence from the early-time transient before attempting any T2star or 13C fit.
