# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Current terminal Ramsey data/metadata: `measurement/m001.json` raw export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` status, `measurement/m005.json` control.
- Most relevant prior plan/model context: `evidence/e014.json`, which defined the refreshed-center Ramsey target: `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`, `tau = 48 ns..8.048 us`, 41 points, `20 x 50000` shots, with expected 13C sidebands near `1.115/1.885 MHz`.

## Calculations/scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis.json`, `ramsey_analysis_targets.csv`, `ramsey_analysis.png`.
- Verified raw data shape and axis contract:
  - `ExperimentData` is `[2, 41]` after selecting the only scan slice.
  - `ExperimentDataEachAvg` is `[20, 2, 41]`.
  - Mean over stored averages reproduces `ExperimentData`, supporting `[avg, readout, tau]`.
  - `ramsey.xml` / `full_experiment=0` path gives readout 1 as zero-level reference and readout 2 as Ramsey signal.
- Acquisition/health checks:
  - Job `nv23_ramsey_20260514_055148_auto_ramsey` completed, final counts `43.433 kcps`.
  - No stop request, monitor error, or safety abort in the provided status/result files.
  - Scan was `48 ns..8.048 us`, `41` points, `dt = 200 ns`, span `8.0 us`, nominal resolution `125 kHz`, Nyquist `2.5 MHz`, total `1.0e6` shots per tau point.
- Noise/drift checks:
  - Median SEM over 20 stored averages: raw signal `0.850 kcps`, point-wise ratio `0.0116`, fitted-reference-line ratio `0.0174`.
  - Local scan-order drift approximation using stored snake order flagged `0/20` averages at a `15%` common-mode drop threshold.
- Frequency checks:
  - Used linear least-squares model `y = c0 + c1*t + a*cos(2*pi*f*t) + b*sin(2*pi*f*t)` for raw signal, point-wise ratio, and fitted-reference-line ratio.
  - Refline-normalized full-span LS top is near `2.271 MHz` with amplitude `0.0168`; skip-first-4 top remains near `2.271 MHz` with amplitude `0.0114`.
  - Programmed carrier `1.500 MHz`: raw LS amplitude `0.705 kcps` full / `0.512 kcps` skip-first-4; refline-ratio amplitude `0.0145` full / `0.0105` skip-first-4.
  - Expected 13C sidebands: refline-ratio amplitudes are small, `0.0030` at `1.115 MHz` and `0.0054` at `1.885 MHz` full-span; after skipping first 4 tau points they fall to `0.00025` and `0.00255`.
  - Phase concentration across stored averages is high for the carrier (`0.85`) but weak for the sidebands (`0.27` low, `0.45` high).
  - Per-average top LS frequencies in the refline-normalized screen are scattered; no stored-average top-frequency consensus is present.
  - FFT cross-check is mixed: refline full-span FFT top is near `2.317 MHz`, with carrier-near bins at `1.463/1.585 MHz`; skip-first-4 FFT top is carrier-near at `1.486 MHz`, followed by `2.297 MHz` and `1.622 MHz`.

## Plausible interpretation

The measurement is healthy and analyzable, and the refreshed center may have produced a weak carrier-like component near the programmed `1.5 MHz` detuning. However, the carrier amplitude is only about `0.705 kcps` raw or `0.0145` normalized, which is below or comparable to the per-point SEM and below the planned expected raw scale. The largest LS screen peak is not at the carrier or the expected 13C sidebands, and per-average top frequencies are inconsistent.

This is best treated as another non-claim-grade Ramsey result: useful evidence that the r03 Ramsey response remains weak/mixed even after refreshing the microwave center, not a clean Ramsey decay suitable for extracting T2star.

## Claims not yet supported

- No numerical T2star value is supported from this dataset.
- No nearby 13C claim is supported; the expected `1.115/1.885 MHz` sidebands are weak and not phase-consistent.
- Do not promote the `2.27 MHz` LS/FFT feature as a physical signal; it is not target-consistent and is not per-average stable.
- Do not claim that the refreshed `3.8765 GHz` center solved the Ramsey problem; it produced at most weak carrier-like evidence.

## Recommended next action

Do not run another blind repeat of the same Ramsey branch. The next project step should be a bridge-free synthesis that marks the r03 Ramsey/T2star/13C branch as unsupported under the current Ramsey protocol, then choose between closing with that supported negative/unsupported conclusion or switching to a different protocol after a fresh model/advisory. If continuing experimentally, use an alternate coherence or nuclear-spin protocol designed to separate early-time transient/readout artifacts from real electron coherence before attempting a 13C claim.
