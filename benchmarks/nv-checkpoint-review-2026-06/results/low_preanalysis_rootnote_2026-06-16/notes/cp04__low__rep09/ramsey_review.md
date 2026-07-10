# Ramsey Review

## Files/Data Used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New terminal Ramsey data: `measurement/m001.json` raw export for `nv23_ramsey_20260514_015423_auto_ramsey`; `measurement/m002.json` job spec; `measurement/m003.json` result; `measurement/m004.json` status; `measurement/m005.json` control.
- Prior comparison context: `evidence/e008.json` terminal review of the previous det=1.0 MHz short-tau Ramsey; `evidence/e019.json` det-shift plan/model.
- Local outputs created: `ramsey_detshift_analysis.json` and `ramsey_detshift_review.png`.

## Calculations/Scripts Run

- Ran a local Python analysis from the working directory using only the neutral snapshot files.
- Verified raw axis contract: `ExperimentDataEachAvg` has shape `[12, 2, 41]`, interpreted as `[avg, readout, point]`; averaging each readout over averages reproduces `ExperimentData`.
- Checked run metadata: completed, `12 x 90000` repetitions, `1,080,000` shots per tau point, `tau = 0.048..1.968 us` in `0.048 us` steps, `mw_freq = 3.8759 GHz`, `det = 1.5 MHz`, final counts `44.796 kcps`, no monitor error, `stop_requested=false`.
- Computed raw/reference/ratio traces, per-point SEM, linear-detrended residuals, FFT amplitudes, and least-squares sinusoid screens over `0.25..2.35 MHz`.
- Compared targeted frequencies:
  - programmed carrier `1.500 MHz`
  - det-tracking hypothesis from prior `~1.192 MHz + 0.500 MHz = 1.692 MHz`
  - prior empirical feature `1.192 MHz`
  - expected 13C sidebands for det=1.5 MHz: `1.115 MHz` and `1.885 MHz`
- Ran a descriptive damped-sinusoid grid fit as a diagnostic only.

## Quantitative Checks

- Median signal SEM: `0.711 kcps`; median ratio SEM: `0.0126`.
- Early `tau <= 0.75 us` transient remains large: signal peak-to-peak `6.46 kcps`, ratio peak-to-peak `0.134`.
- Combined ratio LS screen top is near `1.623 MHz` with ratio amplitude `0.0255` and raw-signal amplitude `1.25 kcps`.
- Target amplitudes in ratio view:
  - `1.500 MHz`: `0.0240` ratio amplitude, `1.13 kcps` raw-signal amplitude.
  - `1.692 MHz`: `0.0250` ratio amplitude, `1.22 kcps` raw-signal amplitude.
  - old `1.192 MHz`: `0.00511` ratio amplitude, `0.474 kcps` raw-signal amplitude.
  - `1.115 MHz` sideband: `0.0108` ratio amplitude.
  - `1.885 MHz` sideband: `0.0173` ratio amplitude.
- FFT bin spacing is `0.508 MHz`, so FFT alone cannot cleanly distinguish `1.5`, `1.62`, and `1.692 MHz`.
- Per-average top-frequency screens are inconsistent (`0.25`, `0.79`, `0.87`, `0.89`, `1.20`, `1.54`, `1.66`, `1.71`, `1.75`, `1.94 MHz` among the 12 averages), although several averages have non-negligible amplitudes near `1.5..1.7 MHz`.
- Descriptive damped-grid fit in ratio view prefers `0.686 MHz`, `T2* ~0.487 us`, but this fit is dominated by the early transient/model choice and is not promoted.

## Plausible Interpretation

- The det-shift run is clean enough to use as evidence: it completed normally and the raw export is internally consistent.
- The old `~1.192 MHz` component is strongly suppressed in the new det=1.5 MHz run, so a fixed analysis artifact exactly at `1.192 MHz` is not favored.
- The dominant combined component is closer to the programmed/det-shifted range (`1.5..1.7 MHz`) than to the old feature. This is qualitatively compatible with some det-dependent Ramsey response, but the data do not cleanly isolate the programmed carrier from the det-tracking prediction because the window is short and the strongest LS peak is broad around `~1.62 MHz`.
- The large early-time transient and inconsistent per-average frequency screens remain the main limitation.

## Claims Not Yet Supported

- No well-supported numeric `T2*` claim from this Ramsey run.
- No supported nearby `13C` claim: expected sidebands at `1.115` and `1.885 MHz` are not dominant or repeatable enough.
- Do not claim that the prior `~1.192 MHz` feature has cleanly tracked by exactly `+0.5 MHz`; the new evidence only says the old fixed component is weak and the combined response is now in the programmed/det-shifted frequency neighborhood.
- Do not treat the descriptive damped-sinusoid `T2* ~0.49 us` as physical without an analysis/protocol that separates the early transient from a real Ramsey envelope.

## Recommended Next Action

Stop blind Ramsey repeats on this branch. Do a bridge-free synthesis of all r03 Ramsey datasets and decide between:

1. closing the r03 Ramsey/13C result as unsupported under the current Ramsey protocol, while preserving the aligned-NV finding; or
2. switching to a targeted alternate protocol or analysis design that specifically suppresses/diagnoses the early transient before attempting a T2*/13C claim.

If further hardware time is used, it should not be another same-grid Ramsey repeat; it should be a targeted diagnostic designed around the early-time transient and the broad `1.5..1.7 MHz` det-dependent response.
