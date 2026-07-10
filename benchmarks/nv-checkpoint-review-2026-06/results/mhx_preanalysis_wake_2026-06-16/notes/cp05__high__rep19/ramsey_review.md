# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json`.
- New Ramsey measurement:
  - `measurement/m001.json`: terminal raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
  - `measurement/m002.json`: bridge job spec.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json` and `measurement/m005.json`: run status/control provenance.
- Recent planning context checked: `evidence/e022.json`, `evidence/e023.json`, `evidence/e024.json`.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`; outputs are `ramsey_analysis.json` and `ramsey_analysis.png`.
- Verified raw-export axis/readout contract: `ExperimentData` shape `[2,41]`, `ExperimentDataEachAvg` shape `[20,2,41]`, and mean of per-average data reproduces combined data to `1.4e-14`.
- Interpreted readouts from the actual sequence text: readout 0 is the 0-level reference; with `full_experiment=0`, readout 1 is the Ramsey signal.
- Built tau from metadata: `0.048..8.048 us`, `0.200 us` step, 41 points. Run settings were `mw_freq=3.8765 GHz`, `det=1.5 MHz`, `20 x 50000` shots, final counts `43.433 kcps`, snake scan order.
- Checked raw signal, point-wise `signal/reference`, and `signal/linear-reference` views; computed per-point SEM from stored averages.
- Ran linear-detrended least-squares sinusoid screens over `0.15..2.45 MHz`, both full-span and skipping the first 4 tau points.
- Checked target amplitudes and per-average vector coherence at carrier `1.500 MHz`, expected 13C sidebands `1.115/1.885 MHz`, prior empirical `1.192 MHz`, and prior det-shift full-span `1.623 MHz`.
- Ran descriptive fixed-carrier damped-cosine fits at `1.5 MHz`; these are fit diagnostics only, not promoted parameters.

## Plausible interpretation

- Data quality is usable but not clean: median raw signal SEM is `0.850 kcps`; median ratio SEM is `0.0116`; median fitted-reference-normalized SEM is `0.00937`.
- There is common-mode drift across averages, but no count collapse: average signal means span `37.38..50.37 kcps`; no stored average is below `20 kcps`. First-half to second-half means drop in both reference (`50.00 -> 47.58 kcps`) and signal (`45.80 -> 43.54 kcps`), while mean ratio is nearly stable (`0.9159 -> 0.9150`).
- The programmed carrier has the best physically motivated support in this dataset. At `1.5 MHz`, combined amplitudes are `0.705 kcps` raw, `0.0157` point-wise ratio, and `0.0145` fitted-reference normalization. Per-average phase-vector coherence is high for raw and fitted-reference views (`~0.85`) and lower but still present for point-wise ratio (`~0.74`).
- The blind frequency screen does not peak at the programmed carrier: all three full-span views peak near `2.27 MHz`, and the skip-first-4 screen also peaks near `2.27 MHz`. That prevents treating the carrier as a clean standalone Ramsey spectrum.
- The prior fixed `~1.192 MHz` empirical component is weak here (`0.0019` ratio amplitude, low coherence), which argues against simply promoting that earlier feature as a stable artifact or physical carrier.
- A fixed-`1.5 MHz` damped-cosine fit gives a short apparent decay: `T2star ~1.04 us` in raw and fitted-reference-normalized views, but `~2.13 us` in point-wise ratio, with only moderate `R2 ~0.43..0.55`. Treat this as a plausible short-T2star hint, not a supported T2star value.
- Expected 13C sidebands are not supported. Lower sideband `1.115 MHz` is weak and incoherent across views (`0.146 kcps` raw, `0.0028..0.0030` normalized, coherence `<0.29`). Upper sideband `1.885 MHz` is somewhat larger in point-wise ratio but not consistent enough across raw/fitted-reference views or per-average coherence to support a 13C assignment.

## Claims that are not yet supported

- A well-supported numeric T2star for r03 is not yet established from this run.
- A nearby 13C coupling, 13C sideband splitting, or specific 13C Hamiltonian parameter is not supported.
- A broad claim that no nearby 13C exists is not supported; only "no Ramsey-visible 13C sideband under these conditions" is supported.
- The blind `~2.27 MHz` peak should not be assigned to a physical transition from this analysis alone.
- The fixed-carrier fit results should not be used downstream as claim-grade parameters because the blind screen peaks elsewhere and fitted T2star depends on normalization choice.

## Recommended next action

- Do not run another blind 8-us Ramsey repeat as the immediate next step.
- If the priority is a claim-grade T2star, run a refreshed-center short-tau Ramsey focused on the apparent decay window, for example using the same `mw_freq=3.8765 GHz` and `det=1.5 MHz` but concentrating points over roughly `0.048..3 us` with high shots and even averages, then require raw/fitted-reference carrier consistency before fitting.
- If the priority is a 13C conclusion, move away from Ramsey-only sideband hunting after this negative sideband check; use an echo/CPMG/XY8-style targeted nuclear-spin spectroscopy protocol, or record a limited conclusion that Ramsey has not shown 13C sidebands under the tested conditions.
