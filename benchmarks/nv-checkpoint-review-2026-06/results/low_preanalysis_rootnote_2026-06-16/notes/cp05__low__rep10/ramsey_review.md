# Ramsey review

## Files/data used

- `project/brief.md`, `project/advice.md`, and `project/state.md` for objective and prior context.
- `measurement/m001.json`: terminal raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- `measurement/m002.json`: submitted Ramsey job spec.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal result/status/control metadata.
- Generated local scratch outputs: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_overview.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed two readout channels from `ExperimentData` and `ExperimentDataEachAvg`.
- Checked run geometry: `tau = 0.048..8.048 us`, 41 points, `det = 1.5 MHz`, `mw_freq = 3.8765 GHz`, `20 x 50000` shots.
- Calculated raw signal, raw reference, point-wise signal/reference, and a fitted-reference-line residual view.
- Ran detrended least-squares sinusoid amplitude screens over `0.15..2.45 MHz`, with full span and skip-first-4-point variants.
- Checked programmed/expected targets: `1.5 MHz` carrier, `1.115/1.885 MHz` 13C sidebands, prior `1.623 MHz` det-shift top, and prior `1.192 MHz` short-tau feature.
- Fit a descriptive damped cosine to raw signal only as a diagnostic; not used for a claim.

## Quantitative checks

- Terminal health: job completed, no `error_code` or `error_message`, `safe_shutdown_ok = True`, `stop_requested = False`.
- Combined readouts: signal mean `48.789 kcps`, reference mean `44.670 kcps`; point scatter across tau was `0.423 kcps` signal and `1.047 kcps` reference.
- Mean SEM across averages was about `0.862 kcps` for signal, `0.834 kcps` for reference, and `0.0140` for signal/reference ratio. Per-average means were broad (`41.739..54.899 kcps` signal, `37.377..50.371 kcps` reference), so average-to-average common-mode variation remains significant.
- Raw-signal LS screen top was near `0.806 MHz` with amplitude `0.306 kcps`; skip-first-4 top stayed near `0.800 MHz` with amplitude `0.337 kcps`.
- Raw-signal target amplitudes were weak: `1.5 MHz` carrier `0.0987 kcps` (`R2 = 0.027`), lower 13C sideband `1.115 MHz` `0.0180 kcps` (`R2 = 0.001`), upper 13C sideband `1.885 MHz` `0.232 kcps` (`R2 = 0.156`).
- Ratio screen top was near `2.270 MHz`, while the ratio carrier at `1.5 MHz` was `0.0191` (`R2 = 0.249`). This is not corroborated by the raw-signal view and is close to the average ratio SEM scale.
- Fitted-reference residual view top matched the raw-signal low-frequency top near `0.806 MHz`; carrier residual was only `0.00202` fractional amplitude.
- Per-average raw-signal top frequencies were scattered across the search band. A few averages landed near target-like positions, but not consistently enough to support a carrier or sideband model.
- Descriptive raw damped-cosine fit returned amplitude `0.143 kcps`, frequency `1.439 MHz`, `T2star = 50 us` at the imposed upper bound, and poor `R2 = 0.051`; this is a failed/unsupported T2star fit, not a measurement result.

## Plausible interpretation

The measurement is operationally valid and analyzable, but it does not provide claim-grade Ramsey physics. The expected `1.5 MHz` Ramsey carrier is weak in raw signal and fitted-reference views, and the target 13C sidebands are not consistently supported across readout views or stored averages. The strongest raw feature near `0.8 MHz` is not the programmed detuning or expected sideband position. The ratio view shows structure near the carrier and a top near `2.27 MHz`, but without raw-signal corroboration and with strong average-to-average baseline variation, it is not enough to promote a T2star or 13C conclusion.

This refreshed-center high-shot long-span run therefore continues the pattern from the previous r03 Ramsey datasets: the accepted NV and pODMR resonance are real, but the Ramsey contrast/carrier model remains non-claim-grade under these conditions.

## Claims not yet supported

- No numeric T2star should be claimed from this dataset.
- No nearby 13C coupling or absence of 13C should be claimed from this dataset alone.
- The `0.806 MHz`, `2.27 MHz`, or descriptive `1.439 MHz` features should not be promoted as physical Ramsey frequencies without a cleaner detuning-tracking or phase-consistent follow-up.
- The weak ratio carrier at `1.5 MHz` is not sufficient as a standalone carrier detection because it is not raw/readout-consistent.

## Recommended next action

Do not run another blind long-span Ramsey repeat on r03. The next decision should be either:

1. switch to an alternate protocol/readout strategy that can test whether Ramsey contrast is being washed out by pulse/readout/reference effects, or
2. write a supported interim conclusion for r03: aligned NV found, but T2star and 13C remain unsupported/non-claim-grade under the completed Ramsey conditions.

If continuing experimentally, first do a targeted diagnostic rather than another accumulation run: e.g. a phase-cycled or quadrature Ramsey implementation if available, or a deliberately changed detuning/frequency check with predefined promotion criteria requiring raw signal, normalization, and per-average consistency.
