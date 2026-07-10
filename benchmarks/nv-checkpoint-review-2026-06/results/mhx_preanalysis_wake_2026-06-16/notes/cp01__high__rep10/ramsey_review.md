# Ramsey Review

## Files/Data Used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Ramsey measurement: `measurement/m001.json` raw savedexperiment export; `measurement/m002.json` job spec; `measurement/m003.json` terminal bridge result; `measurement/m004.json` final status; `measurement/m005.json` run control.
- Prior calibration context: `evidence/e010.json` weak-pi pODMR review supporting `mw_freq = 3.876 GHz`; `evidence/e001.json` weak-pi pODMR terminal result.
- Generated analysis artifacts: `analysis_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis.png`.

## Calculations or Scripts Run

- Ran `python analysis_ramsey.py`.
- Parsed the Ramsey export as `ramsey.xml`, `full_experiment = 0`: readout 1 is the 0-level reference and readout 2 is the Ramsey signal.
- Checked raw signal, point-wise `signal/reference`, and signal normalized by a fitted reference line.
- Fit descriptive damped cosines to raw and normalized traces.
- Ran detrended Hann FFT checks and fixed-frequency sinusoid checks at the planned `det = 1.5 MHz`, the model sideband bins `det +/- 0.385 MHz`, and the observed dominant bin near `0.968 MHz`.
- Checked per-average mean levels, per-average dominant FFT bins, and snake acquisition-order first/last edge changes.

## Quantitative Summary

- Measurement completed cleanly: 31 tau points from `0` to `6 us`, `200 ns` spacing, `4 x 50000` repetitions, `mw_freq = 3.876 GHz`, `det = 1.5 MHz`.
- Sampling gives FFT bin spacing `161.3 kHz` and Nyquist `2.419 MHz` for the exported 31-point grid. Nearest bins: `1.452 MHz` for `det`, `1.129 MHz` for `det - 13C`, and `1.935 MHz` for `det + 13C`.
- Raw signal mean `42.10 kcps`, median per-point SEM across four averages `1.01 kcps`, raw peak-to-peak `7.75 kcps`. Reference mean `45.32 kcps`, reference peak-to-peak `3.90 kcps`.
- Descriptive damped-cosine fits:
  - Raw signal: `f = 0.944 +/- 0.049 MHz`, `T2* = 1.31 +/- 0.49 us`, `R2 = 0.44`.
  - Point-wise ratio: `f = 0.882 +/- 0.032 MHz`, `T2* = 1.97 +/- 0.68 us`, `R2 = 0.38`.
  - Reference-line normalized: `f = 0.962 +/- 0.036 MHz`, `T2* = 2.07 +/- 0.91 us`, `R2 = 0.49`.
- FFT maxima in raw, point-wise ratio, and line-normalized views all occur near `0.968 MHz`, but low-frequency and neighboring bins are comparable.
- Fixed-frequency sinusoid checks are weak at the planned/model bins:
  - Raw signal `R2`: `0.009` at `1.5 MHz`, `0.042` at `1.115 MHz`, `0.042` at `1.885 MHz`, versus `0.293` at `0.968 MHz`.
  - Point-wise ratio `R2`: `0.030` at `1.5 MHz`, `0.042` at `1.115 MHz`, `0.078` at `1.885 MHz`, versus `0.280` at `0.968 MHz`.
- Per-average dominant FFT bins are not stable: averages 1-4 give about `0.968`, `0.484`, `0.161`, and `0.806 MHz`.
- Acquisition-order edge drift within each average is small by the simple common-mode edge check, about `-0.2%` to `-1.3%`, but stored-average mean levels shift by several percent and terminal counts fell to `38.249 kcps` from the prior `43.890 kcps` pODMR final count.

## Plausible Interpretation

- The Ramsey trace likely contains some oscillatory contrast on the `~1 us` period scale, visible most consistently as a broad FFT/fitted feature near `0.9-1.0 MHz` in raw and normalized views.
- The frequency being well below the programmed `1.5 MHz` carrier is plausibly consistent with resonance drift or residual detuning relative to the weak-pi pODMR grid center, rather than a clean centered Ramsey carrier.
- The descriptive decay scale is roughly `T2* ~ 1-2 us`, but the low `R2`, sparse 6 us window, comparable SEM/noise, and inconsistent per-average spectra make this a rough scale estimate only.
- The run is useful as a scout: it shows that r03 can produce Ramsey-like contrast, but it does not yet close the project objective.

## Claims Not Yet Supported

- No well-supported final `T2*` value is established from this run.
- No well-supported nearby `13C` conclusion is established.
- The observed `0.9-1.0 MHz` feature should not be assigned to a `13C` sideband. The expected `det - 13C` bin near `1.129 MHz` and `det + 13C` bin near `1.935 MHz` are not dominant or stable enough.
- The weak-pi pODMR center should not be treated as unchanged during the Ramsey run; the lower-than-planned Ramsey frequency and count drop leave drift/resonance-shift as live explanations.

## Recommended Next Action

Before a longer T2*/13C acquisition, run a short weak-pi pODMR recheck on r03 around `3.876 GHz` to confirm the current resonance after the Ramsey count drop. If the center has shifted, update `mw_freq` and then repeat Ramsey with enough sampling to cover the intended carrier and sidebands. A repeat should preserve an even number of snake-ordered averages and keep per-average tracking windows within the active advisory cap.
