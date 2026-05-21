Active sequence inspection:

- Sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML instructions first polarize and detect a true 0-level/no-MW reference, then skip the optional 1-level reference block because full_expt = 0, then apply one rabi_pulse_mod_wait_time pulse and detect again.
- Readout roles: readout 1 is the initial no-MW reference detection; readout 2 is the post-rabi-pulse signal detection.
- mod_depth from the provided sequence variable values is 1.
- Active pulse duration length_rabi_pulse is 5.2e-08 s, i.e. 52 ns, rounded at the 250 MHz sample rate.

Data assessment:

The raw readouts are noisy, but the relevant comparison is the post-pulse signal relative to the no-MW reference. The combined readout2/readout1 ratio reaches its minimum at 3.885 GHz, about 0.924, and both individual averages also have their minimum ratio at 3.885 GHz. This frequency-localized common dip is consistent with a pODMR resonance rather than only uncorrelated readout noise.

Decision: resonance present.
