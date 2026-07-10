# Ramsey Review

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`.
- Ramsey terminal/job data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` submitted job, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` run control.
- Ramsey planning context: `evidence/e005.json` model/protocol inspection and advisory; `evidence/e010.json`/`evidence/e011.json` status/batch-state snapshots.
- Prior spectroscopy context from project state and evidence summaries: r03 accepted after strong-pi pODMR at 3.875 GHz and weak-pi pODMR grid minimum at 3.876 GHz.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Generated `ramsey_analysis_summary.json`, `ramsey_analysis.png`, and `ramsey_analysis_stdout.txt`.
- Parsed `measurement/m001.json` as a 31-point tau scan from 0 to 6 us, 4 averages x 50000 repetitions. Used `evidence/e005.json` protocol inspection: readout 1 is the mS=0 reference and readout 2 is the Ramsey signal for `full_experiment=0`.
- Checked raw reference/signal traces, signal/reference, signal/fitted-reference-line, stored-average behavior, FFT of line-detrended traces, and linear-baseline-plus-sine fits at the programmed detuning and expected 13C sidebands.

## Quantitative checks

- Job completed without stop/abort: `measurement/m003.json` status `completed`, saved artifact `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`; final text count was 38.249 kcps, down from the recent 43.890 kcps weak-pODMR final count but above the 20 kcps gate.
- Runtime/tracking provenance: pre-enqueue advisory was 417.946 s per average, but live/terminal expected-runtime status reported 492.946 s per average, above the 450 s suggested cap.
- Raw readout scale from `ramsey_analysis_summary.json`:
  - Reference mean 45.318 kcps, range 3.904 kcps, median error 1.882 kcps.
  - Signal mean 42.098 kcps, range 7.750 kcps, median error 1.820 kcps.
  - Signal/reference range 0.136; signal/fitted-reference-line range 0.173.
- FFT sampling:
  - tau step 0.2 us; DFT bin spacing 161.3 kHz, span-based resolution 166.7 kHz, Nyquist 2.419 MHz.
  - Expected programmed carrier 1.5 MHz; expected 13C sideband separation from the planning model 0.385 MHz, so sidebands near 1.115 and 1.885 MHz.
- FFT/fits:
  - Averaged signal FFT largest nonzero component is near 0.968 MHz with amplitude 1.03 kcps.
  - Nearest-bin amplitudes are 0.426 kcps at 1.5 MHz, 0.670 kcps near 1.115 MHz, and 0.465 kcps near 1.885 MHz.
  - Linear-baseline-plus-sine fit at 1.5 MHz gives amplitude 0.133 kcps peak, peak-to-peak 0.266 kcps, R2 0.0095.
  - Sideband-frequency fits give amplitudes about 0.38 kcps and R2 about 0.042.
  - Best unconstrained grid frequency in the averaged signal is about 0.963 MHz with amplitude 1.08 kcps and R2 0.294, but stored-average best frequencies differ strongly: about 0.94, 0.54, 0.21, and 0.84 MHz.

## Plausible interpretation

The Ramsey run is valid terminal data and is analyzable, but it does not show a clean, repeatable Ramsey oscillation at the programmed 1.5 MHz carrier. The strongest averaged FFT feature near 0.97 MHz is not stable across stored averages and should be treated as drift/noise/provenance rather than a resonance-frequency shift or physical oscillation. The expected 13C sideband bins are not distinct from the general FFT background and are weak in simple sine fits.

The data may still be consistent with a short or low-contrast T2star, residual frequency error, drift during the long per-average window, or plain insufficient SNR. This scout should be counted as useful negative/diagnostic evidence, not as a T2star or 13C measurement result.

## Claims not yet supported

- No supported numeric T2star value.
- No supported 13C coupling/nearby-13C conclusion.
- No supported assignment of the 0.97 MHz FFT feature to detuning, hyperfine structure, or any physical sideband.
- No evidence here that invalidates r03 as the aligned candidate; the prior pODMR alignment evidence still stands unless later tracking/spectroscopy contradicts it.

## Recommended next action

Do not claim T2star or 13C from this Ramsey scout. Continue targeted follow-up on r03 with a redesigned Ramsey repeat that shortens the per-average drift window and increases repeatability: re-track r03, then run a shorter-window Ramsey diagnostic such as 0-4 us in 21 points at det = 1.5 MHz with an even number of stored averages, preserving or increasing total shots through averages rather than extending the untracked window. Review raw/FFT/per-average behavior again. If the carrier remains absent, run a weak-pi pODMR refresh or frequency diagnostic before any further T2star/13C interpretation.
