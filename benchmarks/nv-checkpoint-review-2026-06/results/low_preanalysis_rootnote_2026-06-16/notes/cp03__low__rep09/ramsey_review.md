# Ramsey Review: short-tau r03 diagnostic

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json`.
- New Ramsey run metadata/data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control.
- Prior/local evidence context: `evidence/e001.json` through `evidence/e017.md`, mainly the previous det=1.0 MHz 8 us Ramsey terminal review and the short-tau design/start note.
- Generated local artifacts: `ramsey_shorttau_analysis_summary.json` and `ramsey_shorttau_analysis.png`.

## Calculations or scripts run

- Ran local Python inspection of `measurement/m001.json`.
- Extracted two readout traces from `ExperimentData` and 12 stored averages from `ExperimentDataEachAvg`; treated trace 1 as reference and trace 2 as Ramsey signal, while checking raw signal independently.
- Constructed the tau grid from export metadata: 41 points from 0.048 us to 1.968 us, 48 ns spacing.
- Computed raw signal and signal/reference mean traces, per-point SEM across 12 averages, simple common-mode average brightness by stored average, FFT screens after linear detrending/Hann windowing, and least-squares sinusoid screens with linear baseline.
- Checked target frequencies: programmed carrier 1.000 MHz and expected 13C sidebands near 0.616 MHz and 1.384 MHz, plus prior off-target features near 0.884 MHz and 1.178 MHz.
- Tried a descriptive fixed-1 MHz decaying-cosine fit to raw signal only after the signal screens; this is not used as a claim-grade T2star result.

Key numerical results:

- Acquisition completed safely as `nv23_ramsey_20260513_230331_auto_ramsey`; final counts were 35.122 kcps.
- Raw signal median SEM across averages: 1.14 kcps. Ratio median SEM: 0.0127.
- Raw signal range over tau: 6.50 kcps. Ratio range: 0.143.
- Least-squares raw-signal amplitudes: 1.000 MHz = 1.28 kcps, 0.616 MHz = 1.10 kcps, 1.384 MHz = 1.22 kcps, 1.178 MHz = 1.68 kcps.
- Ratio amplitudes: 1.000 MHz = 0.0274, 0.616 MHz = 0.0242, 1.384 MHz = 0.0272, 1.178 MHz = 0.0362.
- FFT peaks after linear detrending put the largest raw/ratio bins at 1.524 MHz, then 1.016 MHz and 0.508 MHz; the coarse bin spacing is about 0.508 MHz over this short window.
- Per-average LS scans were not consistent: most stored averages favored the low-frequency edge of the 0.3-4 MHz scan rather than a stable 1 MHz carrier.
- Simple stored-average common-mode brightness varied substantially, from 39.75 to 53.20 kcps, with first-to-last change about -4.6%. This is provenance for baseline instability, not by itself a hard invalidation.
- Descriptive fixed-1 MHz raw fit returned amplitude 7.94 +/- 4.96 kcps and T about 0.188 +/- 0.117 us with R2 about 0.63; uncertainty is too large and the fit is too model-dependent to promote.

## Plausible interpretation

- The short-tau/high-SNR diagnostic shows real early-time structure and possibly a very fast loss of contrast, but it still does not provide a clean, claim-grade programmed Ramsey carrier.
- The 1.0 MHz target component is only about 1.1x the raw per-point SEM, and the expected 13C sideband checks are comparable rather than distinct.
- The strongest non-low-frequency targeted screen remains closer to the prior off-target region around 1.18 MHz than to a clean det-following 1.0 MHz carrier/13C-sideband model.
- A very short T2star, baseline curvature, reference/common-mode variation, or sequence/readout artifact could plausibly explain the observed shape. The present data do not distinguish those possibilities cleanly.
- This run makes the "just repeat Ramsey with higher short-tau SNR" path less attractive: even with 1.08e6 shots per tau point, the target carrier/sideband model remains weak and unstable.

## Claims not yet supported

- No supported numeric T2star value should be claimed from this run.
- No supported nearby-13C conclusion should be claimed from this run.
- The 1.178 MHz feature should not be assigned to a physical coupling or resonance without a det-shift-following or otherwise protocol-specific confirmation.
- The fixed-1 MHz decaying-cosine fit should not be used downstream as a quantitative T2star measurement.
- The current evidence does not prove r03 lacks 13C coupling; it only says the three Ramsey datasets so far do not support a clean T2star/13C Ramsey claim under these conditions.

## Recommended next action

Do not run another blind Ramsey repeat on r03. The next useful action is a protocol change or branch decision: run a non-Ramsey coherence baseline such as Hahn/CPMG N=1 on the same accepted r03 to test whether electron coherence is measurable under a more robust refocusing protocol, or close the r03 Ramsey/13C branch as unsupported under current Ramsey conditions. If continuing with r03, first verify current tracking/counts and consider a fresh weak-pi pODMR check only if enough time/drift has elapsed to make the 3.8759 GHz center stale.
