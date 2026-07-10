# Ramsey Review: refreshed-center r03 long-span run

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- Prior planning/model context: `evidence/e014.json`.
- New measurement data: `measurement/m001.json` raw savedexperiment export; `measurement/m002.json` job contract; `measurement/m003.json` terminal result; `measurement/m004.json` run status; `measurement/m005.json` run control.
- Scratch artifacts created here: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis_plot.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey.py`.
- Verified the raw export axis contract: `ExperimentDataEachAvg` shape `[20,2,41]` averages back to `ExperimentData` with max mismatch about `1e-14`, so readout/average axes are usable.
- Verified readout roles from embedded `ramsey.xml`: readout 1 is the true `mS=0` reference; `full_experiment=0` skips the optional `mS=1` reference; readout 2 is the Ramsey signal.
- Confirmed terminal run health: completed, final counts `43.433 kcps`, safe shutdown ok, no abort, no stop request, no monitor error.
- Measurement grid: `mw_freq=3.8765 GHz`, `det=1.5 MHz`, `tau=0.048..8.048 us`, `41` points, `0.2 us` step, `8.0 us` span, `20 x 50000 = 1.0e6` shots per tau point. Nyquist is `2.5 MHz`; nominal frequency resolution is `125 kHz`.
- Noise/quality checks: median raw-signal SEM `0.850 kcps`, point-wise ratio SEM `0.0116`, reference-line-normalized SEM `0.0174`. Stored-average raw means vary strongly common-mode (`signal 37.38..50.37 kcps`, `reference 41.74..54.90 kcps`) but reference/signal average means are correlated (`r=0.970`); ratio-average means are tighter (`0.891..0.959`).
- Manual scan-order drift check using `ScanOrderEachAvg` / snake order found no average flagged by the endpoint-residual rule; max endpoint ratio drift was `0.052`, comparable to median residual RMS `0.0477`. Forward/reverse average mean ratio offset was small (`-0.0017`).
- Least-squares/FFT screens were run on raw signal, signal/reference, and signal/reference-line views, both full span and skipping the first 4 tau points.
  - Strongest empirical component is near `2.27 MHz` in all views. Skip-first-4 amplitudes: raw `0.555 kcps`, ratio `0.01418`, ref-line norm `0.01139`; skip FFT peak is near `2.297 MHz`.
  - Programmed `1.5 MHz` carrier is present but weaker/not dominant. Skip-first-4 amplitudes: raw `0.512 kcps`, ratio `0.01231`, ref-line norm `0.01049`.
  - Expected 13C sidebands from the plan (`1.115/1.885 MHz`) are weak: skip-first-4 ratio amplitudes `0.00067/0.00527`, ref-line norm `0.00025/0.00255`.
  - The old `1.192 MHz` control is weak in normalized views: skip-first-4 ratio `0.00191`, ref-line norm `0.00321`.
- Per-average vector checks show the empirical `2.271 MHz` component is more coherent than most target sidebands: ratio combined amplitude `0.01442`, mean individual amplitude `0.01836`, coherence ratio `0.786`; ref-line norm combined amplitude `0.01139`, coherence ratio `0.813`. The carrier is also coherent but weaker (`ratio 0.01265`, coherence `0.628`; ref-line norm `0.01049`, coherence `0.748`).
- Descriptive damped fits on skip-first-4 ref-line-normalized data are non-unique: exponential fits initialized near carrier and near the empirical peak give similar residuals (`rms ~0.0113..0.0114`) but different frequencies (`1.533 MHz` vs `2.250 MHz`) and broad T2-like values (`2.6..2.8 us` with large uncertainty). Gaussian fits are similarly ambiguous.

## Plausible interpretation

The run is valid and analyzable. It shows a small, internally coherent oscillatory feature, strongest around `2.27 MHz`, and a weaker carrier-like component near `1.5 MHz`. The feature survives skip-transient and appears in raw, point-wise ratio, reference-line-normalized, and FFT screens, so it is worth treating as a real diagnostic feature rather than pure numerical noise.

However, the dominant frequency is not the programmed carrier and not the expected `13C` sideband pair. Given the common-mode brightness variation, first-point transient, weak target sidebands, and non-unique damped fits, the data do not support assigning the `2.27 MHz` feature to a physical T2* carrier or nearby `13C` coupling. It may reflect residual detuning, an apparatus/sequence phase artifact, transient structure, or an unmodeled response.

## Claims that are not yet supported

- No well-supported numeric `T2star` value from this dataset.
- No well-supported nearby `13C` conclusion from this dataset.
- Do not claim the `2.27 MHz` feature is a `13C` sideband, a true Ramsey carrier, or evidence for a coupling model.
- Do not claim the weak-pi pODMR center is wrong by the full apparent offset without a targeted detuning/frequency diagnostic.
- Do not use the damped-fit T2-like values as physical results; they are descriptive and model-ambiguous.

## Recommended next action

Do not run another blind 8 us Ramsey repeat. Run a targeted frequency/phase diagnostic: first refresh or confirm the current weak-pi pODMR center if needed, then run short high-SNR Ramsey det-shift or mw-frequency-offset checks designed to test whether the `~2.27 MHz` component tracks the programmed detuning/carrier. If it tracks, redesign a claim-grade Ramsey around that calibrated behavior; if it stays fixed or remains model-ambiguous, move to an alternate protocol or record an unsupported/negative r03 T2*/13C conclusion under current Ramsey conditions.
