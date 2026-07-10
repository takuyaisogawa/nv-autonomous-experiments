# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`.
- New completed Ramsey run:
  - raw export: `measurement/m001.json`
  - job spec: `measurement/m002.json`
  - terminal result: `measurement/m003.json`
  - terminal status: `measurement/m004.json`
  - control stub: `measurement/m005.json`
- Prior context from `project/state.md`: accepted target is `image145844_reimage_r03`; fine weak-pi pODMR supports `mw_freq = 3.8759 GHz`; previous short-tau det=1.0 MHz Ramsey had strongest empirical ratio-screen component near `1.192 MHz` but no supported T2star/13C claim.

## Calculations or scripts run

- Created and ran `analyze_ramsey_detshift.py`.
- Output written to `ramsey_detshift_analysis.json`.
- Checks performed:
  - Verified raw array axis contract: `ExperimentData` shape `(1, 2, 41)`, `ExperimentDataEachAvg` shape `(1, 12, 2, 41)`, and averaging the 12 per-average curves reproduces the combined reference/signal curves.
  - Confirmed run parameters: `tau = 0.048..1.968 us`, 41 points, `dt = 48 ns`, Nyquist `10.42 MHz`, FFT bin spacing `0.508 MHz`, `12 x 90000 = 1.08e6` shots per tau point, `det = 1.5 MHz`, `mw_freq = 3.8759 GHz`.
  - Checked terminal health: completed, final counts `44.796 kcps`, monitor `last_error` empty, `stop_requested=false`, scan order `snake`, data saved in tau order.
  - Computed raw signal/reference, point-wise signal/reference ratio, signal over fitted reference line, per-point SEM, FFT-nearest amplitudes, sinusoid least-squares screens, skip-first/skip-early-tau screens, and descriptive damped-sinusoid grid fits.

## Plausible interpretation

- The new det=1.5 MHz shift-check is analyzable and high-SNR enough for a meaningful diagnostic. Median SEM is about `0.711 kcps` in the raw signal and `0.0126` in the point-wise ratio.
- There is still a large early-time structure: first `0.75 us` peak-to-peak is `6.46 kcps` in raw signal and `0.134` in ratio, well above SEM.
- The prior fixed `~1.192 MHz` feature is not dominant in the new point-wise ratio screen. Its all-tau ratio LS amplitude is only `0.00511`, compared with `0.02399` at the programmed `1.5 MHz` and `0.02505` at the det-tracking prediction `1.692 MHz`.
- The all-tau point-wise ratio screen peaks near `1.623 MHz`, and skip-first-point peaks near `1.650 MHz`, qualitatively in the direction expected if the prior `~1.192 MHz` component partly tracked the `+0.5 MHz` det shift.
- However, the readout-aware views disagree: raw signal and signal/fitted-reference-line screens peak near `0.882 MHz`, not near `1.5-1.7 MHz`. The skip-early-tau ratio screen also moves to about `0.746 MHz`.
- Per-average top frequencies are inconsistent (`0.25..1.94 MHz` range), so the stored averages do not provide strong repeatability support for a single physical carrier.
- Descriptive damped-sinusoid fits prefer short apparent decay values (`~0.47 us` ratio view, `~0.72 us` raw-signal view) at frequencies below the programmed carrier, but these fits are model-dependent diagnostics of the transient, not supported T2star extractions.

## Claims that are not yet supported

- A numeric T2star for r03 is not supported by this Ramsey run.
- Nearby 13C coupling is not supported. The expected det=1.5 MHz sidebands near `1.115 MHz` and `1.885 MHz` are not dominant or readout-consistent.
- The point-wise ratio component near `1.62-1.65 MHz` should not be claimed as the physical Ramsey carrier because raw signal and fitted-reference normalization do not agree.
- The previous `~1.19 MHz` component should not be promoted as either a fixed artifact or a physical carrier from this run alone; the result argues against a simple fixed-frequency ratio artifact, but the readout dependence still prevents a clean model.

## Recommended next action

Do not run another blind same-style Ramsey repeat. Make a bridge-free branch decision from all Ramsey datasets: either move to an alternate protocol better suited to extracting T2/13C under these conditions, or close the r03 Ramsey/T2star/13C branch as unsupported under the current Ramsey protocol. If any further experiment is chosen, it should be explicitly targeted at resolving the readout-dependent transient, not just accumulating more Ramsey averages.
