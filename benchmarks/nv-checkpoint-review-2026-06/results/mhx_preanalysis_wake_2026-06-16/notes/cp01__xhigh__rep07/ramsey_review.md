# Ramsey Review

## Files/Data Used

- Project context: `context.json`, `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`.
- Prior r03 and Ramsey-plan evidence: `evidence/e003.json` weak-pi pODMR review, `evidence/e005.json` Ramsey model/advisory, `evidence/e008.json` planned submit spec, `evidence/e009.json` materialized job, `evidence/e010.json` start status, `evidence/e011.json` batch-state snapshot.
- New Ramsey terminal data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` completed status, `measurement/m005.json` run control.

## Calculations/Scripts Run

- Created and ran `analyze_ramsey.py`; outputs are `ramsey_analysis_summary.json` and `ramsey_analysis.png`.
- Parsed `ramsey.xml` data roles from the raw export: with `full_experiment=0`, readout 1 is the 0-level reference and readout 2 is the Ramsey signal.
- Computed raw signal/reference statistics, normalized contrast `signal/reference - 1`, per-average contrast, acquisition-order slopes, FFTs of raw signal and normalized contrast, simple cosine/damped-cosine fits, and permutation checks.

Key numerical checks:

- Ramsey run completed: `1DExp-seq-ramsey-vary-tau-2026-05-13-185521`, `tau=0..6 us`, 31 points, step `0.2 us`, 4 averages x 50000 reps, final counts `38.249 kcps` after fresh r03 tracking at `43.535 kcps`.
- Raw means: reference `45.318 +/- 0.865 kcps`, signal `42.098 +/- 1.441 kcps` across tau points.
- Normalized contrast mean `-0.0708`, std `0.0340`, peak-to-peak `0.1355`; per-average mean contrast span `0.0178`.
- FFT of normalized contrast: DFT bin spacing `161.3 kHz` using 31 samples at 0.2 us, Nyquist `2.5 MHz`. Largest combined bin is `0.968 MHz` with contrast amplitude `0.0247`.
- Planned target-bin check: nearest bins to `1.5 MHz`, `1.115 MHz`, and `1.885 MHz` are not elevated. Target max permutation check gives `p ~= 0.70`.
- Global peak check for the apparent `0.968 MHz` feature gives `p ~= 0.18`; per-average top bins are inconsistent (`0.968`, `0.484`, `1.290`, `0.806 MHz`).
- Fixed `1.5 MHz` sinusoid fit amplitude is only `0.0057` contrast with `R2 ~= 0.015`.
- A free damped-cosine fit gives a descriptive frequency `0.944 +/- 0.034 MHz` and `T2* ~= 2.39 +/- 1.17 us`, `R2 ~= 0.44`, but this is not claim-grade because it is not the planned carrier/sideband feature and is not robust across stored averages.

## Plausible Interpretation

The Ramsey scout produced analyzable data and real-scale signal/reference contrast is present. The data may contain a short-lived Ramsey-like oscillatory component near `0.95 MHz`, which could reflect resonance offset, sequence phase/timing behavior, drift, or a noise-shaped feature. It does not behave like a clean on-plan `1.5 MHz` Ramsey carrier, and the expected `~0.385 MHz` 13C sideband separation is not supported by the FFT checks.

Counts declined by about `12%` from the fresh TrackCenter result to the terminal final count but stayed well above the `20 kcps` minimum gate. The run is not a tracking/count-collapse failure; the limitation is data quality/interpretability.

## Claims Not Yet Supported

- No well-supported numeric T2star claim. The `~2.4 us` damped-cosine result is descriptive only.
- No supported nearby 13C coupling claim. The planned carrier/sideband bins are not significant, and this scout also does not rule out 13C.
- No supported claim that the apparent `~0.95 MHz` feature is a physical Ramsey carrier.
- No supported claim that the weak-pi pODMR center shifted by a specific amount; the Ramsey mismatch only motivates checking that possibility.

## Recommended Next Action

Do a bounded follow-up that first resolves the carrier mismatch: refresh or narrowly verify the weak-pi resonance near r03, then run a Ramsey repeat/diagnostic designed to test whether the apparent `~0.95 MHz` component is reproducible. Keep the per-average tracking window under the active advisory cap, preserve even snake-ordered averages, and increase total shots by adding averages rather than lengthening the untracked per-average window. Only promote a T2star fit or 13C FFT interpretation after a reproducible carrier is established in raw/readout-aware data.
