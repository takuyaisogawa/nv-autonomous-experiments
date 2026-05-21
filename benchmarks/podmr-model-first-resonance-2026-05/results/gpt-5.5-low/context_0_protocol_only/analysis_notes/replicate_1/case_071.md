Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence/readout interpretation: full_expt is 0, so the optional "Acquire 1 level reference" block is skipped even though do_adiabatic_inversion is true. The active readouts are therefore the initial detection after optical polarization, which serves as the true 0-level/raw reference, followed by a 52 ns rabi_pulse_mod_wait_time microwave pulse and a second detection, which is the pODMR signal readout. The configured mod_depth is 1 in the exported variable values, and length_rabi_pulse is 5.2e-08 s, rounded at 250 MS/s to 52 ns.

Resonance assessment: a real pODMR resonance should appear as a consistent frequency-dependent change in the post-pulse readout relative to the reference readout, ideally reproducible across the two averages. The combined traces fluctuate by roughly a few counts across the scan, but the apparent dips and peaks are not cleanly localized or consistently expressed between averages. Around the lower-count region near 3.865 GHz, both readouts and individual averages show substantial scatter rather than a stable resonance feature. Later variations near 3.91-3.92 GHz are also inconsistent between the reference and signal readouts. I do not see a robust ODMR-like contrast feature above the raw readout noise.

Decision: resonance_absent.
