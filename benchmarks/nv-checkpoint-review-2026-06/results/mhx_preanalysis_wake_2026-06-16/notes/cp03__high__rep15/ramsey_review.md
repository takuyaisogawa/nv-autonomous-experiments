# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New short-tau Ramsey terminal data and metadata:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
  - `measurement/m002.json`: bridge job spec.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json`: terminal status.
  - `measurement/m005.json`: control state.
- Comparison/project evidence: `evidence/e003.json` for the prior det=1.0 MHz, 8 us terminal Ramsey review; `evidence/e017.md` for the short-tau design/start note.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs:
  - `ramsey_analysis_results.json`: numerical review results.
  - `ramsey_analysis_plot.png`: raw/normalized trace and frequency-screen plot.
- Checks performed:
  - Parsed the 2-readout Ramsey data as readout 1 reference and readout 2 signal, consistent with the project protocol basis for `ramsey.xml` with `full_experiment=0`.
  - Confirmed scan settings from data/job/result: `tau = 48 ns..1.968 us`, 41 points, 48 ns step, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `12 x 90000` shots per tau, final counts `35.122 kcps`, no stop request.
  - Computed raw signal/reference traces, signal/reference ratio, and signal divided by a fitted reference line.
  - Estimated per-point SEM from stored averages.
  - Ran linear-baseline least-squares sinusoid screens at the programmed carrier and nominal 13C sideband targets, plus a 0.2-2.5 MHz exploratory grid.
  - Ran FFT checks on detrended ratio data.
  - Ran a simple scan-order-aware common-mode drift screen using the snake acquisition order.
  - Ran a forced descriptive Gaussian-decay fit at the programmed 1.0 MHz carrier, only as a diagnostic.

## Quantitative results

- Acquisition/health:
  - Terminal run completed safely; status completed, stop requested false, monitor error empty.
  - Simple snake-order drift screen flagged no averages.
  - Reference mean `48.573 kcps`; signal mean `44.655 kcps`.
- Signal scale:
  - Raw signal peak-to-peak over tau: `6.499 kcps`.
  - Ratio peak-to-peak over tau: `0.1433`.
  - Median per-point SEM from stored averages: `1.138 kcps` signal and `0.0127` ratio.
- Target-frequency least-squares amplitudes:
  - Programmed 1.0 MHz carrier: ratio amplitude `0.0274`, raw signal amplitude `1.282 kcps`, R2 improvement vs linear baseline `0.355` ratio / `0.377` raw signal.
  - Nominal low 13C sideband at `0.615 MHz`: ratio amplitude `0.0243`, raw signal amplitude `1.102 kcps`.
  - Nominal high 13C sideband at `1.385 MHz`: ratio amplitude `0.0271`, raw signal amplitude `1.222 kcps`.
  - Prior exploratory `0.884 MHz` component: ratio amplitude `0.0126`, raw signal amplitude `0.584 kcps`.
- Exploratory frequency checks:
  - Strongest ratio LS screen was broad near `1.192 MHz`, amplitude `0.0363`, R2 improvement `0.656`.
  - FFT on detrended ratio data had strongest bins at about `0.508 MHz` and `1.016 MHz`; the short `1.92 us` span gives only about `0.521 MHz` nominal resolution.
  - Per-average top ratio frequencies were inconsistent: several averages landed at the low search boundary near `0.2 MHz`, several near `1.13-1.29 MHz`, and one near `2.10 MHz`.
- Forced fit:
  - A forced Gaussian-decay fit at 1.0 MHz returned `T2star ~0.34 us` on ratio and `~0.38 us` on signal/reference-line, with large model dependence. This is diagnostic only, not a supported T2star claim.

## Plausible interpretation

- The short-tau/high-SNR run did improve Ramsey visibility compared with the previous 8 us run: the 1.0 MHz component is now larger than in the prior terminal review (`0.0274` ratio and `1.282 kcps` raw here vs prior `0.00916` ratio and `0.277 kcps` raw).
- The data plausibly contain early-time Ramsey contrast with a very short apparent decay time, on the order of a few tenths of a microsecond if the 1.0 MHz carrier model is forced.
- However, the evidence still does not isolate a clean programmed-carrier model. The strongest screen is displaced and broad near `1.19 MHz`; sideband-target amplitudes are comparable to the carrier; per-average screens are inconsistent; and the short span cannot resolve the carrier from the expected 13C sideband frequencies well enough.

## Claims not yet supported

- A final numeric `T2star` for r03 is not supported. The forced `~0.34-0.38 us` fit is too model-dependent.
- A nearby `13C` conclusion is not supported. The short-tau run was not a high-resolution 13C sideband measurement, and the nominal sidebands are not distinguishable from carrier/baseline ambiguity.
- The `1.192 MHz` exploratory component should not be assigned to a physical coupling or resonance offset without a detuning-dependence check.
- The r03 alignment claim remains supported by prior pODMR context, but this Ramsey data does not by itself add a claim-grade T2star/13C result.

## Recommended next action

Do not run another blind Ramsey repeat on r03. Run a targeted detuning-dependence or phase-cycled short-tau Ramsey check, ideally after a fresh weak-pi pODMR frequency check if bridge conditions permit. The next test should ask whether the observed early-time oscillation follows programmed detuning; if it does, then design a claim-grade short-window T2star extraction. If it does not, close the r03 Ramsey/T2star/13C branch as unsupported under current Ramsey conditions and move to an alternate protocol rather than accumulating more Ramsey averages.
