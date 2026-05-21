Sequence inspection:

- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional 1-level reference block is not active.
- Readout roles: readout 1 is the detection immediately after optical polarization, serving as the true 0 / bright reference; readout 2 is the detection after the microwave Rabi pulse, serving as the microwave-affected signal readout.
- mod_depth is 1 from the active variable values.
- length_rabi_pulse is 5.2e-08 s, rounded at 250 MHz sample rate, i.e. a 52 ns pulse.

Data interpretation:

Readout 1 stays mostly around 41-45 counts without a matching deep feature, while readout 2 shows a clear localized depression centered roughly around 3.87-3.88 GHz, dropping to about 34.7-35.7 counts before recovering near 3.89-3.90 GHz. The two-average overlay indicates variability, but the averaged microwave-affected readout has a coherent dip relative to the reference over adjacent scan points. This is the expected signature of a pODMR resonance in this sequence.

Decision: resonance_present.
