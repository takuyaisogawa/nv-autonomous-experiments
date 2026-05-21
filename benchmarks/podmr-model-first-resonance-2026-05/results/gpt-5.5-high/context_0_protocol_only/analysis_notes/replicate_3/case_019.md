Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

From the provided sequence XML, full_expt is 0, so the conditional "Acquire 1 level reference" block is inactive. The actual readouts are:
- readout 1: detection immediately after adj_polarize, serving as the bright/polarized reference.
- readout 2: detection after rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

The first readout is relatively flat near 40-42 counts across the scan. The second readout has a pronounced, repeatable depression near 3.875-3.880 GHz, dropping to about 32 counts in the combined trace, and both per-average traces show the same feature. Because the contrast appears in the microwave-pulse readout and not in the reference readout, this is consistent with a pODMR resonance.
