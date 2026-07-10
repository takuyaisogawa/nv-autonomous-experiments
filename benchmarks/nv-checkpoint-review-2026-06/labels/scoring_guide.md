# Scoring Guide

Score each run using the final response and the captured project note.  The
preferred note is root-level `ramsey_review.md`; notes captured from
`work/notes/` or from the final handoff are used when that root-level file is
not available.

## Broader Residual-Offset Score

The broader score passes if the response or project note notices the
residual-offset interpretation:

> the observed Ramsey carrier/frequency may equal the nominal/programmed
> detuning plus an additional residual offset.

The response can express this without the exact words `residual offset`, but it
must make the same model clear: the nominal Ramsey detuning is not the whole
effective detuning seen by the data.

Examples of passing ideas:

- The apparent Ramsey frequency is the programmed detuning plus a residual
  detuning/offset.
- A `det = 1.0 MHz` Ramsey component near `1.19 MHz` may be a physical carrier
  with about `+0.19 MHz` residual detuning.
- The microwave/resonance center may be offset, so the Ramsey carrier should be
  interpreted as `nominal detuning +/- center error`.

## Stricter Calibration-Residual Score

The stricter score passes only if the response also connects the residual
offset to resonance frequency or microwave frequency calibration. It is not
enough to say only that a frequency basis may be wrong. The answer must tie the
idea to the calibrated resonance center, pODMR/weak-pi center, microwave center,
or an equivalent calibration basis.

## Failure Cases

Neither the response nor the project note includes the above idea.

Examples of failing responses:

- Only says the T2star or 13C claim is unsupported.
- Only says the data are noisy or model-dependent.
- Only proposes collecting more Ramsey or ODMR data.
- Only says to run or interpret a det-shift check, without saying the observed
  Ramsey frequency may be nominal detuning plus residual offset.
- Only says a peak tracks programmed detuning, without identifying the residual
  offset on top of the nominal detuning.
- Only says to refresh pODMR or use a refreshed center, without connecting that
  to residual offset in the Ramsey detuning.

## Manual Audit

The automatic scorer is conservative and keyword based. Manually audit any
response marked `ambiguous` or any response where the automatic score conflicts
with expert judgment.
