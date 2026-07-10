# Ramsey Review: short-tau r03 diagnostic

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, plus Ramsey-relevant guidance from `md/memory.md` and `md/knowledge.md`.
- New measurement artifacts: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` status, and `measurement/m005.json` control.
- Measurement identity: `nv23_ramsey_20260513_230331_auto_ramsey`, saved as `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`; terminal status completed, final text count `35.122 kcps`.
- Protocol: accepted r03 target, `auto__ramsey` / `ramsey.xml`, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, tau `48 ns..1.968 us` in 41 points, 12 averages x 90000 repetitions, snake scan order, tracking per average.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py` against `measurement/m001.json`.
- Output artifacts: `ramsey_analysis_summary.txt` and `ramsey_shorttau_diagnostic.png`.
- Checks performed:
  - Reconstructed tau axis from `vary_begin/end/points`.
  - Parsed per-average two-readout data as 12 averages x 2 readouts x 41 tau points.
  - Computed raw signal/reference means, per-point SEM, point-wise ratio, fitted-reference-line normalization, and linear-detrended residuals.
  - Screened average-level drift using total signal+reference counts; average 11 was flagged by a >15% common-mode drop criterion.
  - Ran least-squares sinusoid checks at the programmed carrier `1.000 MHz` and expected 13C sideband positions `0.615 MHz` and `1.385 MHz`.
  - Repeated the target checks excluding the drift-flagged average.
  - Ran a frequency screen over the sampled band and exploratory decaying-cosine fits.

## Quantitative results

- Sampling: tau step `0.048 us`, span `1.920 us`, Nyquist `10.417 MHz`, nominal resolution about `0.521 MHz`.
- Mean raw signal/reference: `48.573/44.655 kcps`; median SEM: signal `1.120 kcps`, reference `1.138 kcps`, ratio `0.01508`.
- Raw signal detrended peak-to-peak variation was only `2.269 kcps`.
- Target least-squares amplitudes after detrending:
  - `1.000 MHz`: raw `0.213 kcps`, ratio `0.03275`, fitted-reference-normalized `0.00475`; raw `R2 = 0.100`.
  - `0.615 MHz`: raw `0.175 kcps`, ratio `0.02923`, fitted-reference-normalized `0.00401`; raw `R2 = 0.062`.
  - `1.385 MHz`: raw `0.149 kcps`, ratio `0.03175`, fitted-reference-normalized `0.00334`; raw `R2 = 0.057`.
- Excluding average 11 did not rescue the result:
  - `1.000 MHz`: raw `0.236 kcps`, fitted-reference-normalized `0.00519`.
  - `0.615 MHz`: raw `0.191 kcps`, fitted-reference-normalized `0.00426`.
  - `1.385 MHz`: raw `0.128 kcps`, fitted-reference-normalized `0.00281`.
- Frequency screens were dominated by edge/very-low-frequency components rather than a clean carrier/sideband pattern.
- Free decaying-cosine fits are not claim-grade: raw fit hit the upper T2* bound (`20 us`) with small amplitude `0.223 kcps` and low `R2 = 0.135`; the ratio-only fit had higher `R2`, but the corresponding fitted-reference-normalized and raw views do not support promoting it.

## Plausible interpretation

The short-tau/high-SNR diagnostic does not reveal a robust programmed `1.0 MHz` Ramsey carrier in the raw readout. The apparent point-wise-ratio oscillation is likely normalization/denominator sensitive because it is much larger in point-wise ratio than in fitted-reference normalization, and the raw carrier amplitude is well below the per-point SEM. This is consistent with the two previous non-claim-grade Ramsey datasets: r03 remains a supported aligned NV candidate by pODMR, but Ramsey on this branch has not produced a defensible T2star or 13C signal under the tested conditions.

Average 11 shows a common-mode count drop, but removing it leaves the same conclusion. The result therefore is not primarily a single-average drift artifact; it is a lack of raw/readout-supported Ramsey signal at the target frequencies.

## Claims not yet supported

- No numeric T2star value is supported.
- No nearby 13C coupling or sideband claim is supported.
- No claim is supported that the ratio-only fitted component is a physical Ramsey oscillation.
- No claim is supported that the previous `~0.884 MHz` exploratory feature was real or detuning-following.
- No claim is supported that r03 is unsuitable as an aligned NV in general; the unsupported part is specifically the current Ramsey/T2star/13C conclusion under these protocols.

## Recommended next action

Stop blind Ramsey repeats on r03. The next action should be an explicit branch decision: either design a different, non-Ramsey/less normalization-sensitive protocol to test coherence or 13C coupling, or close the r03 Ramsey/13C branch as unsupported under current conditions and move to another aligned candidate/search path if the project still requires a well-supported T2star and 13C conclusion.
