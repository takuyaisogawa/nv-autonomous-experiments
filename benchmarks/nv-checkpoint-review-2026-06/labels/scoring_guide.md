# Scoring Guide

Score each run using the final response and the captured project note. The
preferred note is the root-level `ramsey_review.md`. Notes captured from
`work/notes/` or from the final handoff are used when that root-level file is
not available.

## Calibration Residual Score

The score passes only if the response or project note suspects that the nominal
Ramsey detuning may include a residual offset from resonance frequency or
microwave frequency calibration. The answer must connect the offset to the
calibrated resonance center, a pODMR or weak-pi center, the microwave center,
the `mw_freq` choice, or an equivalent calibrated frequency basis error.

The response can express this without the exact words `calibration residual`,
but the calibration connection must be clear.

Examples of passing ideas:

- The apparent Ramsey frequency may be the programmed detuning plus an offset
  caused by an error in the resonance center.
- A `det = 1.0 MHz` Ramsey component near `1.19 MHz` may reflect about
  `+0.19 MHz` of residual detuning from microwave frequency calibration.
- The pODMR or weak-pi center may be offset, so the Ramsey carrier should be
  interpreted relative to that calibration error.

## Failure Cases

A response fails if it does not connect the Ramsey frequency offset to a
calibration source.

Examples of failing responses:

- Only says the T2star or 13C claim is unsupported.
- Only says the data are noisy or model dependent.
- Only proposes collecting more Ramsey or ODMR data.
- Only says to run or interpret a detuning shift check.
- Only says a peak tracks programmed detuning.
- Proposes a residual or effective detuning without connecting it to resonance
  frequency or microwave frequency calibration.
- Only says to refresh pODMR or use a refreshed center without connecting that
  action to a residual calibration error in the Ramsey detuning.

## Manual Audit

The automatic scorer is a conservative first-pass helper. Manually audit any
response marked `ambiguous` or any response where the automatic score conflicts
with expert judgment.
