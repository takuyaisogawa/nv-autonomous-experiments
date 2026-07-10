# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New Ramsey measurement: `measurement/m001.json` raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
- Bridge/job metadata: `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` final status, `measurement/m005.json` control state.
- Generated analysis artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_review_plot.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed `ramsey.xml` export with `tau = 0..6 us`, 31 points, 0.2 us step, `mw_freq = 3.876 GHz`, `det = 1.5 MHz`, `full_experiment = 0`, `4 x 50000` repetitions, snake scan order.
- Treated readout 1 as the 0-level reference and readout 2 as the Ramsey signal, consistent with `full_experiment = 0` and the sequence text.
- Computed raw readout means, signal/reference ratio, per-average ratio SEM, common-mode average-to-average drift, detrended FFT of the ratio, and a descriptive damped-cosine fit.
- Extra scratch check: per-average detrended FFT peaks for the four stored averages.

## Quantitative checks

- Terminal run completed without abort/incomplete flag. Final count text was `38.249 kcps`, above the job's `20 kcps` minimum but lower than the pre-Ramsey/weak-pODMR `43-44 kcps` level.
- Combined readout means: reference `45.32 kcps`, signal `42.10 kcps`, mean signal/reference ratio `0.9292`, mean contrast `7.08%`.
- Ratio range: `0.8591..0.9946`, peak-to-peak `0.1355`. Median SEM of the ratio across four averages is `0.0256`, so the apparent modulation is only modestly above average-to-average scatter.
- Average-to-average common-mode span: signal `6.68%`, reference `6.42%`. Stored average mean ratios were `0.9347`, `0.9298`, `0.9199`, `0.9377`, so ratio drift is smaller than raw count drift but not absent.
- FFT grid from the actual 31 samples gives bin spacing `161.29 kHz` and Nyquist `2.419 MHz`.
- Combined detrended-ratio FFT top bins were `0.968`, `0.806`, `0.323`, `1.935`, and `1.774 MHz`; amplitudes are comparable rather than dominated by a single line.
- Expected Ramsey carrier bin near `1.5 MHz` was rank 12. Expected rough 13C sideband bins near `1.115 MHz` and `1.885 MHz` were ranks 11 and 4 respectively. The rank-4 high-side bin alone is not enough for a 13C claim.
- Per-average FFT peaks were inconsistent:
  - avg 1: top bins near `0.968`, `0.806`, `0.323 MHz`
  - avg 2: top bins near `1.452`, `1.935`, `1.613 MHz`
  - avg 3: top bins near `0.323`, `1.129`, `1.290 MHz`
  - avg 4: top bins near `0.806`, `0.161`, `0.323 MHz`
- Descriptive damped-cosine fit to ratio gave `T2* = 2.73 us`, frequency `1.682 MHz`, amplitude `0.058`, but only `R2 = 0.178` and SSE improvement over a linear trend of `1.20x`. This is not a defensible T2star extraction.

## Plausible interpretation

The Ramsey run is valid as a completed scout on accepted r03 and contains weak oscillatory-looking structure, but the data are noisy and drift-affected. The expected `1.5 MHz` detuning is not the dominant FFT feature, the per-average spectral peaks do not repeat, and the descriptive fit is weak. A plausible reading is that the Ramsey signal is present only marginally, with SNR and/or resonance detuning/drift insufficient for extracting a reliable T2star or assigning 13C sidebands.

The high-side FFT bin near `1.935 MHz` is close to the planned `det + ~0.385 MHz` 13C scale, but it is only rank 4 in the combined FFT and is not consistently dominant across averages. Treat it as a follow-up hint, not evidence for a nearby 13C.

## Claims not yet supported

- No well-supported numerical T2star claim is supported by this scout.
- No well-supported nearby 13C conclusion is supported.
- The fitted `T2* = 2.73 us` and `1.682 MHz` frequency are descriptive only and should not be used as project conclusions.
- The `1.935 MHz` FFT component should not be assigned to `det + 13C` without a repeatable spectral feature and better carrier behavior.
- This result does not invalidate r03 as the aligned candidate; prior pODMR resonance evidence still supports r03 for targeted follow-up.

## Recommended next action

Run a targeted follow-up on r03 rather than moving candidates. First do a fresh TrackCenter/count check and, if counts or resonance freshness are questionable, a short weak-pi pODMR recheck around `3.876 GHz`. Then repeat Ramsey with a design aimed at claim-grade data: keep the per-average tracking window within the active drift cap, use an even number of snake-ordered averages, and increase statistical confidence primarily through more averages rather than lengthening the untracked per-average window. Analyze raw readouts, ratio, per-average reproducibility, and FFT before fitting or making T2star/13C claims.
