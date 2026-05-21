Case podmr_028_2026-05-13-100213.

The provided sequence is Rabimodulated.xml. The active experimental block has full_expt = 0, so the optional 1-level reference block is skipped. The executed readouts are therefore:

1. Readout 1: detection immediately after adj_polarize, serving as the true 0-level/reference readout.
2. Readout 2: detection after rabi_pulse_mod_wait_time, serving as the microwave-pulse signal readout.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, i.e. 52 ns before and after sample-rate rounding at 250 MHz. The provided sequence XML and exported variable values give mod_depth = 1.

The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The signal readout has its lowest value at 3.905 GHz, where readout 2 is 24.115 while the reference readout is 27.615. The signal/reference ratio is also lowest there, about 0.873. The neighboring signal points recover toward 26.65 at 3.910 GHz and 28.42 at 3.915 GHz, and the per-average overlays show the signal channel depressed around 3.900-3.905 GHz in both averages. The reference readout is noisy but does not show the same deepest minimum at 3.905 GHz.

Conclusion: a weak but identifiable pODMR-like fluorescence dip is present near 3.905 GHz, so I classify this case as resonance_present.
