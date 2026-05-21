Sequence inspection:

The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes and detects a true 0-level/reference readout, then waits. The full_expt variable is 0, so the optional 1-level reference branch is inactive. The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection. Therefore readout 1 is the reference / 0-level detection and readout 2 is the post-pulse signal readout relevant for pODMR contrast.

Data assessment:

Readout 1 stays near its baseline over the sweep without a matching narrow depression. Readout 2 has a strong localized dip around 3.875-3.880 GHz, falling from a typical mid-46 to 48 count level to about 39 counts, and this dip is visible in both per-average traces. Because the dip is specific to the post-pulse signal channel and is repeated across averages while the reference channel remains comparatively stable, this is consistent with a pODMR resonance.

Decision: resonance_present.
