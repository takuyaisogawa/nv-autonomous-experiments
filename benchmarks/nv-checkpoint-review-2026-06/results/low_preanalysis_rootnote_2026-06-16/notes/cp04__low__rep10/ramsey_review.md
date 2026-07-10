# Ramsey Review

## Files/data used

- Project context: `project/state.md`, `project/brief.md`, `project/advice.md`, `context.json`.
- Prior comparison/model context: `evidence/e008.json` terminal det=1.0 MHz short-tau Ramsey review and `evidence/e019.json` det-shift model/advisory.
- New measurement: `measurement/m001.json` raw savedexperiment export; `measurement/m002.json` job spec; `measurement/m003.json` terminal result; `measurement/m004.json` status; `measurement/m005.json` control.
- Generated local analysis artifacts: `analyze_ramsey_detshift.py`, `ramsey_detshift_analysis.json`, `ramsey_detshift_diagnostic.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey_detshift.py`.
- Confirmed raw export shape: combined readouts `[2, 41]`, per-average readouts `[12, 2, 41]`.
- Used the embedded `ramsey.xml` with `full_experiment=0`: readout 1 is the `mS=0` reference, readout 2 is the Ramsey signal.
- Checked raw signal, point-wise `signal/reference`, and `signal/reference-line` views over `tau = 0.048..1.968 us` with 48 ns spacing.
- Computed per-point SEM across 12 stored averages: median signal SEM `0.711 kcps`, median ratio SEM `0.0126`.
- Ran least-squares sinusoid screens with constant+linear baseline and FFT checks at:
  - programmed carrier: `1.500 MHz`
  - det-tracking prediction from prior `1.192 MHz`: `1.692 MHz`
  - prior fixed component: `1.192 MHz`
  - expected 13C sidebands: `1.115 MHz` and `1.885 MHz`

## Plausible interpretation

- The run completed normally: `12 x 90000` repetitions, final count `44.796 kcps`, no stop request, no abort, safe shutdown OK.
- The prior fixed `~1.192 MHz` feature is not reproduced strongly: ratio LS amplitude `0.0051`, raw signal amplitude `0.474 kcps`, much smaller than the new carrier-region amplitudes.
- The new data contain weak carrier-region support: ratio LS amplitude is `0.0240` at `1.500 MHz` and `0.0250` at `1.692 MHz`; raw-signal amplitudes are `1.13 kcps` and `1.22 kcps`. The strongest detrended FFT ratio bin is `1.524 MHz`, close to the programmed-carrier FFT bin.
- This argues against simply treating the old `1.192 MHz` component as a fixed persistent physical Ramsey frequency. It is weakly consistent with det-dependent Ramsey structure, but not clean enough to promote.
- The data still show substantial slow/early-time structure: the broad LS screen is dominated by the lower search edge near `0.25 MHz`, and per-average screens also prefer that slow component. This makes the carrier-region result baseline/model sensitive.

## Claims not yet supported

- No supported numeric `T2star` claim from this run.
- No supported nearby `13C` claim. The 13C sideband checks are not dominant: ratio LS amplitudes are `0.0108` at `1.115 MHz` and `0.0173` at `1.885 MHz`.
- No supported claim that the det-shift test cleanly confirmed the prior `~1.192 MHz` feature as a physical Ramsey carrier. The fixed feature is suppressed, but the det-tracking/programmed-carrier distinction is not resolved because `1.500 MHz` and `1.692 MHz` have similar weak amplitudes and the FFT resolution is coarse.
- No claim-grade decay-envelope fit should be promoted; carrier presence and baseline behavior remain insufficiently clean.

## Recommended next action

Do not run another blind Ramsey repeat. Treat r03 Ramsey/T2star/13C as still unresolved under this protocol. The next action should be a branch decision: either switch to an alternate protocol that is less sensitive to early-time Ramsey baseline structure, such as a Hahn/CPMG-style baseline before 13C spectroscopy, or close the r03 Ramsey branch as non-claim-grade under current Ramsey conditions while preserving the supported r03 pODMR alignment claim.
