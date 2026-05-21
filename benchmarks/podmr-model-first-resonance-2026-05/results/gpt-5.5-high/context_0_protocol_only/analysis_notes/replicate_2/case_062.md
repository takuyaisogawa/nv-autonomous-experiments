Active sequence: Rabimodulated.xml / Rabimodulated. The provided sequence has full_expt = 0, so the optional 1-level reference branch is skipped even though do_adiabatic_inversion is true. The executed detections are therefore: first, a true 0-level reference after polarization; second, the signal readout after rabi_pulse_mod_wait_time.

Readout roles: readout 1 is the reference detection before the microwave pulse; readout 2 is the post-pulse detection after the modulated Rabi pulse. The microwave frequency is scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Pulse settings used for the decision: length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s to 52 ns; mod_depth = 1; mw_ampl = -5 dBm; ampIQ = 5 dBm; freqIQ = 50 MHz.

Decision: resonance_present. The post-pulse readout shows a coherent depression relative to the reference over several neighboring scan points, especially around 3.895-3.910 GHz, and both averages contribute to this lower signal band. The trace is noisy and there are isolated excursions elsewhere, but the multi-point contrast feature is more consistent with a pODMR resonance than with a flat absent response.
