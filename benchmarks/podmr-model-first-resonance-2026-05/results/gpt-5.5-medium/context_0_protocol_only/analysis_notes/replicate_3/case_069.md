Active pulse sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

From the provided sequence XML, full_expt = 0, so the optional 1-level reference block is inactive even though do_adiabatic_inversion is true. The active detections are therefore:

1. Readout 1: true 0-level / bright reference after adj_polarize and before the microwave pulse.
2. Readout 2: signal detection after rabi_pulse_mod_wait_time.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, mod_depth = 1, switch_delay = 100 ns, mw_ampl = -5 dBm, ampIQ = 5 dBm, and freqIQ = 50 MHz.

The combined raw traces are noisy and the post-pulse signal relative to the reference does not show a clear, localized, reproducible pODMR dip. The largest negative readout2-readout1 differences occur at several separated frequencies (around 3.830, 3.850, 3.880, and 3.900 GHz), while other nearby points show positive differences. The per-average overlay also suggests substantial average-to-average drift and no consistent narrow resonance. I therefore classify this case as resonance absent.
