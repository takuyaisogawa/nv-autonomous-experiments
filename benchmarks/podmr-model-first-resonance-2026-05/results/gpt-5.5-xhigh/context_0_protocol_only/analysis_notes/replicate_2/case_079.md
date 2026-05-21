Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz.

The sequence first polarizes and detects without a microwave pulse; this first detection is the true 0-level/reference readout. The optional 1-level reference block is inactive because full_expt = 0. The active pODMR measurement then applies rabi_pulse_mod_wait_time followed by the second detection, so the second readout is the microwave-affected signal readout.

Resolved pulse settings: mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz, the rounding step leaves the pulse at 52 ns.

The combined raw readouts both have baseline drift, so the signal/reference contrast is more informative than either raw trace alone. The signal/reference ratio shows a local depression around 3.890-3.895 GHz: both averages are low there, and the combined ratio drops relative to neighboring points. This is consistent with a pODMR fluorescence dip from microwave resonance.

Decision: resonance_present.
