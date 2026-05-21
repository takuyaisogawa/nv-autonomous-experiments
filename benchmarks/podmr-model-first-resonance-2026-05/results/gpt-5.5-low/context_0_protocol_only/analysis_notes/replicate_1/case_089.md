Sequence and readout assessment:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The executable path has full_expt = 0, so the optional 1-level reference block is skipped even though do_adiabatic_inversion is true. The sequence therefore takes a true 0-level reference after adj_polarize/detection, then applies rabi_pulse_mod_wait_time followed by the signal detection. The active microwave pulse is length_rabi_pulse = 52 ns after sample-rate rounding. The saved variable list reports mod_depth = 1.

Readout roles:

Readout 1 is the initial polarized 0-level reference detection before the Rabi pulse. Readout 2 is the detection after the 52 ns modulated Rabi pulse.

Resonance decision:

Across the mw_freq scan, the raw readouts and per-average overlays show no reproducible localized pODMR dip or peak between the two readout channels. Both channels mainly show small point-to-point fluctuations plus a broad upward drift toward the high-frequency end. Features near the upper end are shared by the channels and averages rather than forming a narrow, readout-specific ODMR contrast feature. With only two averages and substantial scatter, the data do not support identifying a resonance.

Decision: resonance_absent.
