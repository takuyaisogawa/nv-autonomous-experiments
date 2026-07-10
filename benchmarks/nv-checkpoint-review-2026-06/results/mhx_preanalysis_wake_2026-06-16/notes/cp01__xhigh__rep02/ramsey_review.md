# Ramsey Review: r03 first T2star/13C scout

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `context.json`, plus local NV practice notes in `md/memory.md` and `md/knowledge.md`.
- Prior resonance basis: `evidence/e003.json` weak-pi pODMR review supporting the 3.876 GHz grid minimum; `evidence/e005.json` Ramsey model/protocol/advisory context and expected 13C Larmor scale.
- New Ramsey artifacts: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` executed job spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` terminal status, and `measurement/m005.json` control state.
- Scratch outputs created here: `ramsey_analysis.py`, `ramsey_analysis_results.json`, and `ramsey_analysis.png`.

## Calculations/scripts run

- Ran `python ramsey_analysis.py`.
- Parsed `measurement/m001.json`; used the protocol context that `full_experiment=0` means readout 1 is the `mS=0` reference and readout 2 is the Ramsey signal.
- Confirmed executed grid/acquisition: tau `0..6 us`, 31 points, `0.2 us` step, `det=1.5 MHz`, `mw_freq=3.876 GHz`, 4 averages x 50000 repetitions, snake scan order.
- Raw/readout checks:
  - Reference mean `45.318 kcps`, peak-to-peak `3.904 kcps`, CV `1.91%`.
  - Signal mean `42.098 kcps`, peak-to-peak `7.750 kcps`, CV `3.42%`.
  - Signal/reference mean `0.9292`; normalized ratio peak-to-peak `14.6%`; median pointwise SEM across stored averages `2.88%`.
- FFT check on detrended, windowed normalized signal:
  - Nyquist `2.5 MHz`; DFT bin spacing `161.3 kHz` (`~166.7 kHz` by nominal 6 us span).
  - Largest bins: `0.968`, `0.806`, `0.323`, `1.935`, `1.774 MHz`.
  - Target bins for current `det=1.5 MHz` and expected `13C` Larmor `~0.385 MHz`: carrier target bin `1.452 MHz` amplitude `0.094`, lower sideband target bin `1.129 MHz` amplitude `0.100`, upper sideband target bin `1.935 MHz` amplitude `0.162`; median nonzero FFT amplitude `0.121`.
- Empirical fits to normalized signal:
  - Free damped-cosine fit: frequency `0.941 MHz`, amplitude `7.2%`, `T2star = 2.39 +/- 1.19 us`, `R2 = 0.446`; descriptive only.
  - Fixed carrier `1.5 MHz` fit: `R2 = 0.207`, `T2star ~0.38 us` with large uncertainty.
  - Fixed 13C sideband fits: lower sideband `R2 = 0.283`, upper sideband `R2 = 0.176`; upper fit hits the short-`T2star` bound.
- Per-average stability checks:
  - Top FFT bins by average are not repeatable: `0.968`, `1.452`, `0.323`, `0.806 MHz`.
  - Free-fit frequencies by average are not repeatable: `0.924`, `1.673`, `1.304`, `0.868 MHz`.
  - Combined-trace correlations by average are only `0.42..0.68`.
  - Acquisition-order ratio slope estimates are `+4.6%`, `+6.4%`, `+1.3%`, and `-5.6%` end-to-end, consistent with drift/noise being relevant provenance.

## Plausible interpretation

- The Ramsey acquisition completed and is analyzable. It is not a failed run: the terminal result is completed, safe shutdown succeeded, and final count text was `38.249 kcps`, above the `20 kcps` gate, though lower than the prior weak-pi pODMR final count context.
- The combined trace contains a weak oscillatory-looking modulation, but the frequency content is not stable across stored averages and the programmed carrier bin is not strong. The free `0.94 MHz` fit could reflect residual detuning of order `0.5 MHz`, drift from the weak-pi pODMR grid center, or a fit/noise artifact.
- There is a modest FFT bin near the expected upper `13C` sideband scale (`1.935 MHz` vs expected `~1.885 MHz`), but it is only `~1.34x` the median nonzero FFT amplitude and the carrier/lower-sideband evidence is weak. Treat this as a pointer for follow-up, not as 13C evidence.
- If the oscillation is physical, a few-us T2star is plausible, but this scout does not constrain it robustly enough to claim a value.

## Claims not yet supported

- No well-supported numeric `T2star` value is established from this Ramsey scout.
- No well-supported nearby `13C` conclusion is established.
- The `0.94 MHz` fitted component is not yet a physical Ramsey frequency claim.
- The weak FFT power near the upper expected `13C` sideband is not yet a 13C coupling claim.
- The data do not by themselves prove that the 3.876 GHz weak-pi pODMR center was wrong; they only make a current-frequency/drift check prudent.

## Recommended next action

Run a fresh current resonance check on r03 before another T2star claim attempt: a short weak-pi pODMR around the 3.876 GHz grid-supported center, at the current tracked position, to test whether the resonance has shifted by several hundred kHz. If the resonance remains clear, repeat Ramsey with the updated frequency basis and a shorter per-average tracking window than this run. Prefer reducing repetitions per average and increasing to an even number of stored averages to preserve total shots, keeping the tau span/sampling sufficient for `det=1.5 MHz` and the `~0.385 MHz` 13C sideband check if the advisory permits.
