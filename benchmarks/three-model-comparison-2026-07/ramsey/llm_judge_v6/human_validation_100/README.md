# Human validation of the Ramsey judge

One author (Takuya Isogawa) graded 100 responses sampled without replacement
from the 1,184 responses not used in prompt development. Judge outputs,
previous labels, model identities and reasoning settings were concealed.
The original English was available alongside Japanese machine translations;
AI explanations were also used as reading aids. The author finalized the
labels before the judge's outputs were revealed.

The original labels give **96/100 agreement (96%)**, Wilson 95% CI
**90.2–98.4%**, and **Cohen's kappa 0.9008428359**.

| Human label | Judge PASS | Judge FAIL |
| --- | ---: | ---: |
| PASS | 26 | 3 |
| FAIL | 1 | 70 |

`human_original.json` is the byte-for-byte finalized export. `comparison.json`
contains the original labels and reasons. `selection.json` records the seed,
excluded development cases and sample mapping. `protocol.json` is the plan
saved before labeling; `method.json` records the completed review procedure.
`reading_aids.jsonl` preserves the English segments and Japanese translations.
The conversational explanations were reading assistance, not an additional
independent set of reference labels.

The four disagreements below remain unchanged. English human reasons are
translations; the Japanese reasons are preserved exactly in the JSON files.

## H001: human FAIL, judge PASS

Human reason: The residual detuning is not linked to a calibration error.

Original Japanese: 残留離調キャリブレーションのエラーに結び付けてない。

Judge reason: The note connects the unexpected Ramsey frequency to a possible shifted resonance basis and explicitly proposes checking an inferred center offset with weak-pi pODMR. This establishes the required calibration connection, rather than merely recommending fresh measurements.

From `project_note`:

> A plausible physical interpretation is that the resonance/phase basis shifted by roughly several hundred kHz during the run, or that the Ramsey phase-ramp behavior plus residual detuning did not produce the expected carrier.

From `project_note`:

> TrackCenter/count check plus a fine weak-pi pODMR around the current `3.876 GHz` basis, wide enough to catch an inferred `~0.5 MHz` center shift.

## H032: human PASS, judge FAIL

Human reason: The response considers an additional residual mismatch between the microwave and resonance frequencies.

Original Japanese: マイクロ波周波数と共鳴周波数の残留ずれが加わっている可能性を考えている。

Judge reason: The note recognizes residual detuning but never connects it to an error in resonance-center or microwave-frequency calibration. Merely reporting mw_freq and residual drive/transition detuning does not meet the required calibration connection.

From `project_note`:

> The most economical physical reading is an effective Ramsey carrier near `1.19–1.20 MHz`, plausibly the programmed phase detuning plus residual drive/transition detuning.

From `project_note`:

> The exact origin/sign of the approximately `0.19 MHz` offset from programmed det, and whether one frequency adequately describes all residual structure, remain unresolved.

## H034: human PASS, judge FAIL

Human reason: Detuning from resonance is mentioned as a possible explanation.

Original Japanese: 共鳴からの離調を可能性として挙げている。

Judge reason: The note mentions resonance detuning and recommends recentering, but does not clearly identify a residual error in the calibrated resonance or microwave center as contributing to nominal Ramsey detuning. The guide explicitly excludes recentering recommendations without that connection.

From `project_note`:

> No supported claim that the actual Ramsey oscillation frequency is `0.94 MHz`; this may reflect drift/noise/reference artifacts or resonance detuning, and the stored averages do not lock to one frequency.

From `project_note`:

> First re-check/recenter r03 with a narrow weak-pi pODMR around the current `3.876 GHz` resonance, because the Ramsey carrier was inconsistent with the programmed detuning and the final counts dropped by `12.1%`.

## H066: human PASS, judge FAIL

Human reason: Residual frequency error is mentioned.

Original Japanese: 残留する周波数誤差に言及してる。

Judge reason: The note suspects a residual frequency error but does not clearly attribute it to an error in the calibrated resonance center or microwave frequency basis. Questioning resonance validation and recommending frequency diagnostics do not establish the required calibration connection.

From `project_note`:

> That mismatch could reflect residual frequency error, low SNR, short-window fitting ambiguity, or drift/brightness changes that are not large enough to hard-flag the run.

From `project_note`:

> Do not claim the Ramsey carrier behavior validates exact resonance at `3.876 GHz`; the measured oscillation frequency is not centered on the programmed `det=1.5 MHz` expectation.
