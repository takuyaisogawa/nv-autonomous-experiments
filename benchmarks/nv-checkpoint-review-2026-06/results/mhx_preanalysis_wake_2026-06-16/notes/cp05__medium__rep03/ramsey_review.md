# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New Ramsey data/metadata: `measurement/m001.json` raw savedexperiment export; `measurement/m002.json` job spec; `measurement/m003.json` terminal result; `measurement/m004.json` status; `measurement/m005.json` control.
- Planning/run evidence checked: `evidence/e022.json`, `evidence/e023.json`, `evidence/e024.json`.
- Local outputs created: `analyze_ramsey.py`, `ramsey_analysis.json`, `ramsey_analysis.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Verified raw array contract: `ExperimentData` shape `(1, 2, 41)`, `ExperimentDataEachAvg` shape `(1, 20, 2, 41)`, and averaging the per-average array reproduces the combined data.
- Confirmed scan/acquisition: `tau = 48 ns..8.048 us`, 41 points, `dt = 200 ns`, span `8.0 us`, nominal FFT resolution `125 kHz`, Nyquist `2.5 MHz`, `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`, `20 x 50000 = 1.0e6` shots per tau.
- Checked terminal health: completed, no stop request, empty monitor error, safe shutdown true, final counts `43.433 kcps`.
- Computed raw signal, point-wise ratio, fitted-reference-line normalization, SEM across 20 averages, FFT screens, least-squares sinusoid screens, target amplitudes at `1.5 MHz` carrier and expected 13C sidebands `1.115/1.885 MHz`, per-average frequency screens, and skip-first-4-points screens.

## Plausible interpretation

- The measurement is terminal and analyzable, but it still does not support a clean Ramsey carrier/sideband model.
- Median signal SEM is `0.850 kcps`; median fitted-reference-line ratio SEM is `0.0174`.
- Full-span LS screen is strongest near `2.271 MHz`, not at the programmed `1.5 MHz` carrier or expected `1.115/1.885 MHz` 13C sidebands. The strongest component is only `0.818 kcps` raw / `0.0168` refline-normalized ratio.
- The `1.5 MHz` carrier target is present only weakly: `0.705 kcps` raw and `0.0145` refline-normalized ratio full-span; after skipping the first 4 tau points it falls to `0.512 kcps` raw and `0.0105` refline-normalized ratio.
- The expected 13C sidebands are not a coherent pair. Full-span refline-normalized amplitudes are `0.0030` at `1.115 MHz` and `0.0054` at `1.885 MHz`; after skipping the first 4 points they are `0.00024` and `0.00255`.
- Per-average top frequencies are broadly mixed rather than clustered at the carrier or sidebands, so the empirical `~2.27 MHz` feature is not enough to promote a physical T2star or 13C interpretation.
- A descriptive damped-sine grid fit prefers about `2.2825 MHz` and `T2star ~1.77 us`, but this is fit-only/provenance because signal presence at a physically planned carrier/sideband model is not established.

## Claims not yet supported

- No well-supported numeric T2star claim from this Ramsey dataset.
- No supported nearby 13C claim from FFT/sideband evidence.
- No supported assignment of the `~2.27 MHz` component to the NV Ramsey carrier, a 13C sideband, or a stable physical coupling.
- No sub-grid or high-precision microwave-center claim beyond the prior pODMR refresh basis.

## Recommended next action

Do not run another blind long-span Ramsey repeat on r03 under the same model. Treat the r03 Ramsey branch as non-claim-grade for T2star/13C under current Ramsey conditions, then choose an alternate protocol path: a fresh frequency/track check followed by Hahn/CPMG `N=1` for a robust coherence baseline, and only use dynamical-decoupling/phase-sensitive spectroscopy if the project still needs a 13C-specific conclusion.
