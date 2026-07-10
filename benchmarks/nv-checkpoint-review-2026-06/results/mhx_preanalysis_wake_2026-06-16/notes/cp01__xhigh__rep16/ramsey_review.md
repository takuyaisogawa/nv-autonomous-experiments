# Ramsey Review

## Files/Data Used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`, `md/knowledge.md`, and `context.json`.
- Prior r03 context: `evidence/e003.json` weak-pi pODMR review and `evidence/e005.json` Ramsey model/advisory. r03 had a weak-pi grid-supported resonance at 3.876 GHz with a 14.28% raw signal dip; the planned 13C scale was about 0.3846 MHz.
- New Ramsey measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` executed job spec, `measurement/m003.json` terminal result, `measurement/m004.json` final status.
- Generated local analysis artifacts: `ramsey_analysis.py`, `ramsey_analysis_results.json`, `ramsey_analysis_summary.txt`, `ramsey_traces_fft.png`.

## Calculations/Scripts Run

- Inspected JSON structure and readout dimensions with local Python. The Ramsey export has `ExperimentData` shape `[1,2,31]` and `ExperimentDataEachAvg` shape `[1,4,2,31]`.
- Ran `python ramsey_analysis.py`.
- Treated readout 1 as reference and readout 2 as Ramsey signal from the active `ramsey.xml` path with `full_experiment=0`.
- Checked raw signal, point-wise `signal/reference`, and `signal / fitted_reference_line`.
- Checked per-average means and snake acquisition-order first/second-half drift.
- Ran FFT checks with `dt = 0.2 us`; DFT bin spacing is 161.29 kHz for the 31 sampled points.
- Fit bounded Ramsey-style models: linear baseline plus Gaussian-envelope cosine and exponential-envelope cosine.

## Key Quantitative Checks

- Measurement completed, not aborted. Final count was 38.249 kcps, above the 20 kcps minimum but down 12.1% from fresh r03 track counts of 43.535 kcps and 12.9% from the weak-pODMR final count context of 43.890 kcps.
- Scan was tau = 0..6 us, 31 points, 4 averages x 50000 repetitions.
- Raw Ramsey signal readout: mean 42.098 kcps, peak-to-peak 7.750 kcps, median SEM 1.015 kcps.
- Reference readout: mean 45.318 kcps, peak-to-peak 3.904 kcps, median SEM 1.011 kcps.
- Reference-line-normalized Ramsey signal: mean 0.92896, peak-to-peak 0.17341, median SEM 0.02233.
- Per-average signal means were 43.365, 40.553, 42.797, and 41.677 kcps; reference means were 46.437, 43.682, 46.593, and 44.558 kcps. This is common-mode count variation, not a clean stationary run.
- Fit-compatible oscillation frequency is below the programmed `det = 1.5 MHz`: raw and reference-line-normalized fits prefer about 0.920-0.944 MHz; point-wise ratio fits prefer about 0.876-0.881 MHz.
- Provisional fit scales:
  - raw Gaussian envelope: f = 0.920 MHz, T2 = 2.38 us, R2 = 0.384, reduced chi2 = 1.52.
  - raw exponential envelope: f = 0.944 MHz, T2 = 1.31 us, R2 = 0.443, reduced chi2 = 1.47.
  - line-normalized Gaussian envelope: f = 0.920 MHz, T2 = 2.38 us, R2 = 0.390, reduced chi2 = 1.52.
  - line-normalized exponential envelope: f = 0.944 MHz, T2 = 1.31 us, R2 = 0.448, reduced chi2 = 1.47.
- FFT does not give a clean single carrier at the programmed detuning. Top Hann raw-signal bins were 0.968, 0.161, 0.323, 0.806, and 1.129 MHz. Top Hann line-normalized bins were 0.161, 0.968, 0.323, 0.806, and 1.129 MHz.
- Linear checks at expected 13C-related frequencies were weak. Relative to the line-normalized exploratory carrier near 0.920 MHz, the +/-0.3846 MHz checks at 0.536 and 1.305 MHz did not stand out as a robust pair. Relative to the programmed 1.5 MHz carrier, 1.115 and 1.885 MHz also did not stand out.

## Plausible Interpretation

- The accepted r03 candidate still has plausible Ramsey-like oscillatory signal in the new data. The raw oscillation scale is in the expected few-kcps range from the weak-pODMR contrast context.
- The oscillation is not centered where a clean on-resonance `det = 1.5 MHz` Ramsey carrier would be expected. If physical, the about 0.9-1.0 MHz fitted/FFT feature could indicate residual microwave detuning of roughly 0.5-0.6 MHz from the weak-pODMR grid center; that is plausible given the earlier 1 MHz weak-pODMR grid support and drift context.
- A finite dephasing scale of order 1-3 us is plausible, but the exact T2star depends strongly on envelope model and normalization. The run is useful as a scout, not as a final quantitative T2star measurement.

## Claims Not Yet Supported

- No final T2star value is supported. The fits have modest R2, model-dependent T2 estimates, common-mode count drift, only 31 points, and no repeat.
- No 13C coupling conclusion is supported. The FFT has multiple comparable low-frequency/carrier-neighbor bins and no robust symmetric sideband evidence at about 0.3846 MHz separation.
- The data do not support invalidating r03 as the aligned candidate. They do support recalibrating/rechecking before a claim-grade follow-up.
- The apparent carrier shift should not yet be claimed as a measured resonance shift without a fresh weak-pi pODMR recenter or a phase-controlled Ramsey repeat.

## Recommended Next Action

Run a fresh r03 track/count check and weak-pi pODMR recenter around 3.876 GHz before another Ramsey. If counts and center are healthy, repeat Ramsey with the updated microwave center/detuning, an even number of snake-balanced averages, and a per-average window that stays inside the active drift cap. The repeat should target claim-grade T2star first; only use FFT sidebands for a 13C statement after the carrier is clean and repeatable.
