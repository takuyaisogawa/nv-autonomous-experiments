# Ramsey review: refreshed-center long-span run

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, plus Ramsey/frequency context searched in `md/` and `evidence/`.
- New measurement:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
  - `measurement/m002.json`: submitted run spec.
  - `measurement/m003.json`: terminal result.
  - `measurement/m004.json` and `measurement/m005.json`: final status/control.
- Scratch outputs created here:
  - `analyze_ramsey.py`
  - `ramsey_analysis_summary.json`
  - `ramsey_review_plot.png`

## Calculations/scripts run

- Ran `python analyze_ramsey.py`.
- Confirmed terminal run status: job `nv23_ramsey_20260514_055148_auto_ramsey` completed at `2026-05-14T09:28:25`, elapsed `12990 s`, no stop request or monitor error recorded.
- Measurement settings from `measurement/m002.json` / raw export:
  - `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`.
  - `tau = 48 ns..8.048 us`, `41` points.
  - `20 x 50000` repetitions, i.e. `1.0e6` shots per tau point.
  - Snake scan order, data saved in tau order.
- Extracted combined raw signal, reference readout, point-wise signal/reference ratio, and signal normalized to a fitted linear reference line.
- Least-squares sinusoid checks with offset/slope nuisance terms at:
  - carrier `1.5 MHz`;
  - expected 13C sidebands `1.115 MHz` and `1.885 MHz`;
  - prior det-shift top/control frequencies `1.623 MHz` and `1.192 MHz`.
- Ran exploratory frequency screens from `0.125..2.45 MHz`, full span and skipping first 4 tau points.
- Checked per-average top ratio frequencies and simple average-to-average count drift.

## Quantitative observations

- Combined trace scale:
  - raw signal mean `48.789 kcps`, peak-to-peak `2.065 kcps`;
  - reference mean `44.670 kcps`, peak-to-peak `6.269 kcps`;
  - point ratio mean `1.0928`, peak-to-peak `0.1505`.
- Per-point uncertainty from stored averages:
  - median raw-signal SEM `0.867 kcps`;
  - median ratio SEM `0.01365`.
- Average-to-average brightness changed substantially:
  - per-average signal mean range `41.739..54.899 kcps`;
  - first 10 averages mean `50.002 kcps`, last 10 averages mean `47.577 kcps`, shift `-2.425 kcps`.
- Target LS amplitudes:
  - carrier `1.5 MHz`: raw `0.099 kcps` (`~1.0 sigma`), ratio `0.0192` (`~3.5 sigma`), fitted-reference norm `0.00220` (`~1.0 sigma`).
  - 13C low `1.115 MHz`: raw `0.018 kcps` (`~0.2 sigma`), ratio `0.00364` (`~0.6 sigma`), fitted-reference norm `0.00038` (`~0.2 sigma`).
  - 13C high `1.885 MHz`: raw `0.232 kcps` (`~2.6 sigma`), ratio `0.0120` (`~2.0 sigma`), fitted-reference norm `0.00520` (`~2.6 sigma`).
- Exploratory screens:
  - raw and fitted-reference-normalized views are dominated near `0.800..0.808 MHz` and `1.897..1.924 MHz`, not by the programmed `1.5 MHz` carrier.
  - point-wise ratio has a top component near `2.266..2.270 MHz`, with a secondary component near `1.515..1.517 MHz`.
  - per-average ratio top frequencies are scattered: examples include `0.125`, `0.428`, `0.610`, `0.852`, `0.992`, `1.532..1.569`, `1.891..1.923`, `2.119..2.343 MHz`.

## Plausible interpretation

- The run is analyzable and completed normally, but it is not a clean Ramsey/T2star result.
- The point-wise ratio contains a carrier-near feature around `1.5 MHz`, but this is not supported by the raw signal channel or by fitted-reference-line normalization. Given the large reference readout variation and average-to-average brightness drift, the ratio-only carrier response could be denominator/drift sensitive.
- The raw/fitted-reference screens show stronger components near `~0.8 MHz` and `~1.9 MHz`; the high-side `1.885 MHz` target is only marginal and not paired with a matching low-side `1.115 MHz` feature. That is insufficient for a nearby-13C sideband conclusion.
- Compared with prior short-tau det-shift evidence, this run does not cleanly consolidate into a stable carrier/sideband model. It improves shot budget but still leaves inconsistent frequency content across readout treatments and averages.

## Claims not yet supported

- No defensible numeric `T2*` should be promoted from this dataset.
- No well-supported nearby `13C` coupling claim is supported.
- The ratio-only `1.5 MHz` carrier feature should not be treated as a clean Ramsey carrier without corroboration in raw/readout-aware views.
- The marginal high-side feature near `1.885 MHz` should not be interpreted as a 13C sideband because the low-side partner is absent and per-average screens are inconsistent.

## Recommended next action

- Do not run another blind long-span Ramsey repeat on r03 under the same conditions.
- Treat the current r03 Ramsey/13C evidence as unsupported under this protocol unless an alternate protocol is used.
- Best next experimental action: switch to an alternate coherence/diagnostic protocol that is less sensitive to reference-line drift and denominator artifacts, such as a Hahn echo or a phase-cycled/dual-quadrature Ramsey variant if available in the validated sequence set. If the project must close without new protocol development, record a supported negative/unsupported conclusion for r03 T2star/13C under the tested Ramsey conditions.
