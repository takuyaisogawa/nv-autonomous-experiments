Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz with 21 points. The executable path has full_expt = 0, so the active readouts are the initial polarized/true-0 reference detection followed by a modulated Rabi pulse detection; the optional 1-level reference block is skipped. The Rabi pulse duration is length_rabi_pulse = 52 ns, rounded to the 250 MHz sample clock, and the exported active variable values give mod_depth = 1.

Readout role interpretation: readout 1 is the pre-microwave polarized reference, and readout 2 is the post-rabi-pulse measurement. For an ODMR-like resonance in this sequence I would expect a coherent frequency-localized reduction of the post-pulse fluorescence relative to the reference around resonance.

The combined raw traces fluctuate by roughly the same size as any possible feature. The largest central contrast near 3.875 GHz has readout 2 above readout 1, opposite the expected fluorescence dip, while negative contrasts occur at separated frequencies such as 3.835 and 3.865 GHz without a consistent line shape. The per-average overlay also shows substantial average-to-average drift, so the apparent variations do not form a reproducible pODMR resonance.

Decision: resonance absent.
