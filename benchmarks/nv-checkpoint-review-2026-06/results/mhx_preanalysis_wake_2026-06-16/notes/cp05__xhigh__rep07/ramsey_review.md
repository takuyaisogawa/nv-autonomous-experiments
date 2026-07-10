# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`, `md/knowledge.md`.
- Measurement/design context: `evidence/e014.json` for the intended refreshed-center Ramsey targets.
- New terminal measurement files: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` submitted job, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` run control.
- Scratch outputs created here: `ramsey_analysis_summary.json` and `ramsey_diagnostics.png`.

## Calculations or scripts run

- Ran local Python/NumPy/Matplotlib analysis from the exported JSON.
- Verified axis contract: `ExperimentDataEachAvg` averages reproduce `ExperimentData` for both readouts.
- Confirmed Ramsey XML readout roles from `measurement/m001.json`: channel 0 is the true mS=0 reference, channel 1 is the Ramsey signal.
- Built tau axis: 48 ns to 8.048 us, 41 points, 0.2 us step; Nyquist 2.5 MHz, nominal frequency resolution 125 kHz.
- Checked terminal health: job completed, final counts 43.433 kcps, safe shutdown true, no stop request, monitor `last_error` empty.
- Reproduced a local scan-order-aware drift check using snake-order, normalized common-mode brightness. No averages exceeded the 0.15 drop threshold; max drift score was 0.117.
- Reviewed raw signal, signal/reference, and signal/fitted-reference-line views; median per-point SEM was 0.850 kcps for raw signal and 0.0116 for signal/reference.
- Ran FFT and linear least-squares sinusoid screens on full-span and skip-first-4-tau windows.
- Checked target frequencies: programmed carrier 1.5 MHz, expected 13C sidebands 1.115 and 1.885 MHz, prior det-shift top 1.623 MHz, prior skip/transient 0.746 MHz, old 1.192 MHz control.

## Plausible interpretation

- The refreshed-center long-span run is analyzable and healthy.
- Compared with prior Ramsey branches, this is stronger evidence for a real carrier-like Ramsey component near the programmed detuning. In signal/reference, the full-span LS screen has a local top near 1.516 MHz with amplitude 0.0162, and skip-first-4 has a local top near 1.515 MHz with amplitude 0.0125. Targeted carrier fits give ratio amplitudes 0.0157 full-span and 0.0123 after skipping the first 4 tau points; raw-signal amplitudes are about 0.705 kcps and 0.512 kcps.
- FFT checks are consistent with carrier-region power: skip-first-4 signal/reference FFT has its largest bin near 1.486 MHz, with nearby 1.622 and 1.892 MHz bins also present.
- The old fixed 1.192 MHz control is weak in this run: ratio LS amplitude about 0.0019 in both full and skip-first-4 windows.
- There is also an unexplained high-frequency component near 2.27 MHz that is often the largest LS-screen component. This, plus the large first-point excursion, keeps the interpretation cautious.

## Claims that are not yet supported

- Do not claim a final T2star. Descriptive damped fits are skip-window and normalization sensitive: carrier-fixed/free fits move between roughly 1.5 and 2.27 MHz and give T2star values of order 2-6 us depending on which early points and normalization are used.
- Do not claim nearby 13C coupling. The low sideband at 1.115 MHz is weak or absent, especially after skipping the first 4 tau points. The high sideband region has some full-span power but is not paired with a stable low sideband and is not robust enough for a 13C conclusion.
- Do not claim the 2.27 MHz component is physical. It is a reproducible screen feature in this analysis, but it is not tied to the planned carrier/13C model.
- Do not treat per-average screens as settled: only 5/20 per-average signal/reference top frequencies fall in the 1.2-1.8 MHz carrier band in either full-span or skip-first-4 views, while many per-average tops remain low-frequency or high-frequency.

## Recommended next action

Do not run another blind Ramsey repeat. The next useful step is a targeted confirmation designed to separate the programmed 1.5 MHz carrier from the early-time transient and the unexplained 2.27 MHz component, preferably by validating an alternate/phase-cycled or det-sign/frequency-shift Ramsey check if available. If no such protocol is available under the current bridge constraints, record the present supported conclusion as: r03 has analyzable refreshed-center Ramsey data with carrier-like evidence near 1.5 MHz, but T2star and 13C remain unsupported under current conditions.
