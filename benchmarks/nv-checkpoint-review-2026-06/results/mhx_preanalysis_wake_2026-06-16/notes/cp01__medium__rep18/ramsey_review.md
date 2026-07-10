# Ramsey Review: image145844 reimage r03

## Files/data used

- `project/state.md`, `project/brief.md`, `project/advice.md`, `md/memory.md`, and `md/knowledge.md` for objective, prior candidate decisions, Ramsey design constraints, and interpretation rules.
- `measurement/m001.json`: raw-exported terminal Ramsey savedexperiment for `1DExp-seq-ramsey-vary-tau-2026-05-13-185521.mat`.
- `measurement/m002.json`, `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: Ramsey job, result, terminal/live status, and control provenance.
- `evidence/e008.json` through `evidence/e011.json`: Ramsey submit spec/advisory/status/batch context. Earlier evidence files were used only as context for accepted r03 and the weak-pi pODMR basis.
- Generated local artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, and `ramsey_review_plot.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed the Ramsey scan as 31 tau points from `0` to `6 us`, spacing `0.2 us`, with 4 stored averages x 50000 repetitions and two readouts. `full_experiment=0`, so readout 1 was treated as the 0-level reference and readout 2 as the Ramsey signal, consistent with the sequence comments and project guidance.
- Computed raw signal, raw reference, point-wise `signal/reference`, and `signal/reference-line-fit` views.
- Checked per-average normalized behavior and correlations with the combined normalized trace.
- Computed detrended Hann-window FFTs for raw signal and normalized signals.
- Ran descriptive least-squares frequency scans for line-plus-sinusoid and line-plus-damped-sinusoid models. These were used only as shape checks, not as validated physical fits.

Key quantitative results from `ramsey_analysis_summary.json`:

- Final Ramsey run completed safely; final count text was `38.249 kcps`, above the `20 kcps` gate but lower than the pre-Ramsey weak-pi final count `43.890 kcps`.
- Combined raw signal mean `42.10 kcps`; raw reference mean `45.32 kcps`.
- Raw signal peak-to-peak was `7.75 kcps` (`18.4%` of mean). Point-wise `signal/reference` peak-to-peak was `0.1355` (`14.6%` of mean), with mean `0.929`.
- Reference linear trend was small on average, about `-0.11% per us`, but reference point-to-point variation was still `8.6%` peak-to-peak.
- Per-average normalized means were `0.935`, `0.930`, `0.920`, `0.938`; per-average correlations with the combined normalized trace were only moderate: `0.68`, `0.42`, `0.58`, `0.56`.
- Actual FFT grid from 31 samples at `0.2 us` spacing has bin spacing `161.3 kHz` and Nyquist `2.419 MHz`. The strongest normalized FFT bins were near `0.968 MHz`, `0.806 MHz`, `0.323 MHz`, and `1.935 MHz`.
- The programmed Ramsey detuning was `1.5 MHz`; the nearest FFT bin at `1.452 MHz` ranked only 12th in the normalized FFT.
- Expected first-order 13C sideband scale from the plan was about `0.385 MHz` from the carrier. The upper expected sideband bin near `1.935 MHz` was rank 4, but the carrier bin itself was weak and the lower expected sideband near `1.129 MHz` was rank 11. A low-frequency bin near `0.323 MHz` was rank 3, but this is not sufficient to assign 13C.
- Descriptive damped fits preferred about `0.94-0.96 MHz` and `T2* ~2.1-2.4 us`, with normalized relative amplitude about `7.2%` and `R2 ~0.45`. Undamped fits gave similar frequency but only `R2 ~0.29`.

## Plausible interpretation

The Ramsey experiment completed and produced a non-flat signal with contrast-scale structure in the signal readout and in normalized views. However, the frequency content does not robustly match the intended `det = 1.5 MHz` carrier, and per-average agreement is only moderate. The best descriptive fits are therefore more consistent with a non-claim-grade oscillatory scout than with a reliable T2star extraction.

The high normalized FFT peak near `0.97 MHz` could reflect a real Ramsey oscillation with an effective detuning different from the programmed value, or it could be a mixture of finite-window leakage, noise, drift, and point outliers. Because the programmed carrier bin is weak, the apparent feature near the upper expected 13C sideband is not enough to support a 13C assignment. The low-frequency feature near the expected 13C Larmor scale is also not assignable without a carrier-locked pattern or repeatability.

The live/terminal runtime estimate was `492.946 s` per average, above the `450 s` planning cap, although the job completed and tracked per average. Treat this as drift-risk provenance, not a terminal invalidation. It does make stored-average consistency and repeat design important.

## Claims that are not yet supported

- No well-supported numeric T2star value is established from this Ramsey run.
- No well-supported nearby 13C conclusion is established.
- Do not claim the `~0.94-0.96 MHz` descriptive fit frequency as a calibrated physical detuning without repeat/diagnostic support.
- Do not claim the `~2.1-2.4 us` damped-fit time constant as T2star; the fit quality is modest and the result is sensitive to non-carrier structure.
- Do not assign the `1.935 MHz` FFT bin or the `0.323 MHz` bin to 13C from this single scout.

## Recommended next action

Run a targeted Ramsey diagnostic/repeat on r03 rather than closing T2star/13C. Before repeating, re-check current tracking/counts and preferably a quick resonance/frequency sanity check. Redesign the Ramsey acquisition so each tracked average stays within the drift cap; if preserving total shots is needed, split into more shorter averages or separate jobs rather than lengthening the per-average window.

The immediate scientific goal should be to determine whether the Ramsey carrier is reproducible and whether it can be made to appear at the programmed detuning. Use a repeat or diagnostic grid that can distinguish `~1.0 MHz` from `1.5 MHz` and still covers the expected `~0.385 MHz` 13C sideband spacing. Only fit T2star after a raw/readout-aware, carrier-consistent Ramsey oscillation is present across stored averages.
