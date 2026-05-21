The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML shows a true 0-level reference is acquired first by optical polarization followed by detection. The optional 1-level reference block is disabled because full_expt = 0, so the second active detection is the pODMR signal after rabi_pulse_mod_wait_time.

For the active pODMR pulse, length_rabi_pulse is 5.2e-08 s (52 ns). The provided sequence XML sets mod_depth = 1. The active pulse is therefore a 52 ns modulated Rabi pulse at full modulation depth, followed by the signal readout.

The combined readouts are noisy over the scan. A pODMR resonance from this sequence should appear as a coherent feature in the post-pulse signal relative to the bright reference, typically a repeatable reduction in the post-pulse readout at resonance. The largest post-pulse feature is instead an isolated upward spike near 3.915 GHz, opposite the expected dark-resonance sign. Negative reference-normalized excursions occur at several separate frequencies, but they are not consistently reproduced across the two averages and often appear driven by reference fluctuations rather than a stable signal dip.

Decision: resonance_absent. The data do not show a reliable pODMR resonance in the active signal readout.
