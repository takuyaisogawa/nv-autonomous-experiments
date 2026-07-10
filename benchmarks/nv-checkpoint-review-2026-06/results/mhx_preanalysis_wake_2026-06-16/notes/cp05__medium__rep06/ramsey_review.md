# Ramsey review

## Files/data used

- `measurement/m001.json`: terminal raw export for `nv23_ramsey_20260514_055148_auto_ramsey`, saved experiment `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- `measurement/m002.json`: submitted run spec and metadata.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: completion/status/control records.
- `project/brief.md`, `project/advice.md`, `project/state.md`, `md/knowledge.md`, `md/memory.md`, and relevant `evidence/*.json` context, especially the pODMR refresh and refreshed-center Ramsey design.

## Calculations or scripts run

- Ran local Python inspection of the raw JSON arrays:
  - extracted two readout channels over 41 tau points and 20 averages;
  - checked run geometry: tau `0.048..8.048 us`, `0.200 us` step, `8.0 us` span, nominal FFT/LS resolution `125 kHz`, Nyquist `2.5 MHz`;
  - computed raw signal, point-wise `signal/reference`, `(signal-reference)/reference`, and fitted-reference-line normalization;
  - scanned least-squares sinusoid amplitudes from `0.15..2.45 MHz`;
  - evaluated amplitudes at planned targets: carrier `1.500 MHz`, 13C sidebands `1.1152` and `1.8848 MHz`, prior artifact control `1.192 MHz`, and prior det-shift prediction `1.692 MHz`;
  - checked per-average and first-half/last-half frequency screens;
  - made a descriptive damped-sinusoid fit to the ratio view only as a non-claim diagnostic.
- Saved outputs:
  - `analysis_outputs/ramsey_analysis_summary.json`
  - `analysis_outputs/ramsey_review_plot.png`

## Quantitative observations

- The bridge run completed normally: status `completed`, final counts `43.433 kcps`, `stop_requested=false`, no hard bridge error, safe shutdown OK.
- Mean readouts: reference `48.789 kcps`, signal `44.670 kcps`, mean ratio `0.9156`. Median across-average SEM was about `0.85 kcps` for signal and `0.0116` in ratio.
- Combined full-span frequency screens are dominated near `2.27 MHz`:
  - raw signal top near `2.271 MHz`, amplitude `0.818 kcps`;
  - ratio top near `2.270 MHz`, amplitude `0.01845`;
  - fitted-reference-line normalization top near `2.271 MHz`, amplitude `0.01678`.
- Planned carrier is present but not dominant:
  - ratio LS amplitude at `1.500 MHz` is `0.01575 +/- 0.00445`;
  - raw signal amplitude at `1.500 MHz` is `0.705 +/- 0.201 kcps`.
- Planned 13C sidebands are not convincing:
  - ratio LS amplitude at `1.1152 MHz` is `0.00278 +/- 0.00510`;
  - ratio LS amplitude at `1.8848 MHz` is `0.00962 +/- 0.00484`;
  - the two sidebands are asymmetric and neither forms a clean carrier-plus-sideband pattern.
- First-half/last-half screens disagree:
  - first 10 averages peak near `1.517 MHz`, close to the carrier;
  - last 10 averages peak near `2.270 MHz`;
  - mean ratio shifted from `0.9593` in average 1 to `0.9025` in average 20, about `-5.9%`.
- Per-average top frequencies are mixed across the allowed band rather than locked to the carrier or sidebands.
- A descriptive damped-ratio fit prefers about `2.275 MHz` with `T2star ~2.56 us`, but this follows the non-target full-span maximum and is not claim-grade.

## Plausible interpretation

The refreshed-center Ramsey data contain real oscillatory structure, and the programmed `1.5 MHz` carrier is visible in aggregate and in the first-half screen. However, the strongest full-span component moves to about `2.27 MHz`, the per-average screens are inconsistent, and there is a sizable slow ratio change across averages. The data therefore do not cleanly support the planned carrier/13C-sideband model. The run is useful evidence that a simple fixed `1.192 MHz` artifact is not the whole story, but it still looks contaminated by drift, transient structure, or a sequence/frequency-systematic component.

## Claims not yet supported

- No supported T2star value from this run.
- No supported nearby 13C coupling conclusion.
- No supported claim that the `2.27 MHz` feature is physical NV precession or hyperfine structure.
- No supported claim of sub-grid resonance precision beyond the weak-pi pODMR refresh basis.

## Recommended next action

Pause Ramsey/T2star claim-making and run a bounded diagnostic that separates drift/systematics from real Ramsey phase evolution before spending another long acquisition. The most informative next measurement would be a short, high-SNR det-sign or phase-quadrature Ramsey check at the same refreshed center, with interleaved acquisition if available, comparing `+1.5 MHz` and `-1.5 MHz` detuning or equivalent phase-shifted readout. A physical carrier should move predictably with detuning sign/phase, while the `2.27 MHz` component or slow ratio drift should not.
