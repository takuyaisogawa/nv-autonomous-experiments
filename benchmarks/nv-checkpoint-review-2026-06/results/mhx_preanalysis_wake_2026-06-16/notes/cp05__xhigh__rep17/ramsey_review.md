# Ramsey review

## Files/data used

- Project context: `project/state.md`, `project/brief.md`, `project/advice.md`, `context.json`.
- Ramsey measurement: `measurement/m001.json` raw savedexperiment export; `measurement/m003.json` terminal result; `measurement/m004.json` status/control. `measurement/m002.json` and `measurement/m005.json` were inspected for job/control consistency.
- Planning targets: `evidence/e014.json`, with programmed carrier `1.5 MHz` and expected 13C sidebands `1.115193 MHz` and `1.884807 MHz`.
- Scratch artifacts created here: `ramsey_review_analysis.py`, `ramsey_review_summary.json`, `ramsey_review_plot.png`.

## Calculations or scripts run

- Ran `python ramsey_review_analysis.py`.
- Confirmed run health: job `nv23_ramsey_20260514_055148_auto_ramsey` / run `1DExp-seq-ramsey-vary-tau-2026-05-14-055200` completed, not incomplete, no stop request, no monitor error, final counts `43.433 kcps`.
- Confirmed scan contract: `mw_freq=3.8765 GHz`, `det=1.5 MHz`, tau `0.048..8.048 us` in `41` points with `0.2 us` spacing, `20 x 50000` shots, snake scan order, data saved in tau order. Mean-of-averages axis check matched combined data to numerical precision.
- Used embedded sequence text to treat trace 0 as pre-Ramsey reference and trace 1 as Ramsey signal (`full_experiment=0`).
- Computed raw signal, signal/reference, and signal/fitted-reference-line views; per-point SEM from 20 stored averages; LS sinusoid screens from `0.1..2.4 MHz`; FFT top-bin checks; target amplitudes at carrier, expected 13C sidebands, and prior control frequencies; repeated checks after skipping the first four tau points.

## Plausible interpretation

- The data are usable, but still non-claim-grade for the project objective.
- Full-span combined LS screens peak near `2.27 MHz`, not at the programmed carrier or expected 13C sidebands:
  - raw signal top `2.272 MHz`, amplitude `0.822 kcps`, `R2=0.304`;
  - signal/reference top `2.270 MHz`, amplitude `0.01851`, `R2=0.321`;
  - signal/reference-line top `2.272 MHz`, amplitude `0.01685`, `R2=0.308`.
- Skipping the first four tau points does not recover the expected model: the normalized top remains near `2.266 MHz`.
- The programmed `1.5 MHz` carrier is present only weakly. In signal/reference it is `0.01544` full-span (`1.33x` median point SEM, `R2=0.230`) and `0.01197` after skipping four points (`1.03x` median point SEM, `R2=0.216`). In raw signal it is below one median point SEM.
- The expected 13C sidebands are weaker and not coherent: full-span signal/reference amplitudes are `0.00235` at `1.115 MHz` (`0.20x` SEM) and `0.00960` at `1.885 MHz` (`0.83x` SEM); after skipping four points they drop to `0.00067` and `0.00502`.
- Per-average top frequencies are mixed across low-frequency, carrier-like, and high-frequency regions rather than clustering at `1.5 MHz` or at the sidebands. This argues against fitting a physical T2star/13C model from this run.

## Claims not yet supported

- No numeric T2star should be reported from this measurement.
- No nearby 13C coupling claim is supported by this measurement.
- The `2.27 MHz` component should not be promoted as an NV Ramsey carrier or 13C sideband without a new control; it is off the planned model and close enough to the high-frequency end of the sampled band to treat as empirical/provenance only.
- A strong physical absence claim for all nearby 13C is also not supported; the supported statement is that repeated r03 Ramsey measurements under the current conditions have not produced a claim-grade carrier/sideband model.

## Recommended next action

Record this refreshed-center long-span Ramsey as terminal, analyzable, and non-claim-grade. Do not run another same-protocol blind Ramsey repeat. The next project action should be either an alternate control/protocol that first establishes a clean Ramsey carrier under changed conditions, or a formal unsupported/negative r03 Ramsey/13C conclusion under the current measurement conditions.
