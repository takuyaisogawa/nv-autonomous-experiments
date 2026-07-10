# Ramsey review: refreshed-center long-span r03 run

## Files/data used

- `project/brief.md`, `project/advice.md`, `project/state.md`, and `md/memory.md` for project objective, current candidate state, and prior claim boundaries.
- `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200`.
- `measurement/m002.json`: submitted Ramsey job specification.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal result/status/control snapshots for `nv23_ramsey_20260514_055148_auto_ramsey`.
- `evidence/e001.json` and `evidence/e005.json`: immediately preceding fine weak-pi pODMR refresh context selecting `mw_freq = 3.8765 GHz`.
- Generated locally: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, and `ramsey_review_plot.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey.py`.
- Parsed the Ramsey raw export as readout 1 = reference and readout 2 = Ramsey signal, with `ExperimentDataEachAvg` shape `[20 averages, 2 readouts, 41 tau points]`.
- Confirmed scan settings: `tau = 0.048..8.048 us`, `0.200 us` step, 41 points, `20 x 50000 = 1.0e6` shots/tau, `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`.
- Checked terminal health: completed, final counts `43.433 kcps`, stop not requested in control/status, no abort in result safety.
- Computed raw signal, point-wise `signal/reference`, and signal normalized by a fitted reference line.
- Estimated point uncertainty from stored-average scatter: median signal SEM `0.850 kcps`, median point-wise-ratio SEM `0.0116`, median refline-normalized SEM `0.00937`.
- Ran fixed-frequency least-squares fits with intercept + linear baseline + sine/cosine at the programmed carrier `1.500 MHz`, expected 13C sidebands `1.115/1.885 MHz`, and prior diagnostic controls `1.192/1.623 MHz`.
- Ran dense LS frequency screens from `0.25..2.35 MHz`, both full-span and skipping the first 4 tau points.
- Ran a simple windowed FFT check after linear detrending.
- Checked per-average top-frequency consistency and a simple stored-average common-mode drift trend. Common-mode first-to-last change was `-0.00038` fraction, but average-to-average brightness varied widely (`39.56..52.64 kcps`), so this is not a full drift certification.

## Plausible interpretation

- The measurement is analyzable and not obviously failed. Counts are healthy and the bridge result/status do not show a hard anomaly.
- The data contain oscillatory structure, but it is not cleanly claim-grade.
- Full-span dense LS screens prefer about `2.268 MHz` in raw, point-wise ratio, and refline-normalized views. Windowed FFT also has strong bins near `2.317 MHz` and near the carrier region (`1.463/1.585 MHz` bins).
- After skipping the first 4 tau points, raw and refline-normalized LS screens move near the programmed carrier (`1.520 MHz` raw, `1.538 MHz` refline-normalized). This is plausibly carrier-like Ramsey response after an early-time transient or baseline effect.
- The programmed carrier amplitude is small relative to point scatter: raw LS amplitude `0.713 kcps` full-span and `0.520 kcps` after skip4, versus median raw signal SEM `0.850 kcps`. Refline-normalized carrier amplitude is `0.0145` full-span and `0.0109` after skip4, near the median normalized SEM `0.00937`.
- 13C sideband targets are weak. Refline-normalized full-span amplitudes are `0.00309` at `1.115 MHz` and `0.00557` at `1.885 MHz`; skip4 amplitudes fall to `0.000258` and `0.00155`. These are below the carrier and not consistently enhanced.
- Per-average top frequencies are broadly scattered; there is no dominant frequency shared by the stored averages. This weakens any single-frequency or sideband interpretation.

## Claims not yet supported

- Do not claim a numeric T2star from this run. Signal presence at the programmed carrier is not strong enough and is sensitive to excluding early points and to the readout/normalization view.
- Do not claim nearby 13C coupling. The expected sidebands at `1.115/1.885 MHz` are weak and not consistently supported by full-span/skip-transient/per-average checks.
- Do not claim the `2.27 MHz` full-span screen peak as a physical Ramsey frequency. It may be structure from early-time/transient/baseline behavior or noise; it does not track the planned carrier/sideband model.
- Do not claim a resolved decay envelope or publishable coherence parameter from the descriptive oscillatory structure.

## Recommended next action

Avoid another blind Ramsey repeat on the same settings. The highest-value next step is to choose an alternate protocol or diagnostic that separates true Ramsey phase evolution from early-time/baseline artifacts, such as a deliberately phase-cycled Ramsey/quadrature variant if available in the validated sequence set, or a Hahn echo / dynamical-decoupling branch to test whether coherence is present when slow detuning noise is refocused. If no alternate validated protocol is available, record the current r03 Ramsey/T2star/13C result as unsupported/negative under these conditions rather than continuing same-condition accumulation.
