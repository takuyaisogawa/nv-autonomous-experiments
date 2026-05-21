Sequence inspection:

The active sequence is Rabimodulated.xml, varying mw_freq over 3.825e9 to 3.925e9 Hz. The instructions first polarize and perform detection to acquire the true 0-level reference. The optional 1-level reference block is inactive because full_expt is 0. The active measurement then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s and mod_depth = 1, followed by detection. Thus readout 1 is the reference and readout 2 is the post-microwave signal readout.

Data assessment:

Readout 1 remains relatively flat around 40-43 counts across the sweep. Readout 2 shows a strong localized drop from its baseline near 41-42 counts down to about 31-32 counts around 3.875e9 to 3.88e9 Hz. The per-average overlay shows the same dip in both averages, so the feature is repeatable rather than a single noisy point. Given the sequence role and the localized contrast loss in the signal readout relative to the reference, this is consistent with a pODMR resonance.
