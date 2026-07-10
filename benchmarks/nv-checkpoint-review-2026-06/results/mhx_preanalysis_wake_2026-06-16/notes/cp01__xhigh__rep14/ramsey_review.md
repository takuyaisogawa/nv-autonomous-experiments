# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Prior evidence used for setup/model context: `evidence/e003.json` weak-pi pODMR review, `evidence/e005.json` Ramsey model/advisory, `evidence/e009.json` Ramsey job spec.
- New Ramsey measurement data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` terminal status, `measurement/m005.json` control state.
- Scratch outputs created here: `ramsey_analysis_summary.json`, `ramsey_trace.csv`, `ramsey_repeatability_checks.json`, `ramsey_false_alarm_check.json`, `ramsey_raw_norm_peravg.png`, `ramsey_fft_checks.png`.

## Calculations or scripts run

- Parsed the raw Ramsey export with local Python. The run completed as `nv23_ramsey_20260513_185505_auto_ramsey`, saved as `1DExp-seq-ramsey-vary-tau-2026-05-13-185521`, with `tau=0..6 us`, 31 points, `dt=0.2 us`, `det=1.5 MHz`, `mw_freq=3.876 GHz`, 4 averages x 50000 repetitions.
- Used the inspected protocol context: `full_experiment=0`, so readout 1 is the reference and readout 2 is the Ramsey signal.
- Computed raw signal/reference traces, point-wise ratio, reference-line normalization, per-average summaries, scan-order half-means, fixed-frequency sinusoid regressions, FFT checks, a fixed-carrier exponential decay fit, jackknife/per-average repeatability checks, and a 2000-trial false-alarm check for the best scanned frequency.
- Model targets from the project calculation were rechecked: working `B ~= 359.29 G`, expected `13C` Larmor `~=384.6 kHz`; expected Ramsey spectral locations for `det=1.5 MHz` are carrier `1.500 MHz` and sidebands `1.115 MHz` and `1.885 MHz`. Sampling gives Nyquist `2.5 MHz` and about `0.16-0.17 MHz` frequency resolution.

## Plausible interpretation

- The Ramsey acquisition is valid as a completed scout, but it is not claim-grade for T2star or 13C.
- Raw readout 2 has mean `42.10 kcps`, point-to-point range `38.10..45.85 kcps`, peak-to-peak `7.75 kcps`, and median exported signal error `1.82 kcps`. Final bridge counts were `38.249 kcps`, lower than the recent r03 track/weak-pODMR context around `43.5-43.9 kcps`, so drift/count change is relevant provenance.
- A fixed `1.5 MHz` Ramsey-carrier regression on the raw signal gives amplitude `0.13 kcps`, partial R2 `0.0043`, and p `0.94`; this is effectively no support for the programmed carrier beyond a linear baseline.
- Fixed regressions at the expected `13C` sideband frequencies are also weak: amplitudes about `0.38 kcps`, partial R2 about `0.037`, p about `0.60`.
- The strongest empirical FFT/regression feature is near `0.96-0.97 MHz` with amplitude about `1.0 kcps`, but it was selected after scanning many frequencies. The false-alarm check gives p about `0.28` for obtaining at least this much best-frequency partial R2 from shuffled/sign-flipped data, so this feature should be treated as a weak, non-claim-grade hint at most. It could be residual detuning/drift/noise; it is not enough to assign a 13C sideband.
- A fixed-carrier decaying cosine fit is not useful: fitted `T2star ~=0.44 us` with uncertainty `~=1.52 us`, and fitted amplitude uncertainty exceeds the amplitude.

## Claims not yet supported

- No well-supported numeric T2star can be claimed from this Ramsey scout.
- No well-supported 13C coupling/conclusion can be claimed. The expected carrier and sideband locations are not supported, and the isolated empirical peak near `0.97 MHz` is not statistically robust after frequency scanning.
- The data do not prove absence of T2star coherence or absence of nearby 13C; they show that this particular scout did not produce a claim-grade Ramsey/FFT result.
- The data do not by themselves prove a hardware or sequence failure. The job completed and the exported sequence/variables match the intended Ramsey scout.

## Recommended next action

Do not run a blind longer 13C/T2star measurement from this result. First do a fresh r03 track/count check and preferably a quick weak-pi pODMR center check because the Ramsey final counts dropped and the only notable oscillatory hint is shifted from the programmed carrier. If r03 remains healthy, run a redesigned higher-SNR Ramsey diagnostic aimed at verifying a clear carrier before any 13C sideband claim: use even stored averages, keep the per-average tracking window under the active drift cap, and choose tau span/point spacing from the desired carrier/sideband Nyquist guard.
