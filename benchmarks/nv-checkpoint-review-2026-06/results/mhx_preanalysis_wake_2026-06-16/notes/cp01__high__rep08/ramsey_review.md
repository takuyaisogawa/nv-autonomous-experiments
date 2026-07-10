# Ramsey Review

## Files/Data Used

- `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`: objective and current project state.
- `measurement/m001.json`: completed Ramsey raw export for `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
- `measurement/m002.json`: submitted Ramsey job spec.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal result/status/control metadata.
- Relevant prior context from `evidence/e005.json` through `evidence/e011.json`: Ramsey plan, previews, submitted job, and running-state provenance.

## Calculations/Scripts Run

- Created and ran `analyze_ramsey.py`.
- Outputs:
  - `ramsey_analysis_summary.json`
  - `ramsey_analysis.png`
- Checks performed:
  - Parsed `measurement/m001.json` scan shape: `ExperimentData = [1, 2, 31]`, `ExperimentDataEachAvg = [1, 4, 2, 31]`.
  - Confirmed from the saved sequence text that trace 1 is the true `m_S=0` reference and, because `full_experiment=0`, trace 2 is the Ramsey signal after the Ramsey pulse block.
  - Constructed tau axis from 0 to 6 us in 31 points, `dt = 0.2 us`, Nyquist `2.5 MHz`, FFT bin spacing `161.3 kHz` by DFT length and `166.7 kHz` by 6 us span.
  - Reviewed raw reference, raw signal, signal/reference ratio, per-average traces, detrended FFTs, and descriptive damped-cosine fits.

## Quantitative Findings

- Run completed without abort; terminal result reports final counts `38.249 kcps`, above the configured `20 kcps` minimum but lower than the pre-Ramsey/weak-pODMR count scale around `43.9 kcps`.
- Averaged raw reference mean: `45.32 kcps`; averaged raw signal mean: `42.10 kcps`.
- Raw signal range: `38.10..45.85 kcps`; normalized signal/reference range: `0.859..0.995`.
- Median point SEM across four averages: about `1.01 kcps` for signal and `0.0256` for signal/reference.
- Per-average mean signal values: `43.36`, `40.55`, `42.80`, `41.68 kcps`; per-average mean ratios: `0.935`, `0.930`, `0.920`, `0.938`.
- Per-average signal-shape correlations with the averaged signal trace are positive but moderate: `0.71`, `0.69`, `0.65`, `0.60`.
- Detrended Hann FFT:
  - Raw signal strongest oscillatory bin: `0.968 MHz`; next bins include `0.806`, `1.129`, `0.645`, `0.484 MHz`.
  - Signal/reference strongest bin: `0.968 MHz`; next bins include `0.806`, `1.935`, `1.774`, `0.645 MHz`.
  - Reference itself has strong high-frequency content near `1.935`, `1.774`, `2.097`, `1.452`, `1.613 MHz`, so peaks near the expected upper sideband region are not signal-specific.
- Descriptive single-exponential damped-cosine fits:
  - Raw signal: frequency `0.944 +/- 0.058 MHz`, `T2* ~ 1.31 +/- 0.58 us`, `R2 = 0.44`.
  - Signal/reference: frequency `0.900 +/- 0.040 MHz`, `T2* ~ 2.04 +/- 0.91 us`, `R2 = 0.40`.
  - These fits are useful diagnostics only; the fit quality and per-average scatter are not claim-grade.

## Plausible Interpretation

The completed Ramsey scout likely contains a real Ramsey-scale oscillatory signal on r03: the averaged raw signal and normalized trace share a dominant component near `0.97 MHz`, and all four averages have a positively correlated signal shape. The oscillation frequency is not centered on the programmed `det = 1.5 MHz`, suggesting either resonance offset, sequence phase behavior, or drift/calibration mismatch relative to the weak-pODMR grid frequency.

The data are useful for planning follow-up, but the current SNR, moderate per-average consistency, low descriptive-fit `R2`, and reference-channel spectral structure make this first scout non-final for both T2star and 13C.

## Claims Not Yet Supported

- A well-supported numerical T2star value is not yet supported. The descriptive `~1.3..2.0 us` fit range should not be promoted as a final T2star.
- A nearby `13C` conclusion is not supported. Expected context sidebands around `1.5 +/- 0.385 MHz` would be near `1.115` and `1.885 MHz`, but those bins are not clean, repeatable, signal-specific evidence; the reference channel itself has strong content near the upper-sideband region.
- The data do not support a no-13C conclusion either; this scout is too noisy and too short for that negative claim.
- The mismatch between programmed `1.5 MHz` detuning and observed `~0.9..1.0 MHz` carrier should not be assigned to a specific physical cause from this dataset alone.

## Recommended Next Action

Do not finalize T2star or 13C from this scout. Keep r03 as the target and run a follow-up Ramsey after normal tracking/count/resonance freshness checks and a fresh advisory. Prefer more independent averages rather than more repetitions per average; use the current result to test repeatability of the `~0.97 MHz` carrier and any sideband pattern. A modestly longer span with similar point count can be considered if the advisory stays within the per-average tracking cap, but the immediate requirement is repeatability and improved SNR before changing the project conclusion.
