Sequence context:
- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Pulse path: polarize/detect first, wait, then rabi_pulse_mod_wait_time with length_rabi_pulse, then detect again.
- Readout roles: readout 1 is the initial bright/0-level reference before the microwave pulse; readout 2 is the post-Rabi-pulse signal readout. The optional 1-level reference block is inactive because full_expt = 0.
- mod_depth from the active XML variable values is 1.
- Pulse duration length_rabi_pulse is 5.2e-08 s, i.e. 52 ns, rounded at the 250 MHz sample rate.

Resonance assessment:
The combined traces fluctuate around roughly 53 counts with only two averages. Readout 2 has isolated low points, especially near 3.910 GHz, but these are not smooth or reproducible across averages. The ratio/difference between readout 2 and the reference is also dominated by point-to-point noise and by a readout 1 spike near 3.865 GHz rather than a consistent post-pulse ODMR dip. There is no clear frequency-localized resonance feature across the sweep.

Decision: resonance_absent.
