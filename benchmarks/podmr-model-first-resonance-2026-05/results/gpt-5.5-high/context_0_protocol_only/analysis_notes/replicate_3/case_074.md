Case podmr_060_2026-05-17-060259.

The provided sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active pulse sequence has full_expt = 0, so the optional 1-level reference block is skipped. The executed readouts are:

- readout 1: initial detection after polarization, before the microwave pulse; this is the bright/reference readout.
- readout 2: final detection after rabi_pulse_mod_wait_time using length_rabi_pulse = 52 ns; this is the microwave-affected signal readout.

The variable list in the saved export gives mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. The sequence.xml text embedded in the export shows an older/default mod_depth value of 0.3 in the raw sequence string, but the applied Variable_values and the workspace sequence.xml both indicate mod_depth = 1, so I used mod_depth = 1 for the active setting.

For resonance assessment I compared readout 2 against readout 1 rather than using either raw channel alone. The combined signal/reference contrast has its strongest negative excursion at 3.875 GHz: readout 1 is about 52.50, readout 2 is about 48.87, giving a difference near -3.63 and ratio near 0.931. Nearby frequencies also fluctuate, and the two averages are noisy. Still, the differential dip at 3.875 GHz is consistent with a pODMR resonance in this Rabimodulated mw_freq scan, especially because the active signal readout is lower relative to the pre-pulse reference at that point.

Decision: resonance present, with low-to-moderate confidence because the feature is noisy and only partly repeatable across the two averages.
