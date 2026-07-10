# Ramsey review: refreshed-center r03 det=1.5 MHz long-span run

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`.
- New terminal Ramsey data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control.
- Relevant local evidence context: `evidence/e014.json` measurement model/plan and prior summaries in `project/state.md`.
- Generated during this review: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey.py`.
- Verified raw-data axis contract: `ExperimentDataEachAvg` shape `[20,2,41]` averages over axis 0 to reproduce combined `ExperimentData` shape `[2,41]`.
- Used embedded `ramsey.xml` readout basis: readout 1 is true `m_S=0` reference; with `full_experiment=0`, readout 2 is the Ramsey signal after the Ramsey pulses.
- Checked terminal health: job completed, final counts `43.433 kcps`, `stop_requested=false`, monitor `last_error=""`, `safe_shutdown_ok=true`.
- Computed scan constants: `tau=0.048..8.048 us`, `41` points, `0.2 us` step, `8.0 us` span, Nyquist `2.5 MHz`, nominal resolution `125 kHz`, `20 x 50000 = 1.0e6` shots per tau.
- Screened raw signal, point-wise `signal/reference`, and `signal/fitted-reference-line` views with fixed-frequency least-squares fits using offset + linear trend + sinusoid. Also ran skip-first-4-tau screens and FFT sanity checks.
- Target frequencies checked: programmed carrier `1.500 MHz`, expected 13C sidebands `1.115` and `1.885 MHz`, prior controls `1.192`, `1.623`, and `0.746 MHz`.
- Noise/drift checks: median stored-average SEM was `0.850 kcps` for raw signal, `0.0116` for point-wise ratio, and `0.0174` for fitted-reference-line ratio. Local common-mode drift proxy had no monotonic count collapse (`46.464 -> 46.447 kcps`) but large per-average scatter, relative range `0.280`.

## Plausible interpretation

- The data are usable and contain a weak carrier-compatible component. At `1.500 MHz`, fitted-reference-line normalized amplitude is `0.01447` full-span and `0.01049` after skipping the first 4 tau points; raw-signal amplitude is `0.705 kcps` full-span and `0.512 kcps` after the skip.
- This weak carrier-like response is plausibly Ramsey phase response from the refreshed center, and the old `1.192 MHz` control remains weak (`0.00226` fitted-reference-line ratio full-span).
- The result is still not claim-grade. The strongest full-span and skip-first-4 screens are around `2.27 MHz` in raw and fitted-reference-line views; FFT sanity checks also place a leading peak near `2.32 MHz`. That component is not the planned `1.5 MHz` carrier or the expected `1.115/1.885 MHz` sideband pair.
- The expected 13C sideband pair is not supported: fitted-reference-line amplitudes are low sideband `0.00298` full-span and `0.00025` after skip, high sideband `0.00536` full-span and `0.00255` after skip.
- Per-average top-frequency screens are mixed, so stored averages do not supply a clean repeatability argument for a carrier/sideband model.

## Claims not yet supported

- No numeric T2star value is supported from this run.
- No nearby 13C claim is supported.
- No clean programmed-carrier plus symmetric sideband model is supported.
- The physical origin of the `~2.27 MHz` component is not established.
- The refreshed pODMR center remains grid-supported calibration only; it does not by itself support a Ramsey/T2star/13C claim.

## Recommended next action

Stop blind Ramsey repeats on this r03 branch. Record a supported unsupported/negative Ramsey/T2star/13C conclusion under the current Ramsey conditions, then continue only with a different protocol or a targeted diagnostic for the unexpected `~2.27 MHz` component.
