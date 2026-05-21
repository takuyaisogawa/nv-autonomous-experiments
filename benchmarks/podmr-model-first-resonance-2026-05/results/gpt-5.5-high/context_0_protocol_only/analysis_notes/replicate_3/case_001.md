Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The XML variables and saved export show length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, and full_expt = 0. Because full_expt is zero, the optional "1 level reference" branch is skipped. The active readouts are therefore the initial detection after optical polarization, serving as the 0-level/reference readout, and the later detection after the rabi_pulse_mod_wait_time block, serving as the pODMR signal readout.

I compared the post-pulse readout against the reference readout over the microwave-frequency sweep. A pODMR resonance in this sequence should appear as a coherent frequency-dependent contrast in the signal readout relative to the reference, typically a dip for the microwave-driven darker spin population. The averaged traces do not show a stable dip-shaped resonance. The largest structure is instead an upward excursion of the post-pulse readout near 3.910-3.915 GHz, while the negative excursions near 3.830 and 3.855 GHz are isolated points and not a consistent resonance feature across the sweep.

Decision: resonance_absent. The data show noisy readout variation and a possible high-side artifact/brightening, but not a convincing pODMR resonance.
