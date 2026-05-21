Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The XML instructions first polarize and detect, giving a true 0-level/bright reference readout. Because full_expt is 0, the optional 1-level reference block is skipped. The active experiment then applies rabi_pulse_mod_wait_time with length_rabi_pulse, mod_depth, and switch_delay, followed by detection. Thus readout 1 is the no-MW bright reference and readout 2 is the signal after the microwave pulse.

Relevant pulse settings from the provided sequence/export are length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns, and mod_depth = 1 in the exported variable values. The sequence text embedded in the raw export shows an initial/default mod_depth of 0.3, but the provided sequence.xml and exported Variable_values indicate the active value used for the run is 1.

The combined readout 1 trace stays relatively flat near 33-36 counts without a matching resonance-like feature. Readout 2 shows a pronounced local drop near about 3.875-3.880 GHz down to roughly 29-30 counts, followed by recovery around 3.885 GHz. Since this dip appears in the MW-applied signal readout and not in the reference readout, it is consistent with a pODMR resonance.
