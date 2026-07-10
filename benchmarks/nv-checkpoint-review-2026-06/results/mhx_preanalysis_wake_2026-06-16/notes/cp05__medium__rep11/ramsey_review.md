# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `md/memory.md`, `md/knowledge.md`, and `context.json`.
- New terminal Ramsey measurement: `measurement/m001.json` raw savedexperiment export and `measurement/m002.json` to `measurement/m005.json` bridge/spec/status/control metadata.
- Measurement identity: `nv23_ramsey_20260514_055148_auto_ramsey`, savedexperiment `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`, `ramsey.xml`, `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`, `tau = 0.048..8.048 us` in 41 points, `20 x 50000` shots, snake scan order.
- Scratch outputs created here: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis_stdout.txt`, and `ramsey_analysis_plot.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py` to parse `measurement/m001.json`, extract channel means and per-average data, compute signal/reference ratio and fitted-reference-line normalization, perform fixed-frequency least-squares sinusoid checks, scan frequencies from 0.2 to 2.4 MHz, inspect per-average top frequencies/phases, and generate a diagnostic PNG.
- The first plotting attempt failed because Matplotlib selected a broken Tk backend; the script was updated to use the noninteractive `Agg` backend and then completed.
- Health/drift checks from metadata: run completed, final counts `43.433 kcps`, no stop requested/applied, safe shutdown ok, monitor `last_error` empty. Per-average mean-ratio z-score screen flagged no averages at `abs(z) > 3`.
- Basic raw stats: mean signal `48.789 kcps`, mean reference `44.670 kcps`, mean ratio `1.09284`, ratio peak-to-peak `0.1505`, median ratio SEM `0.01365`, median raw-signal SEM `0.867 kcps`.
- Target LS checks:
  - Programmed carrier `1.5 MHz`: ratio amplitude `0.01916`, about `1.40 x` median ratio SEM; raw-signal amplitude only `0.099 kcps`, far below raw SEM.
  - Expected 13C sidebands `1.1152/1.8848 MHz`: ratio amplitudes `0.00365` and `0.01197`; raw-signal amplitudes `0.018 kcps` and `0.232 kcps`.
  - Prior fixed artifact/control `1.192 MHz`: ratio amplitude `0.00262`.
  - Prior det-shift full-span `1.623 MHz`: ratio amplitude `0.01007`.
- Frequency screens:
  - Full ratio top is near `2.27 MHz` with amplitude `0.02233`, not a planned carrier/sideband.
  - Ratio after skipping first 4 tau points still tops near `2.266 MHz`.
  - Fitted-reference-line normalization and raw signal both top near `0.807 MHz` with raw amplitude `0.307 kcps`, not a planned carrier/sideband.
  - Per-average ratio top frequencies are mixed: examples include `0.430`, `2.264`, `1.926`, `1.572`, `0.854`, `1.536`, `2.250`, `1.532`, `1.434`, `1.892`, etc.
- Per-average phase/coherence check:
  - At `1.5 MHz`, reference-channel coherent amplitude is `0.705 kcps` with phase-resultant `0.829`, while signal-channel coherent amplitude is only `0.099 kcps` with phase-resultant `0.088`.
  - At the ratio-screen top `2.27 MHz`, reference-channel coherent amplitude is `0.818 kcps` with phase-resultant `0.879`, while signal-channel coherent amplitude is only `0.109 kcps`.

## Plausible interpretation

- The run appears technically valid and analyzable: it completed with healthy counts, expected metadata, no stop condition, and no simple per-average drift outlier.
- This is still not claim-grade Ramsey/T2star evidence. The programmed `1.5 MHz` carrier is not a strong raw-signal feature, and the planned `1.115/1.885 MHz` 13C sidebands are weak/inconsistent.
- The carrier-like ratio response is plausibly dominated by structure in the reference/readout channel rather than a coherent Ramsey oscillation in the signal channel. This is especially clear because the reference channel is phase-coherent at `1.5 MHz` and `2.27 MHz`, while the signal channel is not.
- The mismatch between views matters: point-wise ratio favors `2.27 MHz`, fitted-reference-line/raw signal favor `0.807 MHz`, and neither view cleanly supports the planned carrier/sideband model.
- Compared with earlier r03 Ramsey attempts, this higher-shot refreshed-center long-span run reduces the case for simply accumulating more blind Ramsey data under the same protocol.

## Claims that are not yet supported

- No numeric `T2star` should be quoted from this dataset.
- No nearby `13C` coupling conclusion is supported from this Ramsey/FFT evidence.
- The `1.5 MHz` feature should not be treated as a clean programmed-detuning carrier because it is much stronger/coherent in the reference channel than in the raw signal channel.
- The `0.807 MHz` raw/fitted-reference-normalized feature should not be promoted as a physical coupling or detuning without a protocol/control explanation and repeatable phase behavior.
- The refreshed pODMR center remains a frequency calibration only; it does not by itself establish T2star or 13C behavior.

## Recommended next action

Avoid another blind `auto__ramsey` repeat on r03 under the same measurement style. The next project action should be a bridge-free protocol decision: either close the current Ramsey branch as unsupported/negative for claim-grade T2star/13C under these conditions, or design a targeted alternate measurement that directly suppresses/tests reference-channel artifacts before trying to extract T2star. A practical alternate path is a reviewed phase-cycled or otherwise reference-robust Ramsey/echo-style control, with explicit readout-role verification and an acceptance rule that the target oscillation must appear in the raw signal channel, not only after point-wise normalization.
