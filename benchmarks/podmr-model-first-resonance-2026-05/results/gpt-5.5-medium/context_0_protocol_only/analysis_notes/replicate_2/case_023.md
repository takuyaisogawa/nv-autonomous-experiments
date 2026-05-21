Sequence XML/export inspection:

The active pulse sequence is Rabimodulated.xml, swept over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active microwave operation is rabi_pulse_mod_wait_time using length_rabi_pulse = 5.2e-08 s, i.e. 52 ns, with mod_depth = 1. The full_expt variable is 0, so the optional 1-level reference block is skipped.

Readout roles:

The first detection occurs immediately after adj_polarize and is the true 0-level/reference readout. The second detection occurs after the modulated Rabi microwave pulse and is the signal readout sensitive to the pODMR response.

Resonance decision:

Readout 1 remains approximately flat around 40-43 counts across the scan. Readout 2 shows a strong, localized, reproducible drop near the center of the frequency sweep, reaching about 31-32 counts while neighboring points recover toward the low 40s. The same dip is visible in both individual averages, so it is not just a single-average artifact. This is consistent with a pODMR resonance being present.
