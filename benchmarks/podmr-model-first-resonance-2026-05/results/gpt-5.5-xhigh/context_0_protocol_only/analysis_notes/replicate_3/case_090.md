Active sequence assessment from inputs/sequence.xml:

- The active sequence is Rabimodulated, with mw_freq scanned and detuning set to 0.
- The sequence first polarizes the NV and performs detection before any microwave pulse; this is readout 1, the true 0-level / bright reference.
- full_expt is 0, so the optional 1-level reference block is skipped.
- The active microwave operation is rabi_pulse_mod_wait_time using length_rabi_pulse and mod_depth, followed by detection; this final detection is readout 2, the microwave-affected signal readout.
- mod_depth is 1. The requested Rabi pulse duration is 5.2e-08 s; at the 250 MHz sample rate, rounding leaves it at 52 ns.

Data assessment:

The scan spans 3.825 to 3.925 GHz in 5 MHz steps with two averages. The combined post-pulse/reference ratio has a local trough near 3.905 GHz: readout 1 is about 50.808, readout 2 is about 48.173, r2-r1 is about -2.635, and r2/r1 is about 0.948. Both individual averages are negative at this frequency in the post-pulse-minus-reference contrast. Other low points are present, but they are either at the edge of the scan or are less reproducible between the two averages. I therefore interpret the 3.905 GHz local post-pulse reduction as a weak pODMR resonance, noting that the confidence is limited by the noisy two-average data.
