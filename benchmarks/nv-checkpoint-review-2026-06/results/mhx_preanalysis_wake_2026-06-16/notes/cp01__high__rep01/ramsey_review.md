# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `context.json`, `md/memory.md`, `md/knowledge.md`.
- Prior Ramsey planning/model context: `evidence/e005.json` plus job/advisory artifacts in `evidence/e006.json` to `evidence/e011.json`.
- New Ramsey measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` submit spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` final status, `measurement/m005.json` control state.
- Scratch outputs created here: `ramsey_analysis.py`, `ramsey_review_plot.png`.

## Calculations or scripts run

- Parsed `measurement/m001.json` with Python to inspect scan shape, sequence variables, readout roles, stored averages, and scan order.
- Ran `python ramsey_analysis.py`.
- Confirmed saved variables: `mw_freq = 3.876 GHz`, `det = 1.5 MHz`, `full_experiment = 0`, `tau = 0..6 us`, 31 points, 0.2 us spacing, 4 averages x 50000 repetitions.
- Confirmed protocol/readouts from saved XML path: with `full_experiment=0`, readout 1 is the `mS=0` reference and readout 2 is the Ramsey signal.
- FFT sampling check: actual rFFT bin spacing from 31 samples is 161.3 kHz; span-based nominal spacing is 166.7 kHz; Nyquist is 2.5 MHz. This covers the programmed 1.5 MHz carrier and first-pass expected 13C sidebands at about 1.115 and 1.885 MHz, using the prior `f_13C ~= 0.385 MHz` model.
- Averaged raw readouts: reference mean 45.318 kcps, signal mean 42.098 kcps, signal/reference mean 0.9292. Signal range is 38.096 to 45.846 kcps.
- FFT after linear detrend + Hann window:
  - raw signal top components: 0.968 MHz, 0.161 MHz, 0.323 MHz, 0.806 MHz, 1.129 MHz, 0.645 MHz.
  - signal/reference top components: 0.968 MHz, 0.806 MHz, 0.323 MHz, 1.935 MHz, 1.774 MHz, 0.161 MHz.
- Fixed-frequency linear sinusoid fits:
  - 0.968 MHz component: raw amplitude 1.076 kcps, `R2 = 0.293`; ratio amplitude 0.0244, `R2 = 0.280`.
  - programmed 1.500 MHz carrier: raw amplitude 0.133 kcps, `R2 = 0.009`; ratio amplitude 0.0058, `R2 = 0.030`.
  - expected 13C sideband checks near 1.115/1.885 MHz: raw amplitudes about 0.39/0.38 kcps with `R2 ~= 0.04`; ratio amplitudes about 0.0079/0.0118 with `R2 ~= 0.04/0.08`.
- Per-average means show acquisition-level variation: avg signal means 43.365, 40.553, 42.797, 41.677 kcps; avg reference means 46.437, 43.682, 46.593, 44.558 kcps.
- Terminal bridge result completed without abort/incomplete status, but final count text was 38.249 kcps, about 12% below the fresh track count 43.535 kcps and about 13% below the weak-pODMR final count 43.890 kcps.

## Plausible interpretation

The Ramsey run completed and is usable as a scout, but it is not claim-grade for either T2star or 13C. There is weak oscillatory structure in the averaged data, with the strongest averaged component near 0.97 MHz. One plausible physical explanation is residual detuning of roughly 0.5 MHz relative to the weak-pODMR grid center, since that center was only grid-supported at 3.876 GHz and the prior guard allowed roughly +/-0.5 MHz uncertainty. However, this is only a plausible interpretation, not a supported assignment: the programmed 1.5 MHz carrier is not recovered strongly, the 0.97 MHz component explains only about 30% of variance in the averaged traces, one stored average is phase-inconsistent, and average-to-average count variation/drift is visible.

The data do not show a clean decaying Ramsey carrier/envelope. Therefore a T2star fit would be fit-driven rather than signal-driven. The FFT does not show a robust pair of features separated from the carrier by the expected 13C Larmor scale.

## Claims that are not yet supported

- No well-supported T2star value is established from this Ramsey scout.
- No well-supported nearby 13C conclusion is established.
- The 0.97 MHz FFT component should not be claimed as the true Ramsey carrier without a repeat or frequency diagnostic.
- The weak features near expected 13C sideband locations should not be assigned to 13C.
- The run should not be treated as drift-free; final counts and per-average means show meaningful count variation.

## Recommended next action

Do not do a blind T2star/13C claim or fit. First re-check the r03 frequency/condition with fresh tracking and a finer weak-pi pODMR or equivalent narrow frequency diagnostic around the 3.876 GHz grid minimum. Then repeat a bounded Ramsey measurement with the updated center and enough averaging to test whether a stable carrier appears at the programmed detuning; only after a clean carrier/envelope is present should a T2star fit and 13C sideband interpretation be attempted.
