# Ramsey Review: refreshed-center r03 long-span run

## Files/data used

- Project context: `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`, `context.json`.
- New measurement data: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` terminal status, `measurement/m005.json` control state.
- Generated local analysis artifacts: `ramsey_analysis.py`, `ramsey_analysis.json`, `ramsey_review.png`.

## Calculations or scripts run

- Ran `python ramsey_analysis.py`.
- Verified raw-data axis contract: `ExperimentDataEachAvg` is `[scan, avg, readout, point]`; averaging the 20 stored averages reproduces `ExperimentData` to numerical precision.
- Confirmed terminal run health: completed, no stop requested, no monitor error, safe shutdown ok, final counts `43.433 kcps`.
- Scan parameters from metadata/raw export: `tau = 0.048..8.048 us`, `41` points, `0.2 us` step, `20 x 50000` shots, `1.0e6` shots/tau, `mw_freq = 3.8765 GHz`, `det = 1.5 MHz`.
- Working model check: from `mw_freq = 3.8765 GHz`, the project ms=+1 approximation gives `B ~359.46 G`, `13C Larmor ~384.8 kHz`, so Ramsey targets are carrier `1.5 MHz` and sidebands `1.115/1.885 MHz`.
- Reviewed raw signal, point-wise signal/reference ratio, and signal/reference-line normalization. Ran least-squares sinusoid screens from `0.1..2.4 MHz`, FFT checks, full-span and skip-early-point views, target-amplitude checks, per-average frequency screens, SEM estimates, and stored-average common-mode drift summaries.

## Plausible interpretation

- The dataset is terminal and analyzable, but it still does not show a claim-grade Ramsey carrier/sideband pattern.
- There is a strong early-time transient: first signal point is `-4.25 kcps` below the post-first-4-point median, while the second point is `+2.02 kcps` above it.
- The strongest exploratory LS component is near `2.27 MHz` in raw, ratio, and reference-line-normalized views, including after skipping early points. This is not the programmed `1.5 MHz` carrier and not the expected `1.115/1.885 MHz` 13C sideband pair.
- The planned carrier is weak: full-span `1.5 MHz` amplitude is `0.705 kcps` raw and `0.0157` in ratio; after skipping the first 4 points it is `0.512 kcps` raw and `0.0123` in ratio. Median per-point SEM is `0.850 kcps` raw and `0.0116` in ratio.
- The lower 13C sideband is near absent in ratio (`0.0028` full span, `0.00067` skip 4). The upper sideband has some full-span ratio amplitude (`0.0096`) but weakens under skip-early checks (`0.0053`) and is not paired with the lower sideband.
- Per-average ratio frequency screens remain mixed; skip-4 top frequencies include low-boundary hits, carrier-adjacent values, sideband-adjacent values, and high-frequency values rather than one coherent component.
- Stored-average mean reference/signal levels vary by about `27%/29%` common-mode range, while mean ratio varies by about `7.5%`; the simple robust common-mode flag check did not isolate a single bad average. This is cautionary provenance, not a hard terminal anomaly.

## Claims that are not yet supported

- No supported numeric `T2*` can be claimed from this run.
- No supported nearby `13C` coupling/sideband conclusion can be claimed from this run.
- The `~2.27 MHz` feature should not be promoted as a physical Ramsey frequency; it is exploratory and could reflect transient/baseline/readout or route-related structure.
- The data do not support a strong absence claim for nearby `13C`; the Ramsey carrier itself is not clean enough to make the sideband absence decisive.
- More shots under the same Ramsey conditions are not justified by this evidence; the limiting issue is signal structure/consistency, not just shot noise.

## Recommended next action

Do not run another blind 8-us Ramsey repeat on r03 under the same conditions. Treat the r03 Ramsey branch as still non-claim-grade under the current `auto__ramsey` conditions, then change method before spending more acquisition time: first do a route/protocol diagnostic or alternate coherence protocol that can verify det-tracking and suppress the early-time transient. If the project must continue on r03, the next experiment should be a deliberately changed diagnostic, not higher averaging of the same scan.
