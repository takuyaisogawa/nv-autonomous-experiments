Sequence interpretation and decision note

Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence has full_expt = 0, so the "Acquire 1 level reference" block is skipped. The active readout roles are:
- readout 1: true 0-level reference after adj_polarize and detection, with no preceding microwave pulse in the active block.
- readout 2: signal readout after rabi_pulse_mod_wait_time followed by detection.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz this is exactly 13 samples, so the rounded pulse duration remains 52 ns. The active mod_depth value is 1.0.

Decision: I treated readout 1 as the local fluorescence/reference level and looked for a frequency-localized dip in readout 2 relative to readout 1. The two raw readouts both decline near the high-frequency end, so that feature is common-mode rather than readout-specific ODMR contrast. The readout-2/readout-1 contrast has noisy single-point excursions, but the dips are not consistent across the two averages and do not form a reproducible resonance line. I therefore decide that a pODMR resonance is absent in this scan.
