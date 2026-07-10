# Ramsey Review

## Files/data used

- `project/state.md`, `project/brief.md`, `project/advice.md`, and `md/memory.md` for project context and prior Ramsey interpretation rules.
- `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- `measurement/m002.json`: submitted Ramsey configuration for `nv23_ramsey_20260514_055148_auto_ramsey`.
- `measurement/m003.json`: terminal bridge result.
- `measurement/m004.json` and `measurement/m005.json`: terminal status/control snapshots.

## Calculations or scripts run

- Created and ran `analysis_ramsey.py`.
- Outputs: `ramsey_analysis_summary.json` and `ramsey_analysis.png`.
- Checked raw shapes: `ExperimentData` is `1 x 2 x 41`; `ExperimentDataEachAvg` is `1 x 20 x 2 x 41`.
- Confirmed acquisition: `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`, `tau = 48 ns..8.048 us`, `41` points, `20 x 50000` shots, `1.0e6` shots/tau, snake scan order.
- Terminal health: status completed, state completed, final counts `43.433 kcps`, safe shutdown true, no abort, no stop request, monitor error empty.
- Ran least-squares sinusoid checks with offset and linear baseline at predefined targets:
  - carrier `1.500 MHz`
  - expected 13C sidebands `1.115 MHz` and `1.885 MHz`
  - prior diagnostic/control frequencies `1.192 MHz`, `1.623 MHz`, and `0.746 MHz`
- Ran dense empirical frequency screens over `0.2..2.4 MHz`, skip-first-4-point screens, FFT checks, per-average top-frequency screens, and average-to-average brightness checks.

## Plausible interpretation

- The refreshed high-shot Ramsey is usable and terminally healthy, but still not claim-grade for T2star or 13C.
- The programmed `1.5 MHz` carrier is the strongest predefined target:
  - raw signal LS amplitude `0.713 kcps`, about `0.84 x` the median per-point SEM and `0.87 x` the empirical full-span top amplitude.
  - point-wise signal/reference LS amplitude `0.0148`, about `1.27 x` median per-point SEM and `0.80 x` the empirical full-span top amplitude.
  - signal/reference-line LS amplitude `0.0159`, about `0.84 x` median per-point SEM and `0.86 x` the empirical full-span top amplitude.
- The largest empirical full-span component is instead near `2.27 MHz` in raw and normalized views; FFT top bins are near `2.317 MHz` for raw/reference-line and `1.463 MHz` for point-wise ratio. The FFT bin spacing is about `122 kHz`, so these are screening checks, not precise fitted frequencies.
- Skipping the first 4 tau points does not rescue a clean model: the screen top remains near `2.27 MHz`, while the `1.5 MHz` carrier remains the strongest predefined target but not the empirical maximum.
- Per-average top-frequency screens are mixed. In the point-wise ratio view only `5/20` averages have top frequencies within `125 kHz` of `1.5 MHz` and `6/20` within `250 kHz`; raw/reference-line support is similarly not dominant.
- The 13C sideband targets are weaker than the carrier and not mutually consistent:
  - `1.115 MHz` is very weak in all views.
  - `1.885 MHz` is present at a smaller amplitude than the carrier but lacks per-average consistency and does not form a supported sideband pair.
- Average-to-average brightness varies substantially (`common-mode relative range 0.851..1.132`), but the simple robust common-mode check did not flag individual averages. Treat this as provenance/instability, not by itself a hard terminal anomaly.

## Claims not yet supported

- No well-supported numeric T2star should be claimed from this run.
- No nearby 13C coupling claim should be made from this run.
- The `~2.27 MHz` empirical component should not be promoted as a physical frequency without an independent control; it is strongest in the screen but is not the programmed carrier or expected 13C sideband.
- The visible `1.5 MHz` carrier-like response is not sufficient by itself for a decay/T2star claim because it is below or near per-point SEM scale in the raw/reference-line views and does not dominate per-average frequency screens.

## Recommended next action

Do not run another blind Ramsey repeat on r03. Record that the refreshed-center high-shot Ramsey still does not support T2star or 13C under the current Ramsey protocol. The next project action should be either:

1. switch to an alternate validation protocol/control that can disambiguate the carrier from the unexpected `~2.27 MHz` component before fitting T2star, or
2. close r03 with a supported negative/unsupported Ramsey/13C conclusion under current conditions and move to a new aligned NV candidate.

If continuing on r03, predefine a control that must show detuning-tracking or phase/readout consistency before any T2star fit is promoted.
