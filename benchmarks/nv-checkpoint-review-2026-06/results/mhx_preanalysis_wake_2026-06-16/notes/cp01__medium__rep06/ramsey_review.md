# Ramsey Review

## Files/Data Used

- Project context: `context.json`, `project/state.md`, `project/brief.md`, `project/advice.md`.
- Current Ramsey measurement: `measurement/m001.json` raw savedexperiment export, plus `measurement/m002.json` job contract, `measurement/m003.json` terminal result, `measurement/m004.json` status, and `measurement/m005.json` control.
- Local scratch outputs created here: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_review_plot.png`, and `analysis_stdout.txt`.

## Calculations/Scripts Run

- Ran `python analyze_ramsey.py`.
- Parsed the Ramsey export for `ramsey.xml`, tau `0..6 us`, `31` points, `4 x 50000` shots, `mw_freq = 3.876 GHz`, `det = 1.5 MHz`, `full_experiment = 0`.
- Treated readout channel 0 as the bright/reference readout and channel 1 as the Ramsey readout; analyzed `signal/reference`.
- Checked combined and per-average normalized Ramsey traces, per-average mean levels, snake acquisition-order first-vs-second-half drift, windowed FFT, and a bounded decaying-cosine fit used only descriptively.

Key numbers:

- Terminal run completed without abort; final count text was `38.249 kcps`, above the job gate but lower than the preceding weak-pODMR context around `43.890 kcps`.
- Combined reference mean `45.318 kcps`; Ramsey signal mean `42.098 kcps`; mean `signal/reference = 0.9292`.
- Combined normalized `signal/reference` peak-to-peak is `0.146` fractional.
- Per-average mean ratios are `0.9347`, `0.9298`, `0.9199`, `0.9377`; per-average normalized peak-to-peak spans are large, `0.244..0.315`.
- Acquisition-order half-scan ratio shifts are `+2.7%`, `+4.3%`, `+1.0%`, and `-4.3%`, so drift/common-mode changes are not negligible.
- FFT uses `dt = 0.2 us`, Nyquist `2.5 MHz`, and actual `rfftfreq` bin spacing `161.29 kHz` for 31 samples. The combined trace has top windowed FFT peaks at `0.968`, `0.806`, `0.323`, `0.161`, `1.935`, and `1.774 MHz`.
- Per-average FFT peaks are inconsistent: avg 2 has a top peak near `1.452 MHz`, but avg 1 favors `0.968 MHz`, avg 3 favors `0.323/1.129/1.290 MHz`, and avg 4 favors low-frequency/`0.806 MHz`.
- Descriptive decaying-cosine fit to the combined normalized trace gives frequency `0.941 MHz`, `T2* = 2.39 us`, amplitude `7.25%`, `R2 = 0.446`, RMSE `0.0268`; the `T2*` standard error is about `1.19 us`.

## Plausible Interpretation

This scout plausibly contains a weak Ramsey-like oscillatory signal in the accepted r03 NV data, but it is not a clean, claim-grade Ramsey measurement. The fitted oscillation is closer to `0.94 MHz` than the requested `1.5 MHz` detuning, the fit explains less than half the combined variance, and individual averages do not agree on a dominant FFT frequency. The signal scale is comparable to drift/average-level instability, so a descriptive `T2* ~2.4 us` is useful for planning only, not as a final result.

The expected 13C-sideband scale from the project model was around `det +/- 0.385 MHz`, i.e. roughly `1.115 MHz` and `1.885 MHz`. The combined FFT has some power near `1.935 MHz`, and one average has power near the requested carrier, but the dominant combined peak is around `0.968 MHz` and the per-average spectra are not reproducible. That is insufficient for a supported 13C conclusion.

## Claims Not Yet Supported

- A final T2* value for r03 is not supported by this scout.
- A resolved 13C coupling/sideband conclusion is not supported.
- The observed `0.94 MHz` fitted frequency should not yet be claimed as a true detuning shift; it may reflect low SNR, drift, finite-window leakage, or residual calibration/frequency offset.
- The absence of a 13C feature is also not supported; this measurement is too weak/inconsistent to rule one out.

## Recommended Next Action

Do not make final T2* or 13C claims from this run. Keep r03 as the aligned candidate, then run a confirmatory Ramsey follow-up after a fresh track/count sanity check. Use this scout only to plan the follow-up: preserve raw/readout-aware analysis, keep even snake-ordered averages, and choose a Ramsey setting that reduces ambiguity around the observed `~0.9..1.5 MHz` oscillation band while improving reproducibility across averages. A short fresh pODMR or frequency sanity check before the repeat would help determine whether the `0.94 MHz` apparent frequency is a real microwave-center offset or just a noisy scout artifact.
