# Ramsey review: r03 first T2star/13C scout

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/advice.md`, `project/state.md`; searched `md/` and `evidence/` for Ramsey/T2star/13C context.
- New Ramsey measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` status/runtime, `measurement/m005.json` run control.
- Generated local artifacts: `analyze_ramsey.py`, `ramsey_analysis_results.json`, `ramsey_diagnostic.png`.

## Calculations/scripts run

- Reconstructed tau grid from the raw export: `0..6 us`, 31 points, `dt = 0.2 us`; programmed `mw_freq = 3.876 GHz`, `det = 1.5 MHz`, `4 x 50000` shots, snake scan order.
- Checked run health: completed without abort, safe shutdown ok, final counts `38.249 kcps` vs fresh pre-run `43.535 kcps` (`-12.1%`). Status runtime estimate was `492.946 s` per average, above the earlier `450 s` drift-planning cap.
- Readout/normalization checks:
  - line0 mean/span `45.318 / 3.904 kcps`; line1 mean/span `42.098 / 7.750 kcps`.
  - ratio `line0/line1` mean/span `1.0776 / 0.1586`; contrast span `0.0731`.
  - line0-line1 tau correlation only `0.138`, so common-mode cancellation is limited.
- FFT checks used Hann-windowed rFFT; actual bin spacing from the sampled array is `161.29 kHz`, Nyquist `2.419 MHz`.
  - Normalized ratio top bins: `0.968 MHz`, `0.323 MHz`, `0.161 MHz`, `0.806 MHz`, then `1.935 MHz`.
  - Nearest programmed carrier bin (`1.452 MHz`) is weaker: ratio FFT amplitude `0.105` vs top `0.200`.
  - Expected 13C sideband scale (`det +/- ~0.385 MHz`) is not symmetric/convincing: ratio amplitudes near `1.129 MHz` and `1.935 MHz` are `0.099` and `0.176`.
  - Per-average ratio FFT peaks disagree: avg1 `0.968 MHz`, avg2 `1.452 MHz`, avg3 `0.323 MHz`, avg4 `0.161 MHz`.
- Fits:
  - Free damped-cosine fits on ratio/contrast/difference prefer about `0.905..0.910 MHz`, `T2 ~2.1 us`, but only `R2 ~0.38..0.40`.
  - Raw line fits are inconsistent: line0 best near `1.77 MHz` (`R2 0.31`), line1 near `0.964 MHz` (`R2 0.48`).
  - Fixed sine/cosine regression on the normalized ratio explains little at the intended carrier and sidebands: `R2 = 0.017` at `1.5 MHz`, `0.037` at `1.115 MHz`, `0.056` at `1.885 MHz`; the off-target `0.968 MHz` component gives `R2 = 0.265`.

## Plausible interpretation

The Ramsey scout is completed and analyzable, but it is not claim-grade. There are hints of oscillatory structure, strongest in normalized/readout-difference traces near `0.9..1.0 MHz`, with a descriptive decay time around `2 us`. That component is off the programmed `1.5 MHz` detuning and does not reproduce cleanly across stored averages. The per-average runtime exceeded the drift-planning cap and the final count rate dropped by about `12%`, so drift or resonance/center shift during the run is a plausible contributor.

The data therefore support only a provisional statement: r03 remains a reasonable aligned candidate from prior strong/weak pODMR evidence, but this first Ramsey scout did not cleanly measure T2star or reveal a robust 13C sideband pattern.

## Claims not yet supported

- A well-supported T2star value for r03.
- A well-supported nearby 13C coupling conclusion, positive or negative.
- That the `~0.91 MHz` fitted component is the intended Ramsey detuning, a 13C sideband, or a physical coupling rather than drift/resonance-offset/readout artifact.
- That the pODMR resonance center remained at the pre-run `3.876 GHz` value throughout the Ramsey run.

## Recommended next action

Do not record a T2star or 13C conclusion from this scout. Before spending on a longer Ramsey, do a bounded r03 state check: fresh TrackCenter/count check plus a quick weak-pi pODMR center confirmation. If r03 is still bright and centered, repeat Ramsey with an updated microwave center/detuning and a per-average runtime back under the drift cap; otherwise handle the tracking/resonance drift first.
