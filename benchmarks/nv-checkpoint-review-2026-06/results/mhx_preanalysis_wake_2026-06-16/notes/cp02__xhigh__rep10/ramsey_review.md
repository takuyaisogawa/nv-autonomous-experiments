# Ramsey Review: r03 det=1.0 MHz follow-up

## Files/data used

- Project context: `project/brief.md`, `project/advice.md`, `project/state.md`, `context.json`, plus relevant prior notes in `evidence/e006.md`, `evidence/e007.json`, and `evidence/e013.md`.
- New measurement: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job contract, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, `measurement/m005.json` control state.
- Generated scratch artifacts: `analyze_ramsey.py`, `ramsey_analysis_summary.json`, `ramsey_analysis.png`.

## Calculations/scripts run

- Ran `python analyze_ramsey.py`.
- Parsed `measurement/m001.json` as `ramsey.xml`, readout1 reference and readout2 Ramsey signal, with `tau = 0..8 us` in 41 points, `dt = 0.2 us`, snake order, `8 x 50000` shots, `mw_freq = 3.8759 GHz`, `det = 1.0 MHz`.
- Checked raw signal, signal/reference, and signal/reference-line-normalized channels.
- Ran linear-detrended FFT and least-squares sinusoid checks at:
  - programmed carrier: `1.000 MHz`
  - expected 13C sidebands: `0.615423 MHz` and `1.384577 MHz`
  - prior scout component: `0.884 MHz`
- Ran a scratch acquisition-order common-mode drift proxy. This is not the official MATLAB drift diagnostic.

Key quantitative results:

| Check | All points raw signal | Excluding tau=0 raw signal |
| --- | ---: | ---: |
| 1.000 MHz carrier | `0.277 +/- 0.287 kcps`, z=`0.96`, R2=`0.115` | `0.152 +/- 0.240 kcps`, z=`0.63`, R2=`0.044` |
| 0.615 MHz lower 13C sideband | `0.475 +/- 0.287 kcps`, z=`1.66`, R2=`0.156` | `0.522 +/- 0.225 kcps`, z=`2.32`, R2=`0.159` |
| 1.385 MHz upper 13C sideband | `0.263 +/- 0.287 kcps`, z=`0.92`, R2=`0.113` | `0.098 +/- 0.239 kcps`, z=`0.41`, R2=`0.038` |
| 0.884 MHz prior component | `0.286 +/- 0.286 kcps`, z=`1.00`, R2=`0.117` | `0.055 +/- 0.239 kcps`, z=`0.23`, R2=`0.035` |

Other checks:

- Terminal run completed with final counts `44.184 kcps`, no abort, and saved artifact `1DExp-seq-ramsey-vary-tau-2026-05-13-204940`.
- Mean raw reference was `49.31 kcps`; mean raw signal was `44.58 kcps`.
- The tau=0 signal point was `39.31 kcps`, `12.3%` below the median of later tau points, while the reference tau=0 point was only `0.7%` below its later-point median.
- Mean pointwise SEM from stored averages was large: `1.90 kcps` for signal and `1.95 kcps` for reference.
- Average-to-average signal means ranged from `36.20` to `50.27 kcps`; the scratch within-average common-mode drift proxy flagged no average for a `>15%` drop.
- Exploratory frequency scans did not peak cleanly at the designed carrier. Raw/refline channels favored about `0.47 MHz`; signal/reference favored about `1.18 MHz`. These are not the planned `1.0 MHz` carrier or a matched 13C sideband pair.

## Plausible interpretation

- The measurement is analyzable and has no terminal hardware abort, but it does not show a claim-grade Ramsey carrier at the programmed `1.0 MHz`.
- The prior scout's `~0.884 MHz` component is not reproduced in this det-shifted run, especially after excluding the anomalous tau=0 point. That weakens the case that the prior component was a stable physical Ramsey frequency.
- The lower expected 13C sideband has a small exploratory amplitude, but it is only about `2.3 sigma` in the tau=0-excluded raw fit, has low R2, lacks the matching upper sideband, and sits below pointwise average scatter. Treat it as a hint/noise candidate, not 13C evidence.
- The non-target exploratory components around `0.47 MHz` and `1.18 MHz` are more visible than the target carrier, but they disagree across normalization methods and are not enough to fit a defensible T2* decay.
- Large average-to-average brightness changes and the anomalously low tau=0 signal point are likely contaminating the spectral screens.

## Claims not yet supported

- No well-supported T2* value is supported by this Ramsey run.
- No well-supported nearby 13C conclusion is supported by this Ramsey run.
- Do not claim the `0.47 MHz`, `1.18 MHz`, `0.884 MHz`, or lower-sideband-like `0.615 MHz` components as physical without follow-up.
- Do not infer a refined resonance shift from this Ramsey data alone.

## Recommended next action

Do not repeat another long `0..8 us`, `8 x 50000` Ramsey as-is. First verify that r03 still has the expected resonance and that the Ramsey route produces a stable phase-ramp carrier:

1. Run a quick current-center check around the fine pODMR center (`3.8759 GHz`) or equivalent low-cost resonance sanity check.
2. If the center remains usable, run a short dense Ramsey/phase-ramp sanity scan before any longer T2*/13C measurement, for example `det = 1.0 MHz`, `tau = 0..2 us`, `dt <= 0.1 us`, with enough averages to confirm a raw 1 MHz carrier and per-average phase consistency.
3. If that short check still lacks the programmed carrier, pause T2*/13C acquisition on r03 and troubleshoot Ramsey phase/frequency calibration or sequence behavior before spending more shots.
