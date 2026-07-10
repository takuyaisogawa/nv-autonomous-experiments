# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Prior support for target/plan: `evidence/e003.json` weak-pi pODMR review, `evidence/e005.json` Ramsey model/advisory, `evidence/e009.json` submitted Ramsey spec.
- New Ramsey terminal data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` bridge result, `measurement/m004.json` final status, `measurement/m005.json` control file.
- Generated local analysis artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis_points.csv`, `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed embedded `ramsey.xml`: with `full_experiment=0`, readout 1 is the bright `m_S=0` reference and readout 2 is the Ramsey signal.
- Confirmed actual scan/acquisition: `tau = 0..6 us`, 31 points, `0.2 us` step, snake order, 4 averages x 50000 repetitions, `mw_freq = 3.876 GHz`, programmed `det = 1.5 MHz`.
- FFT grid from the saved samples gives `161.3 kHz` DFT bin spacing and `2.5 MHz` Nyquist. The model context gives expected `13C` Larmor `0.3846 MHz`, so the planned sideband checks are near `1.115 MHz` and `1.885 MHz` around the `1.5 MHz` carrier.
- Count/drift checks: fresh track was `43.535 kcps`; Ramsey final count was `38.249 kcps`, a `12.1%` drop. Mean reference was `45.32 kcps`; mean signal was `42.10 kcps`; mean signal/reference was `0.929`. The normalized trace has peak-to-peak `0.136`, with median per-point SEM across stored averages `0.0256`.
- FFT checks on detrended, Hann-windowed signal/reference:
  - largest normalized peaks: `0.968`, `0.806`, `0.323`, `1.935`, `1.774 MHz`.
  - expected carrier nearest bin `1.452 MHz`: amplitude `0.087`, rank 12.
  - expected lower sideband nearest bin `1.129 MHz`: amplitude `0.093`, rank 11.
  - expected upper sideband nearest bin `1.935 MHz`: amplitude `0.151`, rank 4, but the reference channel also has its strongest FFT peak at `1.935 MHz`.
- Fit checks:
  - Free Gaussian-decay cosine fit to signal/reference lands at `0.942 MHz`, `T2* = 3.21 us`, `R2 = 0.434`.
  - Free fit to raw signal lands similarly at `0.961 MHz`, `T2* = 3.19 us`, `R2 = 0.455`.
  - Fixed-frequency least-squares at the programmed `1.5 MHz` carrier gives normalized amplitude `0.0058` and `R2 = 0.030`.
  - Fixed checks at the expected `13C` sidebands also explain little normalized variance: `R2 = 0.042` lower sideband and `0.078` upper sideband.
  - Per-average normalized FFT maxima in the 1-2 MHz band scatter across `1.613`, `1.452`, `1.129`, and `1.290 MHz`; per-average correlations with the mean trace are only `0.42..0.68`.

## Plausible interpretation

The Ramsey run completed and is analyzable, but it is not claim-grade for T2star or `13C`. The data show signal/reference excursions of plausible Ramsey scale, yet the expected `1.5 MHz` programmed carrier is weak and the strongest free-fit/FFT component is around `0.94-0.97 MHz`. That sub-MHz component is descriptive only: it is not the planned carrier, it is not stable across stored averages, and the averaged trace is affected by count drift and reference-channel spectral structure. The upper `13C`-sideband neighborhood has some normalized FFT amplitude, but it coincides with a strong reference peak and lacks a supported carrier/lower-sideband partner.

The prior pODMR evidence still supports r03 as the aligned candidate. This Ramsey scout should be treated as a non-claim-grade follow-up on that candidate, not as evidence that r03 is invalid.

## Claims that are not yet supported

- No supported numeric T2star value. The `~3.2 us` free-fit value should not be used as a T2star conclusion.
- No supported nearby-`13C` conclusion. The FFT does not show a clean carrier plus symmetric sideband structure.
- No supported claim that the actual Ramsey oscillation frequency is `0.94 MHz`; this may reflect drift/noise/reference artifacts or resonance detuning, and the stored averages do not lock to one frequency.
- No supported negative claim that r03 has no useful T2star or no nearby `13C`; this scout was limited by drift/noise and carrier inconsistency.

## Recommended next action

Do not repeat the same Ramsey blindly. First re-check/recenter r03 with a narrow weak-pi pODMR around the current `3.876 GHz` resonance, because the Ramsey carrier was inconsistent with the programmed detuning and the final counts dropped by `12.1%`. If the resonance is still clean, run a redesigned Ramsey with the recentered `mw_freq`, even averages, and more statistical support without increasing the per-average tracking window beyond the current advisory cap; then redo the raw-readout, reference-normalized, per-average, fit, and FFT checks before making T2star or `13C` claims.
