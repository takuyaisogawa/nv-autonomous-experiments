# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `context.json`, and relevant project memory/knowledge text.
- New terminal Ramsey data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job contract, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control.
- Generated local analysis artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis_console.txt`, `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed Ramsey scan: `ramsey.xml`, `tau = 0..8 us`, 41 points, `dt = 0.2 us`, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `8 x 50000` repetitions, snake scan order, final terminal count `44.184 kcps`.
- Used embedded sequence order to treat readout 1 as the mS=0/reference readout and readout 2 as the post-Ramsey signal.
- Computed raw channel means, signal/reference ratio, per-average ratio traces, common-mode average drift, FFT of linearly detrended ratio data, targeted linear least-squares sinusoid amplitudes at `1.0 MHz`, `0.615 MHz`, `1.385 MHz`, and prior `0.884 MHz`, plus an exploratory frequency scan and an exploratory damped-cosine fit.

## Plausible interpretation

- The run completed safely and returned analyzable data. Combined means were reference `49.31 kcps`, signal `44.58 kcps`, and signal/reference ratio `0.9042 +/- 0.0294` across tau.
- There is substantial average-to-average common-mode count motion; average 7 is `-18.4%` versus the median common-mode level and is drift-flagged by a simple `>15%` check. Ratio means are less variable (`0.891..0.926`), so ratio-domain analysis is more appropriate than raw signal alone.
- The exact programmed carrier is weak in the combined ratio trace: targeted `1.0 MHz` fit amplitude `0.0092`, amplitude t-stat `1.39`, `R2 = 0.053`.
- The expected 13C sidebands are not supported in this run: targeted `0.615 MHz` amplitude `0.0111`, t-stat `1.68`, `R2 = 0.074`; targeted `1.385 MHz` amplitude `0.0084`, t-stat `1.28`, `R2 = 0.046`.
- The prior scout's `~0.884 MHz` component is also weak here: amplitude `0.0074`, t-stat `1.10`, `R2 = 0.035`, so the det-shift test does not support a fixed `0.884 MHz` feature.
- The strongest exploratory component is instead near `1.17..1.19 MHz`: least-squares scan best around `1.175..1.180 MHz` with amplitude about `0.0225`, t-stat about `4.0`, `R2 ~ 0.31`, and per-average phase coherence about `0.91`. Removing the common-mode-low average 7 leaves this feature similar.
- An exploratory damped-cosine fit gives `f = 1.187 +/- 0.027 MHz`, `T2* = 2.27 +/- 0.81 us`, `R2 = 0.49`; excluding average 7 gives `T2* = 2.36 +/- 0.90 us`. This is a useful hypothesis, not a final claim, because the fitted frequency is offset from the programmed `1.0 MHz` carrier and the data contain drift/nonideal average behavior.

## Claims not yet supported

- A final T2* value is not yet supported. The current data suggest a possible few-us decay, but the carrier mismatch and modest fit quality make the fit exploratory.
- A positive 13C coupling claim is not supported. The targeted sideband checks near `0.615 MHz` and `1.385 MHz` are weak and not average-consistent enough for a claim.
- A final negative 13C conclusion is also not fully supported from this single det-shifted Ramsey run; the fair statement is no detectable 13C sideband evidence in this measurement.
- The exact microwave resonance offset is not established by this Ramsey alone, even though the strongest exploratory component being near `1.18 MHz` suggests the effective Ramsey carrier may not match the nominal `det = 1.0 MHz`.

## Recommended next action

Do not promote T2* or 13C claims yet. Run a bounded Ramsey frequency diagnostic on the same accepted r03 NV: repeat a short `tau = 0..8 us` Ramsey with the same `det = 1.0 MHz` while shifting `mw_freq` around `3.8759 GHz` by roughly `+/-0.2 MHz`, or otherwise use an equivalent two-point det/mw-frequency diagnostic. Require the observed carrier to move predictably and reproduce per-average phase coherence before taking a final T2* fit. If the `~1.18 MHz` feature reproduces cleanly, then run the final T2* acquisition at the calibrated setting and re-check 13C sidebands.
