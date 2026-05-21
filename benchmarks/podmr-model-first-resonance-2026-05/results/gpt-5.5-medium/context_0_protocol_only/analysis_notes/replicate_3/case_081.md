Active sequence: Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence first performs polarization and detection for the true 0-level reference. Since full_expt is 0, the optional 1-level reference block is inactive. The active experiment then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection. Thus readout 1 is the 0-level reference and readout 2 is the post-pulse pODMR signal.

The raw signal is noisy with only 2 averages, but the post-pulse readout falls below the reference over a cluster of scan points around 3.88-3.90 GHz. The combined signal/reference contrast is most negative near 3.885 GHz and remains negative at nearby points, while the reference readout does not show a matching isolated drop. The per-average traces are not identical, so the feature is weak, but the averaged behavior is consistent with a pODMR resonance rather than a completely flat/no-resonance scan.

Decision: resonance_present.
