# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `context.json`.
- Prior measurement context: `evidence/e003.json` weak-pi pODMR review supporting the 3.876 GHz grid resonance for r03; `evidence/e005.json` Ramsey model/advisory; `evidence/e009.json` job spec; `evidence/e010.json` running status snapshot; `evidence/e011.json` batch state snapshot.
- New Ramsey data and run metadata: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` terminal status, `measurement/m005.json` run control.
- Scratch outputs created here: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed the raw export from `measurement/m001.json`.
- Used `tau = 0..6 us`, 31 points, step `0.2 us`, 4 averages x 50000 repetitions.
- Treated readout 1 as the `m_S=0` reference and readout 2 as the Ramsey signal, consistent with `full_experiment=0` and the saved `ramsey.xml` sequence text.
- Computed raw readout means, `signal/reference`, per-average `signal/reference`, linear-detrended Hann-window FFTs, expected-detuning and expected-13C-sideband bin amplitudes, per-average FFT peak locations, per-average correlations, and a diagnostic Gaussian-damped cosine fit.

Key numerical checks:

- Run completed without abort; savedexperiment path is `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`; final count text was `38.249 kcps`, above the 20 kcps gate but below the earlier r03 weak-pODMR final `43.890 kcps`.
- The terminal status elapsed time was `2124 s`; effective per-average time was about `531 s`, above the pre-enqueue suggested 450 s drift cap and above the runtime estimate of `492.946 s`.
- Combined raw readout means: reference `45.318 kcps`, signal `42.098 kcps`.
- Combined `signal/reference`: mean `0.9292`, min `0.8591`, max `0.9946`, peak-to-peak `0.1355`.
- FFT spacing from the actual 31-point DFT is `161.3 kHz`; the nominal 6 us span resolution is `166.7 kHz`; odd-length rFFT highest positive bin is `2.419 MHz` while the sampling Nyquist from `dt=0.2 us` is `2.5 MHz`.
- Combined detrended `signal/reference` FFT top peaks: `0.968 MHz`, `0.806 MHz`, `0.323 MHz`, `1.935 MHz`, `1.774 MHz`, `0.161 MHz`.
- Planned detuning target `1.5 MHz` maps to the `1.452 MHz` bin, but that bin is only rank 12 in the combined normalized FFT.
- Expected 13C sideband bins for `det +/- 0.385 MHz`: `1.129 MHz` rank 11 and `1.935 MHz` rank 4. The upper-side bin is present but not paired by a lower-side feature and overlaps a strong reference-readout FFT feature.
- Per-average normalized FFT maxima are inconsistent: avg 1 `0.968 MHz`, avg 2 `1.452 MHz`, avg 3 `0.323 MHz`, avg 4 `0.806 MHz`. Only average 2 has the planned detuning bin as its largest peak.
- Per-average normalized trace correlations are weak or mixed, roughly `-0.09` to `0.28` off diagonal.
- A free Gaussian-damped cosine fit returns `f = 0.939 MHz`, `T2* = 3.20 +/- 1.06 us`, `R2 = 0.445`, and RMSE `0.0249` in ratio units. This is diagnostic only, not claim-grade.

## Plausible interpretation

The Ramsey acquisition is real and the trace is not flat: the raw signal and `signal/reference` both show structure at the several-percent to 10-percent scale. However, the structure is not dominated by the deliberately programmed `det = 1.5 MHz` Ramsey carrier, and it is not consistent across the four stored averages. The strongest combined normalized FFT feature is near `0.97 MHz`, and the raw signal FFT also has strong low-frequency components.

The most plausible current interpretation is a non-claim-grade Ramsey scout with mixed physical and technical contributions. A real Ramsey beat may be present, but the carrier mismatch, weak average-to-average repeatability, reference spectral structure, count drift, and over-cap per-average time make it unsafe to promote the fit-derived `T2*` or any FFT sideband assignment.

The `1.935 MHz` bin is near the expected `det + 13C` sideband, but because the expected carrier at `1.5 MHz` is weak, the lower sideband is not comparably present, and the reference readout has strong nearby high-frequency content, this is not sufficient 13C evidence.

## Claims that are not yet supported

- No well-supported numeric `T2*` is established from this Ramsey scout.
- The diagnostic fit result `T2* ~3.2 us` is not supported as a project conclusion.
- No well-supported nearby-13C conclusion is established.
- The FFT peak near `1.935 MHz` should not be claimed as a 13C sideband.
- The data also do not support a negative claim that there is no 13C coupling; this scout is not clean enough for that.
- The programmed `det = 1.5 MHz` carrier is not validated by this dataset as the dominant Ramsey frequency.

## Recommended next action

Do not run a blind longer T2* acquisition yet. First run a targeted Ramsey-frequency diagnostic on r03 after fresh tracking and, ideally, a quick resonance check if counts or temperature have moved: use a shorter per-average tracking window and deliberately test whether the Ramsey FFT peak follows the programmed detuning. For example, acquire two bounded same-span Ramsey scouts with different `det` values while keeping the same weak-pODMR frequency basis, or refresh the weak-pi pODMR center before choosing the next Ramsey detuning. Only after the carrier behavior is validated should the project spend time on a higher-SNR or longer-span T2*/13C measurement.
