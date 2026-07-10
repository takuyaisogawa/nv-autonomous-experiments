# Ramsey review: refreshed-center r03 long-span run

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, plus relevant Ramsey/pODMR guidance in `md/memory.md` and `md/knowledge.md`.
- New terminal measurement set:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
  - `measurement/m002.json`: submitted job/spec metadata.
  - `measurement/m003.json`: completed bridge result.
  - `measurement/m004.json`, `measurement/m005.json`: terminal status/control snapshots.
- Local outputs created here:
  - `analyze_ramsey.py`
  - `ramsey_analysis_summary.json`

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Confirmed raw export is terminal and shaped as `ExperimentDataEachAvg = [1, 20, 2, 41]`: one scan, 20 averages, two readout roles, 41 tau points.
- Confirmed intended acquisition: `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`, `tau = 0.048..8.048 us` in `0.2 us` steps, `20 x 50000` shots.
- Computed raw signal, reference, point-wise ratio, and linear-reference-normalized signal.
- Ran least-squares sinusoid screens and FFT checks over Ramsey-relevant frequencies, with explicit checks at:
  - carrier: `1.5 MHz`
  - expected 13C sidebands from the project model: `1.115 MHz` and `1.885 MHz`
  - prior diagnostic/control frequencies: `1.623 MHz` and `1.192 MHz`
- Re-ran screens after skipping the first 4 and first 8 tau points.
- Checked per-average ratio frequency screens and average-to-average readout variation.

## Quantitative observations

- Combined raw signal range: `47.746..49.812 kcps`; median raw signal error from export: `1.958 kcps`.
- Combined reference range: `40.569..46.838 kcps`.
- Combined ratio range: `1.0448..1.1953`; median ratio SEM across averages: `0.01365`.
- Average-to-average common-mode readout variation is large: signal mean `41.74..54.90 kcps`, reference mean `37.38..50.37 kcps`; ratio mean `1.0478..1.1260`. Scan order is recorded as `snake`, saved in tau order.
- Target LS amplitudes:
  - Raw signal at `1.5 MHz`: `0.099 kcps`, far below the `1.958 kcps` median raw error.
  - Raw signal at `1.885 MHz`: `0.232 kcps`, also far below raw error.
  - Ratio at `1.5 MHz`: `0.0192`, only modestly above the median per-point ratio SEM and not stable across per-average screens.
  - Ratio at `1.115 MHz`: `0.00364`; ratio at `1.885 MHz`: `0.01197`.
- Full-span LS screen peaks:
  - Raw signal top: near `0.807 MHz` with amplitude `0.307 kcps`.
  - Ratio top: near `2.270 MHz` with amplitude `0.0223`.
  - Reference top: near `2.270 MHz` with amplitude `0.818 kcps`, indicating the ratio peak is likely reference/normalization-sensitive.
- FFT peaks broadly agree that the dominant components do not form a clean carrier-plus-13C-sideband pattern. The ratio FFT has bins near the carrier region, but not cleanly enough to override the raw/readout inconsistency.
- Skip-transient screens did not fix the interpretation:
  - After skipping 4 tau points, ratio top remains near `2.266 MHz`; carrier ratio amplitude drops to `0.0150`.
  - After skipping 8 tau points, ratio top remains near `2.277 MHz`; carrier ratio amplitude stays about `0.0149`.
- Per-average ratio screens are mixed, with top frequencies scattered across roughly `0.15..2.34 MHz`; only a few averages peak near the programmed carrier.

## Plausible interpretation

The refreshed-center long-span Ramsey run is analyzable and appears terminal/valid as an acquisition, but it still does not provide claim-grade Ramsey contrast at the programmed `1.5 MHz` carrier. The combined ratio contains a small carrier-region component, but the raw signal carrier amplitude is much smaller than the raw uncertainty, per-average frequency screens are inconsistent, and the strongest ratio component is mirrored more strongly in the reference channel. The safest interpretation is that normalization/common-mode/reference structure is still dominating the spectral screens.

This run is useful evidence that simply refreshing the weak-pi pODMR center and increasing shots did not produce a clean carrier/sideband Ramsey model on r03 under these conditions.

## Claims not yet supported

- Do not claim a numeric `T2*` from this run.
- Do not claim nearby `13C` coupling from the expected `1.115/1.885 MHz` sidebands.
- Do not claim the `2.27 MHz` ratio-screen peak as a physical Ramsey frequency; it is reference-channel sensitive.
- Do not claim the prior `~1.19 MHz` feature; it remains weak here.
- Do not claim sub-grid microwave resonance precision beyond the pODMR-supported `3.8765 GHz` working center with several-100-kHz uncertainty.

## Recommended next action

Avoid another blind long Ramsey repeat on r03. The next action should be a short, diagnostic protocol change that separates true Ramsey phase evolution from readout/reference structure before investing more time. Recommended options, in priority order:

1. Run an alternate Ramsey acquisition/readout design that directly suppresses or diagnoses reference-channel structure, for example phase-cycled Ramsey or a protocol with a clearer signal/reference contrast validation if available in the local bridge.
2. If no alternate Ramsey route is immediately available, pause r03 Ramsey accumulation and write a supported conclusion that current r03 Ramsey data do not support a reliable `T2*` or `13C` claim under the tested conditions.
3. Only after a protocol-level diagnostic resolves the normalization/reference issue should a T2* decay fit or 13C sideband extraction be attempted.
