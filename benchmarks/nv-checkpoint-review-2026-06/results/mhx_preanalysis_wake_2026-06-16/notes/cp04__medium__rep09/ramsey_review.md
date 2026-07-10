# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New terminal Ramsey data and bridge metadata: `measurement/m001.json` through `measurement/m005.json`.
- Main raw data source: `measurement/m001.json`, savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
- Measurement contract/result: `auto__ramsey`, accepted r03, `mw_freq = 3.8759 GHz`, `det = 1.5 MHz`, `tau = 48 ns..1.968 us` in 41 points, `12 x 90000` repetitions, final counts `44.796 kcps`.

## Calculations or scripts run

- Used local Python/numpy to parse `ExperimentData` and `ExperimentDataEachAvg`.
- Verified per-average axis contract: averaging `ExperimentDataEachAvg` over the 12 averages reproduces `ExperimentData` with max absolute difference `1.42e-14`.
- Interpreted XML readout path with `full_experiment = 0`: readout 1 is the 0-level reference and readout 2 is the Ramsey signal.
- Computed raw signal/reference traces, point-wise `signal/reference`, and a reference-line-normalized signal.
- Computed per-point SEM across 12 stored averages: median reference SEM `0.745 kcps`, signal SEM `0.711 kcps`, ratio SEM `0.0126`.
- Ran least-squares sinusoid screens with constant+linear baseline terms over the diagnostic band, plus FFT checks after linear detrending.
- Saved scratch outputs: `ramsey_analysis_summary.json` and `ramsey_detshift_review.png`.

## Plausible interpretation

- The run completed safely: status completed, no stop requested, no bridge error, final counts above gate.
- The data show a large early-time signal rise: signal point 0 is `40.46 kcps` while the median after point 5 is `44.47 kcps`, a `4.00 kcps` change. This transient is a major caveat for any Ramsey fit.
- In the targeted diagnostic band, the combined normalized data favor a component near the det-shift prediction rather than the old artifact-control frequency:
  - Full-window ratio LS amplitudes: prior `1.192 MHz` = `0.0051`, programmed `1.500 MHz` = `0.0240`, det-tracking prediction `1.692 MHz` = `0.0250`.
  - Skipping first 5 points: prior `1.192 MHz` = `0.0089`, programmed `1.500 MHz` = `0.0182`, det-tracking prediction `1.692 MHz` = `0.0191`.
  - Detrended FFT has a strong bin near `1.736 MHz` after skipping first 5 points, consistent with the coarse FFT resolution for a `~1.69 MHz` component.
- Per-average phase consistency is meaningfully better at `1.5..1.692 MHz` than at `1.192 MHz` in the full-window fits, and remains better than the old-frequency control after skipping early points, although individual-average amplitudes still vary substantially.
- The det-shift diagnostic therefore weakly supports that the previous `~1.19 MHz` feature was related to the programmed Ramsey detuning/carrier response rather than a fixed-frequency artifact. It is still not clean enough by itself to promote a final T2star value.

## Claims not yet supported

- No well-supported numeric `T2star` claim from this run. The signal shape has a strong early transient, and the robust carrier evidence is not yet clean enough to justify a decay fit as a physical parameter.
- No supported nearby `13C` claim. The expected sidebands for this det-shift check, about `1.307 MHz` and `2.076 MHz`, are weaker and less consistent than the carrier-region response.
- No claim of sub-grid resonance precision beyond the prior fine weak-pi pODMR-supported `mw_freq = 3.8759 GHz`.
- No claim that all earlier Ramsey discrepancies are resolved. This run argues against a fixed `~1.192 MHz` artifact, but it does not establish a complete carrier/sideband model.

## Recommended next action

- Do not run another blind Ramsey repeat.
- Use this result as evidence that a Ramsey carrier can appear near the programmed detuning under the short-tau/high-SNR settings, then run a non-blind confirmation designed to suppress/diagnose the early-time transient before fitting `T2star`. Practical options are a phase-controlled Ramsey confirmation at the same short-tau grid, or an alternate T2 protocol such as Hahn/CPMG baseline if the goal is now a robust coherence number rather than carrier-debugging.
- Only fit and report `T2star` after raw/readout-aware carrier presence and a plausible decay envelope are established. Only assign `13C` after sidebands appear at the expected offsets with support in raw/normalized views and per-average consistency.
