Active sequence: Rabimodulated.xml.

From the provided sequence XML, the active acquisition is:
- Polarize with the laser, then detect immediately. This first detection is the true 0-level reference readout.
- The 1-level reference block is inactive because full_expt = 0.
- Apply rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, then detect. This second detection is the microwave-driven signal readout.

The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. Comparing the post-pulse signal readout to the 0-reference readout, the strongest coherent negative contrast appears around 3.885-3.890 GHz: the signal is about 6.9% below the reference at both adjacent points. The same sign of signal-below-reference is present in both averages at these points. There are other noisy single-point lows, including near the high-frequency edge, but the adjacent dip near 3.885-3.890 GHz followed by recovery is consistent with a pODMR resonance.

Decision: resonance_present.
