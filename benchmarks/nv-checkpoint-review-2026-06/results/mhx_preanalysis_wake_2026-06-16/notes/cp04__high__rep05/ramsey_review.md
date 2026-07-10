# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New completed Ramsey data/metadata: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` status, `measurement/m005.json` control.
- Planning/prior comparison evidence: `evidence/e019.json` det-shift model plan and `evidence/e008.json` prior det=1.0 MHz short-tau terminal review.
- Generated local artifacts: `analyze_ramsey_detshift.py`, `ramsey_detshift_analysis.json`, `ramsey_detshift_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey_detshift.py`.
- Verified `ExperimentDataEachAvg` axis contract: averaging the `[avg, readout, point]` data reproduces `ExperimentData`.
- Checked acquisition metadata: completed run `nv23_ramsey_20260514_015423_auto_ramsey`, `tau=0.048..1.968 us`, `41` points, `48 ns` step, `det=1.5 MHz`, `mw_freq=3.8759 GHz`, `12 x 90000` repetitions, `1.08e6` shots/tau, final counts `44.796 kcps`, no stop request, no monitor error.
- Computed raw/reference/signal ratio views, fitted-reference-line normalization, per-point SEM, FFT bins, least-squares sinusoid screens, per-average frequency screens, and descriptive damped-sinusoid grid fits.
- Key data-quality numbers: median signal SEM `0.711 kcps`; median ratio SEM `0.0126`; early `tau<=0.75 us` signal peak-to-peak `6.46 kcps`; early ratio peak-to-peak `0.134`.
- Sampling limits: FFT bin spacing `0.508 MHz`, nominal `1/span` resolution `0.521 MHz`, Nyquist `10.42 MHz`; LS screens are more informative than raw FFT bin identity over this short window.

## Plausible interpretation

- The run is analyzable and is useful as a det-shift diagnostic, but it is still not claim-grade for a Ramsey carrier, T2star, or 13C model.
- The previous det=1.0 MHz short-tau top component near `1.192 MHz` did not remain dominant: its new ratio LS amplitude is only `0.0051`, down from `0.0363` in the prior review.
- The new point-wise ratio view has a broad top near `1.623 MHz` with ratio amplitude `0.0255`; the planned det-tracking carrier target `1.692 MHz` is close in amplitude (`0.0250`) and fit improvement, so the ratio view alone is compatible with partial det tracking.
- Raw signal and fitted-reference-line normalization disagree with that assignment: both are dominated near `0.882 MHz`/`0.884 MHz` with raw signal amplitude `~1.53 kcps` and normalized amplitude `~0.0319`. This reappears near the first det=1.5 MHz scout's empirical `0.884 MHz` component.
- Because the dominant frequency depends on readout treatment, the safest interpretation is a weak/ambiguous det-dependent Ramsey response mixed with short-tau baseline or protocol transient structure, not a clean physical carrier/sideband spectrum.

## Claims not yet supported

- No numeric T2star claim. Descriptive damped-grid fits prefer short/interior values (`ratio` best about `0.678 MHz`, `T2star ~0.47 us`; signal/ref-line best about `0.818 MHz`, `T2star ~0.72 us`), but these are model-dependent diagnostics under inconsistent frequency assignment.
- No nearby 13C claim. Programmed sidebands (`1.115/1.885 MHz`) and det-tracking sidebands (`1.307/2.077 MHz`) do not dominate consistently across raw, point-wise ratio, and fitted-reference-line views.
- No claim that the previous `~1.192 MHz` feature was a confirmed physical Ramsey carrier. This run argues against it being a fixed dominant component, but it does not establish a clean det-following replacement.
- No need to revise the accepted aligned-NV conclusion from this Ramsey analysis; the r03 alignment evidence still rests on prior pODMR results.

## Recommended next action

Stop blind Ramsey repeats on r03. Do a branch-level synthesis/closeout for r03 Ramsey/T2star/13C under current conditions. If more experimental evidence is still required, switch to a deliberately phase-controlled Ramsey diagnostic or an alternate T2/13C protocol rather than another same-grid accumulation.
