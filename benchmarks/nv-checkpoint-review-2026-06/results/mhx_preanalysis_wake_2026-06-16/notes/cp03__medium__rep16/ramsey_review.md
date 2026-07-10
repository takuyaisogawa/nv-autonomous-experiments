# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json`.
- New terminal Ramsey data/metadata: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` terminal status, and `measurement/m005.json` control state.
- Prior context note: `evidence/e017.md` for the short-tau diagnostic design/start. `evidence/e002.json` was checked but is the drift analysis for the previous 8 us Ramsey, not this new terminal run.

## Calculations or scripts run

- Added and ran `analyze_ramsey.py`.
- Outputs created: `ramsey_analysis_summary.json` and `ramsey_shorttau_diagnostic.png`.
- Checks performed:
  - Parsed raw readout arrays as readout 1 = reference and readout 2 = Ramsey signal.
  - Confirmed scan settings: `tau = 48..1968 ns`, 41 points, 48 ns spacing, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `12 x 90000` reps.
  - Computed raw signal/reference ranges, point-wise ratio, fitted-reference-line normalization, per-point SEM across averages, FFT screens, exact-frequency least-squares amplitudes at `1.000 MHz`, `0.615 MHz`, and `1.385 MHz`, per-average target consistency, and a local scan-order drift proxy.
  - Ran scratch fixed-carrier envelope fits to test whether a numeric T2star was stable under simple model choices.

Key quantitative results:

- Terminal run completed cleanly: bridge status completed, no stop request, no monitor error in copied status/control, final counts `35.122 kcps`.
- Raw Ramsey signal spans `40.698..47.197 kcps` with `6.499 kcps` peak-to-peak contrast. Median SEM across averages is `1.138 kcps`; exported median error for signal is `1.397 kcps`.
- Reference readout is much flatter over tau: `47.568..49.744 kcps`, `2.176 kcps` peak-to-peak; fitted reference slope about `-0.161 kcps/us`.
- Point-wise signal/reference ratio spans `0.8396..0.9829` (`0.1433` peak-to-peak), with median SEM `0.0127`.
- Exact 1.0 MHz least-squares amplitude:
  - Raw signal: `1.282 kcps`, residual-derived amplitude SE `0.271 kcps`, `R2 = 0.455`.
  - Point-wise ratio: `0.0274`, `R2 = 0.447`.
  - Fitted-reference-line normalization: `0.0264`, `R2 = 0.476`.
- FFT bins are coarse because the short window is only 1.92 us. The largest detrended FFT bins in raw/ratio are near `1.524 MHz`, followed by `1.016 MHz` and `0.508 MHz`; this is compatible with short-window leakage/curvature and does not cleanly resolve sidebands.
- Nominal 13C sideband LS amplitudes are comparable to the carrier (`0.615 MHz`: raw `1.103 kcps`, ratio `0.0243`; `1.385 MHz`: raw `1.220 kcps`, ratio `0.0271`), so they are not independent 13C evidence in this short window.
- Per-average ratio amplitudes at 1.0 MHz are positive by construction but reasonably consistent in scale: median `0.0262`, range `0.0135..0.0441`; phase resultant length `0.948`. Nearby sideband frequencies also show high phase consistency because the short-window sinusoids are strongly correlated.
- Local drift proxy: average-to-average raw signal means span `37.47..51.21 kcps` (`30.8%` fractional span), while average-to-average ratio means span only `0.893..0.956` (`6.8%`). Acquisition-order ratio slopes are small (`-0.00177..0.00190` per point). This is not a substitute for the MATLAB drift analyzer, but it does not reveal a hard scan-order collapse.
- Exploratory fixed-1 MHz envelope fits are model-dependent: exponential-envelope fits give roughly `0.16..0.20 us`; fixed-frequency Gaussian-envelope fits give roughly `0.33..0.38 us`. A raw-signal exponential fit gave `T2 ~0.185 us` with `0.944 kcps` RMS residual.

## Plausible interpretation

This short-tau/high-SNR run changes the Ramsey status: unlike the two earlier long-window datasets, it shows a real early-time Ramsey-scale contrast in raw signal and in ratio/reference-normalized views. The programmed `1.0 MHz` component is now quantitatively visible and phase-consistent across averages, with raw amplitude above the per-fit residual uncertainty and with overall raw contrast larger than the per-point SEM.

The most plausible physical reading is that r03 has very short Ramsey dephasing under these conditions. The useful contrast is concentrated early; model probes put the envelope on a sub-microsecond scale. That explains why the earlier 6-8 us Ramsey scans could fail to provide a clean carrier/sideband model.

## Claims that are not yet supported

- A final numeric T2star is not yet supported. Simple fits prefer sub-microsecond decay, but the extracted value depends on envelope model and baseline treatment.
- A nearby 13C conclusion is not supported. The short tau span cannot cleanly resolve `1.0 +/- ~0.385 MHz` sidebands, and the nominal sideband LS amplitudes are comparable to the carrier because of short-window frequency correlation.
- The `1.524 MHz` FFT-bin prominence should not be assigned as a physical sideband without a longer, carrier-supported dataset.
- This run does not by itself prove whether absent 13C evidence means no nearby 13C or just Ramsey dephasing too fast to observe nuclear sidebands.

## Recommended next action

Do not run another blind long-window Ramsey repeat. Treat the short-tau run as evidence for a real but very short-lived Ramsey carrier. For the project objective, the next useful step is a targeted coherence/13C strategy rather than more identical Ramsey accumulation:

1. If a Ramsey T2star number is still required, run or analyze a purpose-built short-window T2star acquisition with enough early points and explicit model-selection criteria, then report a model-qualified sub-microsecond T2star or a bounded range.
2. For the 13C question, switch to a coherence-preserving protocol such as Hahn echo/CPMG-style spectroscopy after protocol review, because this short Ramsey envelope is too short for a reliable sideband conclusion.
