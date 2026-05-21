Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The XML instructions set microwave parameters, polarize, then perform a detection before any microwave pulse. Since full_expt = 0, the optional "Acquire 1 level reference" block is inactive. The active signal block applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, then performs the second detection.

Readout roles:
- readout 1 is the initial polarized true-0/reference readout.
- readout 2 is the post-modulated-Rabi-pulse signal readout.

The reference readout remains roughly flat/noisy around the high-30s to low-40s counts. The signal readout shows a pronounced frequency-localized dip centered near 3.875-3.880 GHz, falling to about 31 counts while neighboring points are near 36-40 counts. This dip appears in both averages and is not mirrored by the reference readout, so it is consistent with a pODMR resonance rather than common-mode readout drift.

Decision: resonance_present.
