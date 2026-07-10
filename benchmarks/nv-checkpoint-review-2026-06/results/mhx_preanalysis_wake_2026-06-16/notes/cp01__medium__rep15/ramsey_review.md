# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Ramsey measurement files: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` submit spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` terminal status, `measurement/m005.json` control state.
- Supporting evidence: `evidence/e005.json` Ramsey model/protocol/advisory note, plus terminal Ramsey evidence in `evidence/e010.json` and batch state in `evidence/e011.json`.
- Generated local artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Confirmed the run completed cleanly: `ramsey.xml`, `tau = 0..6 us`, 31 points, `dt = 0.2 us`, 4 averages x 50000 repetitions, snake scan, tracking per average, `mw_freq = 3.876 GHz`, `det = 1.5 MHz`, final count `38.249 kcps`.
- Used the protocol note in `evidence/e005.json`: readout 1 is the `mS=0` reference and readout 2 is the Ramsey signal for `full_experiment=0`.
- Raw mean readouts from `measurement/m001.json`: readout 1 mean `45.318`, peak-to-peak `3.904`; readout 2 mean `42.098`, peak-to-peak `7.750`; ratio readout2/readout1 mean `0.92919`, peak-to-peak `0.13551`.
- Across-average ratio SEM is not negligible: median `0.02557`, max `0.06023`, compared with combined-ratio peak-to-peak `0.13551`.
- Working field model from the accepted weak-pi resonance gives `B = 359.29 G`, expected `13C` Larmor `384.6 kHz`; for `det = 1.5 MHz`, expected sidebands are `1.115 MHz` and `1.885 MHz`.
- Ratio FFT after linear detrending/Hann window: bin spacing from the sampled grid is `161.3 kHz`, Nyquist `2.419 MHz`. Largest ratio bins are `0.968 MHz` amp `0.177`, `0.806 MHz` amp `0.160`, `0.323 MHz` amp `0.155`, `1.935 MHz` amp `0.151`, `1.774 MHz` amp `0.142`. Expected-bin amplitudes: det nearest `1.452 MHz` amp `0.087`, lower sideband nearest `1.129 MHz` amp `0.093`, upper sideband nearest `1.935 MHz` amp `0.151`.
- Combined-ratio sine+linear fit prefers `0.949 MHz`, amplitude `0.02489`, `R2 = 0.288`. A damped-cosine fit initialized near the strongest low-frequency component gives `f = 0.944 MHz`, `T2* = 2.39 us`, `R2 = 0.439`, but fits initialized near the expected sideband/carrier frequencies are worse or poorly constrained.
- Per-average best ratio sine+linear frequencies are inconsistent: averages 1-4 prefer `0.925`, `1.652`, `1.301`, and `0.854 MHz`, with `R2 = 0.205..0.447`.

## Plausible interpretation

- The Ramsey run is usable as a completed scout, not as a claim-grade T2star/13C result.
- There is real-looking modulation in the combined raw signal and signal/reference ratio, but it is not a clean programmed `1.5 MHz` Ramsey carrier.
- The strongest combined frequency near `0.95 MHz` is plausibly a Ramsey component shifted by resonance/frequency drift or residual detuning. This is compatible with the project note that several-hundred-kHz weak-pi center shifts can occur, and the final count dropped from the pre-Ramsey weak-pODMR context near `43.9 kcps` to `38.249 kcps`.
- A bin near the expected upper `13C` sideband scale (`1.935 MHz`, close to expected `1.885 MHz`) is present, but the carrier and lower sideband are not comparably clean and other unrelated bins have similar amplitude. This is at most weak motivation for follow-up, not evidence of a nearby `13C`.

## Claims that are not yet supported

- No well-supported numeric `T2*` should be claimed from this measurement. The descriptive `~2.4 us` damped-cosine result depends on a low-frequency component, has only modest `R2`, and is not stable across averages.
- No well-supported `13C` conclusion should be claimed. The FFT has a possible upper-sideband-scale feature, but lacks a clean carrier/lower-sideband pattern and has multiple competing peaks.
- Do not claim that the accepted r03 alignment is invalidated by this Ramsey scout. The prior strong/weak pODMR evidence still supports r03 as the aligned candidate; this run mainly shows that the first Ramsey settings/data quality are not sufficient for the requested T2star/13C conclusion.

## Recommended next action

Before another long Ramsey, refresh the resonance/frequency basis on r03 with retracking and a short weak-pi pODMR or equivalent frequency diagnostic. Then run a redesigned Ramsey with the current center accounted for, an even number of averages, and enough averages/points to test whether the apparent `~0.95 MHz` component is reproducible and whether both `det +/- 13C` sidebands appear coherently. Avoid treating this run's `T2*` fit or single upper-sideband-scale FFT bin as a final result.
