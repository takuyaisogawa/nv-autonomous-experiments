# Ramsey Review

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`.
- Prior Ramsey context: `evidence/e003.json` for the terminal 8 us det=1.0 MHz review, `evidence/e006.json` and `evidence/e017.md` for the short-tau diagnostic design.
- New measurement: `measurement/m001.json` raw savedexperiment export, plus `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` status, and `measurement/m005.json` control.
- Generated local artifacts: `analysis_ramsey_shorttau.py`, `ramsey_shorttau_analysis_summary.json`, and `ramsey_shorttau_analysis.png`.

## Calculations/scripts run

- Ran `analysis_ramsey_shorttau.py` on `measurement/m001.json`.
- Confirmed the combined data are exactly the mean of the 12 stored averages to numerical precision.
- Parsed the terminal settings: `ramsey.xml`, tau `0.048..1.968 us`, step `48 ns`, 41 points, `det=1.0 MHz`, `mw_freq=3.8759 GHz`, `12 x 90000` repetitions, snake scan order.
- Readout statistics: reference mean/min/max `48.573/47.568/49.744 kcps`; Ramsey signal mean/min/max `44.655/40.698/47.197 kcps`; signal dynamic range `6.499 kcps`; median across-average SEM about `1.14 kcps` for the signal.
- Target least-squares sinusoid screens were run on the raw signal and signal/reference-line normalization with linear and quadratic baselines.
  - Raw signal, linear baseline: carrier `1.000 MHz` amplitude `1.282 +/- 0.271 kcps`; expected sidebands `0.615 MHz` and `1.385 MHz` gave `1.103 +/- 0.271 kcps` and `1.220 +/- 0.285 kcps`.
  - Raw signal, quadratic baseline: carrier `1.000 MHz` amplitude `1.010 +/- 0.141 kcps`; sidebands `0.615 MHz` and `1.385 MHz` gave `1.396 +/- 0.384 kcps` and `0.963 +/- 0.150 kcps`.
  - The strongest exploratory local LS peak with quadratic baseline was near `1.1975 MHz` with raw amplitude `1.236 kcps`; the same peak appears in reference-line normalization with amplitude `0.02544`.
- Per-average 1 MHz carrier screens had mostly similar phase near `-pi` and amplitudes `0.70..2.04 kcps`, except the last average was less phase-consistent.
- Scan-order residual proxy found no stop-level anomaly, but substantial intensity motion remains provenance: per-average mean signal ranged `37.47..51.21 kcps`, and one average had a residual acquisition-order end-to-start slope near `5.05 kcps`.

## Plausible interpretation

- The short-tau/high-SNR run is not a null Ramsey result in the same way as the previous 8 us det=1.0 MHz run. It reveals a weak early-time oscillatory component at roughly the expected scale of the improved SEM.
- The component is not cleanly assigned to the programmed `1.0 MHz` carrier. The best local screen is near `1.20 MHz`, close to the previous long-run off-target component near `1.178 MHz`, while the carrier and both simple 13C sideband targets also fit at comparable order because the `1.92 us` span gives poor frequency discrimination.
- A plausible physical possibility is that there is a real Ramsey-like early-time oscillation with an effective detuning offset from the intended carrier. A plausible nonphysical possibility is that short-window baseline/transient structure plus drift/common-mode changes creates or shifts the apparent component. This dataset does not separate those possibilities.

## Claims not yet supported

- No numeric `T2*` is supported. A decay fit would be underconstrained because the carrier frequency/model assignment is not established.
- No nearby `13C` claim is supported. The expected `det +/- f_13C` sidebands near `0.615 MHz` and `1.385 MHz` are not resolved or uniquely dominant.
- Do not claim the exact oscillation frequency is `1.1975 MHz`; that is an exploratory short-window LS maximum, not a high-resolution frequency measurement.
- Do not claim a hardware failure or unsafe run. The bridge result completed, stop was not requested, monitor error was empty, and final counts were `35.122 kcps`, above the configured minimum, though lower than earlier runs.
- Do not claim r03 is unsuitable overall. The alignment/pODMR evidence still supports r03 as the current aligned candidate; only the Ramsey/T2star/13C conclusion remains unsupported.

## Recommended next action

Do not run another blind long-window Ramsey repeat. The next useful step is a controlled detuning/frequency-dependence diagnostic on r03: repeat a short-tau high-SNR Ramsey under deliberately shifted `det` and/or freshly checked `mw_freq` settings to see whether the `~1.2 MHz` component follows the programmed phase ramp/resonance offset. If it follows, then plan a longer measurement for T2* and 13C resolution. If it does not, switch to an alternate protocol or close the r03 Ramsey/13C branch as unsupported under current conditions.
