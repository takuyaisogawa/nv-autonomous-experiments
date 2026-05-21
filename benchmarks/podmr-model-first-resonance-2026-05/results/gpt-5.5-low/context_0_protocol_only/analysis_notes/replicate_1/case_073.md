Sequence inspection:

The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The programmed microwave interaction is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection. Before that pulse, the sequence performs adj_polarize and detection to acquire the true 0-level reference. The optional 1-level reference block is disabled because full_expt = 0, so only the initial reference readout and the post-pulse signal readout are active.

Readout interpretation:

Readout 1 is the pre-pulse reference after polarization. Readout 2 is the post-rabi-pulse signal readout. Since this is pODMR, I looked for a frequency-localized, reproducible change in the post-pulse signal relative to the reference across the two averages, rather than relying on labels or prior cases.

Resonance decision:

The combined readouts fluctuate by roughly the same scale as the per-average variation. Readout 2 has low points near 3.87-3.885 GHz but these are not accompanied by a clean, consistent resonance-shaped contrast feature in the overlay, and the per-average traces show substantial scatter and inconsistent structure. There is no clear, repeatable pODMR dip or peak distinguishable from noise over the scanned range.

Decision: resonance_absent.
