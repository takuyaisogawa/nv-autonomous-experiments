# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `context.json`.
- Measurement data: `measurement/m001.json` raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-14-055200.mat`.
- Measurement metadata: `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` run control.
- Prior context from state: accepted r03 NV, refreshed weak-pi pODMR center `mw_freq = 3.8765 GHz`, Ramsey plan `det = 1.5 MHz`, expected 13C sidebands near `1.115` and `1.885 MHz`.

## Calculations or scripts run

- Used local Python/NumPy/SciPy/matplotlib to inspect the JSON arrays, validate axes, compute SEM, fitted-reference-line normalization, least-squares sinusoid frequency screens, per-average frequency screens, and descriptive damped-sinusoid fits.
- Created `analysis/ramsey_review_metrics.json` with the quantitative review output.
- Created `analysis/ramsey_review_plot.png` with raw readouts, normalized traces, per-average traces, and the frequency-amplitude screen.
- Axis check passed: `ExperimentDataEachAvg` shape `[1,20,2,41]`, averaged over the average axis, reproduces `ExperimentData` shape `[1,2,41]`.
- Acquisition check: `tau = 48 ns..8.048 us`, 41 points, `dt = 200 ns`, span `8.0 us`, Nyquist `2.5 MHz`, nominal resolution `125 kHz`, `20 x 50000 = 1.0e6` shots per tau point.
- Terminal health check: job completed, elapsed `12990 s`, no stop request, `safety.aborted = false`, `safe_shutdown_ok = true`.

## Plausible interpretation

- The refreshed-center Ramsey is analyzable and did not show a hard run anomaly in the available terminal metadata.
- The strongest full-span fitted-reference-line-normalized least-squares component is near `2.272 MHz`, not the programmed `1.5 MHz` carrier or the expected 13C sidebands.
- The same off-model `~2.27 MHz` component appears in raw signal, point-wise ratio, and fitted-reference-line ratio screens. Full-span amplitudes:
  - raw signal top: `2.272 MHz`, amplitude `0.818 kcps`, `R2 ~ 0.326`
  - fitted-reference-line ratio top: `2.272 MHz`, amplitude `0.01677`, `R2 ~ 0.326`
  - point-wise ratio top: `2.270 MHz`, amplitude `0.01845`, `R2 ~ 0.338`
- Target amplitudes in fitted-reference-line ratio are not compelling relative to noise and off-target structure:
  - carrier `1.5 MHz`: amplitude `0.01445`, median ratio SEM `0.00937`
  - lower sideband `1.115 MHz`: amplitude `0.00298`
  - upper sideband `1.885 MHz`: amplitude `0.00536`
  - prior short-tau control `1.192 MHz`: amplitude `0.00226`
  - det-shift predicted `1.692 MHz`: amplitude `0.00430`
- Skip-first-4 checks keep the top near `2.272 MHz`; carrier amplitude drops to `0.01043`, and sidebands remain weak.
- Per-average top frequencies are mixed (`~0.2..2.4 MHz`, including isolated near-target values but no common carrier/sideband pattern). Stored averages are not fully independent repeats, but this still weakens a claim-grade carrier or sideband interpretation.
- A descriptive damped-sinusoid fit can fit the off-model component (`~2.282 MHz`, `T2star ~1.8 us`, `R2 ~0.64` in both raw and fitted-reference-line ratio views), but this should not be promoted because the expected carrier/sideband signal model is not supported first.

## Claims not yet supported

- No supported numeric T2star claim from this Ramsey run.
- No supported nearby 13C claim from this Ramsey run.
- No supported claim that the programmed `1.5 MHz` Ramsey carrier is cleanly observed.
- No supported claim that the `~2.27 MHz` feature is physical; it is an empirical/off-model component that needs a targeted diagnostic before interpretation.
- No sub-grid or refined resonance-frequency claim beyond the prior pODMR refresh basis.

## Recommended next action

Avoid another blind long Ramsey repeat on r03. The next action should be a targeted diagnostic of the off-model Ramsey response before making a final T2star/13C conclusion: re-check the Ramsey protocol/readout/phase convention and run a deliberate detuning-shift test or phase-control Ramsey designed to see whether the `~2.27 MHz` component tracks the programmed detuning. If it does not track, treat r03 Ramsey/T2star/13C as unsupported under current conditions and consider an alternate protocol such as Hahn/CPMG-based coherence/spectroscopy rather than more Ramsey accumulation.
