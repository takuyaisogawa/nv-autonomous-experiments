# Ramsey Review: r03 T2star Scout

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`.
- Ramsey raw export: `measurement/m001.json`, from `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
- Ramsey contract/result/status/control: `measurement/m002.json` through `measurement/m005.json`.
- Prior Ramsey planning/model context: `evidence/e005.json`.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis.json`, `ramsey_analysis.png`, and `ramsey_analysis_stdout.txt`.
- Checks performed:
  - Parsed the two-readout Ramsey scan as reference and signal, using `signal/reference` as the main normalized observable.
  - Verified scan shape: tau `0..6 us`, `31` points, `0.2 us` step, `4` averages, `50000` repetitions, snake scan order, data saved in tau order.
  - Computed average and per-average reference/signal/ratio statistics and SEM across averages.
  - Fit constant, free-frequency exponential damped cosine, and fixed-`1.5 MHz` exponential damped cosine models to the averaged ratio.
  - Ran Hann-windowed zero-padded FFT and fixed-frequency least-squares amplitudes at the programmed carrier and expected 13C sideband frequencies.
  - Checked per-average spectral peak consistency and scan-order ratio drift.

## Quantitative observations

- Run completed: `nv23_ramsey_20260513_185505_auto_ramsey`, final count text `38.249 kcps`; this is lower than the preceding weak-pODMR final count `43.890 kcps`, so drift/count loss remains relevant.
- Mean reference `45.318 kcps`; mean signal `42.098 kcps`; mean normalized ratio `0.9292`.
- Averaged `signal/reference` spans `0.8591..0.9946` with peak-to-peak `0.1355`, but median per-point SEM across four averages is `0.0256` and max SEM is `0.0602`.
- Fixed-`1.5 MHz` damped cosine fit gives a short descriptive `T2star ~0.42 us`, but it does not improve model selection relative to a constant baseline (`delta AICc = +0.35` vs constant), so this is not a supported T2star claim.
- Free-frequency damped cosine fit improves over constant (`delta AICc = -7.1`) with `f ~0.933 MHz` and descriptive `T2star ~2.82 us`, but this frequency is not the programmed `1.5 MHz` Ramsey carrier and is not consistently present across averages.
- FFT/periodogram checks:
  - Standard FFT bin spacing from 31 samples at `0.2 us` is `161.3 kHz`; inverse span is `166.7 kHz`; Nyquist is `2.5 MHz`.
  - Strongest Hann/zero-padded averaged peak is near `0.929 MHz`; a smaller peak occurs near `1.890 MHz`.
  - Fixed-frequency least-squares amplitudes are small: `1.5 MHz` carrier amplitude `0.0058`, expected sidebands at `1.115 MHz` and `1.885 MHz` give `0.0078` and `0.0118`.
  - Individual average peak frequencies are not stable: about `0.93`, `1.65`, `1.31`, and `0.86 MHz`.
- Scan-order ratio slopes imply possible within-average changes of about `+0.043`, `+0.060`, `+0.012`, and `-0.052` ratio units over each average. This is comparable to the spectral amplitudes being discussed.

## Plausible interpretation

The scout produced analyzable Ramsey data and shows real normalized contrast variation, especially at early tau. However, the expected programmed `1.5 MHz` carrier is weak in the averaged data, the best free-frequency feature is off-carrier, and per-average spectral content is inconsistent. The measurement is therefore best interpreted as a non-claim-grade Ramsey scout affected by noise and/or drift, not as a reliable T2star or 13C result.

It remains plausible that r03 has a short T2star on the sub-us to few-us scale, but the present data cannot distinguish a true decaying Ramsey envelope from scan/order drift and average-to-average fluctuation well enough to quote a supported value.

## Claims not yet supported

- A final T2star value for r03.
- Detection or exclusion of a nearby 13C spin.
- Assignment of the `1.89 MHz` FFT bump as a 13C sideband.
- A reliable Ramsey carrier frequency offset from this scan alone.
- A no-coherence conclusion; the scan is too noisy/drifty for that.

## Recommended next action

Repeat a targeted Ramsey/T2star measurement on r03 only if tracking/counts are healthy, with a shorter untracked window and stronger carrier validation. A practical next run is a higher-SNR short-span Ramsey centered on the observed early decay, for example `tau = 0..3 us` with more averages and the same `0.2 us` or finer step, still using per-average tracking and the same readout-aware analysis. If the `1.5 MHz` carrier is recovered consistently across averages, follow with a longer/higher-SNR Ramsey or a purpose-built 13C sideband scan; if it remains inconsistent, first revisit resonance/drive calibration and drift before making T2star or 13C claims.
