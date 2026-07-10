# Ramsey Review: det=1.5 MHz short-tau shift check

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New Ramsey data/metadata: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` final status, `measurement/m005.json` control state.
- Generated local analysis artifacts: `ramsey_analysis_summary.json` and `ramsey_detshift_diagnostic.png`.

## Calculations or scripts run

- Used a local Python scratch analysis on `measurement/m001.json`.
- Verified raw array contract:
  - `ExperimentData` shape is `[1, 2, 41]`.
  - `ExperimentDataEachAvg` shape is `[1, 12, 2, 41]`.
  - Averaging `ExperimentDataEachAvg[0, :, readout, :]` reproduces `ExperimentData[0, readout, :]`, so the stored-average axis is identified.
- Treated readout 1 as reference and readout 2 as signal, consistent with the prior project convention for this Ramsey route.
- Built raw signal, point-wise ratio, and reference-line-normalized views.
- Ran least-squares sinusoid screens using offset + linear baseline + sin/cos terms from 0.2 to 4.0 MHz.
- Checked target frequencies:
  - programmed det: 1.500 MHz
  - prior fixed-feature control: 1.192 MHz
  - det-tracking prediction from prior 1.192 MHz plus +0.5 MHz: 1.692 MHz
  - expected 13C sidebands around det-tracking prediction: about 1.307 and 2.076 MHz
  - sidebands around programmed det: about 1.116 and 1.884 MHz
- Per-point statistics from 12 averages:
  - median signal SEM: about 0.711 kcps
  - median ratio SEM: about 0.0126
  - signal mean: about 44.27 kcps; reference mean: about 48.08 kcps
- Simple per-average mean provenance check:
  - signal average means span about 39.64 to 46.92 kcps
  - reference average means span about 44.59 to 50.60 kcps
  - scan order is recorded as snake and tracking was per average.

## Plausible interpretation

- The experiment completed normally: `nv23_ramsey_20260514_015423_auto_ramsey`, `tau = 48 ns..1.968 us`, 41 points, `det = 1.5 MHz`, `mw_freq = 3.8759 GHz`, 12 averages x 90000 repetitions, final count `44.796 kcps`, no stop request.
- The previous det=1.0 MHz short-tau run's empirical ~1.192 MHz component is not strong here:
  - ratio LS amplitude at 1.192 MHz is about 0.0051 with `delta_R2 ~0.017`;
  - raw-signal LS amplitude at 1.192 MHz is about 0.474 kcps with `delta_R2 ~0.064`.
- There is some support for frequency content nearer the det-shift expectation than the old fixed 1.192 MHz value:
  - ratio screen top components cluster around 1.54 to 1.70 MHz, with the best ratio screen near 1.623 MHz and another near 1.704 MHz;
  - at the explicit 1.692 MHz det-tracking target, ratio amplitude is about 0.0250 with `delta_R2 ~0.411`;
  - the programmed 1.500 MHz target is also comparable, ratio amplitude about 0.0240 with `delta_R2 ~0.359`.
- However, the support is not clean:
  - raw signal and reference-line-normalized views have their strongest LS component near 0.88 MHz, not uniquely near 1.5 to 1.7 MHz;
  - per-average ratio screens are inconsistent, with top frequencies spread across about 0.2, 0.8-0.9, 1.2, 1.5-1.75, and 3.86 MHz;
  - the 1.307 and 2.076 MHz det-tracking 13C sideband targets are weak in the combined ratio screen.
- Best current reading: the det-shift run argues against a simple fixed artifact exactly at the old 1.192 MHz feature, but it still does not establish a clean Ramsey carrier model or 13C sideband model.

## Claims that are not yet supported

- Do not claim a fitted or physical `T2*` from this run.
- Do not claim nearby `13C` coupling from the 1.307/2.076 MHz or 1.116/1.884 MHz sideband targets.
- Do not claim that the Ramsey carrier is confirmed at 1.500 MHz or 1.692 MHz; both are plausible screen components, but neither is uniquely supported across raw/readout-aware views and stored averages.
- Do not use the descriptive frequency-screen maxima as a precision frequency estimate.

## Recommended next action

- Stop doing blind Ramsey repeats on this r03 branch under the same short-tau conditions.
- Since several Ramsey attempts remain non-claim-grade despite good r03 ODMR evidence and high shot count, choose an alternate protocol or a closeout-style supported-negative statement for Ramsey/13C under current conditions.
- Preferred next experiment if continuing the branch: run a Hahn-echo/CPMG `N=1` baseline to test whether coherent refocusing gives a clearer decay/contrast handle before any further 13C spectroscopy. If the goal is specifically 13C, move to a protocol designed for nuclear-spin response after establishing that the electron coherence signal is measurable.
