# Ramsey Review: r03 Short-Tau High-SNR Diagnostic

## Files/data used

- `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, and `md/knowledge.md` for objective, prior decisions, and analysis posture.
- `evidence/e006.json` and `evidence/e009.json` for the short-tau Ramsey design/model: accepted r03, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, expected 13C sideband targets at `0.615423 MHz` and `1.384577 MHz`, and readout-role basis (`readout1 = mS=0 reference`, `readout2 = Ramsey signal`).
- `evidence/e001.json` and prior project summaries for the previous 8 us det=1.0 MHz Ramsey comparison.
- `measurement/m001.json` for the new terminal raw export: `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`, `tau = 48 ns..1.968 us`, 41 points, 12 averages, 90000 repetitions.
- `measurement/m002.json` through `measurement/m005.json` for job spec/result/status/control. The run completed, was not aborted, and had no stop request. Terminal final-count text was `35.122 kcps`, above the `20 kcps` gate but lower than the pre-run/latest context counts near `44 kcps`.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- The script wrote `ramsey_analysis_summary.json` and `ramsey_shorttau_review.png`.
- Checks performed:
  - raw readout and signal/reference summaries;
  - fitted-reference-line normalization (`signal / linear(reference)`);
  - exact-frequency least-squares components at `0.615423`, `1.0`, and `1.384577 MHz`;
  - exploratory target-band frequency screen from `0.45..5.0 MHz`;
  - FFT-bin check after linear detrending;
  - per-average target-vector phase/amplitude checks;
  - lightweight stored-average drift/common-mode checks.

Key quantitative results:

- Median stored-average SEM for raw signal was `1.14 kcps`, close to the planning estimate `~1.17 kcps`; median exported signal error was `1.40 kcps`.
- Exact `1.0 MHz` least-squares component:
  - raw signal amplitude `1.28 kcps`;
  - signal/reference amplitude `0.0274`;
  - fitted-reference-line normalized amplitude `0.0264`.
- Exact sideband-target components were similar in size:
  - `0.615423 MHz`: raw `1.10 kcps`, ratio `0.0243`;
  - `1.384577 MHz`: raw `1.22 kcps`, ratio `0.0271`.
- Target-band screen peaked near `1.205 MHz` with raw amplitude `1.69 kcps` and ratio amplitude `0.0364`; because the scan span is only `1.92 us`, this is not enough frequency resolution to distinguish a carrier from nearby sidebands or broad baseline curvature.
- FFT after linear detrending had its largest bins at `0.508 MHz` (`1.39 kcps`) and `1.016 MHz` (`1.33 kcps`), consistent with limited resolution rather than a precise frequency assignment.
- Early-window (`tau <= 0.768 us`) detrended raw-signal peak-to-peak was `5.09 kcps`, about `4.47x` the median stored-average signal SEM.
- Stored-average mean levels drifted substantially: reference range `13.17 kcps`, signal range `13.74 kcps`; ratio mean range `0.0626`. The ratio slope across averages was small, but odd/even ratio mean differed by `0.0222`, comparable to the target oscillation amplitudes.

## Plausible interpretation

The new short-tau/high-SNR Ramsey diagnostic is stronger than the previous long-window r03 Ramsey runs for signal presence. It shows a coherent early-time oscillatory component in the raw signal and in both normalization views at the carrier/sideband frequency scale. The exact `1.0 MHz` component is much larger than the previous 8 us terminal review's reported `0.277 kcps` raw and `0.00916` ratio component.

This supports the idea that the earlier 8 us Ramsey failures were at least partly a measurement-condition problem: lower SNR, tau=0/baseline behavior, and long-window dilution could hide a weak early-time Ramsey component. A complete "no Ramsey signal on r03" conclusion is no longer the best interpretation.

However, the current dataset is a diagnostic, not a final T2star/13C measurement. It spans only about two carrier cycles and has substantial common-mode stored-average drift. The carrier and expected 13C sideband target fits are all comparable in amplitude, so this run cannot isolate the physical spectral content.

## Claims not yet supported

- No supported numeric `T2*` value. The data support an early-time oscillatory component, but not a robust decay envelope fit.
- No supported nearby-13C claim. The target sideband amplitudes are comparable to the carrier amplitude and the short span cannot resolve the sideband separation cleanly.
- No supported exact Ramsey frequency assignment. The target-band maximum near `1.205 MHz`, the exact `1.0 MHz` component, and the sideband-target components are too correlated over this short window.
- No claim that drift was negligible. The bridge run completed safely, but stored-average common-mode drift is visible and must be treated as provenance in the next analysis/design.

## Recommended next action

Run one confirmatory r03 Ramsey designed for decay and sideband discrimination, not another short diagnostic or blind repeat. Keep `mw_freq = 3.8759 GHz` and `det = 1.0 MHz`, start after tau=0 again, extend the span to at least `6..8 us` so the `~0.385 MHz` sideband separation is resolvable, and preserve a higher shot budget than the previous 8 us run while respecting the per-average tracking cap. The post-run review should again start from raw readouts, fitted-reference-line normalization, scan-order-aware drift, and exact carrier/sideband LS checks before fitting `T2*`.

If that longer confirmation reproduces the carrier-scale oscillation, then fit a damped Ramsey model and check for sidebands. If it does not reproduce, close the r03 Ramsey/T2star/13C branch as unsupported under current conditions rather than continuing blind Ramsey repeats.
