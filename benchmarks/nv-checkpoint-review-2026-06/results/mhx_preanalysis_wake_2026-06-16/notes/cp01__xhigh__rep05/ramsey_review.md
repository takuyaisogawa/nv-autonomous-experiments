# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`, plus local practice notes in `md/memory.md` and `md/knowledge.md`.
- Prior r03 basis: `evidence/e003.json` for weak-pi pODMR acceptance at 3.876 GHz and `evidence/e005.json` for the Ramsey model/advisory.
- New Ramsey data and metadata: `measurement/m001.json` raw savedexperiment export; `measurement/m002.json` job contract; `measurement/m003.json` terminal result; `measurement/m004.json` final status; `measurement/m005.json` control.
- Scratch outputs created here: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_diagnostic.png`.

## Calculations/scripts run

- Ran JSON/schema inspection with local Python and PowerShell.
- Ran `python analyze_ramsey.py`.
- The script parsed the embedded `ramsey.xml`: with `full_experiment=0`, readout 1 is the pre-Ramsey `m_S=0` reference and readout 2 is the Ramsey signal.
- Run completed normally: `nv23_ramsey_20260513_185505_auto_ramsey`, saved run `1DExp-seq-ramsey-vary-tau-2026-05-13-185521`, 0..6 us tau, 31 points, 0.2 us step, 4 averages x 50000 repetitions, `mw_freq=3.876 GHz`, `det=1.5 MHz`, snake order, tracking per average. Final count text was 38.249 kcps, down 12.1% from the fresh pre-Ramsey track count of 43.535 kcps but still above the 20 kcps gate.
- Raw/readout checks: reference mean 45.318 kcps with 0.865 kcps std over tau; reference fitted end-start change -0.309 kcps over the scan. Signal mean 42.098 kcps, signal peak-to-peak 7.750 kcps, median signal SEM across stored averages 1.015 kcps. Point-wise signal/reference peak-to-peak was 0.136; signal/reference-line peak-to-peak was 0.173.
- Simple acquisition-order drift check using `ScanOrderEachAvg`: max absolute five-point common-mode end-start change was 2.6% within an average. Stored average means still shifted noticeably between averages, so drift/noise remain data-quality caveats.
- FFT check on line-normalized signal: actual DFT bin spacing was 161.3 kHz, Nyquist 2.419 MHz. The largest peak was 0.968 MHz, amplitude 2.81x the median nonzero-bin amplitude. The programmed-det bin nearest 1.5 MHz was weak at 0.80x median; expected 13C sideband bins near 1.115 and 1.885 MHz were 0.77x and 0.70x median. Dropping the tau=0 point kept the dominant peak near 1.0 MHz and did not make the programmed carrier or both sidebands robust.
- Fits on line-normalized signal were model-dependent: fixed `f=1.5 MHz` gave an apparent `T2* = 0.253 us`, R2 0.30, only small AICc improvement over a line; free-frequency damped cosine gave `f=0.962 MHz`, apparent `T2* = 2.07 us`, R2 0.49, better AICc. This disagreement is not claim-grade.

## Plausible interpretation

- The Ramsey scout is analyzable and shows Ramsey-scale variation in the signal readout that is larger than the stored-average SEM, but the oscillation is not cleanly tied to the programmed 1.5 MHz carrier.
- If the 0.96-1.0 MHz component is physical, it could indicate that the actual transition was offset from the 3.876 GHz grid frequency by roughly several hundred kHz, which is plausible given the previous weak-pi pODMR grid and fit uncertainty. It could also be influenced by the low tau=0 point, short tau span, drift/noise, or sequence/timing systematics.
- The data do not show robust FFT peaks at the expected `det +/- ~0.385 MHz` 13C sideband positions. This scout therefore does not support a nearby-13C assignment.

## Claims not yet supported

- No well-supported numeric `T2*` should be claimed from this scout.
- No claim of resolved 13C coupling, 13C absence, sideband splitting, or Hamiltonian parameters is supported.
- The apparent 0.96 MHz Fourier/fitted frequency should not be treated as a calibrated resonance correction without follow-up.
- The current data do not invalidate the prior r03 alignment conclusion, which rests on the strong/weak pODMR evidence, not this Ramsey scout.

## Recommended next action

Do a targeted frequency-centering follow-up before spending more time on a high-SNR Ramsey: run a narrow weak-pi pODMR refinement around the 3.876 GHz grid minimum, then repeat Ramsey with the refined `mw_freq` and a design that keeps per-average tracking windows under the active cap. If the refined Ramsey carrier is clean, then use a higher-SNR/even-average repeat or split acquisition for a defensible `T2*` and 13C FFT check.
