The provided sequence XML defines the active pulse sequence as Rabimodulated.xml. It sets a 250 MHz sample rate and uses mw_freq as the swept parameter. The microwave pulse is applied by rabi_pulse_mod_wait_time after the initial reference detection, with length_rabi_pulse = 5.2e-08 s, which rounds to 52 ns at the sample rate. The XML sets mod_depth = 1. full_expt = 0, so the optional 1-level reference block is inactive.

Readout roles from the instructions:
- The first detection follows adj_polarize and is the true 0-level reference, with no preceding Rabi pulse.
- The second active detection follows the 52 ns modulated Rabi pulse and is the measurement channel that should show pODMR contrast.

In the combined raw readouts, readout 1 stays near 40.4 to 44.1 counts without a matching central dip, while readout 2 drops strongly from the low 40s to about 33.9 counts near 3.88 GHz before recovering. The same depression is visible in both per-average readout-2 traces, while the reference channel does not show a corresponding feature. Because the dip is localized in the pulsed readout relative to the reference and is reproducible across averages, this is consistent with a pODMR resonance being present.
