I used the provided sequence XML as the active sequence description. The sequence is Rabimodulated.xml, scanned by mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active variables are length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s to 52 ns, and mod_depth = 1. full_expt = 0, so the optional 1-level reference block is skipped.

The two active detections therefore have these roles:
- readout 1: detection immediately after adj_polarize, the polarized true-0 reference.
- readout 2: detection after rabi_pulse_mod_wait_time with the 52 ns modulated microwave pulse, the pODMR signal readout.

For a resonance I would expect a frequency-localized decrease in readout 2 relative to readout 1. The combined traces instead show substantial common-mode baseline drift, especially toward the high-frequency end, and the normalized readout-2/readout-1 contrast alternates between positive and negative excursions. The larger negative points are isolated and not shaped like a coherent resonance; the two averages also show inconsistent contrast features. I therefore do not see a defensible pODMR resonance in this scan.
