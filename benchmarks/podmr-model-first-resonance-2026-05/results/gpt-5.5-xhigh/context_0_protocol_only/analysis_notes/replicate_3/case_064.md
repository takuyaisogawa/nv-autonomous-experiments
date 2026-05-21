Sequence XML review:

The active sequence is Rabimodulated. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML has full_expt = 0, so the optional 1-level reference block is skipped.

Readout roles:

1. First detection follows adj_polarize only, so it is the no-microwave bright/reference readout.
2. Second detection follows rabi_pulse_mod_wait_time, so it is the microwave-pulse signal readout.

Pulse settings used for the active signal shot:

- length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns.
- mod_depth = 1.
- switch_delay = 1e-07 s.

Data assessment:

The microwave-shot readout should be compared against the preceding reference readout at each frequency. The signal-minus-reference contrast is noisy overall, but it has a localized repeatable negative feature at 3.865 GHz: the two averages give about -3.35 and -3.50 counts, producing the strongest combined contrast dip. A second weaker negative feature appears near 3.910 GHz and is also negative in both averages. These dips are localized rather than a smooth baseline offset, and their sign matches reduced fluorescence after the microwave pulse.

Decision:

A pODMR resonance is present, with the clearest evidence at 3.865 GHz and weaker supporting evidence near 3.910 GHz.
