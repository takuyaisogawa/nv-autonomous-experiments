Active pulse sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz.

Sequence/readout roles from the XML:
- The first detection occurs after adj_polarize and before any Rabi microwave pulse, so readout 1 is the true 0-level/reference readout.
- full_expt is 0, so the optional 1-level reference block is inactive.
- The active signal block applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection, so readout 2 is the microwave-pulse signal readout.

Relevant pulse settings:
- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate, i.e. 52 ns
- mw_freq is the scanned parameter.

Decision:
Readout 2 has a clear localized decrease from about 29 near the sides to about 24.2 around 3.875-3.880 GHz, while readout 1 remains near 29-31 without a matching dip. Since the active sequence compares the post-pulse signal against a no-pulse reference and the dip is localized in microwave frequency, this is consistent with a pODMR resonance.
