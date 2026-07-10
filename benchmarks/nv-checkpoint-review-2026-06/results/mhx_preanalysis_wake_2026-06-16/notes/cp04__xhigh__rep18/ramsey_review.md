# Ramsey Review

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/advice.md`, `project/state.md`.
- New completed measurement: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control.
- Prior comparison: `evidence/e006.json` previous short-tau det=1.0 MHz raw export and `evidence/e008.json` previous short-tau terminal review.

## Calculations or scripts run

- Created and ran `analyze_ramsey_detshift.py`.
- Outputs: `ramsey_detshift_analysis.json` and `ramsey_detshift_analysis.png`.
- Verified the raw-export axis contract by checking that per-average readouts average back to `ExperimentData`.
- Checked run health and acquisition metadata: completed job `nv23_ramsey_20260514_015423_auto_ramsey`, final counts `44.796 kcps`, `12 x 90000` shots per tau point, monitor `last_error=""`, `stop_requested=false`.
- Recomputed the tau grid: `48 ns..1.968 us`, `41` points, `48 ns` step, Nyquist `10.42 MHz`, nominal `1/span` resolution `0.521 MHz`.
- Computed raw/reference/ratio summaries and per-point SEM: signal mean `44.269 kcps`, reference mean `48.084 kcps`, ratio mean `0.92069`, median signal SEM `0.711 kcps`, median ratio SEM `0.01262`.
- Ran a robust per-average mean drift proxy using reference, signal, and ratio means; no averages crossed the `|robust z| > 3.5` flag threshold. This is provenance only, not a replacement for the full lab drift tool.
- Ran linear-baseline least-squares sinusoid screens from `0.25..2.60 MHz` at `1 kHz` spacing for ratio, raw signal, and signal/fitted-reference-line views; also ran FFT checks and descriptive damped-sinusoid grid fits.

## Plausible interpretation

- The new det=1.5 MHz short-tau run is analyzable terminal evidence.
- The old fixed `1.192 MHz` component is not reproduced in the new combined ratio trace: new ratio LS amplitude at `1.192 MHz` is only `0.00511` with baseline-residual improvement `0.0167`.
- The new combined ratio screen is broad and peaks near `1.623 MHz` with amplitude `0.02547`. The programmed `1.500 MHz` target has ratio amplitude `0.02399`, and the predicted det-shifted empirical target `1.692 MHz` has ratio amplitude `0.02505`.
- Relative to the prior det=1.0 MHz top at `1.192 MHz`, the new ratio top shifted by `+0.431 MHz`, close to the programmed `+0.5 MHz` det change but smaller than the nominal `0.521 MHz` frequency resolution. Treat the apparent shift as suggestive, not precise.
- This weakly favors some detuning-sensitive Ramsey response over a perfectly fixed `1.192 MHz` artifact. It does not yet establish a clean physical carrier model because raw signal and signal/refline screens peak near `0.882 MHz`, the skip-early-time ratio screen shifts to about `0.746 MHz`, and per-average top frequencies scatter.

## Claims not yet supported

- No claim-grade numeric T2star. Descriptive damped-grid fits are readout/window dependent: ratio fit preferred about `0.674 MHz` / `0.461 us`, while signal/refline fits preferred about `0.82 MHz` / `0.739 us`.
- No nearby 13C conclusion. Programmed-det sideband amplitudes were not dominant (`1.115 MHz`: ratio amp `0.01076`; `1.885 MHz`: `0.01732`), and shifted-empirical sidebands were weaker (`1.307 MHz`: `0.00953`; `2.077 MHz`: `0.00614`).
- No clean programmed-carrier or det-shifted-carrier conclusion. The `1.500` and `1.692 MHz` ratio targets are comparable and broad, and the other readout views do not agree.
- The aligned-r03 conclusion remains supported by prior pODMR context; this Ramsey run does not invalidate the target, but it also does not finish the T2star/13C objective.

## Recommended next action

Do not run another blind Ramsey repeat. Make a branch decision: either close the r03 Ramsey/T2star/13C result as unsupported under the current Ramsey protocol, or switch to an alternate phase/readout-aware protocol specifically designed to resolve the carrier and possible 13C sidebands before attempting any T2star extraction.
