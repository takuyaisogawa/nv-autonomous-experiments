Active pulse sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

From inputs/sequence.xml, full_expt is 0, so the optional 1-level reference block is inactive. The first detection after adj_polarize is the true 0-level/reference readout. The second detection follows rabi_pulse_mod_wait_time and is the microwave-pulse signal readout. The active pulse uses length_rabi_pulse = 5.2e-08 s, which is 52 ns and already matches the 250 MS/s sample grid, with mod_depth = 1 and switch_delay = 100 ns.

The combined raw readouts show readout 1 staying near the low-to-mid 40s without a comparable localized feature. Readout 2 has a clear dip centered near the 3.875 GHz scan point, falling to about 34.17 from a surrounding baseline near 43-45, and both individual averages show the same minimum region. This is a coherent microwave-frequency-dependent contrast feature in the signal readout, so I classify the pODMR resonance as present.
