# Ramsey Review: r03 det=1.5 MHz short-tau shift check

## Files/data used

- `project/brief.md`, `project/advice.md`, `project/state.md`, and `md/memory.md` for the project objective, current r03 status, prior Ramsey conclusions, and the intended det-shift test.
- `measurement/m001.json`: raw savedexperiment export for `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
- `measurement/m002.json`: submitted job spec for `nv23_ramsey_20260514_015423_auto_ramsey`.
- `measurement/m003.json` and `measurement/m004.json`: terminal run/status records. The run completed at `2026-05-14T04:15:00`, final counts were `44.796 kcps`, with `12` averages and `90000` repetitions.
- `evidence/e008.json`: prior terminal det=1.0 MHz short-tau review used as the comparison point for the `~1.192 MHz` empirical component.
- `evidence/e019.json`, `evidence/e021.json`, `evidence/e028.json`: det-shift model/intent/spec context.

## Calculations or scripts run

- Added and ran `analysis/ramsey_det1p5_analysis.py`.
- Outputs:
  - `analysis/ramsey_det1p5_review.json`
  - `analysis/ramsey_det1p5_review.png`
- The script used the validated tau grid from the job/state (`48 ns..1.968 us`, `41` points, `48 ns` step), extracted the two readouts from `m001`, and interpreted them from `ramsey.xml` as readout 0 = 0-level reference and readout 1 = Ramsey signal because `full_experiment=0`.
- Checks performed:
  - Raw signal and reference review.
  - Per-point SEM across stored averages.
  - Linear reference-fit normalization, plus point-wise ratio SEM as a secondary noise check.
  - Least-squares sinusoid screens with intercept and linear baseline over `0.2..4.0 MHz`.
  - FFT check on detrended fitted-reference-normalized ratio.
  - Target-frequency checks at `1.500 MHz`, det-tracking hypothesis `1.692 MHz`, prior control `1.192 MHz`, and expected 13C sidebands `1.307/2.076 MHz`.

Key quantitative results from `analysis/ramsey_det1p5_review.json`:

- Mean reference/signal: `48.08/44.27 kcps`.
- Median SEM: raw signal `0.711 kcps`, point-wise ratio `0.0126`.
- Raw signal peak-to-peak across tau: `6.46 kcps`; fitted-reference-normalized ratio peak-to-peak: `0.133`.
- Reference linear slope: `0.423 kcps/us`, so slow baseline variation is present but not by itself a Ramsey model.
- Global LS screen is dominated by the low-frequency boundary (`0.2 MHz`), indicating a strong slow transient/baseline term.
- Target amplitudes in fitted-reference-normalized ratio:
  - `1.500 MHz`: `0.0235`
  - `1.692 MHz`: `0.0255`
  - `1.192 MHz` prior control: `0.00993`
  - `1.307 MHz` 13C lower sideband: `0.00563`
  - `2.076 MHz` 13C upper sideband: `0.00531`
- Local maximum near the det-tracking target is `1.626 MHz` with ratio amplitude `0.0261`; raw-signal local maximum in that band is also near `1.626 MHz` with amplitude `1.25 kcps`.
- FFT best in the ratio-line view is `0.707 MHz`, not a clean carrier/sideband confirmation.
- Per-average frequency screens are not coherent; in this simple broad screen all averages peak at the low-frequency boundary, consistent with slow transient/baseline dominance.

## Plausible interpretation

The det=1.5 MHz run is terminal and analyzable, with healthy final counts and no export warnings. It weakens the specific hypothesis that the prior `~1.192 MHz` feature was a fixed feature that would remain dominant: the amplitude at `1.192 MHz` is now much smaller than the amplitude near the `1.5..1.7 MHz` band. However, it does not cleanly validate the physical Ramsey-carrier hypothesis either. The strongest broad LS component remains a low-frequency transient/baseline term, and the local feature is offset from the exact programmed carrier (`1.500 MHz`) and det-tracking prediction (`1.692 MHz`) toward `~1.626 MHz`.

Taken together with the prior det=1.0 MHz short-tau run, this is suggestive but still not claim-grade. A real det-dependent Ramsey component may be present under a strong early-time/baseline transient, but the data do not yet support extracting a reliable T2star or assigning 13C sidebands.

## Claims that are not yet supported

- Do not claim a numeric T2star from this run.
- Do not claim resolved nearby 13C coupling or sidebands.
- Do not claim the prior `~1.192 MHz` component has been fully explained.
- Do not claim the carrier is exactly at the programmed `1.500 MHz` or exactly at the prior-feature det-tracking prediction `1.692 MHz`.
- Do not infer a change in the accepted r03 alignment conclusion from this Ramsey run; the aligned-candidate conclusion still rests on the prior pODMR evidence.

## Recommended next action

Do not run another blind Ramsey repeat. Perform a bridge-free synthesis across all four r03 Ramsey datasets using the same raw/readout-aware pipeline and explicit target table. If continuing experimentally, switch to a protocol or analysis design that suppresses/separates the short-tau transient before fitting T2star: for example, a phase-cycled/quadrature Ramsey variant if available in the validated local protocol set, or a deliberately nonzero-start tau grid with matched det-shift controls. If no suitable validated alternate protocol is available, close the r03 Ramsey/13C branch as unsupported under current conditions while retaining r03 as the aligned NV candidate.
