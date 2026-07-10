# Ramsey Review

## Files/data used

- `project/brief.md`, `project/advice.md`, and `project/state.md` for objective and prior project state.
- `evidence/e017.md` for the short-tau Ramsey design/start note.
- `measurement/m001.json` terminal raw export for `1DExp-seq-ramsey-vary-tau-2026-05-13-230350.mat`.
- `measurement/m002.json` job spec, `measurement/m003.json` terminal bridge result, `measurement/m004.json` status, `measurement/m005.json` control.

Measurement identity: accepted r03, `auto__ramsey` / `ramsey.xml`, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`, `tau = 0.048..1.968 us` in 41 points, `12 x 90000` repetitions. The bridge result completed without abort; final text count was `35.122 kcps`.

## Calculations or scripts run

- Created and ran `analyze_ramsey.py`.
- Outputs: `ramsey_analysis_summary.json` and `ramsey_shorttau_review.png`.
- Checks included raw signal/reference readouts, point-wise ratio, signal divided by a fitted linear reference baseline, per-average common-mode counts, target least-squares amplitudes at `0.615`, `1.000`, and `1.385 MHz`, exploratory harmonic screens, and free exponentially decaying cosine fits.

Key quantitative results:

- Combined raw signal mean `48.573 kcps`; reference mean `44.655 kcps`.
- Median exported point errors: signal `1.455 kcps`, reference `1.397 kcps`.
- Raw signal target LS amplitudes: `0.052 kcps` at `1.000 MHz` (`SNR 0.26`), `0.289 kcps` at `0.615 MHz` (`SNR 1.19`), `0.237 kcps` at `1.385 MHz` (`SNR 1.43`).
- Point-wise ratio target LS amplitudes look large, including `0.0343` fractional at `1.000 MHz` (`SNR 11.7`), but this is not corroborated by the raw signal channel.
- Reference readout itself carries large target-frequency structure: `1.470 kcps` at `1.000 MHz` (`SNR 13.9`), so the point-wise ratio feature is reference-denominator sensitive.
- Signal/reference-line normalization removes that apparent carrier: `0.00105` fractional at `1.000 MHz` (`SNR 0.25`), with sideband checks also below claim grade (`SNR 1.22` at `0.615 MHz`, `1.45` at `1.385 MHz`).
- Per-average common-mode counts span `39.745..53.200 kcps` (`28.7%` relative span), with late averages 10-11 low. Treat this as drift/provenance concern rather than positive Ramsey evidence.
- Free raw-signal exponential-cosine fit is unconstrained: it hits the `20 us` upper T2star bound with `376 us` standard error. The ratio-only fit gives `T2star ~2.96 us`, but it is not physically supported because the raw signal and reference-line-normalized views do not support the carrier.

## Plausible interpretation

This short-tau/high-SNR diagnostic did not reveal a reliable early-time Ramsey carrier in the raw signal readout. The strongest apparent carrier evidence is in point-wise signal/reference ratio, but the same target-frequency structure is much stronger in the reference channel and disappears under fitted-reference-line normalization. That makes the ratio feature most plausibly a readout/reference artifact or drift-normalization artifact, not supported Ramsey contrast from r03.

Together with the previous two non-claim-grade Ramsey datasets described in `project/state.md`, this terminal result argues that r03 still lacks a supported T2star measurement under the current Ramsey protocol. It also provides no supported nearby 13C sideband conclusion.

## Claims that are not yet supported

- A numerical T2star for r03.
- A resolved Ramsey carrier at the programmed `1.0 MHz` detuning.
- Nearby 13C coupling or sidebands at `det +/- f13C` (`0.615` and `1.385 MHz` in this project model).
- That the aligned r03 pODMR resonance is wrong; the pODMR evidence remains separate and still supports r03 as the accepted aligned candidate.
- That more shots in the same short-tau Ramsey design would resolve the issue. The limiting problem is readout/channel consistency, not only shot noise.

## Recommended next action

Do not run another blind Ramsey repeat on r03. Close the current Ramsey evidence as non-claim-grade, then choose one deliberate branch: either run an alternate protocol that does not rely on the same reference-sensitive Ramsey readout (for example a phase-readout/echo-family or otherwise independently validated coherence check), or close r03 with "aligned NV found, but T2star/13C unsupported under current Ramsey conditions" and move to a new candidate only if the project requires a claim-grade T2star/13C conclusion.
