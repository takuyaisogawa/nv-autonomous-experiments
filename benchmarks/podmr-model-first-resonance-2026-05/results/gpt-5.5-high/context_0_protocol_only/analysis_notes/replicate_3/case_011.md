Active sequence: Rabimodulated.xml / Rabimodulated. The XML sets full_expt = 0, so the optional 1-level reference block is inactive. The active readout order is: first detection after adj_polarize, serving as the true 0-level reference; second detection after rabi_pulse_mod_wait_time, serving as the microwave-driven signal readout.

Key pulse settings from the provided sequence XML: length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns; mod_depth = 1; mw_freq is swept from 3.825 GHz to 3.925 GHz in the scan export.

Decision: resonance_present. The signal readout shows a distinct frequency-localized drop near 3.900-3.905 GHz, reaching roughly 24.8 and 24.1 counts, while neighboring signal points and much of the scan are higher. The 0-level reference readout does not show the same pronounced trough, so the feature is consistent with a pODMR resonance rather than only a shared collection drift.
