# Ramsey review: det=1.0 MHz r03 follow-up

## Files/data used

- `measurement/m001.json`: terminal savedexperiment raw export for `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- `measurement/m002.json`: submitted job contract for `nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg`.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal result/status/control metadata.
- Project context: `project/state.md`, `project/brief.md`, `project/advice.md`, `evidence/e007.json`, `evidence/e013.md`.
- Generated locally: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis_plot.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed readout 1 as the `full_experiment=0` reference and readout 2 as the Ramsey signal over `tau = 0..8 us` in 41 points.
- Computed raw signal, signal/reference, mean per-average signal/reference, fitted-reference-line normalization, per-average consistency, and snake scan-order drift.
- Screened frequencies by linear-plus-sinusoid least squares and FFT at the pre-planned frequencies: carrier `1.000 MHz`, expected 13C sidebands `0.615423/1.384577 MHz`, and prior component `0.884 MHz`.
- Tried empirical decaying-cosine fits on the mean per-average ratio as screens only.

## Quantitative checks

- Run completed safely: final counts `44.184 kcps`, `8 x 50000` shots, safe shutdown true.
- Sampling: `dt = 0.2 us`, nominal span resolution `125 kHz`, NumPy FFT bin spacing `121.95 kHz`, Nyquist `2.5 MHz`.
- Combined trace: reference mean `49.31 kcps`, signal mean `44.58 kcps`, signal/reference mean `0.904`, raw signal peak-to-peak `7.72 kcps`.
- Cross-average brightness varied strongly, so raw counts alone are not sufficient: per-average reference means ranged `40.47..55.53 kcps`.
- Scan-order drift check did not flag any averages at the prior `15%` drop threshold. Worst common-mode drop score was `3.86%`; worst trace drop score was `5.95%`.
- The strongest robust feature is early-tau contrast: mean per-average ratio at `tau=0` was `0.803 +/- 0.018 SEM`; `tau=0.4 us` was higher by `0.136 +/- 0.015`, positive in all 8 averages (`paired p = 3.65e-5`). Median `tau >= 0.4 us` exceeded `tau=0` by `0.102 +/- 0.017`, positive in all 8 averages (`p = 5.22e-4`).
- Pre-specified frequency screens on mean per-average ratio were weak:
  - `1.000 MHz`: amplitude `0.0094 +/- 0.0066`, SNR `1.43`, incremental R2 `0.052`, p-screen `0.37`.
  - `0.615423 MHz`: amplitude `0.0112 +/- 0.0066`, SNR `1.71`, incremental R2 `0.073`, p-screen `0.25`.
  - `1.384577 MHz`: amplitude `0.0082 +/- 0.0066`, SNR `1.25`, incremental R2 `0.041`, p-screen `0.46`.
  - `0.884 MHz`: amplitude `0.0074 +/- 0.0067`, SNR `1.11`, incremental R2 `0.032`, p-screen `0.55`.
- FFT top bins in the normalized trace were small and not cleanly claim-grade: strongest bins were near `1.098`, `1.220`, and `0.976 MHz`; the bin near the lower 13C sideband (`0.610 MHz`) was weaker.
- Per-average phase coherence was modest rather than decisive: coherent fractions were `0.64` at `1.000 MHz`, `0.56` at `0.615 MHz`, `0.58` at `1.385 MHz`, and `0.51` at `0.884 MHz`.
- Empirical fit screens are compatible with a short initial decay but are not stable enough for a final number. A fixed `1 MHz` decaying cosine gave amplitude `0.120` in ratio units and `T2* = 0.33 us`; a free-frequency fit gave `f = 1.196 MHz`, amplitude `0.094`, and `T2* = 1.32 us`. Once the earliest tau point is excluded, target-frequency amplitudes remain weak and decay fits become unstable or boundary-sensitive.

## Plausible interpretation

The run is analyzable and shows a real early Ramsey/readout contrast on r03: `tau=0` is reproducibly low relative to later points across all stored averages, and this is not explained by scan-order drift. The lack of a sustained coherent `1 MHz` carrier over the full `8 us` window suggests either very short T2* on the order of sub-us to about `1 us`, or an early pulse/readout transient that a long-span Ramsey cannot separate cleanly. This would also explain why the 8 us FFT does not provide claim-grade 13C sideband evidence.

The prior `~0.884 MHz` scout feature is not reproduced as a strong coherent line in this det-shifted run, which weakens the case that it was a physical Ramsey carrier. It does not by itself prove the prior feature was an artifact.

## Claims that are not yet supported

- No well-supported numeric T2* value yet. The current data suggest short dephasing, but the fitted value is too dependent on the first few tau points.
- No supported 13C coupling claim. The expected sideband positions are not coherently resolved.
- No supported absence-of-13C claim. If T2* is very short, this Ramsey window may simply be unable to resolve weak sidebands.
- No supported claim that the Ramsey carrier is exactly `1.000 MHz`.
- No definitive claim that the prior `0.884 MHz` component was an artifact; it is only not supported by this follow-up.

## Recommended next action

Do not repeat the same `0..8 us` Ramsey. Run a short-tau Ramsey on the same r03 branch using the fine pODMR frequency `mw_freq = 3.8759 GHz`, with a dense early grid such as `tau = 0..2 us` in `41` to `51` points, `det = 1.0 MHz`, and the same per-average tracking and shot scale if runtime allows. The goal should be to resolve the first `0..1 us` oscillation/envelope and decide whether the early contrast is a real sub-us T2* decay or a pulse/readout transient. Only after that should the project either report a T2* value or close the Ramsey-based 13C attempt as not supported for this NV.
