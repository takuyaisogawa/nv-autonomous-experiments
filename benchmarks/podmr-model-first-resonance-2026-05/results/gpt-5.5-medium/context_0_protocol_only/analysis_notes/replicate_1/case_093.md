Sequence inspection:
- Active sequence: Rabimodulated.xml, with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Readout roles: first detection follows adj_polarize and is the true 0-level reference readout; the optional 1-level reference block is inactive because full_expt = 0; the final detection after rabi_pulse_mod_wait_time is the microwave-modulated signal readout.
- mod_depth: 1.
- Rabi pulse duration: length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate, so 52 ns.

Resonance decision:
The two combined raw readouts fluctuate around roughly 50 to 52 counts with no consistent, repeatable dip or peak across both readout roles at the same microwave frequency. Features such as the high point in readout 1 near 3.87 GHz and the high point in readout 2 near 3.92 GHz are not corroborated by the other readout or consistently reproduced in the per-average overlay. With only two averages and point-to-point noise of comparable size to the apparent excursions, the scan does not show a credible pODMR resonance.
