# Ramsey review: r03 det=1.0 MHz, 0-8 us, 8 avg

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `context.json`.
- Planning/context evidence: `evidence/e007.json` for the expected Ramsey carrier/13C sideband model and `evidence/e013.md` for the fine-pODMR review plus Ramsey start note.
- New Ramsey measurement:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
  - `measurement/m002.json`: submitted job spec.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json`: terminal bridge status.
  - `measurement/m005.json`: run control state.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs:
  - `ramsey_analysis_summary.json`
  - `ramsey_analysis.png`
- Checks performed:
  - Parsed combined and per-average raw readouts.
  - Used the project protocol inspection readout roles: readout 1 = reference, readout 2 = Ramsey signal.
  - Computed raw signal, signal/reference, and signal/reference-line views.
  - Checked common-mode drift across the 8 stored averages.
  - Ran detrended FFT screens.
  - Ran fixed-frequency least-squares sinusoid screens at:
    - programmed carrier: `1.000 MHz`
    - model 13C sidebands: `0.615423 MHz` and `1.384577 MHz`
    - prior scout component: `0.884 MHz`
  - Ran exploratory damped-cosine fits; these collapsed to the lower decay bound/early-point behavior and were not treated as physical T2star fits.
  - Ran additional scratch checks excluding the first one or two tau points and checking per-average phase consistency.

## Quantitative summary

- Run completed cleanly:
  - terminal result status `completed`
  - no stop requested
  - safe shutdown OK
  - final counts `44.184 kcps`
  - `8` averages x `50000` repetitions
  - tau `0..8 us`, `41` points, step `0.2 us`
  - FFT bin spacing about `121.95 kHz`; span resolution about `125 kHz`; Nyquist about `2.5 MHz`
- Combined readouts:
  - reference mean `49.31 kcps`
  - signal mean `44.58 kcps`
  - signal range `39.31..47.03 kcps`
  - signal/reference mean `0.9042`, standard deviation `0.0294`
- Per-average stability:
  - signal average means ranged `36.20..50.27 kcps`, a `31.6%` common-mode range relative to the combined signal mean
  - signal/reference average means ranged only `0.8909..0.9258`, a `3.9%` range
  - average 7 was the clear low common-mode average; normalized shape RMS did not mark a clear shape outlier
- FFT / frequency checks:
  - normalized signal/reference FFT strongest bins were near `1.098 MHz` and `1.220 MHz`, not cleanly at the exact `1.000 MHz` target
  - fixed-frequency signal/reference amplitudes:
    - `1.000 MHz`: amplitude `0.00916`, z about `1.39`, R2 `0.053`
    - `0.615423 MHz`: amplitude `0.01105`, z about `1.67`, R2 `0.074`
    - `1.384577 MHz`: amplitude `0.00843`, z about `1.28`, R2 `0.046`
    - `0.884 MHz`: amplitude `0.00742`, z about `1.10`, R2 `0.035`
  - fixed-frequency signal/reference-line amplitudes were similarly weak; the lower sideband-like component was about `0.00970` with z about `1.65`.
  - Per-average phases were not consistent enough for a physical sideband claim. For the lower sideband check, the circular phase concentration was only about `0.43`.

## Plausible interpretation

This Ramsey run is analyzable and useful as a diagnostic, but it still does not provide claim-grade Ramsey oscillation evidence. The expected `1.0 MHz` carrier is not strongly recovered in the fixed-frequency fits. The strongest normalized FFT bins near `1.1-1.2 MHz` are close to, but not cleanly locked to, the programmed carrier, and fixed-frequency carrier amplitude is only about `0.9%` in signal/reference with low explanatory power.

The weak lower-sideband-like content near the expected `0.615 MHz` 13C sideband is also not enough to claim coupling. Its combined amplitude is only about `1.1%` in signal/reference, below a 2-sigma fixed-frequency screen, and the per-average phase/strength consistency is weak. The large raw common-mode average-to-average count motion means raw-channel oscillation and decay fits should be treated cautiously; normalization helps but does not create a robust physical signal.

The exploratory damped-cosine fits should not be used for T2star. They are driven by the low first tau point / early transient and hit unphysical or boundary-like short decay times rather than a supported Ramsey envelope.

## Claims not yet supported

- No supported numeric T2star claim from this measurement.
- No supported nearby 13C conclusion from this measurement.
- No supported assignment of the prior `~0.884 MHz` scout component as physical.
- No supported claim that the det-shifted Ramsey carrier cleanly follows the programmed `1.0 MHz` phase ramp.
- No supported Hamiltonian/coupling extraction.

## Recommended next action

Do not repeat the same long Ramsey blindly. First run a targeted Ramsey/protocol diagnostic on the same accepted r03 branch: verify the live Ramsey sequence/phase-ramp behavior and use a short, higher-SNR, densely sampled Ramsey control that should show an unmistakable programmed carrier before attempting another T2star/13C acquisition. If that diagnostic still fails to recover the carrier, pause T2star/13C claims and investigate sequence/IQ phase implementation, resonance freshness, or readout/transient artifacts before spending more acquisition time.
