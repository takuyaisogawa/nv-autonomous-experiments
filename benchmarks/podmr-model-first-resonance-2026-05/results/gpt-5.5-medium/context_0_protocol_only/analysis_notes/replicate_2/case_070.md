Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided XML sets full_expt = 0, so the optional 1-level reference block is inactive even though do_adiabatic_inversion is true. The executed readout roles are therefore:
- readout 1: true 0-level reference acquired immediately after optical polarization.
- readout 2: signal readout acquired after the rabi_pulse_mod_wait_time microwave pulse.

The active microwave operation is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on). The exported variable values give length_rabi_pulse = 5.2e-08 s, i.e. 52 ns, and mod_depth = 1. The pulse duration is also rounded to the 250 MHz sample grid, which keeps it at 52 ns.

The combined readouts and per-average traces show broad drift and average-to-average scatter across the sweep. The signal readout does not show a clear, localized ODMR-like dip relative to the reference at a consistent frequency. Features near the middle and high-frequency side are not reproducible as a clean resonance in the two averages and appear comparable to noise/drift. I therefore judge the pODMR resonance to be absent in this measurement.
