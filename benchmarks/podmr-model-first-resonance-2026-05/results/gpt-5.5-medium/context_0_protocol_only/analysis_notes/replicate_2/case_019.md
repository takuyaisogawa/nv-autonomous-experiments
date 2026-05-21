Active sequence: Rabimodulated.xml / Rabimodulated sequence, sweeping mw_freq.

The provided sequence XML sets length_rabi_pulse = 5.2e-08 s, which is rounded at 250 MHz sample rate and remains 52 ns. mod_depth is set to 1 in the provided XML. full_expt = 0, so the "Acquire 1 level reference" block is inactive even though do_adiabatic_inversion is true. The executed readouts are therefore:

1. Readout 1: after adj_polarize and detection, before the MW Rabi pulse. This is the true 0-level / no-MW reference.
2. Readout 2: after rabi_pulse_mod_wait_time using length_rabi_pulse and mod_depth, then detection. This is the MW-dependent pODMR signal readout.

Decision: resonance present. Readout 1 is comparatively flat around 40-42 counts across the sweep. Readout 2 shows a pronounced, reproducible drop around 3.875-3.88 GHz, reaching about 32 counts, with both averages showing the same feature. Because the dip appears in the MW-pulse readout and not in the reference readout, it is consistent with a pODMR resonance rather than a shared optical/readout drift.
