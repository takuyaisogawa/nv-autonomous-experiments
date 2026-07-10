# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`, plus local guidance in `md/memory.md` and `md/knowledge.md`.
- New Ramsey measurement:
  - `measurement/m001.json`: savedexperiment raw export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
  - `measurement/m002.json`: submitted job contract for `nv23_ramsey_20260514_055148_auto_ramsey`.
  - `measurement/m003.json`, `measurement/m004.json`, `measurement/m005.json`: terminal result/status/control records.
- Generated local analysis artifacts:
  - `analyze_ramsey.py`
  - `ramsey_analysis_summary.json`
  - `ramsey_trace_check.png`
  - `ramsey_frequency_screen.png`

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Parsed the raw export as 41 tau points from 48 ns to 8.048 us, 20 averages x 50000 repetitions, `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`, final counts `43.433 kcps`.
- Verified `ExperimentDataEachAvg` axis contract by averaging `[avg, readout, point]` back to `ExperimentData`; max absolute mismatch was `1.4e-14 kcps`.
- Used the local default Ramsey readout convention because the neutral snapshot includes the manifest/metadata but not the Ramsey XML: readout 1 treated as reference, readout 2 as signal.
- Checked terminal health: completed, no stop requested, monitor error empty, no aborted safety state.
- Used snake-order/per-average drift proxy from stored averages: mean total readout varied by `28.1%` peak-to-peak across averages, but robust outlier score max was `1.85 sigma`; no average exceeded the `|z| > 3.5` flag threshold.
- Computed raw signal, point-wise `signal/reference`, and fitted-reference-line normalization. For each view, ran least-squares sinusoid screens from 0.2 to 2.45 MHz, explicit target fits at carrier `1.5 MHz`, expected 13C sidebands `1.1152/1.8848 MHz`, and prior control `1.192 MHz`, plus FFT checks.

## Plausible interpretation

- The run is analyzable and terminally healthy, but the Ramsey signal is still not claim-grade.
- Raw signal median was `44.804 kcps`; median per-point signal SEM was `0.850 kcps`.
- Full-span raw-signal LS screen peaked near `2.271 MHz` with amplitude `0.818 kcps` and `R2 = 0.378`. The programmed `1.5 MHz` carrier fit was weaker, `0.705 kcps` with residual std `0.906 kcps` and `R2 = 0.307`.
- Skipping the first four tau points did not produce a clean carrier model: raw signal still peaked near `2.271 MHz` with amplitude `0.555 kcps`; the `1.5 MHz` carrier was close but lower at `0.512 kcps`.
- Ratio/fitted-reference views also favored about `2.27 MHz` by LS, while FFT bins put substantial power around both the carrier region (`1.46/1.59 MHz`) and `2.2-2.3 MHz`. This is spectral ambiguity, not a clean Ramsey carrier.
- Per-average screens were mixed: top frequencies ranged from `0.356` to `2.341 MHz`; only `5/20` averages had top frequency within `0.125 MHz` of the `1.5 MHz` carrier, `0/20` near the lower 13C sideband, and `2/20` near the upper sideband.
- The lower 13C sideband target was weak in the combined ratio fit (`0.0030` fractional amplitude), and the upper sideband was not consistent enough to separate from other spectral structure.
- Best interpretation: this high-shot refreshed-center Ramsey continues the previous pattern of weak, normalization-sensitive or model-inconsistent spectral content. It does not support a fitted T2star or a nearby-13C conclusion.

## Claims not yet supported

- No numeric T2star is supported from this Ramsey branch.
- No nearby 13C coupling or sideband assignment is supported.
- The `~2.27 MHz` LS feature is not supported as a physical Ramsey frequency; it is off the programmed carrier/13C targets and not per-average consistent.
- A physical absence of nearby 13C is not proven; the supported statement is narrower: this Ramsey data set does not provide claim-grade 13C evidence under the current conditions.
- A clean programmed-carrier Ramsey model is not established, even though carrier-region FFT power exists.

## Recommended next action

Avoid another blind same-style Ramsey repeat on r03. The refreshed-center, higher-shot long-span run still did not produce a robust carrier/sideband model. The next decision should be explicit:

1. Record the r03 Ramsey/T2star/13C branch as unsupported under current Ramsey conditions, or
2. Switch to a different diagnostic protocol rather than adding Ramsey averages. If continuing experimentally, start with an alternate coherence/readout check such as a Hahn-echo baseline via the locally recommended `auto__cpmg` / `CPMG.xml` with `N = 1`, then only pursue 13C spectroscopy if that establishes a cleaner coherent signal path.
