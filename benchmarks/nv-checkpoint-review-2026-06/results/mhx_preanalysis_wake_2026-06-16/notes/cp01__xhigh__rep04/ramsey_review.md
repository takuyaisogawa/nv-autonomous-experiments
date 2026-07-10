# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Prior support for target/frequency: `evidence/e003.json` weak-pi pODMR raw review supporting r03 at `3.876 GHz`; `evidence/e005.json` Ramsey model/advisory; `evidence/e001.json` weak-pi pODMR bridge result.
- New Ramsey data: `measurement/m001.json` raw savedexperiment export; `measurement/m002.json` submitted job; `measurement/m003.json` terminal bridge result; `measurement/m004.json` final status; `measurement/m005.json` control state.
- Generated local analysis artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_diagnostic.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py` on the local JSON files. It parsed the Ramsey raw arrays, used the locally recorded protocol basis that `full_experiment=0` gives readout 1 as reference and readout 2 as Ramsey signal, generated reference-line-normalized signal, scan-order drift metrics, FFT summaries, linear-plus-sinusoid scans, fixed-frequency tests at the expected Ramsey/13C frequencies, and damped-cosine descriptive fits.
- The Ramsey run completed as `nv23_ramsey_20260513_185505_auto_ramsey`: `tau=0..6 us`, 31 points, `0.2 us` step, `mw_freq=3.876 GHz`, `det=1.5 MHz`, `4 x 50000` repetitions, `full_experiment=0`.
- Basic readout checks: reference mean `45.32 kcps` with SD `0.87 kcps`; signal mean `42.10 kcps` with SD `1.44 kcps`; line-normalized signal mean `0.929` with SD `0.032`; median signal SEM across the four stored averages `1.01 kcps`.
- Drift/provenance checks: final count `38.249 kcps`, down `12.1%` from the fresh r03 track count `43.535 kcps` and below the prior weak-pODMR final `43.890 kcps`, but still above the 20 kcps gate. Saved Ramsey position is `0.612 um` from the fresh tracked position. Scan-order common-mode drift within each average did not cross a 15% drop threshold; largest linear drop was about `3.5%`.
- FFT checks on the line-normalized trace: practical rFFT bin spacing `161.3 kHz`, Nyquist `2.419 MHz`. The largest bins were `0.968 MHz`, `0.161 MHz`, and `0.323 MHz`. Expected frequencies from the local model are `det=1.500 MHz` and `det +/- 13C = 1.115/1.885 MHz`; their nearest-bin amplitudes were not dominant.
- Fit checks: a free linear-plus-sinusoid scan prefers `0.962 MHz` on both raw signal and line-normalized signal (`p ~= 0.0099` versus a linear baseline for the line-normalized trace). Fixed-frequency fits at `1.115`, `1.500`, and `1.885 MHz` do not improve the line-normalized trace meaningfully (`p ~= 0.60`, `0.94`, `0.60`). A descriptive damped cosine on the line-normalized data gives `T2* = 2.07 +/- 0.91 us`, `f = 0.962 +/- 0.036 MHz`, amplitude `0.070 +/- 0.020`, `R2 = 0.489`; the raw-signal fit gives essentially the same `T2*` and frequency with amplitude `3.18 +/- 0.90 kcps`.

## Plausible interpretation

The completed Ramsey data contain a plausible low-SNR Ramsey oscillation with a few-microsecond decay scale. The most stable combined-trace component is near `0.96 MHz`, not at the programmed `1.5 MHz` carrier. This could reflect effective microwave detuning from the weak-pODMR grid center, sequence phase/sign convention, drift during the run, or analysis/noise structure. The prior r03 alignment evidence is not invalidated by this run, but the Ramsey result does not yet give a clean, model-consistent T2* or 13C conclusion.

## Claims not yet supported

- A final T2* value is not supported. The `~2.1 us` value is a descriptive fit from a noisy, model-mismatched trace with modest `R2` and sensitivity to low-frequency/background structure.
- Nearby `13C` coupling is not supported. The expected sideband bins around `1.115 MHz` and `1.885 MHz` are not a clean symmetric or dominant feature, and fixed-frequency sideband fits are not statistically persuasive.
- Absence of nearby `13C` is also not supported. This scout has limited SNR, only four stored averages, a short 6 us span, visible drift/count provenance, and a carrier mismatch.
- A calibrated Ramsey carrier shift or updated resonance center is not supported from this Ramsey alone.

## Recommended next action

Do not close T2* or 13C from this scout. Continue on r03 with a targeted frequency-and-Ramsey follow-up: fresh TrackCenter first, then a narrow weak-pi pODMR or short Ramsey frequency diagnostic to test whether the effective carrier really sits near `0.96 MHz`; only then run a redesigned Ramsey repeat under the current advisory, with enough SNR and span to fit T2* and test `13C` sidebands while keeping the per-average tracking window inside the live cap.
