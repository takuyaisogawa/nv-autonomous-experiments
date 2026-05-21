Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz.

From the provided sequence XML, the microwave frequency is set by mw_freq plus detuning, and the active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s (52 ns) and mod_depth = 1. The optional "Acquire 1 level reference" block is gated by full_expt, which is 0, so that block is inactive despite do_adiabatic_inversion being true.

Readout roles: the first detection occurs immediately after adj_polarize and is the true 0-level/reference readout. The second active detection occurs after the 52 ns modulated Rabi pulse and is the microwave-driven signal readout.

Decision: the signal readout has a clear, localized drop near 3.875-3.880 GHz, reaching roughly 31 counts while neighboring points and the reference readout stay near the high-30s to low-40s. This dip appears in both per-average traces, so it is not a single-average artifact. Because the dip is selective to the post-pulse signal readout rather than the pre-pulse reference, it is consistent with a pODMR resonance.
