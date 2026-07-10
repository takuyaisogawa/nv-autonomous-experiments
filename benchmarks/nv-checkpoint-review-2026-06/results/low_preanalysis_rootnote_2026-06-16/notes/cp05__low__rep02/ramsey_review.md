# Ramsey Review

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/advice.md`, `project/state.md`.
- New terminal Ramsey measurement: `measurement/m001.json` raw export, `measurement/m002.json` submitted recipe/metadata, `measurement/m003.json` completed bridge result, `measurement/m004.json` final run status, `measurement/m005.json` control state.
- Generated local analysis artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed `measurement/m001.json` as a 2-channel Ramsey trace with 41 tau points from 0.048 to 8.048 us in 0.200 us steps, 20 averages x 50000 repetitions.
- Computed signal/reference ratio and `(signal-reference)/mean` contrast, per-average drift summaries, odd/even snake-order consistency, a weighted damped-cosine fit to the ratio trace, and Hann-window FFT checks against the planned carrier and 13C sideband frequencies.
- Ran an additional Python scratch cross-check comparing FFT peaks in raw signal, raw reference, ratio, and contrast views.

## Plausible interpretation

- The measurement completed normally: bridge status is `completed`, run time 2026-05-14 05:51:56 to 09:28:25, no stop request, no bridge error code.
- The refreshed-center Ramsey now shows a credible detuning-following Ramsey carrier. The ratio fit gives frequency `1.5135 +/- 0.0152 MHz`, consistent with the programmed `det=1.5 MHz`; the main FFT bins around the carrier are 1.463 and 1.585 MHz, as expected from the 0.122 MHz FFT bin spacing.
- A descriptive T2star scale is now plausible: weighted ratio damped-cosine fit gives `T2star = 3.39 +/- 1.02 us`, amplitude `0.0466` in signal/reference ratio, residual RMS `0.0213`, reduced chi-square `2.33`. Treat this as claim-grade only for an approximate few-us dephasing scale, not high-precision T2star.
- Drift is present but not an obvious hard invalidation: signal mean changed 47.47 to 48.87 kcps from average 1 to 20, reference mean 45.45 to 44.03 kcps, ratio mean 1.0478 to 1.1151. The fitted ratio drift slope is small (`4.18e-4 per average`) relative to the Ramsey modulation, but odd/even ratio RMS `0.0275` is about 2x the median point SEM `0.0136`, so per-average consistency remains imperfect.
- The 13C evidence is not supported. The planned lower sideband near 1.115 MHz is weak in ratio/contrast FFT (`~0.006-0.007`, far below carrier `~0.146-0.162`). The upper sideband bin near 1.829 MHz has nonzero ratio/contrast power (`~0.100-0.111`) and remains in fit residuals, but it is not paired with a matching lower sideband and raw-channel FFTs show channel-dependent structure rather than a clean symmetric sideband model.

## Claims that are not yet supported

- Do not claim a nearby 13C coupling from this dataset.
- Do not claim a precise T2star beyond an approximate few-us scale; the fit uncertainty, reduced chi-square above 1, and odd/even mismatch argue against overprecision.
- Do not claim sideband-resolved coupling or nuclear-spin identification from the upper-side residual feature alone.
- Do not use this Ramsey result to revise the pODMR alignment conclusion; alignment remains supported by earlier r03 pODMR evidence, not by Ramsey alone.

## Recommended next action

- Stop blind repeat Ramsey accumulation. Record the refreshed-center Ramsey as supporting an approximate r03 T2star of about `3.4 us` under current conditions and as not supporting a nearby 13C claim.
- If a 13C conclusion is still required rather than an unsupported/negative conclusion, run a targeted follow-up protocol that tests the residual upper-side structure explicitly, such as a phase-cycled or alternate-readout Ramsey repeat centered on the same pODMR frequency with enough repeats to compare per-average sideband stability, or move to an echo/XY-style nuclear modulation check. The immediate project action should be to update the living state with this terminal review and decide whether the acceptable final conclusion is "no supported nearby 13C observed under current Ramsey conditions."
