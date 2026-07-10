# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`.
- New Ramsey measurement:
  - Raw export: `measurement/m001.json`.
  - Job specification: `measurement/m002.json`.
  - Terminal bridge result: `measurement/m003.json`.
  - Terminal status/control: `measurement/m004.json`, `measurement/m005.json`.
- Supporting prior context/evidence:
  - Prior det=1.0 MHz 8 us Ramsey review/export: `evidence/e001.json` through `evidence/e004.json`.
  - Short-tau Ramsey design/start evidence: `evidence/e006.json`, `evidence/e009.json`, `evidence/e017.md`.

## Calculations or scripts run

- Parsed `measurement/m001.json` with Python/NumPy.
- Confirmed data dimensions:
  - Combined `ExperimentData`: 2 readouts x 41 tau points.
  - Per-average data: 12 averages x 2 readouts x 41 tau points.
  - Tau grid: 0.048 us to 1.968 us, 48 ns step.
- Computed raw readout summaries, per-point SEM across 12 averages, reference-line-normalized signal, per-average mean drift flags, and least-squares sinusoid amplitudes at:
  - Programmed carrier: 1.000 MHz.
  - Expected 13C sidebands from the prior model: 0.615 MHz and 1.385 MHz.
  - Previous exploratory feature: 1.178 MHz.
- Ran a dense LS frequency screen over the short-tau trace. The unconstrained low-frequency screen is dominated by baseline curvature; a restricted 0.5 to 3.0 MHz screen peaks near 1.207 MHz.
- Ran a descriptive fixed-1 MHz damped-cosine fit only as a diagnostic, not as a claim.
- Wrote scratch artifacts:
  - `ramsey_analysis_summary.json`.
  - `ramsey_shorttau_review.png`.

## Plausible interpretation

- The run completed cleanly: bridge status is completed, no stop request, final count text is 35.122 kcps, 12 averages were saved, and no simple per-average mean drift flags were found.
- The raw signal has an early-time transient: signal rises from about 40.70 kcps at 48 ns to roughly 45 kcps by the first few hundred ns, then shows smaller oscillatory/curvature structure.
- Median per-point SEM of the signal readout is about 1.14 kcps. Target LS amplitudes are comparable to this scale:
  - 0.615 MHz: 1.15 kcps raw, 0.0240 ratio-line amplitude.
  - 1.000 MHz: 1.22 kcps raw, 0.0251 ratio-line amplitude.
  - 1.385 MHz: 1.29 kcps raw, 0.0267 ratio-line amplitude.
  - 1.178 MHz: 1.64 kcps raw, 0.0336 ratio-line amplitude.
- The restricted frequency screen prefers about 1.207 MHz, close to the previous non-claim-grade 1.178 MHz feature, but the short window and baseline curvature make this a weak assignment.
- A descriptive 1 MHz damped fit returns an apparent short decay time around 0.28 us with `R2 ~ 0.61`, but this is not claim-grade because it can be driven by the early transient and does not cleanly establish a stable Ramsey carrier.
- Overall, the data are consistent with either very short early-time Ramsey contrast plus baseline/transient effects, or a non-Ramsey transient/artifact that is being partially projected onto nearby MHz sinusoids. The measurement improves the diagnostic picture but still does not support a robust T2star or 13C conclusion.

## Claims not yet supported

- No supported numeric T2star value from this dataset.
- No supported nearby 13C claim.
- No supported claim that the programmed 1.0 MHz carrier is cleanly observed.
- No supported assignment of the 1.18 to 1.21 MHz feature to NV physics or 13C coupling.
- No support for rescuing the previous long-window Ramsey datasets by simply accumulating more Ramsey averages under similar conditions.

## Recommended next action

- Do not run another blind Ramsey accumulation on r03.
- Branch to an alternate diagnostic before any T2star/13C claim. Recommended next action: run a control-oriented protocol that separates Ramsey phase evolution from the early-time transient, such as a short-tau Ramsey phase/detuning control or a Hahn/CPMG-N=1 baseline using the established r03 resonance, then decide whether r03 can yield a supported dephasing conclusion. If the alternate diagnostic does not produce a clean coherent response, close the r03 Ramsey/13C branch as unsupported under current conditions.
