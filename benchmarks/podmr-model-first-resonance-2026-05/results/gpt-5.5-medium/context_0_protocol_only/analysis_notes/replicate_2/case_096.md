Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML sets length_rabi_pulse to 5.2e-08 s (52 ns) and mod_depth to 1. The instructions acquire a true 0-level reference with polarization followed by detection, then skip the 1-level reference because full_expt is 0, then apply rabi_pulse_mod_wait_time with the 52 ns pulse and detect again. Thus readout 1 is the 0/reference readout and readout 2 is the pulse-affected pODMR readout.

The two averaged traces are noisy and only weakly reproducible across the two averages. The pulse readout has isolated high points near 3.865 and 3.875 GHz and a lower region around 3.905-3.915 GHz, but these changes are comparable to the scatter seen between averages and do not form a clear, consistent resonance-shaped dip or peak relative to the reference trace. The normalized contrast would not show a robust localized ODMR resonance across the scan.

Decision: resonance_absent.
