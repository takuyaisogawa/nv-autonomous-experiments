Sequence inspection:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instructions first polarize and detect a true 0-level reference readout, then wait. The optional 1-level reference block is inactive because full_expt = 0, despite do_adiabatic_inversion being true. The active measurement pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, i.e. 52 ns, mod_depth = 1, and switch_delay = 100 ns, followed by the signal detection. Thus readout 1 is the bright/reference readout and readout 2 is the post-microwave signal readout for the pODMR test.

Data assessment:

The raw readouts are around 45 to 50 counts with point-to-point fluctuations. Readout 2 does not show a stable, localized ODMR-like dip or peak relative to readout 1 across the frequency sweep. The largest excursions are isolated and not reproduced consistently in both per-average traces; for example, the low signal near 3.855 GHz is followed by a high point near 3.860 GHz, and the per-average overlay shows broad drift/noise rather than a coherent resonance feature. With only two averages and the visible scatter comparable to any apparent contrast, there is no convincing pODMR resonance in this scan.

Decision: resonance_absent.
