# Ramsey Review

## Files/Data Used

- `project/brief.md`, `project/state.md`, `project/advice.md`: project objective and current context.
- `md/memory.md`, `md/knowledge.md`: local NV/Ramsey analysis guidance.
- `measurement/m001.json`: terminal raw export for `nv23_ramsey_20260514_015423_auto_ramsey`.
- `measurement/m002.json`: submitted job/config metadata.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal result/status/control metadata.
- `evidence/e008.json`: prior det=1.0 MHz short-tau terminal review used as the immediate comparison point.

## Calculations/Scripts Run

- Created and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis.json` and `ramsey_analysis.png`.
- Checked terminal health: run status completed, final counts `44.796 kcps`, `12 x 90000` repetitions, no stop request, no monitor error.
- Verified raw-array contract by averaging `ExperimentDataEachAvg` back to `ExperimentData`; readout 1 used as reference and readout 2 as Ramsey signal.
- Reproduced a local scan-order-aware common-mode drift check using `Scan.ScanOrderEachAvg` with snake order; no averages were flagged.
- Computed signal/reference ratio, signal divided by fitted reference line, per-point SEM, linear-detrended FFTs, least-squares sinusoid screens, target-frequency amplitudes, per-average frequency screens, and descriptive damped-sinusoid grid fits.

Key numbers:

- Tau grid: `0.048..1.968 us`, `41` points, `0.048 us` step; FFT bin spacing `0.508 MHz`, so FFT is coarse for distinguishing nearby `1.5..1.7 MHz` hypotheses.
- Median SEM: signal `0.711 kcps`, ratio `0.0126`.
- Early `tau <= 0.75 us` peak-to-peak: signal `6.46 kcps`, ratio `0.134`.
- Prior det=1.0 MHz short-tau all-tau ratio top: `1.192 MHz`, ratio LS amplitude `0.03631`.
- New det=1.5 MHz all-tau ratio-screen top: `1.623 MHz`, ratio LS amplitude `0.02547`.
- Programmed `1.500 MHz` target: ratio LS amplitude `0.02399`, raw-signal amplitude `1.128 kcps`.
- Predicted det-tracked prior component at `1.692 MHz`: ratio LS amplitude `0.02505`, raw-signal amplitude `1.225 kcps`.
- Prior fixed-component control at `1.192 MHz`: ratio LS amplitude `0.00511`.
- Shifted 13C sideband checks at `1.307/2.077 MHz`: ratio LS amplitudes `0.00953/0.00614`.
- Det-centered 13C sideband checks at `1.115/1.885 MHz`: ratio LS amplitudes `0.01076/0.01732`.
- Mask/readout sensitivity: ratio all-tau screen peaks near `1.623 MHz`; ratio with `tau <= 0.2 us` skipped peaks near `0.746 MHz`; raw signal and signal/fitted-reference-line screens peak near `0.882 MHz`.
- Descriptive damped fits are inconsistent with a clean carrier assignment: ratio fit `0.678 MHz`, `T2* ~0.469 us`; raw-signal fit `0.818 MHz`, `T2* ~0.717 us`.

## Plausible Interpretation

The measurement is terminal, healthy, and analyzable. The det-shift run argues against the prior `~1.192 MHz` feature being a completely fixed component, because the `1.192 MHz` LS amplitude is weak in the new data. However, the new evidence does not cleanly establish det tracking either: the strongest all-tau ratio component is broad near `1.6 MHz` and the programmed `1.5 MHz`, predicted tracked `1.692 MHz`, and all-tau top `1.623 MHz` have very similar LS amplitudes within this short, coarse-resolution window.

The result is best treated as another non-claim-grade Ramsey diagnostic. It suggests there is real early-time structure and possibly a broad det-related response, but the frequency assignment depends strongly on readout normalization and early-tau masking. The per-average top frequencies are also inconsistent.

## Claims Not Yet Supported

- No supported numeric `T2*` for r03 from this Ramsey data.
- No supported nearby `13C` conclusion.
- No supported carrier/sideband model tying the data to the programmed detuning.
- No supported claim that the prior `~1.192 MHz` feature is a stable hardware artifact; it is weak here, but the replacement feature is not cleanly physical either.
- No basis for another blind same-family Ramsey repeat as the next step.

## Recommended Next Action

Stop repeating same-family Ramsey scans on r03. Do a branch-level synthesis/closeout: report r03 as a supported aligned NV, but report Ramsey-derived `T2*` and nearby-`13C` as unsupported under the current Ramsey conditions. If further lab time is justified, switch to a different targeted protocol only after choosing a specific failure mode to test; otherwise close this r03 Ramsey/13C branch as inconclusive rather than accumulating more comparable Ramsey scans.
