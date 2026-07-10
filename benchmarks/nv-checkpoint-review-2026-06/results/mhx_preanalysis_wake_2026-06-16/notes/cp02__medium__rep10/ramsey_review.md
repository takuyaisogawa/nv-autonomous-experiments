# Ramsey Review: r03 det=1.0 MHz, 8 us, 8 averages

## Files/data used

- `project/state.md`, `project/brief.md`, and `project/advice.md` for objective, accepted NV candidate context, prior pODMR/Ramsey interpretation, and expected Ramsey/13C checks.
- `measurement/m002.json` for submitted job contract: `tau=0..8 us`, 41 points, `mw_freq=3.8759 GHz`, `det=1.0 MHz`, `8 x 50000` repetitions, target `image145844_reimage_r03`.
- `measurement/m003.json` and `measurement/m004.json` for terminal run status: completed 2026-05-13 22:17:11, not aborted, final counts `44.184 kcps`, autosaved experiment `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- `measurement/m001.json` for raw savedexperiment export: two-channel combined data plus `ExperimentDataEachAvg`, snake scan order, data saved in tau order, position `['117.298','117.538','115.370']`.
- Prior context says expected programmed carrier near `1.0 MHz`, possible 13C sidebands near `0.615/1.385 MHz`, and prior non-claim-grade component near `0.884 MHz`.

## Calculations or scripts run

- Ran inline Python from this working directory to parse `measurement/m001.json`, build tau axis, inspect combined and per-average two-channel data, and compute:
  - raw signal/readout traces;
  - point-wise ratio `signal/readout`;
  - signal normalized by a fitted readout line;
  - linear detrending before FFT/least-squares frequency checks;
  - windowed FFT of the detrended ratio;
  - least-squares amplitudes/R2 at `0.615`, `1.000`, `1.385`, and `0.884 MHz`;
  - per-average means, per-average FFT peaks, and per-average 1.0 MHz LS amplitudes/phases.
- Outputs created:
  - `ramsey_analysis_summary.json`
  - `ramsey_det1p0_review.png`
- Image viewer access to the generated PNG failed locally with an access-denied error, but the JSON/numeric output from the same run was available and used.

## Quantitative checks

- Combined scan: 41 tau points, `dt=0.2 us`, `0..8 us`, 8 averages, 50000 repetitions/average.
- Combined channel means: signal `49.31`, readout `44.58`, ratio `1.1071`.
- Combined ranges: signal `4.29`, readout `7.72`, ratio `0.217`.
- Fitted readout-line change over tau is `+3.05%`; fitted ratio-line change over tau is `-0.92%`.
- Detrended ratio FFT strongest nonzero bin: `1.098 MHz`, amplitude `0.0255` ratio units.
- Nearest FFT-bin amplitudes:
  - `0.610 MHz` sideband bin: `0.00869`
  - `0.976 MHz` carrier bin: `0.01636`
  - `1.341 MHz` sideband bin: `0.00792`
  - `0.854 MHz` prior-component bin: `0.00819`
- Least-squares checks on detrended ratio:
  - `0.615 MHz`: amplitude `0.0132`, `R2=0.066`
  - `1.000 MHz`: amplitude `0.0119`, `R2=0.054`
  - `1.385 MHz`: amplitude `0.0107`, `R2=0.044`
  - `0.884 MHz`: amplitude `0.00945`, `R2=0.033`
- Per-average behavior is not coherent enough for a hard spectral claim:
  - per-average FFT peaks scatter across `0.488`, `0.610`, `1.098`, `1.220`, `1.463`, and `2.317 MHz`;
  - per-average 1.0 MHz LS amplitudes range `0.0053..0.0303` ratio units;
  - 1.0 MHz phases vary substantially;
  - signal/readout mean spans are large (`~30.5%` and `~31.6%`), while ratio mean span is smaller (`~4.0%`), consistent with substantial common-mode count changes partly corrected by normalization.
- Exploratory damped-cosine fits are descriptive only, not claim-grade:
  - fixed 1.0 MHz Gaussian-envelope fit gives `T ~0.44 us`, `R2 ~0.46`;
  - free-frequency Gaussian-envelope fit gives `f ~1.20 MHz`, `T ~1.07 us`, `R2 ~0.43`;
  - the fitted T values are sensitive to model choice and early-time structure, so they should not be reported as T2star.

## Plausible interpretation

- The run completed cleanly and returned analyzable Ramsey-like data on accepted candidate r03.
- The det-shifted data contain weak spectral content near the programmed Ramsey scale: the strongest combined FFT bin is `1.098 MHz`, close to but not exactly the `1.0 MHz` programmed detuning within the `~0.122 MHz` bin spacing.
- The prior `~0.884 MHz` component is not reinforced in this run; its LS/FFT amplitudes are weaker than the combined peak/carrier-scale content. This argues against treating the previous `~0.884 MHz` feature as a stable physical Ramsey carrier.
- The expected 13C sidebands at about `0.615` and `1.385 MHz` are not clearly resolved. Their least-squares amplitudes are small and explain only `~4-7%` of detrended variance, with no convincing per-average reproducibility.
- The large signal/readout common-mode variation across averages means normalization helps, but it does not by itself establish a coherent Ramsey oscillation or sideband structure.

## Claims not yet supported

- A well-supported T2star value is not yet supported. The available damped-cosine fits are exploratory and model-sensitive.
- A 13C coupling/sideband conclusion is not yet supported.
- A precise Ramsey carrier frequency is not yet supported beyond saying weak content appears near the programmed `1 MHz` scale.
- The data do not support claiming that the previous `~0.884 MHz` feature was a real stable carrier.

## Recommended next action

- Do not immediately repeat the same acquisition unchanged.
- First do a short diagnostic Ramsey on r03 with a deliberately larger and cleaner detuning, e.g. `det=2.0 MHz`, shorter window sized for several visible cycles, and enough averages to check per-average phase consistency. The goal is to confirm that the observed oscillation tracks programmed detuning before investing in a claim-grade T2star/13C acquisition.
- If the carrier tracks detuning and per-average phases become consistent, then run a claim-grade T2star acquisition around that validated setting and fit only after signal presence is established. If it does not track detuning, inspect sequence/IQ/reference-channel behavior or consider closing r03 for T2star/13C rather than accumulating more weak Ramsey data.
