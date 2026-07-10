# Ramsey Review

## Files/data used

- Project context: `project/state.md`, `project/brief.md`, `project/advice.md`, `context.json`, plus local analysis rules in `md/memory.md` and `md/knowledge.md`.
- Prior local evidence: `evidence/e001.json` for the pODMR refresh that selected `mw_freq = 3.8765 GHz`, and `evidence/e014.json` for the planned Ramsey targets.
- New measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control state.
- Generated locally: `analyze_ramsey.py`, `ramsey_analysis.json`, `ramsey_analysis.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey.py`.
- Verified terminal health: job completed, safe shutdown true, no abort/stop/monitor error, final counts `43.433 kcps`.
- Verified scan contract: `tau = 48 ns..8.048 us`, `41` points, `200 ns` step, `20 x 50000` shots (`1.0e6` shots/tau), snake order, raw arrays `(1,2,41)` and per-average arrays `(1,20,2,41)` with per-average means reproducing combined data.
- Reviewed raw signal, point-wise `signal/reference`, and fitted-reference-line normalization.
- Computed per-point SEM across stored averages: raw signal median SEM `0.850 kcps`; point-wise ratio median SEM `0.0116`; ref-line normalized median SEM `0.00937`.
- Ran robust per-average drift check on mean reference, signal, and ratio: no flagged averages.
- Ran full-span and skip-first-4 least-squares frequency screens, FFT checks, fixed target amplitudes, bootstrap over stored averages, shuffled-residual checks, and descriptive damped-cosine fits.

## Plausible interpretation

- The run is healthy and analyzable, but not claim-grade for the planned Ramsey carrier/sideband model.
- There is structured oscillatory content. Full-span LS screens in all three views peak near `2.270-2.271 MHz`; raw/ref-line FFT also peaks near `2.278 MHz`. The programmed carrier region is present as a local feature near `1.515 MHz`, but it is not dominant in the main raw/ref-line screens.
- The fixed `1.5 MHz` carrier amplitude is small relative to the project expectation: raw LS amplitude `0.705 kcps`, below the raw median SEM `0.850 kcps`; ref-line normalized carrier amplitude `0.01447`, about `1.54x` the normalized median SEM. Bootstrap top-frequency support is split: ref-line bootstraps select the observed `~2.27 MHz` region `76.8%` of the time and the carrier region `23.2%` of the time.
- A conservative shuffled-residual check says the structured content is unlikely to be pure shuffled noise (`p ~0.004` for the ref-line carrier amplitude and `p ~0.008` for the ref-line max-amplitude screen), but this does not identify the physical carrier.
- Descriptive damped fits are sensitive to the early tau points: full-span free fits lock near `2.27-2.28 MHz` with `T2* ~2.1 us` (`p=1`) or `~3.3 us` (`p=2`), while skip-first-4 fits lock near `1.53 MHz` with `T2* ~3.0 us` (`p=1`) or `~3.9 us` (`p=2`). That sensitivity keeps the T2star value descriptive only.
- The expected `13C` sideband targets are weak: ref-line LS amplitudes are `0.00298` at `1.115 MHz` and `0.00536` at `1.885 MHz`; neither sideband is a stable bootstrap top feature. No supported nearby-13C conclusion follows from this run.

## Claims not yet supported

- A numeric, well-supported `T2star` for r03.
- A nearby `13C` coupling/sideband claim, or a no-13C physical exclusion stronger than "not supported by these Ramsey data."
- Assignment of the `~2.27 MHz` component as the true Ramsey carrier rather than a transient, detuning error, alias-proximate feature, or sequence/readout artifact.
- Sub-grid precision for the pODMR refresh center beyond the local `3.8765 GHz` calibration basis.

## Recommended next action

- Do not run another blind long Ramsey repeat on r03 under the same conditions. Treat this refreshed-center, high-shot Ramsey as another non-claim-grade Ramsey result.
- Next project action should be a synthesis/decision point: either close the r03 Ramsey/T2star/13C branch as unsupported under the current Ramsey protocol, or switch to a deliberately different diagnostic/protocol. If continuing experimentally, first resolve whether the `~2.27 MHz` component is a detuned carrier or an artifact with a targeted protocol/control, then use an alternate coherence/spectroscopy path for 13C rather than fitting this Ramsey trace into a claim.
