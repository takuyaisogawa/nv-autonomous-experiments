# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `context.json`.
- Ramsey measurement: `measurement/m001.json` raw export, `measurement/m002.json` job contract, `measurement/m003.json` terminal bridge result, `measurement/m004.json` terminal status, `measurement/m005.json` stop-control state.
- Prior support/context: `evidence/e005.json` Ramsey model/advisory and `evidence/e009.json` copied job contract. The readout role used here is the project-inspected Ramsey contract: readout1 reference, readout2 Ramsey signal for `full_experiment=0`.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis_summary.json` and `ramsey_analysis.png`. The PNG was generated with the noninteractive Matplotlib `Agg` backend; direct image viewing from this environment failed with a local permission error, so conclusions below use the JSON/numeric checks.
- Core checks:
  - Loaded 31 tau points from 0 to 6 us, step 0.2 us, 4 averages x 50000 repetitions, snake scan order.
  - Computed raw readout means, signal/reference trace, per-average ratio traces, SEM across averages, FFTs of the normalized trace, and simple cosine / damped cosine fits.
  - Actual DFT bin spacing from 31 samples at 0.2 us is 161.3 kHz; the planning shorthand `1 / 6 us` is 166.7 kHz. Highest positive FFT bin is 2.419 MHz for this odd-length trace; sampling Nyquist is 2.5 MHz.
  - Expected frequencies for the revised run: programmed Ramsey carrier 1.500 MHz, 13C Larmor estimate 0.385 MHz, sidebands near 1.115 MHz and 1.885 MHz.

## Plausible interpretation

- The Ramsey job completed normally. `measurement/m003.json` reports `status=completed`, no abort, safe shutdown OK, final counts 38.249 kcps, above the 20 kcps run gate.
- Raw means are reasonable for this scout: reference mean 45.32 kcps, signal mean 42.10 kcps. Per-average reference means span 43.68 to 46.59 kcps, signal means span 40.55 to 43.36 kcps, and ratio means span 0.920 to 0.938.
- The normalized trace has visible structure and lower late-time variation than early-time variation: signal/reference peak-to-peak is 0.136 overall, with early-half peak-to-peak 0.136 and late-half peak-to-peak 0.057. This is qualitatively compatible with a Ramsey-like oscillation that damps within a few us.
- A damped-exponential cosine fit is the best of the simple fits but is weak: fitted frequency 1.681 +/- 0.035 MHz, T2* 2.74 +/- 1.87 us, amplitude -0.058 +/- 0.028 in signal/reference units, R2 = 0.173. A Gaussian-envelope fit gives T2* 2.27 +/- 0.95 us but lower R2 = 0.071. A no-decay cosine has negative R2. These numbers make a few-us T2* plausible, not established.
- FFT evidence is not clean. In the Hann-windowed normalized FFT, the largest bins are 0.968, 0.806, 0.323, 0.161, and 1.935 MHz. The nearest carrier bin to 1.500 MHz is 1.452 MHz and is below the median nonzero normalized FFT amplitude in the quick cross-check. The nearest upper 13C sideband bin, 1.935 MHz, is a local peak but only about 1.34x the median nonzero normalized FFT amplitude and is not consistently selected by individual averages.

## Claims that are not yet supported

- Do not claim a well-supported T2*. The current fit is model-dependent, has low R2, and returns a large fractional T2* uncertainty.
- Do not claim 13C coupling. The expected sideband pair is not jointly resolved: the upper-sideband-near bin is only weakly elevated, the lower-sideband-near bin is not a clear peak, the carrier is weak in the normalized FFT, and per-average FFT maxima disagree.
- Do not claim the measurement disproves 13C coupling or long T2*. The 6 us / 31 point scout has coarse spectral resolution, low SNR, and only four averages.
- Do not treat the weak fitted frequency offset from the programmed 1.5 MHz carrier as a calibrated resonance correction without a higher-SNR Ramsey or frequency follow-up.

## Recommended next action

Repeat or extend Ramsey on the same accepted r03 target under tighter drift/SNR conditions before making final T2* or 13C claims. A reasonable next measurement is a higher-SNR Ramsey centered on the same weak-pODMR frequency, with either more averages at the same 0..6 us grid or a modestly longer tau span only if the tracking/advisory window is acceptable. The analysis target should be: raw/reference consistency across averages, a stable carrier near the programmed detuning, a defensible envelope fit, and sideband evidence that appears symmetrically around the carrier and repeats across averages.
