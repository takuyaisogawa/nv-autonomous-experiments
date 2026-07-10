# Ramsey Det-Shift Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/knowledge.md`, `md/memory.md`.
- New measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job plan, `measurement/m003.json` terminal result, `measurement/m004.json` status, `measurement/m005.json` control.
- Prior comparison: `evidence/e008.json` terminal short-tau det=1.0 MHz Ramsey review, plus project-state summaries of the earlier det=1.5 MHz scout and det=1.0 MHz 8 us follow-up.
- Scratch outputs created here: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_detshift_analysis.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey.py` locally.
- Verified raw-axis contract: `ExperimentDataEachAvg` is `[slice, average, readout, point]`; averaging the 12 averages reproduced `ExperimentData` with max error `1.42e-14`.
- Used the prior project readout assignment for `ramsey.xml full_experiment=0`: readout 1 is reference, readout 2 is Ramsey signal.
- Measurement grid: `tau = 0.048..1.968 us`, `41` points, `48 ns` step, nominal `1/span = 0.5208 MHz` and FFT bin spacing about `0.508 MHz`.
- Terminal run metadata: completed safely, `12 x 90000` repetitions, final counts `44.796 kcps`, no stop request.
- Combined signal stats: raw Ramsey signal mean `44.269 kcps`, tau-std `1.392 kcps`, point-to-point span `6.460 kcps`, median signal SEM `0.711 kcps`; ratio mean `0.92069`, tau-std `0.02842`, median ratio SEM `0.01262`.
- Frequency checks on signal/reference-line-normalized views used linear-baseline plus sinusoid least squares and FFT/detrended screens.
- Target ratio amplitudes:
  - Prior fixed component `1.192 MHz`: `0.00511`, weak.
  - Programmed det `1.500 MHz`: `0.02399`, delta-R2 `0.359`.
  - Det-tracking prediction from prior `~1.692 MHz`: `0.02505`, delta-R2 `0.411`.
  - Expected 13C sidebands `1.307/2.076 MHz`: `0.00949/0.00616`, weak.
- Raw-signal target amplitudes:
  - `1.500 MHz`: `1.128 kcps`.
  - `1.692 MHz`: `1.225 kcps`.
  - `1.192 MHz`: `0.474 kcps`.
- Per-average ratio frequency screens were mixed: top components included boundary/low-frequency behavior and scattered peaks near `0.863`, `0.887`, `1.166`, `1.523`, `1.676`, and `1.742 MHz`.
- Average-level common-mode variation remained visible: reference average means relative range `12.5%`, signal `16.4%`, ratio `6.9%`.

## Plausible interpretation

- The det=1.5 MHz short-tau diagnostic is terminal and analyzable.
- The prior det=1.0 MHz short-tau run had a strongest empirical component near `~1.19 MHz`. In the new det=1.5 MHz run, the fixed `1.192 MHz` target is weak in the ratio and raw-signal checks, while the programmed-carrier/det-tracking region around `1.5..1.7 MHz` is stronger. That argues against simply promoting a fixed `~1.19 MHz` artifact as the physical Ramsey frequency.
- The data still do not cleanly establish a physical Ramsey carrier. The strongest broad screen in normalized views is affected by short-window low-frequency/transient structure, and the `1.5 MHz` and `1.692 MHz` hypotheses are not well separated by the `~0.52 MHz` resolution of this 1.92 us span.
- The sideband checks do not support nearby 13C: expected `~1.307` and `~2.076 MHz` targets are weak compared with the carrier-region amplitudes and are not dominant in per-average screens.

## Claims not yet supported

- No claim-grade numeric `T2*` is supported from this run or the prior Ramsey set.
- No supported nearby-13C coupling conclusion is supported.
- Do not claim that the observed `1.5..1.7 MHz` response is definitely the programmed Ramsey carrier; it is plausible but still not cleanly resolved from transient/baseline behavior and per-average inconsistency.
- Do not claim that a damped-sinusoid fit gives a reliable `T2*`; the prerequisite carrier/decay-shape evidence is not yet met.

## Recommended next action

Stop doing blind Ramsey repeats on r03. Use the four Ramsey datasets as a branch-level synthesis: aligned NV r03 remains supported, but Ramsey/T2*/13C remains unsupported under the present short-tau Ramsey protocol. The next experimental action should change protocol rather than repeat the same measurement, e.g. run a Hahn-echo/CPMG `N=1` baseline or another non-Ramsey coherence diagnostic to separate real spin coherence from Ramsey transient/readout artifacts before attempting any further T2*/13C claim.
