# Ramsey Review: refreshed-center r03 long-span run

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`.
- New measurement files: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` status, `measurement/m005.json` control.
- Generated local artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_review_plot.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed Ramsey data as 20 averages x 2 readouts x 41 tau points. Tau span was 0.048 to 8.048 us in 0.200 us steps; total shots per tau point were 20 x 50000 = 1.0e6.
- Checked terminal health: job completed, final counts 43.433 kcps, no stop request, no monitor error. The result has 9 warnings, but they are bridge/provenance/cleanup warnings rather than a measurement abort.
- Checked common-mode per-average stability from readout means. No robust common-mode outliers were flagged.
- Reviewed raw signal, point-wise signal/reference, and signal/reference-polynomial normalization. Median SEM was about 0.0116 in ratio and 0.850 kcps in raw signal.
- Ran least-squares sinusoid screens from 0.25 to 2.30 MHz and an FFT cross-check. Target amplitudes were checked at the programmed carrier 1.500 MHz and expected 13C sidebands using the project model: B about 359.46 G from 3.8765 GHz, 13C Larmor about 0.3848 MHz, sidebands about 1.115 and 1.885 MHz.

## Plausible interpretation

- The measurement is analyzable and not obviously invalidated by counts, stop/error state, or common-mode drift.
- The strongest least-squares component in ratio, reference-corrected normalization, and raw signal is near 2.27 MHz, not at the programmed 1.5 MHz carrier or expected 13C sidebands. This remains true after skipping the first 4 or 8 tau points.
- The programmed 1.5 MHz carrier is present only modestly: ratio LS amplitude 0.0157, about 1.36x median point SEM; raw-signal amplitude 0.705 kcps, below the median raw SEM. Per-average phase coherence at the carrier is moderate (0.737), but the carrier is not the dominant combined screen.
- The expected 13C lower sideband near 1.115 MHz is weak and phase-incoherent; the upper sideband near 1.885 MHz is not dominant and has only moderate phase coherence. This does not support a nearby-13C claim.
- The run strengthens the pattern that r03 Ramsey data are real/analyzable but do not cleanly follow the intended carrier-plus-13C-sideband model under the tried conditions.

## Claims not yet supported

- No claim-grade numeric T2star is supported from this run.
- No supported nearby 13C coupling conclusion is supported from this run.
- The 2.27 MHz feature should not be promoted as physical without a targeted control, because it is not the programmed carrier/sideband expectation and sits close enough to the high-frequency end of the sampled band to require alias/sequence/systematic checks.
- Sub-grid microwave-frequency precision from the pODMR refresh is not supported; the Ramsey used the grid-supported 3.8765 GHz center only.

## Recommended next action

Stop doing blind repeats of the same Ramsey. Either run a targeted control that can disambiguate the 2.27 MHz feature from sequence/sampling/systematic structure, or switch protocol for T2star/13C support. A practical next control is a detuning-shift Ramsey at the same refreshed center and tau grid, chosen so a true Ramsey carrier should move predictably while a fixed 2.27 MHz systematic should not; include the same raw/readout-aware and per-average phase-coherence checks before fitting T2star.
