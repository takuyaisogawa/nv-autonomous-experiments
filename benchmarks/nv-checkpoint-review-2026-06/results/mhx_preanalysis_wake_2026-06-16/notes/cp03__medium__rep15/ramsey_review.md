# Ramsey Review

## Files/Data Used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New Ramsey terminal data and metadata: `measurement/m001.json` through `measurement/m005.json`.
- Recent supporting context: `evidence/e017.md` plus selected prior evidence summaries in `evidence/e001.json` through `evidence/e016.json`.
- Generated during this review: `analyze_ramsey.py`, `ramsey_analysis_results.json`, `ramsey_shorttau_review.png`.

## Calculations or Scripts Run

- Ran `python analyze_ramsey.py`.
- The script loads `measurement/m001.json`, extracts the two readouts over tau, computes raw signal/reference and signal/reference ratio views, per-average SEM, linear-baseline least-squares sinusoid amplitudes at 0.615, 1.000, and 1.385 MHz, and a frequency screen from 0.25 to 4 MHz.
- Ran an additional local Python/SciPy scratch fit for damped-cosine sanity checks.

Key numerical checks:

- Measurement: accepted r03 short-tau Ramsey, `tau = 0.048..1.968 us`, 41 points, 48 ns step, `det = 1.0 MHz`, `mw_freq = 3.8759 GHz`, `12 x 90000` shots per tau point, snake scan, completed safely with final count text `35.122 kcps`.
- Combined raw signal readout spans `40.70..47.20 kcps` (`6.50 kcps` peak-to-peak). Combined signal/reference ratio spans `0.8396..0.9829` (`0.1433` peak-to-peak).
- Median exported signal error is `1.40 kcps`; median SEM across stored averages is `1.14 kcps` for raw signal and `0.0127` for ratio.
- Stored-average means drift/common-mode substantially: reference average means span `42.02..55.19 kcps`, signal average means span `37.47..51.21 kcps`; ratio average means are tighter at `0.893..0.956`.
- Linear-baseline LS components in combined ratio:
  - `0.615 MHz`: amplitude `0.0243`.
  - `1.000 MHz`: amplitude `0.0274`; adding 1 MHz to a linear baseline reduces ratio residual sum-of-squares by `35.5%`.
  - `1.385 MHz`: amplitude `0.0271`.
- Linear-baseline frequency screen peaks near `1.20 MHz` in both raw signal (`1.69 kcps`) and ratio (`0.0364`), not exactly at the programmed 1.0 MHz.
- Per-average 1 MHz ratio fits have consistent phase: vector/scalar coherence `0.963`, with amplitudes `0.013..0.044`.
- FFT after linear detrending has coarse bins from the short window; ratio-bin amplitudes are largest at about `1.524 MHz` (`0.0287`) and `1.016 MHz` (`0.0222`). This is not enough frequency resolution to separate carrier from expected sidebands cleanly.
- Exploratory damped-cosine fits were not claim-grade: free-frequency fits either favored about `1.10..1.21 MHz` and/or hit parameter bounds; a fixed-1 MHz fit gave a rough sub-us decay but with phase at a bound and poorer residuals.

## Plausible Interpretation

- This short-tau/high-SNR Ramsey run appears to have recovered an early-time Ramsey-like oscillatory signal in the accepted r03 dataset. The strongest support is the visible raw/ratio modulation and the phase-coherent 1 MHz component across stored averages after ratio normalization.
- The data are consistent with the prior hypothesis that the long-window Ramsey scans may have missed or diluted early-time structure because the useful contrast is concentrated in the first roughly 2 us.
- The frequency content is still ambiguous. The programmed 1.0 MHz component is present and coherent, but the broad frequency screen prefers about 1.2 MHz and the FFT bins are too coarse to cleanly distinguish 1.0 MHz carrier from nearby sideband-like content.
- Ratio normalization reduces common-mode average-to-average count motion, but the raw average means move enough that drift/baseline structure remains important provenance.

## Claims Not Yet Supported

- Do not claim a numeric T2star from this dataset. The bounded damped-cosine checks are model-dependent and not robust enough.
- Do not claim nearby 13C coupling from this dataset. The short tau span is intentionally not a high-resolution sideband measurement, and the 0.615/1.385 MHz target amplitudes are comparable to the 1 MHz component.
- Do not claim that the exact Ramsey carrier is 1.20 MHz. The screen maximum may reflect the short window, slow envelope/decay, baseline terms, or sideband/carrier mixing.
- Do not claim that r03 has failed Ramsey/T2star measurement; unlike the previous long-window scans, this run provides plausible early-time signal presence.

## Recommended Next Action

Use this run as evidence that r03 has a measurable early-time Ramsey response, then run a non-blind follow-up designed for parameter extraction rather than discovery:

- Recalibrate or verify the weak-pi ODMR center if enough time has elapsed or counts have shifted.
- Acquire a higher-quality short/intermediate Ramsey window that preserves early-time sampling but extends enough for decay and frequency discrimination, for example starting after tau=0, keeping 48 ns or similar spacing, and extending to roughly 3-4 us with enough points and even averages under the per-average tracking cap.
- Predefine the analysis target: raw and fitted-reference-normalized carrier/decay review first; fit T2star only after signal shape is supported. Treat 13C as unsupported until a longer or dedicated sideband-sensitive measurement resolves carrier vs sidebands.
