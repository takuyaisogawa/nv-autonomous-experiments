# Ramsey Review: short-tau high-SNR r03 diagnostic

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New measurement data: `measurement/m001.json` raw savedexperiment export, plus execution metadata/control/status in `measurement/m002.json` through `measurement/m005.json`.
- Scratch outputs created: `analyze_ramsey.py`, `scratch_ramsey/ramsey_analysis_summary.json`, `scratch_ramsey/ramsey_traces.png`, `scratch_ramsey/ramsey_frequency_screen.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey.py`.
- Parsed `ExperimentData` with shape `[2, 41]` and `ExperimentDataEachAvg` with shape `[12, 2, 41]`.
- Used the project/default Ramsey readout convention: readout 1 as reference, readout 2 as signal, while judging signal presence primarily from raw signal.
- Confirmed scan metadata: `ramsey.xml`, tau `0.048..1.968 us`, 41 points, 48 ns spacing, 12 averages, 90000 reps per average, final count from result `35.122 kcps`.
- Estimated field and 13C frequencies from the project mw center: `(3.8759 GHz - 2.87 GHz) / 2.8 MHz/G = 359.25 G`; 13C Larmor `0.3846 MHz`; expected Ramsey sidebands for `det=1.0 MHz` at `0.6154 MHz` and `1.3846 MHz`.
- Calculated per-tau SEM across the 12 stored averages: median raw-signal SEM `1.14 kcps`, reference SEM `1.12 kcps`, ratio SEM `0.0127`.
- Least-squares screened sinusoidal components with constant + linear baseline. Target amplitudes:
  - `1.000 MHz` carrier: raw `1.28 kcps` (`1.13x` median raw SEM), ratio `0.0274` (`2.16x` median ratio SEM).
  - `0.615 MHz` lower 13C sideband: raw `1.10 kcps` (`0.97x` median raw SEM), ratio `0.0243` (`1.91x` median ratio SEM).
  - `1.385 MHz` upper 13C sideband: raw `1.22 kcps` (`1.07x` median raw SEM), ratio `0.0271` (`2.14x` median ratio SEM).
- Frequency screen was dominated by low-frequency/baseline structure: raw top components were near `0.100 MHz` (`26.0 kcps`), `0.220 MHz` (`4.92 kcps`), and `0.340 MHz` (`2.33 kcps`). The largest non-low target-near component was around `1.204 MHz` with raw amplitude `1.69 kcps`.
- Stored-average mean levels varied substantially: signal mean min/max `37.47..51.21 kcps` and reference mean min/max `42.02..55.19 kcps`, although first/last means were closer. This looks like common-mode stored-average variation and is important provenance for normalization.
- Compared fixed-frequency damped-cosine descriptions with smooth baseline-only fits. A fixed `1.0 MHz` damped-cosine grid fit gave descriptive `T2star ~0.16..0.19 us`, but it fit worse than smooth polynomial baseline models by AIC/SSE. This is not a supportable T2star estimate.

## Plausible interpretation

- The measurement completed cleanly and produced analyzable high-shot short-tau data.
- The new short-tau window shows a real early-time structure: signal/reference starts low, rises over the first few hundred ns, and then rolls over. This is consistent with either very fast Ramsey contrast loss plus baseline curvature or a pulse/readout/baseline transient.
- There is modest oscillatory content near the intended carrier region, with a broad screen maximum around `1.1..1.2 MHz`, but the target `1.0 MHz` raw amplitude is only comparable to the measured SEM and the expected 13C sidebands have similar amplitudes. The evidence does not cleanly det-follow or sideband-resolve.
- The result supports the previous conclusion that r03 is an aligned, trackable NV with usable pODMR resonance evidence, but the Ramsey branch remains non-claim-grade.

## Claims not yet supported

- No well-supported numeric `T2star` claim from this dataset. The descriptive `~0.16..0.19 us` fit is not promoted because smooth baseline-only models explain the shape at least as well.
- No supported nearby `13C` claim. The expected sidebands at about `0.615 MHz` and `1.385 MHz` are not distinct from the carrier-region/noise/baseline structure.
- No claim that the broad `~1.2 MHz` component is a physical Ramsey carrier. Per-average frequency screens are inconsistent, and low-frequency baseline components dominate.
- No claim that normalization-only contrast is sufficient evidence. Raw signal evidence remains marginal.

## Recommended next action

Do not run another blind Ramsey repeat on r03. Treat this short-tau diagnostic as still non-claim-grade and switch to an alternate, explicitly discriminating step: either design a control/det-shifted short-tau Ramsey whose only pass criterion is a det-following raw carrier, or close the r03 Ramsey/13C branch as unsupported under the present Ramsey protocol. If continuing experimentally, the next plan should first target artifact rejection, not higher shot count.
