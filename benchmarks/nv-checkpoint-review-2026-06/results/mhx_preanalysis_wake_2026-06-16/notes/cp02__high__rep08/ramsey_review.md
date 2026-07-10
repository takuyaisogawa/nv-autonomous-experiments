# Ramsey Review: r03 det=1.0 MHz follow-up

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/knowledge.md`, `context.json`.
- Prior/supporting evidence: `evidence/e004.json`, `evidence/e006.md`, `evidence/e007.json`, `evidence/e013.md` for the fine pODMR center, readout-role basis, and planned Ramsey checks.
- New measurement data: `measurement/m001.json` raw savedexperiment export; `measurement/m002.json` job spec; `measurement/m003.json` terminal result; `measurement/m004.json` terminal status; `measurement/m005.json` run control.

## Calculations or scripts run

- Created and ran `python analyze_ramsey.py`.
- Outputs: `ramsey_analysis_summary.json` and `ramsey_diagnostics.png`.
- Checks performed:
  - Parsed combined and per-average readouts for `tau = 0..8 us`, 41 points, 8 averages x 50000 repetitions.
  - Used project-context readout roles: readout1 reference, readout2 Ramsey signal for `ramsey.xml` with `full_experiment=0`.
  - Compared raw signal, signal/reference, and signal/fitted-reference-line normalization.
  - Ran scan-order common-mode drift scoring from recorded snake acquisition order.
  - Ran windowed FFTs and exact least-squares sinusoid checks at 0.615 MHz, 0.884 MHz, 1.000 MHz, and 1.385 MHz.
  - Checked per-average amplitude and phase coherence at those same frequencies.
  - Ran diagnostic damped-cosine fits only after signal checks; these were treated as non-claim diagnostics because they were mask/start-frequency dependent.

## Plausible interpretation

- The measurement completed safely: terminal status `completed`, final counts `44.184 kcps`, safe shutdown true.
- The dataset is analyzable and not obviously invalidated by common-mode drift. No average crossed the 0.15 drop-fraction drift flag threshold; largest drop score was about 0.039.
- There is a strong low point at `tau=0` in the normalized trace (`signal/ref = 0.8025`, while the full trace range is 0.8025..0.9721). Excluding this point materially changes the spectral/fitting diagnostics, so tau=0 should not be allowed to drive a T2* claim.
- The prior scout's non-claim `~0.884 MHz` component is not reproduced coherently. With tau=0 excluded in signal/refline normalization, exact 0.884 MHz adds only `R2 ~0.001`, with coherent per-average amplitude `0.0012` versus mean individual amplitude `0.0123`.
- The programmed `1.0 MHz` Ramsey carrier is weak in exact-frequency checks. With tau=0 excluded in signal/refline normalization, exact 1.000 MHz adds only `R2 ~0.011`; the FFT has nearby carrier-like bins around `1.125` and `1.25 MHz`, and signal/ref gives a best single-tone near `1.188 MHz`, but this is not a clean one-for-one detuning confirmation.
- The expected 13C sideband pair is not supported. The lower model sideband near `0.615 MHz` has some coherent-looking amplitude in a few checks (`R2 ~0.13` with tau=0 excluded in signal/refline), but the upper sideband near `1.385 MHz` is absent/phase-incoherent (`R2 ~0.005`, phase resultant ~0.07). A single weak lower-side feature without its paired upper sideband is not claim-grade 13C evidence.
- Damped-cosine fits are unstable: depending on tau mask and starting frequency, fitted frequencies range around `0.486`, `0.711`, `1.145`, and `1.195 MHz`, and T2* estimates range from a few us to tens of us. This supports "not yet fit-constrained" rather than a T2* value.

## Claims that are not yet supported

- No well-supported T2* value from this Ramsey run.
- No claim of nearby 13C coupling or resolved 13C sidebands.
- No claim that the Ramsey carrier is exactly the programmed `1.0 MHz` detuning.
- No claim that the earlier `~0.884 MHz` scout feature is physical; the det-shifted run argues against it being a stable coherent feature.
- No sub-grid resonance-frequency claim beyond the existing fine pODMR-supported `mw_freq = 3.8759 GHz` grid choice.

## Recommended next action

Do not repeat another long 13C/T2* Ramsey blindly. First run a short same-NV Ramsey frequency/phase diagnostic after confirming the pODMR center has not drifted: skip or separately handle `tau=0`, use a denser tau grid, and test two programmed detunings so the fitted carrier must shift one-for-one with the requested detuning before attempting a T2* fit or 13C sideband claim.
