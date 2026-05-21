Active sequence: Rabimodulated.xml, varying mw_freq from 3.825e9 to 3.925e9 in 5e6 steps.

The provided sequence XML sets length_rabi_pulse = 5.2e-08 s, sample_rate = 250000000 Hz, so the rounded active microwave pulse remains 52 ns. The active modulation depth is mod_depth = 1. The full_expt variable is 0, so the optional "Acquire 1 level reference" block is skipped even though do_adiabatic_inversion is true.

Readout roles from the executed instruction order:
- readout 1: detection after adj_polarize, the true 0-level / bright reference before the swept rabi pulse.
- readout 2: detection after rabi_pulse_mod_wait_time with the 52 ns pulse and mod_depth 1, the pODMR-sensitive readout.

The first readout is comparatively flat over the scan, with only normal scatter. The second readout shows a strong, localized drop centered around about 3.875e9 to 3.88e9 Hz, falling to roughly 39.6 counts while neighboring points and the outer scan range are mostly near 46 to 48 counts. The same dip is visible in both per-average traces, so it is not just one average or a global drift. This is the expected ODMR contrast signature in the post-pulse readout.

Decision: resonance_present.
