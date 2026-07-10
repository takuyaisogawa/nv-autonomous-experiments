# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Ramsey measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` submitted job spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` final status, `measurement/m005.json` run control.
- Supporting evidence summaries checked: `evidence/e009.json`, `evidence/e010.json`, `evidence/e011.json`.
- Scratch outputs created: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed `measurement/m001.json`; the saved `ramsey.xml` has `full_experiment=0` and two active readouts: leading `m_S=0` reference, then Ramsey signal.
- Confirmed scan settings: `tau = 0..6 us`, step `0.2 us`, `31` points, `4` averages, `50000` repetitions, `mw_freq = 3.876 GHz`, `det = 1.5 MHz`.
- Computed signal/reference ratio, per-average means, FFT, expected 13C scale, and a bounded diagnostic damped-cosine fit.
- From `mw_freq = 3.876 GHz`, using the ordinary NV electron gyromagnetic scale gives `B ~ 359.0 G`; expected 13C Larmor scale is `~384.3 kHz`.
- FFT grid from the exported samples: bin spacing `161.3 kHz`, Nyquist `2.419 MHz`.

## Quantitative checks

- Terminal bridge result is clean: completed, not aborted, savedexperiment present, final counts `38.249 kcps`; no stop request.
- Mean reference readout: `45.318 kcps`; mean Ramsey signal readout: `42.098 kcps`; mean signal/reference ratio: `0.9292`.
- Ratio range is broad but noisy: min `0.8591`, max `0.9946`, peak-to-peak `0.1355`, sample std `0.0340`.
- Per-average ratio means are close but not identical: `[0.9347, 0.9298, 0.9199, 0.9377]`; raw reference/signal levels drift by several percent across averages.
- FFT of the averaged ratio is not dominated by the programmed carrier. Largest ratio FFT peaks are `0.968 MHz`, `0.161 MHz`, `1.613 MHz`, `0.806 MHz`, and `1.290 MHz`.
- Target-bin amplitudes in the ratio FFT:
  - `det - f13C ~ 1.116 MHz` maps to `1.129 MHz`, amplitude `0.109`.
  - `det = 1.500 MHz` maps to `1.452 MHz`, amplitude `0.070`.
  - `det + f13C ~ 1.884 MHz` maps to `1.935 MHz`, amplitude `0.203`.
- Per-average FFT peak locations are inconsistent; the same dominant frequency is not shared by all four averages.
- Bounded diagnostic Ramsey fit returns `T2* ~ 5.4 us`, fitted frequency `~1.69 MHz`, but the fit is weak (`R2 ~ 0.17`) and the T2* uncertainty is comparable to the value. Treat this fit as non-claim evidence only.

## Plausible interpretation

- The measurement completed and contains real readout contrast variation, so it is not a hardware/no-data failure.
- The trace is not a clean Ramsey oscillation at the programmed `1.5 MHz` detuning. The strongest FFT component is near `0.97 MHz`, and the nominal carrier bin is weak.
- A feature near the upper expected 13C sideband bin exists, but it is not enough to assign nearby 13C coupling because the carrier itself is weak, the top FFT peaks are distributed across many bins, and per-average spectra do not repeat cleanly.
- The final count drop from the prior weak-pi pODMR context (`43.890 kcps` early status to `38.249 kcps` terminal text) plus several-percent average-to-average readout changes are consistent with drift contributing to the non-claim-grade result.

## Claims not yet supported

- No well-supported T2* value is established from this Ramsey scout.
- No well-supported nearby 13C conclusion is established.
- The diagnostic fit result must not be used as a physical T2* claim.
- The FFT feature near `det + f13C` must not be called a 13C sideband without a repeatable carrier/sideband structure.
- The result does not invalidate the prior r03 alignment conclusion; it only says this Ramsey scout is not claim-grade.

## Recommended next action

Run one redesigned Ramsey repeat on r03 before changing candidate: keep the same weak-pi frequency basis unless a fresh check shows a shift, but shorten the untracked per-average window by reducing repetitions per average and increasing the number of averages to preserve total shots as much as practical. A concrete starting point is the same `0..6 us`, `31` point, `det = 1.5 MHz` scan with a split such as `8 x 25000` or `16 x 12500`, subject to the normal advisory/bridge gates. Require the repeat to show a repeatable raw/readout-aware carrier near the programmed detuning before fitting T2* or interpreting 13C sidebands. If the repeat is still non-claim-grade, do not blind-repeat; first re-check weak-pi resonance frequency or run a Ramsey route/phase diagnostic.
