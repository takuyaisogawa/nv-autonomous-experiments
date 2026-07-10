# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`.
- Prior Ramsey/design evidence: `evidence/e003.json`, `evidence/e006.json`, `evidence/e009.json`, `evidence/e017.md`.
- New completed measurement: `measurement/m001.json` raw export for `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
- New job metadata/artifacts: `measurement/m002.json` job contract, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs created: `ramsey_analysis_summary.json` and `ramsey_shorttau_review.png`.
- Parsed the terminal short-tau Ramsey: `tau=48 ns..1.968 us`, 41 points, `mw_freq=3.8759 GHz`, `det=1.0 MHz`, 12 averages x 90000 repetitions, final counts `35.122 kcps`.
- Used the project-recorded readout convention for this `ramsey.xml`: readout 1 is the mS=0 reference, readout 2 is the Ramsey signal.
- Quantitative checks:
  - Signal mean `44.655 kcps`, reference mean `48.573 kcps`.
  - Median signal SEM across tau `1.138 kcps`; median ratio SEM `0.0127`.
  - Scan-order/common-mode average check flagged no averages by the local robust outlier rule, though late averages 10-11 are visibly lower in both channels.
  - Windowed FFT of signal/reference has largest bins near `1.524 MHz` (`0.0138` ratio amplitude), `1.016 MHz` (`0.0119`), and `0.508 MHz` (`0.0116`).
  - Least-squares target amplitudes on signal/reference: `1.000 MHz` carrier `0.0247`; expected 13C sidebands `0.615 MHz` `0.0264`, `1.385 MHz` `0.0288`.
  - Least-squares target amplitudes on raw signal: `1.000 MHz` carrier `1.222 kcps`; `0.615 MHz` `1.150 kcps`; `1.385 MHz` `1.285 kcps`.
  - Raw 1.0 MHz carrier amplitude is about the same size as the measured median signal SEM, not clearly above it.
  - Linear-detrended full-window signal peak-to-peak is `5.25 kcps`, but the per-average frequency screen is dominated by low-frequency/trend content rather than a stable target carrier.

## Plausible interpretation

- The short-tau/high-SNR run completed safely and produced analyzable data. It improves the shot budget relative to the previous 8 us run and directly tests the very-short-T2star/early-time-carrier failure mode.
- There is weak oscillatory structure in the combined data, but it is not a clean Ramsey result. The target carrier and the two expected 13C sideband frequencies all fit with similar amplitudes, and the largest FFT bin is offset from the programmed `1.0 MHz` carrier.
- Because the raw-signal target amplitudes are only about `1.1..1.3 kcps`, comparable to the measured per-point SEM, this run does not supply a robust carrier/decay shape for fitting T2star.
- Together with the two prior non-claim-grade Ramsey datasets, this result argues that r03 remains a supported aligned NV by pODMR, but the Ramsey/T2star/13C branch is still not claim-grade under the current protocol.

## Claims not yet supported

- A numeric T2star for r03 is not supported.
- A nearby 13C coupling/splitting conclusion is not supported.
- The `1.524 MHz` FFT feature should not be promoted as a physical Ramsey frequency without an independent detuning-following or repeatability check.
- The similar amplitudes at `0.615`, `1.000`, and `1.385 MHz` do not support assigning 13C sidebands.
- The data do not support saying the failure is solely due to very short T2star; low-frequency/trend/common-mode structure remains a plausible contributor.

## Recommended next action

Stop blind Ramsey repeats on r03. Either switch to an alternate protocol designed to establish dephasing/13C under weak Ramsey visibility, or close the r03 Ramsey/13C branch as unsupported while preserving the aligned-NV claim. If continuing experimentally, first run a non-Ramsey or calibration diagnostic that can explain the missing detuning-following carrier, rather than increasing averages on the same Ramsey scan.
