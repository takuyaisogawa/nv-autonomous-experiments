Active pulse sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Readout roles: the first detection after adj_polarize is the true 0-level/reference readout. The optional 1-level reference block is not active because full_expt = 0. The second active detection follows a rabi_pulse_mod_wait_time call and is the microwave-applied signal readout.

Key pulse settings from the provided XML/export: length_rabi_pulse = 5.2e-08 s, which rounds to 52 ns at 250 MHz sample rate; mod_depth = 1 in Variable_values for this run; switch_delay = 100 ns; delay_wrt_1mus = 200 ns.

Decision: the two combined readouts mostly track each other with small noisy fluctuations. There is a pronounced downward point in readout 2 near 3.895 GHz, but it is not mirrored as a robust resonance feature across both readout channels or across the two averages, and the per-average traces show comparable scatter over the scan. I do not see a reproducible pODMR resonance dip or peak distinct from noise.
