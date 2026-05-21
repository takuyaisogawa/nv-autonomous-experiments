Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825e9 to 3.925e9 with 5 MHz steps.

The XML instructions first polarize and detect a true 0-level reference, then wait. Because full_expt is 0, the optional 1-level reference block is inactive. The active signal operation is a rabi_pulse_mod_wait_time followed by detection. Therefore readout 1 is the polarized reference/background readout, and readout 2 is the post-microwave-pulse pODMR signal readout.

Key pulse settings from the sequence are mod_depth = 1 and length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate. That corresponds to a 52 ns microwave/Rabi pulse. The microwave frequency is the scanned variable.

The combined post-pulse readout shows a pronounced, localized reduction around 3.875-3.880 GHz, reaching about 34.7-35.7 counts from a surrounding baseline near 40-44 counts. The reference readout does not show a matching dip at the same frequencies; it stays near the low 40s with ordinary fluctuations. The dip is also present in both per-average signal traces around the same frequency region, although the endpoints and reference traces have drift/noise.

Decision: a pODMR resonance is present, based on the frequency-localized contrast in the active post-Rabi readout relative to the reference/background readout.
