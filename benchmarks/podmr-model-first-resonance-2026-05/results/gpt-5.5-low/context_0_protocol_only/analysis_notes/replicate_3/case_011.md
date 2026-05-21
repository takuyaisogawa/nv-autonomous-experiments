Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz.

The XML sets full_expt = 0, so the optional 1-level reference block is inactive. The executed sequence first polarizes and detects the true 0-level/bright reference, waits, then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection. Thus readout 1 is the reference/background readout and readout 2 is the microwave-modulated pODMR signal readout.

The reference readout is comparatively noisy but does not show a matching strong feature. The signal readout shows a clear depression on the high-frequency side of the sweep, with the combined readout dropping to its minimum around 3.900-3.905 GHz. The same dip is visible in both per-average signal traces, making it more consistent with a pODMR resonance than a single-average fluctuation.

Decision: resonance_present.
