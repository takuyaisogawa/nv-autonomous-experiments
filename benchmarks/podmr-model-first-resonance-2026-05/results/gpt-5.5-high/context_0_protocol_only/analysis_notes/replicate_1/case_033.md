I inspected inputs/sequence.xml and the raw readout data before deciding.

The active sequence is Rabimodulated.xml. With full_expt = 0, the optional 1-level reference block is inactive. The active detections are therefore:
- readout 1: the true 0-level reference acquired after adj_polarize and before the microwave/Rabi pulse.
- readout 2: the signal readout acquired after rabi_pulse_mod_wait_time.

The active Rabi-modulated pulse uses length_rabi_pulse = 5.2e-08 s, which is 52 ns. The sequence XML sets mod_depth = 1. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The raw data show a clear, localized dip only in the post-pulse signal readout. Readout 2 falls from typical values near 46-49 counts to 42.88 at 3.870 GHz, 39.77 at 3.875 GHz, and 38.96 at 3.880 GHz, while the reference readout remains near 47-49 counts through the same region. The per-average traces both show the same suppression near 3.875-3.880 GHz, so the feature is not just a single-average fluctuation. This is consistent with a pODMR resonance being present.
