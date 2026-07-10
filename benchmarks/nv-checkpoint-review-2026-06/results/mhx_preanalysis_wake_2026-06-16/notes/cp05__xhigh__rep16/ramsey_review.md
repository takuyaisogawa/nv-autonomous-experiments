# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New terminal Ramsey measurement: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` result, `measurement/m004.json` status, `measurement/m005.json` control snapshot.
- Planning context checked: `evidence/e014.json` and `evidence/e016.json` for the refreshed-center Ramsey intent and frequency targets.
- Generated locally: `analyze_ramsey.py`, `ramsey_analysis.json`, `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Verified raw axis contract: `ExperimentDataEachAvg` has shape `[1, 20, 2, 41]`; averaging over the 20 stored averages reproduces `ExperimentData` `[1, 2, 41]`.
- Confirmed readout roles from `ramsey.xml` embedded in the raw export: readout 1 is the true 0-level reference; `full_experiment=0` skips the optional 1-level reference; readout 2 is the Ramsey signal.
- Run health: completed, no stop request, no monitor error, `safety.aborted=false`, final count `43.433 kcps`.
- Scan: `tau = 0.048..8.048 us`, `41` points, `0.2 us` step, `mw_freq=3.8765 GHz`, `det=1.5 MHz`, `20 x 50000 = 1.0e6` shots per tau, Nyquist `2.5 MHz`, FFT bin spacing about `122 kHz`.
- Noise estimates from stored averages: median signal SEM `0.850 kcps`, median reference SEM `0.867 kcps`, median signal/reference SEM `0.0116`.
- Local drift/provenance summary: snake order; per-average mean signal ranged `37.38..50.37 kcps`, reference `41.74..54.90 kcps`, signal/reference mean `0.891..0.959`; second-half signal mean was `2.27 kcps` below first half. This is notable common-mode/normalization provenance, not a hard run anomaly.
- Least-squares frequency screens used constant+slope+sin+cos models from `0.25..2.40 MHz`; FFT checks used detrended Hann-window spectra.

## Plausible interpretation

- The data are analyzable, but they do not support a clean Ramsey carrier/sideband model.
- The strongest full-span LS component is off target near `2.27 MHz` in all combined views:
  - raw signal: `2.271 MHz`, amplitude `0.818 kcps`;
  - signal/reference: `2.270 MHz`, amplitude `0.01845`;
  - signal/reference-line: `2.271 MHz`, amplitude `0.01678`.
- Skipping the first four tau points does not move the top component to the target model; it remains near `2.27 MHz`, with reduced amplitudes.
- The programmed carrier at `1.5 MHz` is present only weakly/marginally:
  - raw amplitude `0.705 kcps`, below the median signal SEM (`0.83 x SEM`);
  - signal/reference amplitude `0.01575`, about `1.36 x` median ratio SEM;
  - signal/reference-line amplitude `0.01447`, about `1.25 x` median ratio SEM;
  - it is not the top normalized LS component (`rank 100` on the 1 kHz grid).
- FFT bins near the carrier (`1.463/1.585 MHz`) are visible, but comparable off-target power near `2.2..2.3 MHz` prevents a claim-grade carrier interpretation.
- The expected 13C sidebands are not supported:
  - low sideband `1.115 MHz`: ratio amplitude `0.00278` (`0.24 x` ratio SEM), raw amplitude `0.145 kcps` (`0.17 x` signal SEM);
  - high sideband `1.885 MHz`: ratio amplitude `0.00962` (`0.83 x` ratio SEM), raw amplitude `0.261 kcps` (`0.31 x` signal SEM);
  - per-average top-frequency support is weak: carrier `5/20`, low sideband `0/20`, high sideband `2/20` within one nominal FFT bin.

## Claims not yet supported

- No numerical T2star should be claimed from this run. A decay fit would be model-dependent because signal presence at the programmed carrier is not cleanly established.
- No nearby 13C coupling/sideband claim is supported.
- The `2.27 MHz` component should not be assigned to a physical resonance from this data alone; it is off the programmed carrier and expected sidebands and could be artifact, noise, or an unmodeled protocol effect.
- This run does not rescue the previous non-claim-grade Ramsey branch, despite the refreshed pODMR center and higher shot count.

## Recommended next action

Stop blind same-protocol Ramsey repeats on r03. Record that, under the current Ramsey conditions, r03 has a supported aligned pODMR resonance but still no supported T2star or 13C conclusion. If the project must continue toward a 13C/T2-family answer, switch to a deliberately different, model-checked protocol or diagnostic after a fresh frequency check, rather than accumulating another identical long-span Ramsey.
