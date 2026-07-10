# Ramsey Review: short-tau/high-SNR r03 diagnostic

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `evidence/e017.md`.
- New terminal Ramsey data/artifacts:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
  - `measurement/m002.json`: bridge job spec/metadata.
  - `measurement/m003.json`: terminal bridge result.
  - `measurement/m004.json`: terminal bridge status.
  - `measurement/m005.json`: run control state.
- Generated local analysis artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_shorttau_diagnostic.png`.

## Calculations or scripts run

- Inspected JSON schemas and array dimensions with local Python.
- Ran `python analyze_ramsey.py`.
- The script computed raw readout summaries, per-average SEM, stored-average drift screens, fixed-frequency least-squares screens at 0.615, 1.000, and 1.385 MHz, a broad frequency screen, FFT bin check, per-average carrier phase/amplitude, early-vs-late subset checks, and an exploratory fixed-1 MHz decay fit.

Key quantitative checks:

- Run completed cleanly: `auto__ramsey`, tau `0.048..1.968 us`, step `48 ns`, 41 points, `12 x 90000` reps, `mw_freq=3.8759 GHz`, `det=1.0 MHz`, final counts `35.122 kcps`, no stop request.
- Raw readout 1/reference mean `48.57 kcps`; raw readout 2/signal mean `44.65 kcps`, range `40.70..47.20 kcps`, peak-to-peak `6.50 kcps`.
- Median per-point SEM from stored averages was about `1.12 kcps` for readout 1 and `1.14 kcps` for signal.
- Stored-average common-mode level drifted: first 8 averages mean `48.29 kcps`, last 4 mean `43.25 kcps`; average 2 was high (`+3.1` robust sigma) and average 11 low (`-3.5` robust sigma). This is provenance/caution rather than a hard failure because the run completed and normalized carrier screens survive subset checks.
- Fixed-frequency LS at the programmed carrier:
  - Raw signal carrier amplitude `1.28 +/- 0.27 kcps`, `R2=0.455`.
  - Point-wise ratio amplitude `0.0274 +/- 0.0061`, `R2=0.447`.
  - Reference-line-normalized amplitude `0.0264 +/- 0.0056`, `R2=0.476`.
- Expected sideband screens are not discriminating: low sideband `0.615 MHz` raw amplitude `1.10 kcps`, high sideband `1.385 MHz` raw amplitude `1.22 kcps`, similar to the carrier scale.
- Broad frequency screen is dominated by the lower search edge at `0.25 MHz` with raw amplitude `3.89 kcps`, indicating a larger slow transient/envelope than the target carrier.
- FFT after linear detrending has coarse bin spacing `0.508 MHz`; the largest bin is `1.524 MHz`, so FFT does not provide a precise carrier or sideband assignment in this short window.
- Carrier robustness:
  - First 8 averages: raw carrier `1.48 kcps`, ratio carrier `0.0300`.
  - Last 4 averages: raw carrier `0.89 kcps`, ratio carrier `0.0219`.
  - Excluding common-mode outlier averages with `|z| > 2.5`: raw carrier `1.29 kcps`, ratio carrier `0.0278`.
  - Carrier phase is mostly stable across stored averages, with late/outlier averages less clean.
- Exploratory fixed-1 MHz decay fit is not claim-grade:
  - Raw signal fit gives `T2* ~0.27 us` with `~2.4 us` uncertainty and poor `R2=0.19`.
  - Normalized fits give `T2* ~0.16..0.18 us` with `~0.10..0.11 us` uncertainty, but they rely strongly on the early transient/baseline model.

## Plausible interpretation

The short-tau/high-SNR diagnostic likely did reveal a weak early-time Ramsey component at the programmed `1.0 MHz` carrier that was not convincingly visible in the previous long-window data. The component is present in raw signal, point-wise ratio, and reference-line-normalized views, and it survives early/late and outlier-excluded subset checks at roughly the `0.9..1.5 kcps` raw scale.

However, the dataset is still contaminated by a larger slow transient/envelope and appreciable count drift across stored averages. The target carrier is comparable to the per-point SEM, and the fitted decay is baseline/view dependent. The short tau span is useful for early-time carrier visibility but is intrinsically poor for resolving 13C sidebands.

## Claims that are not yet supported

- No supported numeric `T2*` claim from this dataset. The exploratory fixed-carrier decay fits are unstable and baseline-sensitive.
- No supported 13C coupling/sideband conclusion. The 0.615, 1.000, and 1.385 MHz LS amplitudes are similar, and FFT resolution is too coarse for sideband assignment.
- No claim that the larger `0.25 MHz` broad component is a physical Ramsey frequency; it is more plausibly a transient/envelope/baseline term unless a control shows otherwise.
- No claim that the r03 branch is complete. This result improves the carrier evidence but does not finish the objective.

## Recommended next action

Do not run another blind long-window Ramsey repeat. First refresh/check tracking and resonance conditions because final counts ended at `35.122 kcps`, down about `20%` from the pre-run/latest `~44 kcps` context.

Then design a carrier-confirmation control that separates true Ramsey phase accumulation from the slow transient: same short-tau/high-shot regime, but with an intentional detuning/phase-control change such as a detuning sign flip or zero-detuning control if the current manifest/advisory supports it safely. Promote a T2* fit only if the carrier moves/disappears as predicted while the slow transient does not. If confirmed, follow with a longer/high-quality Ramsey or alternate spectroscopy designed specifically for 13C resolution; if not confirmed, close the r03 Ramsey/13C branch as unsupported under current conditions or switch protocol.
