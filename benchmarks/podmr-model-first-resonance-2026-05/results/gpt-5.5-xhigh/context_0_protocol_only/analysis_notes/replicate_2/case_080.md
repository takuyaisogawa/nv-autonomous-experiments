Sequence inspection:
- The exported scan uses Rabimodulated.xml and varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- In the active XML, full_expt = 0, so the optional 1-level reference block is skipped. do_adiabatic_inversion is set true, but it is only inside the skipped/commented reference logic and is not active for the measured signal path.
- The active path is: polarize, first detection, wait, rabi_pulse_mod_wait_time, second detection, final wait.
- Therefore readout 1 is the pre-pulse/0-level fluorescence reference, and readout 2 is the post-microwave-pulse signal readout.
- mod_depth = 1.
- length_rabi_pulse = 5.2e-08 s; at sample_rate = 250 MHz this rounds to 52 ns.

Data assessment:
The combined readout 2 signal is lower than readout 1 over a localized band near 3.880-3.895 GHz, with signal-reference contrast around -5.7%, -4.4%, -6.4%, and -3.5% at those four points. The per-average data also show a negative signal-reference difference through this band, so the feature is not solely from one average. There are noisy excursions elsewhere, including a positive point at 3.875 GHz and edge variation, but the localized replicated fluorescence deficit after the active microwave pulse is consistent with a pODMR resonance.

Decision: resonance_present.
