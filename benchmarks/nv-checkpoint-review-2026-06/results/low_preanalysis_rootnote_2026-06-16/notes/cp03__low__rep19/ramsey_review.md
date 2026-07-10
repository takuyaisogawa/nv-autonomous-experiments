# Ramsey Review: short-tau r03 diagnostic

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, and `md/memory.md`.
- New measurement data: `measurement/m001.json`, raw export from `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
- Run metadata: `measurement/m002.json` job contract, `measurement/m003.json` terminal result, `measurement/m004.json` run status, `measurement/m005.json` control state.
- Generated local analysis artifacts: `analyze_ramsey_shorttau.py`, `ramsey_shorttau_analysis.json`, `ramsey_shorttau_diagnostic.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey_shorttau.py`.
- Parsed the Ramsey scan as 41 tau points from `48 ns` to `1.968 us`, `12` averages, `90000` repetitions per average, `1.08e6` shots per tau point, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`.
- Checked raw signal and reference readouts, linear-reference normalization, per-point SEM across stored averages, FFT screens, and least-squares sinusoid amplitudes at:
  - programmed carrier `1.000 MHz`,
  - expected 13C sidebands from the project model, `0.615 MHz` and `1.385 MHz`.
- The first script run wrote the numeric JSON but failed while plotting because matplotlib selected a broken Tk backend. Updated the script to use `Agg`, reran successfully, and generated the plot.

## Plausible interpretation

- The run completed without a bridge-level hard anomaly. Terminal final counts were `35.122 kcps`, above the run gate but lower than recent prior r03 counts.
- Raw signal mean was `48.573 kcps`; reference mean was `44.655 kcps`. The signal endpoint change was about `1.20%`, while the reference endpoint change was about `6.28%`, so reference/common-mode variation is visible and should not be ignored.
- The median across-average SEM was about `1.12 kcps` in raw signal and `0.0109` in signal/reference-line ratio.
- Least-squares target amplitudes were small:
  - `1.000 MHz`: `0.213 kcps` raw, `0.00475` ratio.
  - `0.615 MHz`: `0.175 kcps` raw, `0.00401` ratio.
  - `1.385 MHz`: `0.149 kcps` raw, `0.00334` ratio.
- FFT screening placed the largest combined raw/ratio bin near `1.016 MHz`, close to the programmed carrier, with amplitude about `0.289 kcps` raw and `0.00646` ratio. This is directionally more carrier-like than the previous long-window datasets, but it remains far below the per-point across-average scatter and far below the expected order-kcps Ramsey contrast scale used in the project notes.
- Per-average frequency screens are not stable enough to promote a physical frequency. Most averages are dominated by very-low-frequency/baseline-like components near the lower search bound, with a couple of high-frequency single-average maxima.
- Practical interpretation: the short-tau/high-SNR diagnostic gives at most a weak carrier-consistent hint, not a clean Ramsey oscillation. The data are consistent with a Ramsey contrast that is very small under this protocol, residual common-mode/reference variation, phase/timing/protocol contrast loss, or T2star shorter than the first measured point. It does not support extracting T2star.

## Claims that are not yet supported

- No supported numeric T2star value from this Ramsey run.
- No supported nearby 13C coupling claim from this Ramsey run.
- No supported claim that the prior `~0.884 MHz` feature was physical.
- No supported claim of 13C absence; the Ramsey carrier itself is not robust enough to make a sensitivity/absence statement.
- No supported decay-envelope fit. A fit would be model promotion without first establishing raw/readout-aware Ramsey signal presence.

## Recommended next action

- Do not run another blind Ramsey repeat on r03.
- First perform a protocol/sequence-level sanity check focused on why Ramsey contrast is suppressed despite clear pODMR alignment: verify Ramsey readout roles, phase convention, detuning implementation, pi/2 pulse timing/amplitude for the current Siglent route, and whether the adiabatic-inversion boolean is intended for this Ramsey use.
- If protocol checks pass, use an alternate coherence protocol with stronger expected observable contrast, such as a Hahn echo or a deliberately phase-stepped/fixed-short-tau Ramsey contrast check, before attempting any T2star or 13C closeout claim.
