# Ramsey Review: r03 det=1.0 MHz follow-up

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/knowledge.md`, `md/memory.md`.
- Prior/local evidence: especially `evidence/e004.json` for the fine weak-pi pODMR center, `evidence/e007.json`/`e008.json`/`e009.json`/`e010.json` for the second Ramsey plan and submission, and `evidence/e013.md` for the handoff into this run.
- New Ramsey measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` status, `measurement/m005.json` control.
- Derived scratch outputs written under `analysis/`: `ramsey_analysis_results.json`, `ramsey_combined_series.csv`, `ramsey_raw_readouts.png`, `ramsey_normalized.png`, `ramsey_ls_frequency_scan.png`.

## Calculations or scripts run

- Parsed the new Ramsey export with local Python/numpy/scipy/matplotlib.
- Verified scan shape and acquisition: `tau = 0..8 us`, `41` points, `dt = 0.2 us`, Nyquist `2.5 MHz`, nominal FFT-bin spacing `0.122 MHz`, `8` averages, `50000` repetitions/average, terminal final counts `44.184 kcps`.
- Built combined readout series:
  - readout-1/reference mean `49.31 kcps`, range `46.95..51.24 kcps`;
  - readout-2/signal mean `44.58 kcps`, range `39.31..47.03 kcps`;
  - signal/reference mean `0.9042`, range `0.8025..0.9721`;
  - signal/reference-line normalization mean `0.9040`, peak-to-peak `0.1536`.
- Checked per-average stability. Absolute readout means vary strongly across averages, about `30.5%` reference and `31.6%` signal common-mode range, while per-average signal/reference means are much tighter (`0.8909..0.9258`).
- Ran FFT on detrended/windowed reference, signal, ratio, and reference-line-normalized traces. For the normalized trace, largest FFT peaks were near `1.220`, `1.098`, `0.488`, `0.122`, `0.610`, and `1.341 MHz`.
- Ran linear least-squares sinusoid checks with offset+slope at the planned diagnostic frequencies:
  - normalized trace at `0.6155 MHz`: amplitude `0.0097`, delta-R2 vs line `0.0688`;
  - normalized trace at prior `0.884 MHz`: amplitude `0.0059`, delta-R2 `0.0266`;
  - normalized trace at programmed `1.000 MHz`: amplitude `0.0056`, delta-R2 `0.0244`;
  - normalized trace at `1.3845 MHz`: amplitude `0.0054`, delta-R2 `0.0223`.
- Scanned `0.25..2.25 MHz` with the same linear model. The best normalized exploratory component was near `0.465 MHz` with amplitude `0.0186` and delta-R2 `0.261`, not at the programmed carrier or expected 13C sidebands.
- Tried descriptive damped-cosine fits to the normalized trace. The exponential model pegged the lower bound (`T = 0.1 us`) with implausibly large amplitude, and the Gaussian model near `1.0 MHz` had tiny amplitude (`0.0025`) and poor explanatory power (`R2 = 0.014`). These fits are not claim-grade T2star estimates.

## Plausible interpretation

- The measurement completed and returned analyzable data on the accepted r03 branch. Counts were adequate at terminal, and ratio/line normalization substantially suppress the large common-mode per-average swings.
- There is weak oscillatory structure in the normalized Ramsey trace. FFT energy appears around the intended carrier region (`~1.1..1.2 MHz`) and near the lower expected sideband bin (`~0.610 MHz`), but exact-frequency least-squares support at `1.0 MHz` and the expected `13C` sidebands is small.
- The second, det-shifted Ramsey does not cleanly demonstrate that spectral content follows the programmed `det = 1.0 MHz` phase ramp. The strongest exploratory normalized component is instead near `0.465 MHz`, and per-average phases at candidate frequencies are inconsistent.
- Taken with the earlier `det = 1.5 MHz` scout summary, this run strengthens the conclusion that the current Ramsey evidence is non-claim-grade rather than simply under-sampled.

## Claims that are not yet supported

- No supported T2star value from this run. The damped-cosine fits are descriptive failures or near-null fits.
- No supported nearby `13C` conclusion. Frequencies near `0.6155` and `1.3845 MHz` are not consistently separated from background/exploratory spectral structure, and per-average phase consistency is weak.
- No supported claim that the observed Ramsey spectral content tracks the programmed detuning.
- Do not use this run to revise the accepted r03 alignment claim; alignment remains supported by prior strong-pi/weak-pi/fine-pODMR evidence, not by this Ramsey dataset.

## Recommended next action

Do not start another long Ramsey accumulation on r03 without a protocol sanity check. First run a short, targeted Ramsey/phase-ramp validation or sequence/readout diagnostic that can answer whether the `auto__ramsey` route produces a carrier at a deliberately chosen detuning under conditions where the signal should be obvious. If that check passes, then choose a higher-SNR T2star run with a narrowed frequency/fit plan; if it fails, close the r03 Ramsey/T2star/13C branch as route-limited or signal-limited rather than claiming T2star or 13C.
