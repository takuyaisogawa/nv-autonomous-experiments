# Ramsey Review: r03 T2star Scout

## Files/data used

- `project/state.md`: project context, accepted r03 candidate, weak-pi pODMR grid resonance at `3.876 GHz`, planned Ramsey settings, expected `13C` Larmor scale near `0.385 MHz`.
- `measurement/m001.json`: raw export for `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
- `measurement/m002.json`: submitted Ramsey job contract.
- `measurement/m003.json`: terminal bridge result; status `completed`, final counts `38.249 kcps`.
- `measurement/m004.json`: final run status; elapsed `2124 s`.
- `measurement/m005.json`: run control; no stop requested.
- Derived local artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed the saved scan: `tau = 0..6 us`, step `0.2 us`, `31` points, `4` averages, `50000` repetitions, two readout channels.
- Confirmed saved variables include `mw_freq = 3.876e9 Hz`, `det = 1.5e6 Hz`, `length_pi_pulse = 52 ns`, `mod_depth = 1`, `full_experiment = 0`, and `do_adiabatic_inversion = 1`.
- Computed combined signal/reference ratio and per-average signal/reference ratios.
- Fitted the combined normalized ratio to a Gaussian-decay cosine.
- Ran a Hann-windowed FFT on the combined normalized ratio and on each average.
- Checked nearest FFT bins to the planned carrier and expected sideband scale: `1.115 MHz`, `1.500 MHz`, and `1.885 MHz`.

## Quantitative checks

- Final count text is `38.249 kcps`, down from the prior weak-pODMR final count `43.890 kcps` by about `12.9%`.
- Combined readout means: signal `45.318 kcps`, reference `42.098 kcps`.
- Combined normalized signal/reference peak-to-peak span is `14.70%`; standard deviation is `3.65%`.
- Per-average signal/reference traces correlate only moderately with the combined trace:
  - avg 1: `r = 0.707`
  - avg 2: `r = 0.418`
  - avg 3: `r = 0.546`
  - avg 4: `r = 0.605`
- Descriptive combined fit: frequency `0.946 MHz`, `T2star = 3.12 us`, amplitude `5.79%`, `R2 = 0.427`.
- FFT bin spacing is `0.161 MHz`; Nyquist is `2.419 MHz`.
- Combined FFT top bins include `0.968 MHz`, `0.323 MHz`, `0.161 MHz`, `0.806 MHz`, and `1.935 MHz`.
- Sideband-bin amplitudes:
  - `1.115 MHz` target -> nearest `1.129 MHz`, amplitude `0.091`
  - `1.500 MHz` target -> nearest `1.452 MHz`, amplitude `0.097`
  - `1.885 MHz` target -> nearest `1.935 MHz`, amplitude `0.163`
- Individual-average FFT peaks are inconsistent. Avg 2 has a strong `1.452 MHz` bin, but avg 1 favors `0.968/0.806 MHz`, avg 3 favors `0.323/1.129/1.290 MHz`, and avg 4 favors `0.161/0.806/0.323 MHz`.

## Plausible interpretation

The Ramsey scout contains an oscillatory signal in the normalized signal/reference ratio, but it is not yet a clean detuned Ramsey trace at the planned `1.5 MHz` carrier. The combined fit prefers about `0.95 MHz` and has weak explanatory power (`R2 ~ 0.43`). The per-average behavior shows real structure but not stable frequency content across averages, and the final counts dropped substantially during/relative to the preceding context.

This is best treated as an analyzable but non-claim-grade Ramsey scout. It supports that r03 still produces Ramsey-scale contrast, but it does not yet support a precise T2star value or a 13C conclusion.

## Claims that are not yet supported

- A final `T2star = 3.12 us` claim is not supported; the value is only a descriptive fit to a noisy/inconsistent scout.
- A resolved `13C` coupling claim is not supported. The `1.935 MHz` FFT bin is near the expected high sideband, but per-average inconsistency and comparable low-frequency/other peaks prevent assignment.
- A no-13C conclusion is also not supported; the scan length and SNR are insufficient for a decisive absence claim.
- The planned `det = 1.5 MHz` carrier is not cleanly recovered, so any frequency-domain interpretation must remain provisional until the detuning mismatch/frequency content is understood.

## Recommended next action

Before committing to a longer T2star/13C acquisition, run a targeted Ramsey repeat on r03 with better diagnostic leverage:

- retrack/check counts first, since the final count dropped to `38.249 kcps`;
- keep `mw_freq = 3.876 GHz` unless a quick pODMR check shows resonance movement;
- repeat Ramsey with enough SNR and span to distinguish the carrier and sidebands, while preserving per-average readout export;
- consider two short diagnostic Ramsey repeats with different detunings, for example keeping one at `1.5 MHz` and one shifted, to verify that the observed FFT peak follows programmed detuning rather than drift/artifact;
- only fit/report T2star after the carrier frequency is reproducible across averages.
