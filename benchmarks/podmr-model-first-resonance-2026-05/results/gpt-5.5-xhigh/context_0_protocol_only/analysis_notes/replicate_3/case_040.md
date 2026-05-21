Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The active instructions create two detections because full_expt = 0 disables the optional 1-level reference block. The first detection occurs immediately after adj_polarize, so it is the bright/0-level reference readout. The second detection occurs after rabi_pulse_mod_wait_time, so it is the pODMR signal readout after the microwave pulse.

The microwave pulse is the rabi_pulse_mod_wait_time call using length_rabi_pulse. With sample_rate = 250 MHz and length_rabi_pulse = 5.2e-08 s, rounding leaves a 52 ns pulse. The provided sequence XML sets mod_depth = 1. The do_adiabatic_inversion flag is true, but no adiabatic inversion is active in this run because that code is inside the disabled full_expt block.

Decision: resonance_present. The post-pulse signal readout drops relative to the 0-level reference around 3.895-3.900 GHz, with about -4% combined contrast across two adjacent frequency points and recovery by 3.905 GHz. The scan is noisy and there are other excursions, but this localized dip in the signal/reference contrast is consistent enough with a pODMR resonance to call present.
