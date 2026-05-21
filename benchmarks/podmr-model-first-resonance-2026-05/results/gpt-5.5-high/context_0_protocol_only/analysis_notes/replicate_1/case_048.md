I used the provided sequence.xml to identify the active measurement sequence before making the call.

Active sequence: Rabimodulated mw_freq scan. The instructions first polarize and detect, then skip the 1-level reference block because full_expt = 0, then apply rabi_pulse_mod_wait_time followed by detection. The do_adiabatic_inversion flag is inside the inactive reference block and is not part of the active scan.

Readout roles:
- readout 1 is the initial polarized/detection reference, described in the XML as the true 0 level reference.
- readout 2 is the detection after the microwave Rabi pulse.

Pulse settings from sequence.xml:
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate, so the active pulse duration is 52 ns.
- mod_depth = 1.

The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps with two averages. A pODMR resonance should appear as a consistent localized change in the post-pulse readout relative to the reference, normally a dip in the microwave readout or normalized contrast. Here the combined signal/reference contrast is jagged, with low points spread across multiple unrelated frequencies rather than centered on a single reproducible feature. The per-average overlay shows substantial average-to-average scatter, and the candidate dips are not stable enough to distinguish from noise.

Decision: resonance_absent.
