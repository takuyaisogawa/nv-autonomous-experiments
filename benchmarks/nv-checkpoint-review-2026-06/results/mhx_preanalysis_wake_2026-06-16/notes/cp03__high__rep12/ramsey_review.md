# Ramsey Review: short-tau/high-SNR r03 diagnostic

## Files/data used

- Project context: `project/state.md`, `project/brief.md`, `project/advice.md`, `context.json`.
- Prior Ramsey planning/context: `evidence/e006.json`, `evidence/e009.json`, `evidence/e017.md`.
- New terminal measurement packet:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-230350`.
  - `measurement/m002.json`: bridge job/spec.
  - `measurement/m003.json`: terminal result; completed, final count `35.122 kcps`.
  - `measurement/m004.json`: terminal status; completed, no monitor error recorded.
  - `measurement/m005.json`: control; no stop requested.
- Derived local outputs: `analyze_ramsey_shorttau.py`, `ramsey_shorttau_analysis.json`, `ramsey_shorttau_review.png`.

## Calculations/scripts run

Ran:

```powershell
python analyze_ramsey_shorttau.py
```

The script reads only local snapshot files. It treats trace 1 as the `mS=0` reference and trace 2 as the Ramsey signal, following the project protocol notes for `ramsey.xml` with `full_experiment=0`.

Checks performed:

- Raw/reference summary over `tau = 0.048..1.968 us`, `41` points, `48 ns` step, `12 x 90000 = 1.08e6` shots per point.
- Per-point SEM from stored averages.
- Scan-order-aware common-mode drift using `ScanOrderEachAvg` snake order.
- Linear-baseline plus sinusoid least-squares screens at:
  - programmed carrier `1.000 MHz`
  - expected 13C sidebands `0.615423 MHz` and `1.384577 MHz`
  - prior exploratory component `0.884 MHz`
- Exploratory frequency sweep and FFT check.

Key quantitative results:

- Median raw signal SEM: `1.138 kcps`, close to the planned `~1.17 kcps`; median ratio SEM: `0.0127`.
- Scan-order drift flags: none; largest acquisition-order common-mode drop score `0.060`.
- Cross-average brightness variation remains nontrivial: signal average means span `37.47..51.21 kcps` (`13.74 kcps` range); ratio means span `0.893..0.956`.
- Programmed `1.000 MHz` LS amplitude:
  - raw signal: `1.375 kcps`, `R2` improvement vs linear baseline `0.409`
  - signal/reference ratio: `0.0236`, `R2` improvement `0.325`
  - signal/fitted-reference-line: `0.0283`, `R2` improvement `0.410`
- Expected sideband-frequency fits are comparable over this short window:
  - `0.615 MHz` ratio amplitude `0.0235`
  - `1.385 MHz` ratio amplitude `0.0247`
- FFT top ratio bins after linear detrending: `1.524 MHz`, `1.016 MHz`, `0.508 MHz`.
- Nominal frequency resolution from the `1.92 us` span is only about `0.52 MHz`, so the `1.0 MHz` carrier and +/-`0.385 MHz` 13C sidebands are not cleanly resolvable in this dataset.

## Plausible interpretation

The short-tau/high-SNR diagnostic completed safely and did improve the per-point SEM to the planned scale. Unlike the prior `0..8 us` det=`1.0 MHz` Ramsey, the combined short-tau data has a visible early-time oscillatory component that is compatible with a `1 MHz` Ramsey carrier in simple LS checks.

That said, the evidence is still not clean enough for a claim-grade T2star/13C conclusion. The raw `1 MHz` amplitude is only `~1.2x` the median raw SEM, there is substantial average-to-average brightness variation, and the short span makes the carrier and expected 13C sidebands highly covariant. The exploratory LS screen is also dominated by a slow low-frequency trend at the lower sweep bound, while FFT bins are broad and place the largest ratio bin at `1.524 MHz`.

Best current reading: r03 may have a weak early-time Ramsey-like response that was washed out in the long-window scans, but the present dataset supports only a tentative carrier-presence hint, not a robust decay-envelope measurement.

## Claims not yet supported

- No numeric T2star should be promoted from this dataset.
- No nearby-13C coupling/sideband assignment is supported; the short-tau span cannot resolve `1.0 MHz` from the expected `0.615/1.385 MHz` sidebands.
- Do not claim that the `1.524 MHz` FFT bin is a physical 13C sideband; it is within the broad-resolution/short-window ambiguity.
- Do not claim the r03 Ramsey branch is entirely null; this run gives a weak carrier-like hint that deserves targeted confirmation or explicit closeout.

## Recommended next action

Do not run another blind long-window Ramsey repeat. Use one targeted discriminator: repeat a short-tau/high-SNR Ramsey with a deliberately changed programmed detuning or phase-cycled readout, keeping the same r03 target and similar shot budget. Require the fitted frequency/phase to follow the programmed change before fitting T2star. If it does not follow, close the r03 Ramsey/T2star and 13C branch as unsupported under current conditions and switch to an alternate protocol rather than accumulating more Ramsey repeats.
