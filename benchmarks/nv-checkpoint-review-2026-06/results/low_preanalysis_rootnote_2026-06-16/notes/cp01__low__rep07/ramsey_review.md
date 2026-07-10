# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, plus Ramsey-related guardrails from `md/knowledge.md`.
- New Ramsey measurement: `measurement/m001.json`, raw export for `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
- Ramsey job/provenance files: `measurement/m002.json` job contract, `measurement/m003.json` terminal result, `measurement/m004.json` final status, `measurement/m005.json` control.
- Scratch outputs created here: `ramsey_analysis_summary.txt` and `ramsey_analysis.png`.

## Calculations or scripts run

- Parsed `measurement/m001.json` with Python/numpy/scipy.
- Extracted `ExperimentData` and `ExperimentDataEachAvg`; used signal/reference as the main Ramsey trace.
- Confirmed scan shape: `tau = 0..6 us`, `31` points, `dt = 0.2 us`, `4` averages, `50000` repetitions, `mw_freq = 3.876 GHz`, `det = 1.5 MHz`.
- Checked per-average normalized traces and snake acquisition-order first-half vs second-half drift proxies.
- Fit signal/reference to exponential-decay cosine, Gaussian-decay cosine, and no-decay cosine.
- Computed Hann-window FFT after mean/linear detrending; checked native-bin and zero-padded amplitudes near `1.5 MHz` and expected `1.5 +/- 0.385 MHz` sidebands.

Key numeric results from `ramsey_analysis_summary.txt`:

- Mean signal/reference ratio `1.077617`; peak-to-peak normalized variation `14.72%`.
- Signal channel range `44.038..47.942 kcps`; reference channel range `38.096..45.846 kcps`. The reference channel varies more strongly than the signal channel.
- Per-average ratio correlations to the mean trace: avg1 `0.71`, avg2 `0.42`, avg3 `0.55`, avg4 `0.60`.
- Acquisition-order first-half to second-half ratio shifts: avg1 `-3.15%`, avg2 `-4.08%`, avg3 `-1.13%`, avg4 `+4.77%`.
- Exponential-cosine fit to signal/reference: `f = 0.947 +/- 0.035 MHz`, `T2* = 2.29 +/- 1.11 us`, `R2 = 0.435`.
- Gaussian-cosine fit: `f = 1.679 +/- 0.058 MHz`, `T2* = 3.46 +/- 2.01 us`, `R2 = 0.191`.
- Plain 1.5 MHz-ish cosine fit: `f = 1.496 +/- 0.138 MHz`, amplitude `0.0072 +/- 0.0105`, `R2 = 0.017`.
- Zero-padded FFT top peaks above `0.2 MHz`: `0.925 MHz`, `0.270 MHz`, `1.891 MHz`, `2.423 MHz`.
- Expected-bin amplitudes: carrier `1.500 MHz -> 0.0133`; lower sideband `1.115 MHz -> 0.0137`; upper sideband `1.885 MHz -> 0.0222`.

## Plausible interpretation

- The Ramsey run completed and is analyzable, but the trace is not claim-grade for T2star or 13C.
- There is real structure in signal/reference, but the strongest fit/FFT feature is near `0.93..0.95 MHz`, not the programmed `1.5 MHz` Ramsey detuning.
- The reference channel itself has a large oscillatory/structured variation and fits near `0.96 MHz` with higher apparent contrast than the signal channel; therefore the strongest normalized feature may be readout/reference artifact or common-mode drift rather than clean NV Ramsey precession.
- The expected upper 13C sideband region near `1.885 MHz` appears in the mean FFT, but it is not reproducibly dominant across averages. Avg2 supports `1.45/1.94 MHz` bins, while avg1/avg4 are dominated by lower-frequency bins and avg3 is mixed. This is suggestive at most, not evidence for a nearby 13C.
- A loose exponential-cosine fit gives `T2* ~2.3 us`, but the frequency mismatch, modest `R2`, large uncertainty, and reference-driven behavior make this a descriptive fit only.

## Claims not yet supported

- No well-supported T2star value is established from this Ramsey scout.
- No well-supported nearby-13C conclusion is established.
- The `1.89 MHz` FFT feature should not be claimed as a 13C sideband yet.
- The `0.95 MHz` feature should not be treated as the NV Ramsey detuning without explaining why it is stronger in the reference channel than in the signal channel.

## Recommended next action

Repeat a targeted Ramsey on accepted r03 under better claim conditions rather than making a conclusion from this scout. Keep the same weak-pi resonance basis (`mw_freq = 3.876 GHz`) but improve robustness: use more averages if advisory permits, retain enough tau span/resolution to separate `det` and `det +/- f13C`, and inspect raw signal and reference channels before accepting any normalized FFT peak. If runtime allows, a cleaner follow-up would use a tau grid that keeps Nyquist above `det + ~0.385 MHz` while increasing average count or reducing per-average drift exposure.
