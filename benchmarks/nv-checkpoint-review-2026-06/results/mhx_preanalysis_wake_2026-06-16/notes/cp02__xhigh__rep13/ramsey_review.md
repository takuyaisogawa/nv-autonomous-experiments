# Ramsey Review: det=1.0 MHz r03 follow-up

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/state.md`, `project/advice.md`.
- Prior context: `evidence/e004.json` / `evidence/e006.md` for fine weak-pi pODMR center at `3.8759 GHz`; `evidence/e007.json` / `evidence/e013.md` for the second Ramsey model/advisory and readout-role inspection.
- New Ramsey data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, plus `measurement/m004.json` and `measurement/m005.json` status/control snapshots.
- The new run completed as `ramsey.xml`, `tau = 0..8 us` in 41 points (`dt = 0.2 us`), `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `8 x 50000` repetitions, final counts `44.184 kcps`.
- Readout roles from the local sequence/context: readout 1 is the `mS=0` reference and readout 2 is the Ramsey signal for `full_experiment=0`.

## Calculations/scripts run

- Created and ran `analyze_ramsey.py`.
- Wrote `ramsey_analysis.json` and `ramsey_analysis.png`.
- Parsed raw/reference readouts, point-wise `signal/reference`, fitted-reference-line normalization, stored-average traces, scan order, FFT spectra, and least-squares sinusoid amplitudes.
- Used the project model from `evidence/e007.json`: expected `13C` Larmor `384.577 kHz`, so expected Ramsey features are carrier `1.000 MHz` and sidebands `0.615423 MHz` / `1.384577 MHz`; prior scout component to check was `~0.884 MHz`.

Key quantitative checks:

- Combined raw signal mean `44.58 kcps`, peak-to-peak `7.72 kcps` (`17.3%` of mean); exported signal point-error scale is about `1.87 kcps`.
- Direct least-squares amplitudes in raw signal:
  - `0.615423 MHz`: `0.475 +/- 0.287 kcps`, amplitude SNR `1.66`, `R2 = 0.156`.
  - `1.000 MHz`: `0.277 +/- 0.287 kcps`, amplitude SNR `0.96`, `R2 = 0.115`.
  - `1.384577 MHz`: `0.263 +/- 0.287 kcps`, amplitude SNR `0.92`, `R2 = 0.113`.
  - prior `0.884 MHz`: `0.286 +/- 0.286 kcps`, amplitude SNR `1.00`, `R2 = 0.117`.
- Point-wise ratio target amplitudes are also weak, with target SNRs below `1.7`.
- FFT nearest-bin raw amplitudes are small at the planned targets: `0.397 kcps` near `0.610 MHz`, `0.336 kcps` near `0.976 MHz`, and `0.369 kcps` near `1.341 MHz`.
- Exploratory peaks are analysis-dependent: raw sinusoid scan prefers about `0.465 MHz` (`R2 ~ 0.33`), while ratio prefers about `1.18 MHz` (`R2 ~ 0.31`). That disagreement is not claim-grade carrier evidence.
- Stored-average baseline variation is large: signal means range from `36.20` to `50.27 kcps`; max deviation from the median is `18.8%`, and the second half mean is `5.2%` lower than the first half. Per-average target preference is inconsistent across carrier, sideband, and prior-frequency checks.
- A descriptive raw-signal Gaussian-decay cosine fit returned `f = 0.465 MHz`, `T2star = 2.62 +/- 0.70 us`, `R2 = 0.51`, but it is not supported as a physical T2star because the selected frequency is not the planned carrier/sideband and is not stable across readout views.

## Plausible interpretation

- The job completed safely and the NV remained bright enough; this is analyzable Ramsey data, not a failed acquisition.
- The expected `det = 1.0 MHz` Ramsey carrier is not supported in raw, ratio, or reference-line-normalized checks.
- The modeled `13C` sidebands at `0.615/1.385 MHz` are also not supported.
- The prior scout's `~0.884 MHz` component is not reproduced after the det shift, which argues against treating that prior feature as a stable physical carrier or 13C feature.
- The visible raw contrast/range is dominated by analysis-dependent low-frequency structure and large stored-average baseline variation. It may reflect weak/washed-out Ramsey contrast, residual detuning/phase-path issues, drift/readout artifacts, or noise; this dataset does not distinguish those cleanly.

## Claims not yet supported

- No supported numeric `T2star` value from this Ramsey run.
- No supported nearby-`13C` coupling claim.
- No general "no nearby 13C exists" claim; the data only says the planned Ramsey carrier/sidebands were not resolved under this protocol/run condition.
- No claim that the fine weak-pi pODMR center is wrong; the Ramsey result only shows that this Ramsey follow-up did not convert that center into a clean carrier.
- No claim that the Ramsey sequence or hardware route is faulty without a deliberate phase-ramp/control diagnostic.

## Recommended next action

Do not repeat another long T2star acquisition blindly. Run a compact Ramsey phase-ramp diagnostic on r03, after a fresh track and preferably a quick weak-pi center sanity check if time/drift allows. The diagnostic should test whether the observed Ramsey frequency follows programmed `det` across at least two detunings, e.g. `0.5 MHz` and `1.5 MHz`, with enough tau sampling to cover both. If det-following is recovered, then run a higher-SNR T2star scan using that verified condition. If det-following is not recovered, switch to protocol/readout/phase-path review or an alternate T2-family route before making T2star or 13C conclusions.
