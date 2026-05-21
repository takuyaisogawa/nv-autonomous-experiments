Sequence review: inputs/sequence.xml is the Rabimodulated sequence with mw_freq swept from 3.825 GHz to 3.925 GHz. The instructions first polarize and detect, so readout 1 is the true 0-level reference. full_expt = 0 skips the optional 1-level reference block. The active microwave operation is rabi_pulse_mod_wait_time followed by detection, so readout 2 is the post-pulse signal.

Relevant active parameters from the provided XML: sample_rate = 250 MHz, length_rabi_pulse = 5.2e-08 s, which is exactly 13 samples or 52 ns after rounding, and mod_depth = 1. The pulse is therefore a full-depth 52 ns modulated Rabi pulse before the signal readout.

The raw readouts show frequency-dependent drift, especially in readout 1, so the resonance decision should be based on the post-pulse signal relative to the same-scan reference rather than either raw trace alone. The combined readout2/readout1 ratio has its lowest point near 3.905 GHz, about 0.947, and the points from roughly 3.905 to 3.920 GHz remain below the reference before recovering at the high-frequency edge. Both individual averages also show low normalized signal at 3.905 GHz, approximately 0.941 and 0.954.

The feature is noisy and not a deep smooth ODMR line, but the repeated post-pulse contrast dip relative to the no-MW reference is sufficient evidence for a weak pODMR resonance.
