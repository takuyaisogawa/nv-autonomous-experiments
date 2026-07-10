# Ramsey Review

## Files/data used

- `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json` for objective and prior project state.
- `measurement/m001.json` raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- `measurement/m002.json` submitted job spec: `auto__ramsey`, `mw_freq=3.8765 GHz`, `det=1.5 MHz`, `tau=48 ns..8.048 us`, 41 points, `20 x 50000`.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json` terminal bridge/status/control metadata. Run completed, safe shutdown ok, no stop request, final counts `43.433 kcps`.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Output artifacts:
  - `ramsey_review_analysis.json`
  - `ramsey_review_traces.png`
  - `ramsey_review_spectrum.png`
- Parsed raw shape checks:
  - `ExperimentData`: `[1, 2, 41]`
  - `ExperimentDataEachAvg`: `[1, 20, 2, 41]`
  - oriented as 2 readouts x 20 averages x 41 tau points.
- Basic checks:
  - tau window `0.048..8.048 us`, step `0.200 us`; nominal FFT bin scale about `125 kHz`.
  - scan order mode `snake`, tracking `Per average`, 20 averages.
  - signal range `47.746..49.812 kcps`, peak-to-peak `2.065 kcps`.
  - reference range `40.569..46.838 kcps`.
  - median per-point SEM from averages: signal `0.867 kcps`, ratio `0.01365`.
  - simple common-mode drift screen flagged 0/20 averages.
- Least-squares sinusoid screens from `0.25..2.4 MHz` were run on raw signal, point-wise ratio, and signal/fitted-reference-line ratio, both full-span and skipping first 4 tau points.
- Target frequencies checked:
  - programmed carrier `1.500 MHz`
  - expected 13C sidebands `1.115 MHz` and `1.885 MHz`
  - prior control/top frequencies `1.192 MHz` and `1.623 MHz`
- FFT/Hann peak checks were also run on ratio and fitted-reference-line ratio.
- Exploratory damped-sinusoid fits were run only as descriptive diagnostics, not promoted as T2star evidence.

## Plausible interpretation

- The run is terminal and analyzable. Counts and bridge status do not show a hard acquisition anomaly.
- The raw signal does not show a clean programmed-carrier Ramsey oscillation. In raw signal, the full-span LS top is near `0.808 MHz` with amplitude `0.308 kcps`; the programmed `1.500 MHz` amplitude is only `0.101 kcps` with low `R2=0.028`.
- The point-wise ratio view does contain carrier-region power. Its strongest LS component is near `2.27 MHz`, but the target `1.500 MHz` has amplitude `0.0188` and `R2=0.224`; FFT bins in the ratio view peak near `1.46/1.59 MHz` full-span and `1.49 MHz` after skipping 4 points.
- That carrier-region evidence is normalization-dependent: signal/fitted-reference-line ratio instead has weak carrier amplitude (`0.0018` full, `0.0024` skip4) and low `R2`, with strongest LS components near `0.79..0.80 MHz`. This argues against treating the point-wise ratio carrier as standalone claim-grade evidence.
- The `1.885 MHz` high sideband target is visible in raw/fitted-reference-line views more than the low sideband, but it is not accompanied by a consistent carrier/sideband model. The low `1.115 MHz` sideband is weak in all views.
- Per-average ratio LS top frequencies are scattered across the search band rather than clustered at carrier or sideband frequencies. This weakens both T2star and 13C interpretations.
- Descriptive damped fits are unstable across views: point-wise ratio full fit gives `f=1.535 MHz`, `T2star=2.22 us`, `R2=0.409`, but skip4 drops to `R2=0.278`, and fitted-reference-line fits move to unrelated frequencies with low `R2`. Treat these as descriptive only.

## Claims not yet supported

- No supported numeric T2star claim from this run.
- No supported nearby-13C claim. The expected sideband pattern at `1.115/1.885 MHz` is not consistent across raw, ratio, fitted-reference-line, FFT, and per-average views.
- No claim that the old empirical features or the new `~0.8 MHz` raw/fitted-reference-line component are physical coupling signatures.
- No sub-grid or sub-100-kHz resonance-frequency precision beyond the prior pODMR calibration context.

## Recommended next action

Avoid another blind Ramsey repeat on r03 under the same conditions. The refreshed-center high-shot long-span Ramsey still does not yield a robust raw/readout-aware carrier/sideband model. The next project decision should be either:

1. move to an alternate protocol that can establish T2star without relying on this unstable normalization-sensitive Ramsey carrier, or
2. record a supported negative/unsupported conclusion for r03 under the tested Ramsey conditions, especially for nearby-13C evidence.
