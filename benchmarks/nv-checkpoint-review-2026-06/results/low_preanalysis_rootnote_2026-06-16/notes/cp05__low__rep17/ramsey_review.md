# Ramsey review: refreshed-center r03 long-span run

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New measurement metadata: `measurement/m002.json` submit spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` terminal status, `measurement/m005.json` control state.
- New raw data: `measurement/m001.json`, raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- Generated local analysis outputs: `analyze_ramsey.py`, `analysis_outputs/ramsey_analysis_summary.json`, `analysis_outputs/ramsey_terminal_review.png`.

## Calculations or scripts run

- Parsed `measurement/m001.json` with Python and verified the raw average-axis contract:
  `ExperimentDataEachAvg` has shape `[1, 20, 2, 41]`; averaging over the average axis reproduces `ExperimentData` with max absolute difference `1.4e-14`.
- Confirmed measurement settings from metadata:
  `auto__ramsey`, `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`, `tau = 0.048..8.048 us` with `0.200 us` spacing, `20 x 50000` shots, final counts `43.433 kcps`, no stop request, run completed without bridge abort.
- Computed raw readout means and uncertainty from stored averages:
  reference mean `48.789 kcps`, signal mean `44.670 kcps`, median signal SEM `0.850 kcps`, signal point-to-point span `6.269 kcps`.
- Computed signal/reference and signal/fitted-reference-line views:
  median point-wise ratio SEM `0.0116`; median fitted-reference-line normalized SEM `0.0174`.
- Ran least-squares sinusoid screens with constant + linear trend over `0.125..2.45 MHz`, plus target checks at carrier and sideband frequencies.
  - Raw signal top: `2.272 MHz`, amplitude `0.818 kcps`.
  - Ratio top: `2.270 MHz`, amplitude `0.01845`.
  - Fitted-reference-line top: `2.272 MHz`, amplitude `0.01678`.
  - Programmed carrier `1.5 MHz`: raw `0.705 kcps`, ratio `0.01575`, fitted-reference-line `0.01447`.
  - Expected 13C sidebands from the plan, `1.115/1.885 MHz`: ratio amplitudes `0.00277/0.00961`, fitted-reference-line amplitudes `0.00299/0.00536`.
  - Prior fixed-artifact control `1.192 MHz`: ratio amplitude `0.00194`, fitted-reference-line `0.00226`.
  - Previous det-shift top `1.623 MHz`: ratio amplitude `0.00801`, fitted-reference-line `0.00770`.
- Repeated the LS screen after skipping the first four tau points:
  combined tops remain near `2.27 MHz` in raw, ratio, and fitted-reference-line views.
- FFT sanity check on detrended ratio:
  largest bins at about `2.317`, `2.195`, `1.463`, `1.585`, and `1.829 MHz`; this is broadly compatible with the LS screen showing no clean isolated target-frequency carrier/sideband pattern.
- Per-average ratio LS screens are not consistent:
  individual top frequencies range across the search window, including `0.125`, `0.432`, `0.544`, `0.699`, `0.855`, `0.991`, `1.534`, `1.538`, `1.577`, `1.681`, `1.895`, `1.926`, `2.054`, `2.116`, `2.139`, `2.248`, `2.264`, and `2.341 MHz`.
- Local drift/provenance check from per-average means:
  average-level reference range `13.16 kcps`, signal range `12.99 kcps`, ratio range `0.0682`. The run used snake scan order and per-average tracking. No separate formal scan-order drift-review artifact was present in this checkpoint.

## Plausible interpretation

- The run is valid and analyzable: it completed terminally, has the intended scan, no stop/abort signal, and the raw export axis contract checks out.
- The refreshed pODMR center did not produce a clean claim-grade Ramsey carrier/decay model. A carrier-like component at `1.5 MHz` is present in the combined screens, but its raw amplitude (`0.705 kcps`) is below the median per-point signal SEM (`0.850 kcps`) and the dominant combined component is instead near `2.27 MHz`.
- The old fixed `~1.19 MHz` feature is weak in this run, so this dataset continues to argue against simply promoting that prior feature as a stable physical Ramsey frequency.
- The `2.27 MHz` component is a plausible empirical feature of this dataset, but it is not yet a supported physical assignment: it is not the programmed `1.5 MHz` carrier, not the expected `1.115/1.885 MHz` 13C sideband pair, and per-average frequency screens are mixed.
- The 13C sideband evidence remains weak. The high sideband target near `1.885 MHz` is visible at only modest amplitude, the low sideband near `1.115 MHz` is very weak, and there is no symmetric pair around the carrier that is consistent across raw/normalized/per-average views.

## Claims that are not yet supported

- Do not claim a numerical T2star from this Ramsey run. The raw/readout-aware carrier signal and decay shape are not established strongly enough to justify promoting a fit.
- Do not claim nearby 13C coupling from this run. The expected sideband pair is not consistently resolved or dominant.
- Do not claim the `2.27 MHz` screen maximum is a physical detuning or coupling without a targeted follow-up; it may be an empirical/noise/drift/sequence artifact feature.
- Do not treat the weak `1.5 MHz` carrier amplitude alone as confirmation of the refreshed-center Ramsey model because it is near or below the observed per-point uncertainty and not the dominant spectral feature.

## Recommended next action

Avoid another blind long Ramsey repeat on r03 under the same conditions. The next useful step is a targeted diagnostic that tests whether the `2.27 MHz` component follows programmed detuning or stays fixed: repeat a shorter/high-SNR Ramsey with a deliberately shifted detuning and enough points to keep Nyquist above both the old targets and `2.27 MHz`, or use an alternate protocol such as Hahn/CPMG if the objective is now to establish a bounded coherence conclusion rather than keep accumulating non-claim-grade Ramsey spectra. If no bridge work is to be launched immediately, update the project state to record this terminal run as valid but still non-claim-grade for both T2star and 13C.
