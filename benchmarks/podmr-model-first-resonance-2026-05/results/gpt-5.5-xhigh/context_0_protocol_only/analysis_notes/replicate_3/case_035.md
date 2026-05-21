Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML has full_expt = 0, so the optional 1-level reference branch is inactive. The executed readouts are therefore:

1. Readout 1: detection immediately after optical polarization, annotated in the sequence as the true 0 level reference.
2. Readout 2: detection after rabi_pulse_mod_wait_time with the scanned microwave frequency, so this is the MW-probed pODMR signal readout.

The active pulse parameters are mod_depth = 1 and length_rabi_pulse = 52 ns. With a 250 MHz sample rate, the pulse length is already on a 4 ns sample grid and remains 52 ns after rounding.

Decision: resonance absent.

Reasoning: for this readout ordering, a pODMR resonance should appear as a localized reduction of the post-MW signal readout relative to the 0-reference, or as a repeatable localized feature in the normalized signal/reference contrast. The raw traces and the two per-average overlays show drift and crossing between the readouts, but not a stable, isolated dip at a specific frequency. The largest normalized deviations occur at scattered points and are not reproducible between the two averages, so the scan does not provide convincing evidence of a pODMR resonance.
