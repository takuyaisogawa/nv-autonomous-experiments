# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, plus local guardrails in `md/memory.md` and `md/knowledge.md`.
- New Ramsey raw export: `measurement/m001.json`, from `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- New Ramsey job/result/status/control: `measurement/m002.json`, `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`.
- Planning context for this run: `evidence/e007.json`, `evidence/e008.json`, `evidence/e009.json`, `evidence/e010.json`.
- Derived local artifacts from this review: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis_stdout.json`, `ramsey_analysis_plot.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed combined raw data shape `[1, 2, 41]` and stored averages shape `[1, 8, 2, 41]`.
- Used local project readout role: readout 1 is the Ramsey reference and readout 2 is the Ramsey signal for `ramsey.xml` with `full_experiment=0`.
- Confirmed run parameters: `tau = 0..8 us`, 41 points, `dt = 0.2 us`, Nyquist `2.5 MHz`, FFT bin spacing `0.12195 MHz`, `8 x 50000` repetitions, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, final count text `44.184 kcps`.
- Checked raw signal, signal/reference ratio, linear-reference-corrected signal, FFT peaks, least-squares sinusoid amplitudes at:
  - expected lower 13C sideband: `0.6155 MHz`
  - prior scout component: `0.884 MHz`
  - programmed carrier: `1.000 MHz`
  - expected upper 13C sideband: `1.3845 MHz`
- Quantitative summary:
  - Combined readout 2 mean/std: `44.58 / 1.34 kcps`; full raw readout 2 range: `39.31..47.03 kcps`.
  - Per-average readout 2 mean range: `36.20..50.27 kcps`; readout 1 mean range: `40.47..55.53 kcps`, so there is substantial average-to-average common-mode variation.
  - Median SEM across stored averages: readout 2 `1.92 kcps`, ratio `0.0187`.
  - Least-squares exact carrier at `1.000 MHz`: readout 2 amplitude `0.277 kcps`, peak-to-peak `0.553 kcps`, `R2 = 0.115`; ratio amplitude `0.00916`, `R2 = 0.053`.
  - Exact 13C-sideband fits are also weak: lower sideband readout 2 amplitude `0.475 kcps`, `R2 = 0.155`; upper sideband `0.262 kcps`, `R2 = 0.113`.
  - Prior `0.884 MHz` component is weak here: readout 2 amplitude `0.286 kcps`, `R2 = 0.117`; ratio amplitude `0.00742`, `R2 = 0.035`.
  - Exploratory FFT peaks are near `1.10..1.22 MHz` in ratio and signal, with another raw-signal component near `0.49 MHz`; these are not cleanly the exact programmed carrier or the expected 13C sidebands.

## Plausible interpretation

- The run completed and returned analyzable data on the accepted r03 NV; counts were not collapsed.
- There is tau-dependent structure in the Ramsey signal, but the exact programmed `1.0 MHz` carrier is small compared with the stored-average scatter and explains little variance.
- The first scout's non-claim-grade `~0.884 MHz` component did not reproduce as a strong component in the det-shifted run, which argues against promoting that earlier feature as physical.
- The FFT/least-squares results do not show a clean pair of 13C sidebands near `0.615/1.385 MHz`.

## Claims not yet supported

- No well-supported T2star value is supported by this run. A decay fit would be fit-driven because a coherent carrier/decay shape is not established first.
- No well-supported nearby 13C conclusion is supported. The expected sidebands are not clean or consistent enough to claim coupling, and non-observation in a non-claim-grade Ramsey carrier is not strong evidence of absence.
- Do not claim the prior `~0.884 MHz` feature as a real Ramsey carrier or 13C-related feature.
- Do not claim sub-grid precision for the fine pODMR center beyond the existing grid-supported `3.8759 GHz` input.

## Recommended next action

Do not spend the next hardware step on a blind longer Ramsey repeat. Treat Ramsey signal extraction or sequence/condition validation as the current blocker: run a short, high-SNR carrier-control Ramsey diagnostic or equivalent sequence validation on r03 before attempting another T2star/13C claim measurement. If that diagnostic still lacks a supported carrier, close the r03 Ramsey/T2star/13C branch as unsupported from the present route and switch strategy rather than accumulating more weak FFT peaks.
