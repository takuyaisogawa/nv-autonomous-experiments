# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json`.
- Prior/local evidence: especially `evidence/e007.json` and `evidence/e013.md` for the second-Ramsey model/advisory and expected checks, plus `evidence/e010.json`/`e011.json` for the in-progress job state at snapshot time.
- New measurement data:
  - `measurement/m001.json`: raw savedexperiment export for `1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
  - `measurement/m002.json`: submitted job spec.
  - `measurement/m003.json`: terminal bridge result; completed, final counts `44.184 kcps`.
  - `measurement/m004.json`: terminal run status; completed, elapsed `5256 s`.
  - `measurement/m005.json`: run control; no stop requested.
- Generated local analysis artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, and `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Extracted the 41-point tau grid: `0..8 us`, `dt = 0.2 us`, nominal FFT resolution `0.125 MHz`, Nyquist `2.5 MHz`.
- Verified measurement settings from raw export: `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `8 averages x 50000 repetitions`, two readouts.
- Treated readout 1 as reference and readout 2 as signal, consistent with the project context for this route.
- Calculated raw signal, point-wise signal/reference, and signal divided by a fitted linear reference line.
- Ran windowed, linearly detrended FFTs for raw signal and normalized traces.
- Ran fixed-frequency least-squares checks at:
  - prior scout component: `0.884 MHz`
  - expected 13C lower sideband: `0.615 MHz`
  - programmed Ramsey carrier: `1.000 MHz`
  - expected 13C upper sideband: `1.385 MHz`
- Checked per-average amplitude/phase consistency at the carrier and prior component.
- Ran a diagnostic decaying-cosine grid fit on the reference-line-normalized trace; this was used only as a robustness check, not as a claimed T2star extraction.

## Quantitative observations

- The run completed cleanly and produced analyzable data. Terminal final counts were `44.184 kcps`; raw-export warnings were empty.
- Combined raw signal mean was `44.58 kcps`; reference mean was `49.31 kcps`; mean signal/reference was `0.904`.
- Raw signal peak-to-peak variation across tau was `7.72 kcps`; reference peak-to-peak was `4.29 kcps`; reference-line-normalized signal peak-to-peak was `0.154`.
- The dominant FFT content is not centered exactly at the programmed `1.0 MHz` bin:
  - raw signal top bins: `1.220 MHz`, `1.098 MHz`, `0.488 MHz`, `0.122 MHz`, `0.610 MHz`, `1.341 MHz`.
  - reference-line-normalized top bins: `1.220 MHz`, `1.098 MHz`, `0.488 MHz`, `0.122 MHz`, `0.610 MHz`, `1.341 MHz`.
- Fixed-frequency least-squares on the reference-line-normalized trace:
  - `1.000 MHz`: amplitude `0.00564`, variance reduction vs linear baseline `2.4%`.
  - `0.884 MHz`: amplitude `0.00586`, variance reduction `2.7%`.
  - `0.615 MHz`: amplitude `0.00974`, variance reduction `6.9%`.
  - `1.385 MHz`: amplitude `0.00541`, variance reduction `2.3%`.
- A scan around the apparent carrier region gives stronger descriptive support near `1.1..1.2 MHz` than at exactly `1.0 MHz`; for example, reference-line-normalized least-squares at `1.19 MHz` gives amplitude `0.01736` and variance reduction `23.2%`.
- Per-average behavior is only moderately coherent. At `1.19 MHz`, the reference-line-normalized per-average phase resultant is about `0.64`; at the exact `1.0 MHz` carrier it is about `0.45`. Several averages disagree in phase.
- Per-average signal mean varies from `36.20` to `50.27 kcps` (`31.6%` range relative to mean), so drift/tracking/readout baseline changes remain material provenance even though the run was terminal and complete.
- Diagnostic decay fitting is not robust. Including tau = 0 drives a decaying-cosine grid fit to the lower T2star bound; excluding tau = 0 moves the best fit to several microseconds, and per-average best fits scatter widely. This is not a stable T2star estimate.

## Plausible interpretation

- The new Ramsey run likely contains a real Ramsey-like oscillatory component, strongest around `1.1..1.2 MHz` in the combined traces.
- The component is plausibly related to the intended Ramsey phase ramp, but the strongest frequency being above `1.0 MHz` suggests residual microwave detuning, resonance-frequency drift, or a frequency-calibration offset relative to the fine pODMR grid center. It is not a simple exact-carrier confirmation.
- The prior scout's non-claim-grade `~0.884 MHz` component did not reappear as the dominant component after changing `det` to `1.0 MHz`; this weakens the case that the prior `0.884 MHz` peak was a stable physical carrier.
- The expected 13C sideband model for a `1.0 MHz` carrier predicted features near `0.615/1.385 MHz`. The lower-sideband region has some power, but the upper sideband is weak and there is no convincing symmetric sideband pair. This is insufficient for a 13C conclusion.
- The data are useful evidence that r03 can produce Ramsey contrast, but baseline/average scatter and unstable decay fits keep it below a well-supported T2star claim.

## Claims that are not yet supported

- No well-supported numerical T2star should be claimed from this run.
- No well-supported nearby-13C conclusion should be claimed.
- Do not claim that the Ramsey carrier is exactly the programmed `1.0 MHz`; the combined data favor a descriptive component closer to `1.1..1.2 MHz`.
- Do not claim the `0.615 MHz` feature as a 13C sideband without a matching upper sideband or a repeat/sequence diagnostic.
- Do not interpret the diagnostic decay fit as physical; it is sensitive to tau = 0 handling and per-average selection.

## Recommended next action

Before another long Ramsey repeat, run a targeted frequency/sequence diagnostic rather than blindly accumulating more averages. The most useful next step is a short weak-pi pODMR refresh or compact Ramsey detuning sweep around the apparent offset to determine whether the observed `~1.19 MHz` component is residual detuning from an updated resonance center. Then repeat Ramsey only after choosing a carrier/detuning condition that produces a phase-consistent oscillation; use that repeat for T2star fitting and 13C sideband testing.
