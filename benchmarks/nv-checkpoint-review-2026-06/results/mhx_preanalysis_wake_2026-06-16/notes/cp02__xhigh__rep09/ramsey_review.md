# Ramsey Review

## Files/data used

- Project context: `context.json`, `project/brief.md`, `project/state.md`, `project/advice.md`, `md/memory.md`, `md/knowledge.md`.
- Prior planning context: `evidence/e007.json` for the second Ramsey model/advisory, `evidence/e010.json` for the submitted job spec, and `evidence/e013.md` for the fine-pODMR-to-Ramsey handoff.
- New Ramsey terminal package: `measurement/m001.json` raw savedexperiment export, `measurement/m002.json` job spec copy, `measurement/m003.json` terminal result, `measurement/m004.json` terminal status, and `measurement/m005.json` control.
- Generated local analysis artifacts: `ramsey_analysis.py`, `ramsey_analysis_summary.json`, and `ramsey_analysis.png`.

## Calculations/scripts run

- Ran `python ramsey_analysis.py`.
- The script loaded the two-readout Ramsey data (`readout1 = reference`, `readout2 = Ramsey signal` per `evidence/e007.json`), built `tau = 0..8 us` in 41 points, and checked raw signal, pointwise signal/reference, and signal normalized by a fitted reference line.
- It computed per-average drift/common-mode metrics, per-point SEM from the 8 stored averages, FFT peaks after linear detrending, least-squares sinusoid screens with a linear baseline, subset/endpoint stability checks, and exploratory damped-cosine fits.

## Quantitative checks

- Run completed normally: `measurement/m003.json` reports status `completed`, final counts `44.184 kcps`, `8` averages x `50000` repetitions, `ramsey.xml`, `tau` step `0.2 us`, scan order `snake`.
- Combined raw signal readout2 spans `39.31..47.03 kcps` (`7.72 kcps` peak-to-peak). Pointwise signal/reference spans `0.8025..0.9721`.
- Stored averages show strong common-mode count drift: average-mean reference/signal deviations from median reach about `-18%` and `+12%`; averages `4`, `7`, and `8` exceed a 10% common-mode flag. Ratio means are much more stable, within about `+2.6%/-1.3%`. Reference and signal average means correlate at `0.995`.
- Per-tau SEM from stored averages is large compared with the candidate components: median raw-signal SEM is `1.92 kcps`, and median ratio SEM is `0.0187`.
- Fixed-frequency screens are weak:
  - At programmed `1.000 MHz`, raw-signal LS amplitude is `0.277 kcps` (`R2 = 0.024`, amplitude/SE `0.68`); ratio amplitude is `0.0092` (`R2 = 0.050`, amplitude/SE `0.98`).
  - Expected 13C sidebands near `0.615` and `1.385 MHz` are not resolved as a symmetric pair; ratio amplitudes are `0.0111` and `0.0084` with amplitude/SE `1.20` and `0.90`.
  - The prior scout component near `0.884 MHz` is not reproduced strongly; ratio amplitude is `0.0074` with amplitude/SE `0.79`.
- Exploratory frequency screens find non-target components:
  - Raw signal and fitted-reference-normalized signal prefer about `0.466 MHz` with amplitude about `0.92 kcps`, `R2 ~ 0.26`, amplitude/SE about `2.55`.
  - Pointwise ratio prefers about `1.178 MHz` with amplitude `0.0225`, `R2 = 0.305`, amplitude/SE `2.83`. Dropping `tau=0` keeps the ratio component near `1.188 MHz`; dropping the first two points gives `1.174 MHz`; removing common-mode flagged averages gives `1.172 MHz`.
  - Subset stability is mixed: first 4 averages prefer a lower ratio component near `0.442 MHz`, while last 4 averages prefer about `1.198 MHz`.
- Exploratory damped-cosine fits are not claim-grade. The ratio fit gives frequency `1.187 MHz` and `T2* ~ 2.27 us`; raw/reference-line-normalized fits give frequency near `0.461 MHz` and `T2* ~ 1.64 us`. These are useful scale estimates only, because the preferred component depends on normalization and average subset.

## Plausible interpretation

- The run is analyzable and contains oscillatory structure. The most plausible Ramsey-like feature is a weak normalized component around `1.17..1.20 MHz`, close enough to the programmed `1.0 MHz` detuning to be worth targeted follow-up, but not close or stable enough to call a clean programmed carrier.
- The previous scout's non-claim-grade `~0.884 MHz` component is not supported by this det-shifted run.
- The low-frequency raw feature around `0.46 MHz` is not enough for a 13C interpretation: it does not appear as a supported `det +/- f13C` sideband pair, and the ratio view points elsewhere.
- The large common-mode drift means ratio-normalized evidence is more informative than raw amplitude, but the ratio candidate amplitude is only comparable to the stored-average SEM scale.

## Claims not yet supported

- No well-supported `T2*` value is established. The `~1.6..2.3 us` damped-fit scale is exploratory only.
- No well-supported nearby `13C` conclusion is established. The expected sidebands near `0.615` and `1.385 MHz` are not resolved.
- The Ramsey carrier is not confirmed at exactly the programmed `1.0 MHz`; the best normalized component is offset to about `1.18 MHz`.
- The measurement does not prove absence of 13C coupling, because the carrier itself is not yet claim-grade and drift/systematics remain significant.

## Recommended next action

Do not launch another long higher-SNR Ramsey repeat yet. First run a compact frequency/phase diagnostic: re-check the weak-pi pODMR center around `3.8759 GHz`, then, if the center is stable, run a shorter det-shift Ramsey diagnostic to test whether the normalized `~1.18 MHz` component follows the programmed detuning. Only plan a claim-grade T2* acquisition after that carrier behavior is verified; otherwise treat the present features as artifact/noise candidates and move to an alternate sequence or branch-close/no-13C decision.
