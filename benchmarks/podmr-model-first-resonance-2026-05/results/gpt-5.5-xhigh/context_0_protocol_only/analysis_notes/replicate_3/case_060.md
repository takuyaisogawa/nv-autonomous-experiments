Active sequence interpretation from inputs/sequence.xml:

The scan is a Rabimodulated-style mw_freq sweep. The sequence first runs adj_polarize, then a detection window for the true 0-level reference, then waits. The optional "Acquire 1 level reference" block is inactive because full_expt = 0, so the adiabatic inversion setting is not used in the active path. The active microwave operation is rabi_pulse_mod_wait_time followed by the second detection window.

Readout roles:
- readout 1: true 0-level optical reference after polarization, before the Rabi pulse.
- readout 2: signal readout after the modulated microwave Rabi pulse.

Pulse parameters from the XML:
- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 13 samples = 52 ns

Data assessment:

The combined post-pulse contrast (readout 2 - readout 1) / readout 1 reaches its strongest negative value at about 3.860 GHz, approximately -8.6%. This same scan point is also the strongest negative contrast point in both individual averages, about -7.9% and -9.3%, while the immediately neighboring points return much closer to baseline. There are additional noisy fluctuations elsewhere, but the repeated negative contrast at the same frequency in the active signal readout is consistent with a pODMR resonance.

Decision: resonance_present.
