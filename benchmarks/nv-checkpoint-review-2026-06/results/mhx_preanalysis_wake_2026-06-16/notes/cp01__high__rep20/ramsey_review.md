# Ramsey Review

## Files/data used

- `project/brief.md`, `project/advice.md`, and `project/state.md` for the objective, candidate history, and prior decisions.
- `measurement/m001.json` for the raw exported Ramsey savedexperiment data.
- `measurement/m002.json` for the submitted Ramsey contract: r03, `mw_freq = 3.876 GHz`, `det = 1.5 MHz`, `tau = 0..6 us`, 31 points, `4 x 50000`, `full_experiment = 0`.
- `measurement/m003.json`, `measurement/m004.json`, and `measurement/m005.json` for terminal status/result/control: job completed without abort; final count text was `38.249 kcps`.
- Scratch outputs created here: `ramsey_analysis_summary.txt`, `ramsey_analysis_points.csv`, and `ramsey_analysis.png`.

## Calculations or scripts run

- Used local Python to parse `measurement/m001.json`, extract the two readouts, per-average arrays, tau axis, and snake scan order.
- Treated readout 0 as the 0-level reference and readout 1 as the Ramsey readout for this `full_experiment = 0` sequence. Reviewed raw readouts and `signal/reference`.
- Checked basic acquisition numbers:
  - 31 tau points from `0.0` to `6.0 us`, `dt = 0.200 us`.
  - Sampling Nyquist `2.5 MHz`; actual 31-point rFFT bin step `161.3 kHz`, highest rFFT bin `2.419 MHz`.
  - Mean reference `45.318`, mean Ramsey readout `42.098`, mean ratio `0.92919`.
  - Median point SEM of the per-average ratio `0.02557`, max `0.06023`.
- Checked per-average consistency:
  - Ratio means by average: `0.93474`, `0.92983`, `0.91990`, `0.93773`.
  - Per-average ratio correlations were weak or negative, ranging from about `-0.09` to `0.28` off diagonal.
  - Acquisition-order ratio trend deltas were `+4.6%`, `+6.4%`, `+1.3%`, and `-5.6%` of mean for averages 1-4.
- Ran FFT checks after linear detrending and Hann windowing:
  - Top normalized-ratio FFT bins: `0.968`, `0.806`, `0.323`, `1.935`, `1.774`, `0.161`, `0.645`, `1.613 MHz`.
  - Expected checks using `det = 1.5 MHz` and prior expected `13C` separation near `0.385 MHz`:
    - `det - 13C`: target `1.115 MHz`, nearest `1.129 MHz`, rank 11 among nonzero bins.
    - `det`: target `1.500 MHz`, nearest `1.452 MHz`, rank 12.
    - `det + 13C`: target `1.885 MHz`, nearest `1.935 MHz`, rank 4.
  - Per-average FFT peak frequencies were not consistent: avg 1 peaked at `0.968 MHz`, avg 2 at `1.452 MHz`, avg 3 at `0.323 MHz`, avg 4 at `0.806 MHz`.
- Tried descriptive damped-cosine fits to the normalized ratio:
  - Free damped cosine: `R2 = 0.397`, fit frequency `0.900 MHz`, fitted decay `~2.04 us`.
  - Near-det damped cosine constrained to `1.2..1.8 MHz`: `R2 = 0.173`, fitted frequency `1.681 MHz`, fitted decay `~2.74 us`.
  - Fixed `1.5 MHz` damped cosine: `R2 = 0.190`, fitted decay `~0.50 us`.

## Plausible interpretation

- The Ramsey scout completed and is analyzable, but it is not claim-grade.
- The normalized mean trace has fluctuations on the same order as the per-average scatter, and the four stored averages do not share a stable oscillation pattern.
- The expected deliberate Ramsey carrier near `1.5 MHz` is not a dominant feature in the averaged FFT. Only one of four averages has its strongest FFT bin at the detuning bin.
- The `1.935 MHz` bin is close to the expected high-side `det + 13C` location, but it is not enough by itself: the carrier bin is weak, the low-side sideband is weaker, and per-average FFT peaks are inconsistent.
- The final count dropped to `38.249 kcps` from the prior weak-pi pODMR final `43.890 kcps`. This is still above the minimum gate but supports treating drift/count changes as a likely contributor to the poor Ramsey consistency.

## Claims not yet supported

- No well-supported `T2*` value is established from this Ramsey run. The fitted decay constants depend strongly on fit constraints and are not anchored by a stable expected carrier.
- No supported nearby-`13C` conclusion is established. The FFT does not show a robust carrier plus symmetric/consistent sideband structure.
- This run does not invalidate r03 as the aligned candidate; prior strong-pi and weak-pi pODMR evidence still support r03 as the current target.
- This run does not support moving to a final report or claiming absence of `13C`; it is a noisy/non-claim-grade Ramsey scout.

## Recommended next action

Do a short r03 health check before spending more Ramsey time: TrackCenter/count check, then a compact weak-pi pODMR spot check around `3.876 GHz` to confirm the resonance has not shifted after the count drop. If r03 is still healthy and the weak-pi center is stable, repeat Ramsey under lower drift risk with a predeclared acceptance criterion: the 1.5 MHz carrier should be visible in the averaged trace and in most individual averages before fitting `T2*` or interpreting `13C` sidebands. Do not escalate to `13C`-specific claims or sequences until a cleaner Ramsey carrier is obtained.
