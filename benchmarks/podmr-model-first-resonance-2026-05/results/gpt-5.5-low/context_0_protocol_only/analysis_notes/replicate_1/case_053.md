Active sequence: Rabimodulated.xml / Rabi-modulated pODMR while sweeping mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

From the provided sequence XML, full_expt = 0, so the optional 1-level reference block is inactive even though do_adiabatic_inversion is true. The active readouts are therefore:
- readout 1: true 0-level reference after optical polarization, before the microwave pulse.
- readout 2: signal readout after the Rabi-modulated microwave pulse.

The microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate, so the active pulse duration is 52 ns. The provided sequence XML sets mod_depth = 1.

The expected pODMR signature would be a coherent, frequency-localized depression or contrast feature in the post-pulse signal relative to the reference, reproducible across averages. Here the two averages are noisy and do not show a stable, localized resonance-shaped feature. The combined readouts drift and cross, with isolated fluctuations near several frequencies, but no consistent dip or peak centered within the swept range that is clearly distinguishable from average-to-average scatter.

Decision: resonance_absent.
