# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`, `md/knowledge.md`.
- Prior r03 resonance context: `evidence/e003.json` for the local readout convention and weak-pi pODMR conclusion.
- New Ramsey measurement:
  - `measurement/m001.json`: raw savedexperiment export from `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
  - `measurement/m002.json`: submitted job spec.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json`: terminal run status.
  - `measurement/m005.json`: control state.
- Derived local artifacts from this review:
  - `analyze_ramsey.py`
  - `ramsey_analysis_summary.json`
  - `ramsey_review_plot.png`

## Calculations/scripts run

- Ran `python analyze_ramsey.py`.
- Parsed `m001` raw arrays as 31 tau points from 0 to 6 us in 0.2 us steps, 4 averages, two readout channels.
- Used the local weak-pODMR review convention: readout1 is reference, readout2 is signal.
- Computed raw signal, point-wise `signal/reference`, and `signal/reference-line` views.
- Checked per-average behavior and snake scan-order common-mode drift.
- Fit linear-baseline plus sinusoid models:
  - fixed at the planned `det = 1.5 MHz`;
  - scan-selected over 0.2 to 2.45 MHz.
- Ran FFT checks on detrended traces. Numpy FFT bin spacing is 161.3 kHz for 31 samples at 0.2 us spacing; project planning estimate was 166.7 kHz from the 6 us span.
- Ran 1000-permutation checks for the scan-selected sinusoid improvement over a linear baseline.

## Quantitative checks

- Run completed, but counts dropped: fresh r03 track was 43.535 kcps; Ramsey terminal final count was 38.249 kcps.
- Combined raw readouts:
  - reference mean 45.318 kcps, range 44.038 to 47.942 kcps;
  - signal mean 42.098 kcps, range 38.096 to 45.846 kcps;
  - raw signal peak-to-peak is 18.4% of mean, but the pattern is not a stable 1.5 MHz Ramsey fringe.
- Fixed 1.5 MHz fits:
  - raw signal amplitude 0.133 kcps, `R2 = 0.0095`, AIC worsens by +3.87 vs linear baseline;
  - `signal/reference` amplitude 0.00576, `R2 = 0.0298`, AIC worsens by +3.52;
  - `signal/reference-line` amplitude 0.00295, `R2 = 0.0215`, AIC worsens by +3.86.
- Scan-selected descriptive sinusoid:
  - raw signal best frequency 0.963 MHz, amplitude 1.081 kcps, `R2 = 0.294`, AIC improves by -6.61;
  - normalized views also pick about 0.95 to 0.963 MHz;
  - however permutation p-values are not significant after frequency search: raw signal p = 0.279, `signal/reference` p = 0.392, `signal/reference-line` p = 0.284.
- Per-average scan-selected raw-signal frequencies are not consistent: 0.938, 0.538, 0.208, and 0.840 MHz. Per-average 1.5 MHz phases are also inconsistent.
- FFT top bins in raw signal are led by 0.968 MHz and low-frequency structure; target bins around 1.5 MHz and `1.5 +/- 0.385 MHz` are not clean, stable, or supported by the fits/permutation checks.
- Scan-order common-mode drift within averages is modest by this check, about +0.7%, -3.5%, -3.0%, and +0.8% linear end-to-start. Between-average count changes and the terminal count drop remain important provenance.

## Plausible interpretation

The Ramsey acquisition completed and is analyzable, but it does not provide a claim-grade Ramsey fringe at the intended 1.5 MHz detuning. The data contain low-frequency/descriptive structure near 0.95 MHz in combined views, but that feature is not statistically supported once the frequency search is penalized and it is not stable across single averages.

This is most plausibly a non-claim-grade scout limited by SNR, between-average/count drift, and/or a Ramsey phase/frequency implementation issue. It does not invalidate the prior r03 alignment/resonance conclusion from pODMR, but it also does not advance the project to a T2star or 13C conclusion.

## Claims not yet supported

- No supported T2star value from this run.
- No supported nearby 13C coupling or sideband claim.
- No supported absence-of-13C claim; this scout is not clean enough for that negative conclusion.
- No supported claim that the 0.95 to 0.96 MHz descriptive feature is physical.
- No supported claim that r03 is invalid as an aligned candidate; the issue is the Ramsey scout quality/behavior, not the prior pODMR alignment evidence.

## Recommended next action

Do not fit/report T2star or 13C from this run. Next, run a targeted Ramsey repeat/phase diagnostic on r03 only after tracker recovery and normal bridge/advisory gates pass. Preserve roughly the same total shots but shorten the per-average untracked window, for example by reducing repetitions per average and increasing averages. The immediate goal should be to confirm a stable intentional Ramsey carrier near the requested detuning before spending time on longer T2star or 13C-sensitive acquisitions.
