# Ramsey Review

## Files/data used

- `project/brief.md`, `project/advice.md`, and `project/state.md` for the objective, candidate history, and prior Ramsey/pODMR interpretation.
- `measurement/m001.json`: raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal result/status/control snapshots for `nv23_ramsey_20260514_055148_auto_ramsey`.
- New local reproducibility artifacts: `analyze_ramsey.py` and `ramsey_analysis_summary.json`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Confirmed the measurement matches the planned refreshed-center Ramsey:
  - `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`.
  - `tau = 0.048..8.048 us`, step `0.2 us`, `41` points.
  - `20` averages x `50000` repetitions.
  - Job status completed, `stop_requested=false`, monitor `last_error` empty in the status/control snapshots.
- Built combined raw signal, reference, and signal/reference ratio from `ExperimentData` and `ExperimentDataEachAvg`.
- Estimated point scatter across stored averages:
  - mean signal `48.789 kcps`, mean reference `44.670 kcps`.
  - median signal SEM `0.867 kcps`.
  - median ratio SEM `0.01365`.
- Performed scan-order-aware common-mode drift check using `ScanOrderEachAvg`/snake order.
  - Average 3 was flagged by the simple acquisition-order trend check: common-mode span fraction `0.138` versus residual scatter fraction `0.033`.
  - Other averages were not flagged by this criterion; average 9 was borderline but below the implemented `max(0.08, 3*scatter)` threshold.
- Ran least-squares sinusoid screens with offset and linear baseline over `0.125..2.45 MHz`.
  - Combined ratio, full span: strongest screen near `2.270 MHz`, amplitude `0.02233`, `R2=0.371`.
  - Combined ratio, skipping first 4 tau points: strongest screen near `2.268 MHz`, amplitude `0.01688`, `R2=0.295`.
  - Raw signal full span: strongest screen near `0.808 MHz`, amplitude `0.307 kcps`, `R2=0.277`.
  - Excluding flagged average 3 preserved the combined ratio top near `2.267 MHz`; it did not promote the carrier/sideband model.
- Checked planned target frequencies:
  - Carrier `1.500 MHz`: ratio amplitude `0.01916` full span, `0.01498` skip-4; raw signal amplitude `0.099 kcps`.
  - Expected 13C lower sideband `1.115 MHz`: ratio amplitude `0.00364` full span, `0.00082` skip-4; raw signal amplitude `0.018 kcps`.
  - Expected 13C upper sideband `1.885 MHz`: ratio amplitude `0.01197` full span, `0.00651` skip-4; raw signal amplitude `0.232 kcps`.
  - Prior `1.192 MHz` control: ratio amplitude `0.00262` full span, `0.00200` skip-4.
- Per-average ratio frequency screens were mixed: several averages peak near `1.53..1.57 MHz`, but many peak elsewhere including low frequency, `~1.89 MHz`, `~2.1..2.34 MHz`, and `~2.26 MHz`.

## Plausible interpretation

The refreshed long-span Ramsey produced analyzable data and mostly healthy run metadata, but it still does not give a clean Ramsey carrier/decay model. The combined ratio contains carrier-region power at `1.5 MHz`, yet the strongest combined ratio screen is near `2.27 MHz`, close enough to the high-frequency edge of the sampled band to require caution, while the raw signal screen prefers `~0.81 MHz`. Per-average frequency estimates remain scattered rather than clustering around the programmed carrier or a stable 13C sideband pair.

The result is therefore best interpreted as another non-claim-grade Ramsey on accepted r03 under the current protocol. It argues against promoting the old fixed `~1.192 MHz` feature, because that target is weak here, but it also does not supply a supported T2star or nearby-13C conclusion.

## Claims that are not yet supported

- A numeric T2star for r03 is not supported from this dataset.
- A resolved 13C coupling/sideband claim is not supported.
- The `~2.27 MHz` combined-ratio feature should not be claimed as a physical Ramsey frequency without an explicit aliasing/sequence/readout/systematics check and reproducibility across averages or a shifted-detuning test.
- The carrier at `1.5 MHz` should not be treated as established just from combined-ratio amplitude, because raw-signal support is weak and per-average screens are inconsistent.
- The single drift-flagged average does not by itself invalidate the run, but it is enough provenance to avoid over-interpreting a marginal spectral result.

## Recommended next action

Do not run another blind Ramsey repeat on r03. The next action should be a decision step: either switch to an alternate protocol designed to establish T2star more robustly under weak/unstable Ramsey contrast, or close the current r03 Ramsey/13C branch with a supported "not established under these conditions" conclusion. If continuing experimentally, first perform an explicit systematics check for high-frequency/near-Nyquist ratio artifacts and readout-normalization effects before spending more long-span Ramsey time.
