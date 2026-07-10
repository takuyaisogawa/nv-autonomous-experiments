# Ramsey Review

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, and `context.json`.
- New terminal Ramsey data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` terminal status, and `measurement/m005.json` control state.
- Prior comparison/context: `evidence/e003.json` terminal review of the previous 8 us det=1.0 MHz Ramsey and `evidence/e017.md` short-tau diagnostic design/start note.
- Scratch outputs created here: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, and `ramsey_shorttau_diagnostic.png`.

## Calculations or scripts run

- Ran `python analyze_ramsey.py`.
- Confirmed run completed safely: `nv23_ramsey_20260513_230331_auto_ramsey`, savedexperiment `1DExp-seq-ramsey-vary-tau-2026-05-13-230350`, `tau=48 ns..1.968 us`, 41 points, `mw_freq=3.8759 GHz`, `det=1.0 MHz`, `12 x 90000` repetitions, final counts `35.122 kcps`, no stop request.
- Parsed the saved sequence text: `full_experiment=0`, readout 1 is the true `mS=0` reference and readout 2 is the Ramsey signal.
- Computed raw signal/reference statistics, point-wise ratio, signal/reference-line normalization, FFT screens, least-squares sinusoid fits at `0.615 MHz`, `1.0 MHz`, and `1.385 MHz`, exploratory frequency screens, a snake-order per-average drift screen, and a descriptive fixed-1 MHz decaying-cosine grid fit.
- Key quantitative results:
  - Raw reference mean `48.573 kcps`, span `2.176 kcps`; raw signal mean `44.655 kcps`, span `6.499 kcps`; signal peak-to-peak is `14.6%` of signal mean.
  - Median per-point signal SEM across averages is `1.138 kcps`; median ratio SEM is `0.0127`.
  - Programmed `1.0 MHz` LS amplitude is `1.30 kcps` raw / `0.0274` ratio, with residual RMS `1.15 kcps` / `0.0256`.
  - Expected sideband LS amplitudes are comparable: `0.615 MHz` gives `1.11 kcps` / `0.0243`; `1.385 MHz` gives `1.21 kcps` / `0.0271`.
  - Exploratory LS screen is dominated by the low-frequency lower bound: `0.200 MHz` gives `5.90 kcps` raw / `0.118` ratio, larger than the programmed carrier.
  - FFT bin spacing is coarse for 13C interpretation at `0.508 MHz`; top raw FFT bins are `1.524 MHz`, `1.016 MHz`, and `0.508 MHz`, all with amplitudes around `0.94..1.23 kcps`.
  - Local drift screen flagged averages `2`, `10`, and `11` for average-wide signal offsets. Excluding them does not rescue the carrier: the `1.0 MHz` amplitude remains `1.29 kcps` raw / `0.0278` ratio and the screen still peaks at `0.200 MHz`.
  - A forced fixed-1 MHz decaying-cosine grid fit prefers `T2star ~0.19 us`, but this is descriptive only because it is driven by early-time curvature and not by a clean carrier.

## Plausible interpretation

The short-tau/high-SNR Ramsey run improved early-time visibility relative to the previous 8 us run: the `1.0 MHz` component rose from the prior `0.277 kcps` raw / `0.00916` ratio to about `1.30 kcps` / `0.0274`. However, the trace is still not a clean programmed-detuning Ramsey oscillation. The largest structure is broad and low-frequency/baseline-like, the target carrier and expected 13C sidebands have similar amplitudes, and several stored averages show count-offset drift. This is compatible with a very short apparent dephasing/transient problem or a protocol/readout artifact, but it is not enough to extract a defensible T2star.

## Claims not yet supported

- No well-supported numeric T2star claim from this Ramsey data.
- No supported nearby 13C claim; the short span has coarse frequency resolution and does not separate carrier/sideband structure.
- No claim that the forced `~0.19 us` fixed-carrier decay fit is physical.
- No claim that r03 is invalid as an aligned NV; prior pODMR evidence still supports r03 alignment.
- No claim that Ramsey signal is strictly absent; there is weak target-frequency content, but it is not dominant or clean enough to promote.

## Recommended next action

Do not run another blind Ramsey repeat on r03. Treat the current Ramsey/T2star/13C result as unsupported under the existing Ramsey evidence. If the project should continue on r03, make the next measurement a targeted control rather than accumulation: use a detuning-control Ramsey such as same short window with `det=0` and/or sign-reversed detuning, or switch to an alternate coherence/13C protocol. The decision criterion should be whether the broad short-tau structure follows the programmed detuning; if it does not, close the r03 Ramsey/T2star branch as unsupported and move to an alternate protocol or candidate.
