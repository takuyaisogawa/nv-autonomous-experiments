# Ramsey Review: refreshed-center r03 long-span run

## Files/data used

- `project/brief.md`, `project/advice.md`, `project/state.md`, and `md/memory.md` for the project objective, prior r03 alignment/Ramsey context, and interpretation rules.
- `measurement/m002.json` for the submitted Ramsey intent: accepted target `image145844_reimage_r03`, `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`, `tau = 48 ns..8.048 us`, 41 points, `20 x 50000` shots.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json` for terminal status/control: job `nv23_ramsey_20260514_055148_auto_ramsey` completed, final count `43.433 kcps`, no stop request, safe shutdown ok.
- `measurement/m001.json` for the raw savedexperiment export from `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- Generated analysis artifacts: `ramsey_refreshed_center_analysis.json` and `ramsey_refreshed_center_analysis.png`.

## Calculations/scripts run

- Parsed the raw export with local Python/NumPy/SciPy.
- Confirmed raw array shape: `ExperimentDataEachAvg` is `20 x 2 x 41`; the active Ramsey sequence has a leading 0-level reference readout and a Ramsey signal readout (`full_experiment = 0`).
- Built three views: raw Ramsey signal, point-wise `signal/reference`, and `signal / linear(reference fit)`.
- Computed per-point SEM across the 20 stored averages, full-span and skip-first-4 least-squares sinusoid screens from `0.1..2.35 MHz`, FFT checks, and target amplitudes at the programmed carrier and expected 13C sidebands.
- Quantitative checks from `ramsey_refreshed_center_analysis.json`:
  - Mean reference/signal: `48.789 / 44.670 kcps`.
  - Signal range: `6.269 kcps`; median signal SEM: `0.850 kcps`; median ratio SEM: `0.0116`.
  - Average-mean common-mode range: reference `27.0%`, signal `29.1%`.
  - Full-span LS top: raw signal, ratio, and fitted-reference normalization all peak near `2.27 MHz`.
  - Skip-first-4 LS top remains near `2.26..2.27 MHz`.
  - Target LS amplitudes, full span: carrier `1.5 MHz` has raw `0.705 kcps` and ratio `0.0157`; expected 13C sidebands have much weaker/mixed amplitudes (`1.115 MHz`: raw `0.146 kcps`, ratio `0.00277`; `1.885 MHz`: raw `0.261 kcps`, ratio `0.00961`).
  - FFT of the normalized ratio has carrier-like power near `1.51 MHz`, but the LS screen and raw/fitted-reference views are dominated by `~2.27 MHz`.
  - Per-average ratio screen frequencies are scattered from the lower search edge to above `2 MHz` with median `1.535 MHz` and IQR `0.661..2.070 MHz`.

## Plausible interpretation

This is analyzable terminal Ramsey data on the accepted r03 NV, with adequate nominal shot count (`1e6` shots per tau point) and no bridge terminal anomaly. The run does show oscillatory structure above SEM scale, and the programmed carrier is visible in some normalized/FFT views. However, the dominant full-span component is not at the programmed `1.5 MHz` detuning and not at the expected `1.115/1.885 MHz` 13C sidebands. The strong `~2.27 MHz` component, large average-to-average common-mode variation, and scattered per-average frequency screens make the physical model ambiguous.

The data therefore support only: "r03 remains a usable aligned candidate and this Ramsey run contains real structure, but it does not yet yield a clean carrier/decay/13C-sideband model."

## Claims not yet supported

- No claim-grade numeric `T2*` from this run. A damped sinusoid fit would be model-selected after the fact and would not be anchored by a clean raw/readout-aware carrier.
- No supported nearby `13C` conclusion. The expected sidebands at about `1.115 MHz` and `1.885 MHz` are not consistently dominant across raw, normalized, fitted-reference, FFT, and per-average checks.
- Do not claim the `~2.27 MHz` feature as physical without a detuning-shift/control test; it could reflect timing/readout/analysis structure, drift interaction, or another non-target component.
- Do not claim that the earlier `~1.19 MHz` empirical feature is confirmed; it is weak in this dataset.

## Recommended next action

Stop blind Ramsey repeats on r03 under the same protocol. The next useful action is a targeted diagnostic that distinguishes a physical Ramsey frequency from protocol/readout artifact: repeat a short, high-SNR Ramsey with a deliberately changed detuning and/or phase-cycled/quadrature variant if available, while keeping the refreshed pODMR center bracketed before and after. Promote `T2*` only if the dominant frequency shifts with detuning and the raw/readout-aware carrier decay is coherent; otherwise record a supported "unsupported/negative under current Ramsey protocol" conclusion for r03 and move to an alternate protocol such as Hahn/echo-based coherence or a different aligned NV candidate.
