# Ramsey Review

Review date: 2026-06-16. Measurement reviewed: `nv23_ramsey_20260513_185505_auto_ramsey`, saved as `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.

## Files/Data Used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Prior support for the target and model: `evidence/e003.json` weak-pi pODMR review supporting `mw_freq = 3.876 GHz`; `evidence/e005.json` Ramsey model/advisory; `evidence/e006.json` and `evidence/e007.json` preview/advisory records for the rejected and revised Ramsey plans.
- Ramsey execution and raw data: `measurement/m001.json` raw savedexperiment export; `measurement/m002.json` job spec; `measurement/m003.json` terminal bridge result; `measurement/m004.json` terminal status; `measurement/m005.json` control state.

## Calculations/Scripts Run

- Added and ran `python ramsey_analysis.py`.
- Generated `ramsey_analysis_summary.json` and `ramsey_analysis.png`; the PNG file was verified as a valid `1980 x 1440` PNG via PIL.
- Quantitative checks included raw readout summaries, reference-normalized traces, stored-average SEM, snake-order common-mode drift checks, per-average repeatability correlations, detrended/windowed FFT checks, and descriptive decaying-cosine fits with free frequency and with frequency fixed at the programmed `det = 1.5 MHz`.

Key numeric checks:

- Ramsey scan: `tau = 0..6 us`, 31 points, `0.2 us` step, `4 x 50000` repetitions, `mw_freq = 3.876 GHz`, `det = 1.5 MHz`.
- Run completed without bridge abort; final count was `38.249 kcps` versus `43.535 kcps` fresh-track count before the Ramsey.
- Readout roles from the saved sequence/context: readout 1 reference, readout 2 Ramsey signal for `full_experiment = 0`.
- Combined raw trace equals the mean of the four stored averages to numerical precision (`7.1e-15` max absolute difference).
- Raw reference mean/ptp: `45.318 kcps` / `3.904 kcps`; raw signal mean/ptp: `42.098 kcps` / `7.750 kcps`.
- Signal/reference ratio mean/ptp: `0.9292` / `0.1355`; signal over fitted reference-line ptp: `0.1734`.
- Median across-average SEM: signal `1.015 kcps`, ratio `0.0256`; the combined trace dynamic range is several SEM, but only four stored averages are available.
- Average 1 to average 4 mean drop: reference `-4.0%`, signal `-3.9%`. Per-average acquisition-order common-mode end-start fractions were small (`+0.2%`, `-1.8%`, `-1.6%`, `+1.0%`), but detrended normalized traces had weak repeatability across averages (mean off-diagonal correlation `0.11`).
- FFT: expected `13C` Larmor from the prior model is `384.6 kHz`, so sidebands around a true `1.5 MHz` Ramsey carrier would be near `1.115 MHz` and `1.885 MHz`. The strongest detrended FFT bin in raw and line-normalized traces is instead `0.968 MHz`, only about `1.84x` the median nonzero-bin amplitude. The programmed-carrier nearest bin (`1.452 MHz`) is below the median FFT floor in normalized views (`0.76x`, rank 13). Candidate sideband bins are weak/mixed rather than a robust symmetric pair.
- Descriptive free-frequency fit to line-normalized data: `f = 0.962 +/- 0.036 MHz`, `T2star = 2.07 +/- 0.91 us`, `R2 = 0.489`, `delta AIC = -12.3` versus a linear baseline. Signal/reference gives a similar free fit (`f = 0.941 +/- 0.035 MHz`, `T2star = 2.39 +/- 1.19 us`, `R2 = 0.446`).
- Fit forced to the programmed `1.5 MHz` carrier is not stable: line-normalized fit gives `T2star = 0.253 +/- 0.214 us`, `R2 = 0.302`; signal/reference improves only marginally over linear (`delta AIC = -0.73`).

## Plausible Interpretation

The Ramsey run is technically usable as a scout: it completed, the readouts are present, and the combined signal has modulation larger than the median stored-average SEM. The modulation is not cleanly centered on the programmed `1.5 MHz` Ramsey carrier. The most coherent descriptive fit and the strongest FFT bin sit near `0.95-0.97 MHz`, and the programmed-carrier bin is not prominent.

A plausible physical explanation is residual resonance-frequency offset relative to the weak-pi pODMR grid center, possibly combined with the Ramsey phase convention and drift during the run. A nonphysical/noise explanation is also plausible because the FFT contrast is weak, per-average trace repeatability is poor, and the final count dropped relative to the fresh track. Treat the `~2 us` free-frequency T2star fit as a descriptive hypothesis only, not a project conclusion.

## Claims Not Yet Supported

- No well-supported T2star value is established from this scout.
- No well-supported `13C` coupling or sideband conclusion is established.
- The `0.95-0.97 MHz` feature should not yet be claimed as the true Ramsey carrier or as a physical resonance offset.
- The accepted aligned-candidate status of r03 is not invalidated by this Ramsey scout; the earlier pODMR evidence still supports using r03 for targeted follow-up.

## Recommended Next Action

Do not blind-repeat the identical Ramsey. First re-check the current r03 resonance/tracking state with a fresh track/count check and a narrow weak-pi pODMR recenter around `3.876 GHz`. If the resonance is still usable, repeat Ramsey with the microwave frequency updated from that recentering and with acquisition redesigned for better repeatability under the drift cap, preferably by keeping per-average windows shorter and accumulating more stored averages or split jobs rather than extending a single untracked window. Only promote T2star or `13C` after the carrier is reproducible in raw/readout-aware traces and the FFT shows a carrier/sideband structure stronger than the present weak-bin evidence.
