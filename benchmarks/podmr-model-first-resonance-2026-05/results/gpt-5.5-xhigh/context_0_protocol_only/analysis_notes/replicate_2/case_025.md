Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. From the provided sequence XML, full_expt = 0, so the "Acquire 1 level reference" block is inactive despite do_adiabatic_inversion being true in the variables. The active flow is polarization, detection, wait, then one rabi_pulse_mod_wait_time pulse followed by detection and final wait.

Readout roles: readout 1 is the true 0-level reference immediately after adj_polarize and before the microwave pulse. Readout 2 is the signal readout after the modulated microwave Rabi pulse.

Pulse settings used for the decision: length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns; mod_depth = 1; switch_delay = 100 ns.

The combined data show a clear signal-only depression in readout 2 near 3.870-3.880 GHz while readout 1 remains comparatively high. The largest contrast occurs at 3.875 GHz, where readout 2 is 31.19 versus readout 1 at 40.90, a ratio of about 0.763 and a difference of about -9.71 counts. The same feature appears in both averages: at 3.875 GHz the readout-2/readout-1 ratios are about 0.727 and 0.788. The local recovery after the dip supports interpreting this as a pODMR resonance rather than only broad drift.

Decision: resonance_present.
