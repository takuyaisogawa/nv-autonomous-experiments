# Ramsey Review: det=1.5 MHz Short-Tau Shift Check

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New Ramsey run: `measurement/m001.json` raw export for `nv23_ramsey_20260514_015423_auto_ramsey`, `measurement/m002.json` submit/job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control.
- Prior comparison context: `evidence/e008.json` terminal det=1.0 MHz short-tau Ramsey review and project-state summaries of earlier Ramsey attempts.

## Calculations or scripts run

- Created and ran `analyze_ramsey_m001.py`.
- Outputs: `ramsey_m001_analysis.json` and `ramsey_m001_diagnostic.png`.
- Verified raw-export axis contract: `ExperimentDataEachAvg` averaged over the stored-average axis reproduces `ExperimentData` with max absolute difference `1.42e-14`.
- Measurement grid: tau `0.048..1.968 us`, step `0.048 us`, 41 points, 12 averages x 90000 repetitions = `1.08e6` shots per tau point.
- Noise/variation scale: median signal SEM `0.711 kcps`; median ratio SEM `0.0126`; signal mean `44.27 kcps`; ratio mean `0.9207`.
- Frequency checks used linear-baseline + sinusoid least squares and detrended FFT. FFT bin spacing is coarse at `0.508 MHz`, so LS screens are more informative than exact FFT-bin labels.
- Target LS ratio amplitudes:
  - programmed carrier `1.5 MHz`: amplitude `0.0240`, baseline R2 improvement `0.359`, signal amplitude `1.13 kcps`.
  - prior fixed-artifact control `1.192 MHz`: amplitude `0.0051`, R2 improvement `0.0167`, signal amplitude `0.474 kcps`.
  - prior component shifted by det change, `1.692 MHz`: amplitude `0.0250`, R2 improvement `0.411`, signal amplitude `1.22 kcps`.
  - programmed 13C sidebands `1.115/1.885 MHz`: ratio amplitudes `0.0108/0.0173`.
  - shifted-carrier 13C sidebands `1.307/2.077 MHz`: ratio amplitudes `0.0095/0.0061`.
- All-tau ratio frequency screen peaked near `1.624 MHz` with amplitude `0.0255` and R2 improvement `0.430`. Skipping `tau <= 0.2 us` moved the best screen to about `0.746 MHz`, showing the model is still sensitive to early-time structure/baseline choices.
- Per-average best-frequency screens are inconsistent (`~0.79..1.94 MHz`), so stored-average repeatability is not claim-grade.

## Plausible interpretation

- The det-shift diagnostic argues against the previous `~1.192 MHz` component being a purely fixed-frequency artifact: the fixed `1.192 MHz` check is weak in the new det=1.5 MHz data, while components near the expected shifted region (`~1.5..1.7 MHz`) are much stronger.
- The result is plausibly Ramsey-like phase evolution tied to the programmed detuning or sequence timing, but it is not clean enough to promote a precise carrier frequency. The strongest all-tau LS component (`~1.624 MHz`) sits between the programmed `1.5 MHz` carrier and the prior-component-plus-0.5-MHz target (`1.692 MHz`), and the FFT resolution is too coarse to arbitrate.
- No supported nearby 13C signature is visible. The expected sideband checks are weaker than the carrier-region checks and not repeatable across analysis choices.
- A numeric T2star is still not supported. This run was intentionally short-tau; the apparent oscillation is only modestly above per-point SEM, early-time/baseline sensitivity is material, and per-average frequency screens disagree.

## Claims not yet supported

- A well-supported T2star value for `image145844_reimage_r03`.
- A well-supported nearby 13C coupling or sideband assignment.
- A precise Ramsey carrier frequency or a physical explanation for the carrier offset from the programmed `1.5 MHz`.
- That the det-dependent feature is free of pulse-sequence timing, IQ/mixer, fitting-window, or baseline-analysis artifacts.

## Recommended next action

- Do not run another blind Ramsey repeat.
- Before more acquisition, inspect/reconcile the Ramsey timing/phase model against the active `ramsey.xml`/function semantics and the observed det-dependent frequency shift. Specifically check whether the phase ramp, finite pulse timing, `delay_wrt_1mus`, or readout/tau definition predicts an apparent frequency between the programmed det and the empirical shifted component.
- If the model can make a concrete prediction, run a compact non-blind det-calibration Ramsey/control at the same short-tau grid using at least two deliberately separated detunings, with success defined by a precomputed frequency-tracking slope and raw/readout-aware amplitude above SEM. Only after the carrier model is supported should T2star/13C be pursued with a longer or sideband-resolving scan.
