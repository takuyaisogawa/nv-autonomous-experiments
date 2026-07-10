# Ramsey Review: refreshed-center r03 long-span run

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`, with spot checks in `md/knowledge.md`/`md/memory.md`.
- Measurement files:
  - `measurement/m001.json`: terminal savedexperiment raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
  - `measurement/m002.json`: job specification, `auto__ramsey`, `mw_freq=3.8765 GHz`, `det=1.5 MHz`, `tau=48 ns..8.048 us`, `41` points, `20 x 50000`.
  - `measurement/m003.json`: completed bridge result, final counts `43.433 kcps`, no abort/incomplete run.
  - `measurement/m004.json`/`measurement/m005.json`: completed status and no stop request.
- Relevant project targets from context: carrier `1.5 MHz`; expected 13C sidebands `1.115 MHz` and `1.885 MHz`; prior controls near `1.192 MHz`, `1.623 MHz`, and `0.746 MHz`.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Output files: `ramsey_analysis_summary.json` and `ramsey_analysis_plot.png`.
- Checks performed:
  - Loaded raw signal/reference arrays and per-average arrays from `measurement/m001.json`.
  - Built the tau axis from `48 ns` to `8.048 us` in `200 ns` steps.
  - Compared raw signal, raw reference, point-wise `signal/reference`, and `signal / fitted-reference-line`.
  - Computed per-point SEM across the 20 stored averages.
  - Ran least-squares sinusoid screens from `0.2..2.4 MHz` in `1 kHz` steps for full-span and skip-first-4-point views.
  - Checked LS amplitudes at `1.5`, `1.115`, `1.885`, `1.192`, `1.623`, and `0.746 MHz`.
  - Ran Hann-window FFT checks and per-average frequency screens.
  - Checked per-average mean signal/reference/ratio ranges with a MAD-style common-mode outlier screen; no average fell outside a broad 3-MAD range, though average-to-average common-mode variation is visible.

## Quantitative observations

- Run health: completed, final text counts `43.433 kcps`, scan order `snake`, no stop request, no incomplete/abort flag.
- Combined raw levels: signal mean `48.789 kcps`, reference mean `44.670 kcps`.
- The first tau point is a normalization transient: `signal/reference = 1.1953` at `48 ns` versus `1.0448` at the second point. Therefore skip-first-4 checks are more relevant than full-span-only screens.
- Mean SEM across tau:
  - raw signal `0.862 kcps`
  - raw reference `0.834 kcps`
  - point-wise ratio `0.0140`
  - fitted-reference normalization `0.0109`
- Skip-first-4 target amplitudes:
  - raw signal: carrier `0.127 kcps`, 13C lower `0.026 kcps`, 13C upper `0.270 kcps`.
  - point-wise ratio: carrier `0.01498`, 13C lower `0.00082`, 13C upper `0.00651`.
  - fitted-reference normalization: carrier `0.00283`, 13C lower `0.00055`, 13C upper `0.00605`.
- Skip-first-4 dominant screens are not a clean carrier/sideband set:
  - raw-signal LS top near `0.800 MHz`; raw FFT has a strong component near `1.892 MHz`.
  - point-wise ratio LS top near `2.266 MHz`; ratio FFT has components near `1.486`, `2.297`, `1.622`, and `1.892 MHz`.
  - fitted-reference LS top near `0.800 MHz`; fitted-reference FFT top near `1.892 MHz`.
- Per-average frequency screens remain scattered. Ratio skip-first-4 tops include values around `0.2`, `0.465`, `0.7`, `1.005`, `1.34`, `1.51`, `1.55`, `1.58`, `1.69`, `1.905`, `1.92`, `2.06`, `2.13`, `2.165`, `2.26`, and `2.28 MHz`; fitted-reference tops are similarly mixed.

## Plausible interpretation

The measurement is usable as terminal evidence but still not claim-grade for T2star or 13C. The run improved shot count and kept the refreshed pODMR center/detuning plan, but the expected `1.5 MHz` carrier does not appear as a robust raw/readout-aware feature. In the normalized ratio view the carrier-scale amplitude is only about the mean ratio SEM and is not corroborated by raw signal or fitted-reference normalization. The `~1.89 MHz` component is a plausible hint near the upper expected 13C sideband, but it is not paired with a clear carrier or lower sideband and is not stable enough across per-average screens to support a 13C claim.

The most likely conservative reading is that this Ramsey branch remains dominated by weak oscillatory content plus early-tau/reference-normalization structure and average-to-average variability. It argues against promoting a numeric T2star from this run.

## Claims not yet supported

- No well-supported numeric T2star is established from this run.
- No well-supported nearby-13C conclusion is established from this run.
- The `~1.89 MHz`, `~0.80 MHz`, or `~2.27 MHz` screen components should not be promoted as physical frequencies without an alternate readout/control that makes the carrier and sideband model coherent.
- The refreshed pODMR frequency remains a grid-supported calibration, not sub-grid frequency precision.

## Recommended next action

Do not run another blind same-route long-span Ramsey on r03. If continuing data acquisition, switch to an alternate diagnostic protocol that directly tests the failure mode: for example, a phase-cycled/quadrature Ramsey or equivalent reference-normalization-control Ramsey that can verify the programmed detuning carrier before any T2star fit, followed by a 13C-sensitive protocol only if the carrier/readout model becomes coherent. If no alternate protocol is available, record the current state as an unsupported/negative Ramsey/T2star/13C result for r03 under the present `auto__ramsey` conditions rather than accumulating more repeats.
