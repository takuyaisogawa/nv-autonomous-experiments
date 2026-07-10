# Ramsey Review: det=1.5 MHz short-tau shift check

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json`.
- New terminal Ramsey data and metadata: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` bridge job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, and `measurement/m005.json` control state.
- Prior det-shift plan/context from local evidence searched/read with `rg` and `Get-Content`, especially `evidence/e019.json`, `evidence/e021.json`, `evidence/e028.json`, and project-state summaries of the preceding det=1.0 MHz short-tau Ramsey.

## Calculations or scripts run

- Created and ran `analyze_ramsey_detshift.py`.
- Outputs: `ramsey_detshift_analysis.json` and `ramsey_detshift_analysis.png`.
- Checks performed:
  - Verified `ExperimentDataEachAvg` axis contract as `[scan, avg, readout, point]` by reconstructing `ExperimentData`; max absolute mismatch was `1.42e-14`.
  - Confirmed terminal run metadata: completed, `tau = 48 ns..1.968 us`, 41 points, `dt = 48 ns`, `det = 1.5 MHz`, `mw_freq = 3.8759 GHz`, `12 x 90000` repetitions, final counts `44.796 kcps`, snake scan order, no stop request.
  - Computed raw signal, reference, point-wise signal/reference ratio, fitted-reference-line normalization, per-point SEM across stored averages, per-average mean readouts, linear-sinusoid least-squares frequency screens, targeted LS fits, and detrended/Hann FFT checks.
  - Target frequencies checked: programmed carrier `1.500 MHz`, det-tracking prediction from prior `1.192 MHz` component at `1.692 MHz`, prior artifact-control `1.192 MHz`, programmed 13C sidebands `1.115/1.885 MHz`, and det-tracking sidebands `1.307/2.077 MHz`.

## Quantitative findings

- Median per-point SEM: raw Ramsey signal `0.711 kcps`, reference `0.745 kcps`, ratio `0.0126`.
- Full-trace ratio LS screen:
  - Best SSE frequency: `1.624 MHz`, ratio amplitude `0.0255`.
  - Programmed `1.500 MHz`: ratio amplitude `0.0240`, SSE improvement over baseline `0.0116`.
  - Det-tracking `1.692 MHz`: ratio amplitude `0.0250`, SSE improvement `0.0132`.
  - Prior `1.192 MHz` control: ratio amplitude only `0.00511`, SSE improvement `0.00054`.
- Full-trace raw-signal LS:
  - Best SSE frequency: `0.883 MHz`, amplitude `1.53 kcps`.
  - Programmed `1.500 MHz`: `1.13 kcps`.
  - Det-tracking `1.692 MHz`: `1.22 kcps`.
  - Prior `1.192 MHz`: `0.474 kcps`.
- Skip-first-3-points sensitivity check:
  - Ratio best SSE frequency moved to `0.808 MHz`, while det-tracking `1.692 MHz` still fit with ratio amplitude `0.0207`.
  - This sensitivity means the full-trace carrier-like feature is not robust enough for a parameter claim.
- FFT sanity check:
  - Coarse FFT bin spacing is about `0.508 MHz` for the 41-point grid, so it cannot cleanly distinguish `1.500` from `1.692 MHz`.
  - Full-trace ratio top bins included `0.508`, `1.524`, `2.033`, and `1.016 MHz`; skip-first-3 ratio top bin was `1.645 MHz`.
- Stored-average consistency is mixed:
  - Ratio per-average best-SSE frequencies split across about `0.79-0.90 MHz`, `1.20 MHz`, `1.54-1.75 MHz`, one `1.94 MHz`, and one low-frequency edge case.
  - Average-to-average mean readouts vary by about `16.4%` in raw signal, `12.5%` in reference, and `6.9%` in ratio.

## Plausible interpretation

The new det=1.5 MHz short-tau Ramsey run argues against simply promoting the prior `~1.192 MHz` feature as a fixed artifact or as the same dominant component: in the full combined ratio trace, `1.192 MHz` is weak while the best LS fit sits in the programmed/det-shift band near `1.62 MHz`, with targeted `1.500` and `1.692 MHz` fits both much stronger than the old control.

However, the evidence is still not claim-grade. The preferred frequency depends on baseline/early-tau treatment and readout view, and stored averages are not consistent enough to establish a clean Ramsey carrier. The 13C sideband targets do not appear as a coherent pair around either the programmed carrier or the det-tracking carrier.

## Claims not yet supported

- No well-supported numeric `T2star` from this Ramsey branch.
- No well-supported nearby `13C` conclusion.
- No supported claim that the physical Ramsey carrier is exactly `1.500 MHz`, `1.624 MHz`, or `1.692 MHz`.
- No supported assignment of the `0.8-0.9 MHz` components, low-frequency FFT/LS structure, or single sideband-like peaks to NV physics.

## Recommended next action

Do not run another blind Ramsey repeat on r03. Treat the r03 Ramsey evidence as still non-claim-grade under the current Ramsey protocol. The next project action should be a deliberate branch decision: either design a targeted protocol/control that tests Ramsey phase linearity and early-time baseline behavior before any T2star fit, or switch to an alternate validated protocol for a supported negative/unsupported r03 T2star/13C closeout under these conditions.
