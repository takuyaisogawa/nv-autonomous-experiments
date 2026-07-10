# Ramsey Review: image145844 reimage r03

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`, `md/knowledge.md`.
- New Ramsey measurement: `measurement/m001.json` raw export from `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
- Run/job metadata: `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control.
- Generated local analysis artifacts: `ramsey_analysis_results.json`, `ramsey_review_timeseries.png`, `ramsey_review_fft.png`.

## Calculations or scripts run

- Used local Python with `numpy`, `scipy`, and `matplotlib` to inspect JSON schema, parse two readout traces, fit simple damped sinusoid models, check FFT peaks, and plot raw/normalized Ramsey traces.
- Sequence text in `m001.json` indicates trace 1 is the true `m_S=0` reference; because `full_experiment=0`, trace 2 is the Ramsey signal after the pulse block.
- Measurement settings confirmed from `m002.json`: `tau=0..6 us`, 31 points, `dt=0.2 us`, `mw_freq=3.876 GHz`, `det=1.5 MHz`, `length_pi_pulse=52 ns`, `4 x 50000` repetitions.
- Sampling check: 31 samples at 0.2 us give Nyquist `2.5 MHz`. The actual discrete FFT bin spacing for the stored 31-point array is `161.29 kHz`; the planned `1/span` scale is `166.7 kHz`.
- Raw/normalized levels:
  - reference mean `45.32 kcps`, range `44.04..47.94 kcps`;
  - signal mean `42.10 kcps`, range `38.10..45.85 kcps`;
  - signal/reference mean `0.929`, range `0.859..0.995`.
- Per-average mean ratios were `0.935`, `0.930`, `0.920`, `0.938`; per-average detrended ratio correlations were weak and mixed, roughly `-0.11..0.26` off diagonal.
- Fixed-frequency ratio fits:
  - at programmed `1.5 MHz`, amplitude `0.0058`, `R2=0.030`;
  - at `1.667 MHz`, amplitude `0.0177`, `R2=0.155`;
  - at approximate sideband bins `1.167 MHz` and `1.833 MHz`, `R2=0.029` and `0.063`.
- Free damped-sinusoid fits prefer about `0.94..0.96 MHz`, not the programmed `1.5 MHz`; ratio fit gives `T ~2.39 us`, `f ~0.941 MHz`, but only `R2=0.446`, so this is descriptive, not claim-grade.
- FFT checks on detrended/windowed data:
  - ratio top bins include `0.968 MHz`, `0.806 MHz`, `0.323 MHz`, `1.935 MHz`, `1.774 MHz`;
  - nearest bins to `det-13C`, `det`, `det+13C` were `1.129`, `1.452`, `1.935 MHz` with ratio FFT amplitudes `0.093`, `0.087`, `0.151`.

## Plausible interpretation

- The Ramsey run completed and produced analyzable data. It was not a zero-average or hardware-aborted failure; final counts were `38.249 kcps`, above the `20 kcps` guard but lower than the pre-Ramsey weak-pODMR final count of `43.890 kcps`.
- There is visible oscillatory/non-flat structure in the raw signal and signal/reference ratio, but it is not coherent enough across averages or tied strongly enough to the programmed `1.5 MHz` detuning to support a robust T2star extraction.
- The dominant descriptive frequency near `0.94 MHz` may reflect detuning error, phase/programming mismatch, drift/noise structure, or an imperfect scout dataset. It should be treated as an empirical feature needing confirmation, not as a physical conclusion.
- The FFT has some power near the upper expected `det + 13C` sideband bin, but comparable or larger structure appears elsewhere and the programmed carrier bin itself is weak. This does not support a 13C coupling claim.

## Claims not yet supported

- No well-supported T2star value is established from this Ramsey scout.
- No well-supported nearby 13C conclusion is established.
- Do not claim the measured Ramsey carrier is `1.5 MHz`; the data do not show a coherent programmed-carrier response.
- Do not interpret the descriptive `~0.94 MHz`, `T ~2.4 us` fit as a validated T2star measurement.
- Do not use normalization-only or single FFT-bin structure as evidence for 13C.

## Recommended next action

Run a targeted Ramsey follow-up on r03 rather than broad candidate search: first repeat a short bounded Ramsey under better drift/SNR conditions with the same weak-pODMR frequency basis but adjust the programmed detuning toward the observed empirical frequency scale, or run a calibration Ramsey designed specifically to verify the phase-ramp/carrier response before attempting a claim-grade longer T2star/13C scan. Keep even averages and raw/readout-aware review; avoid increasing the per-average tracking window blindly.
