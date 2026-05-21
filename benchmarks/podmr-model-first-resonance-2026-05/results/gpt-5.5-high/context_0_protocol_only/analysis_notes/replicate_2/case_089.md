Active sequence: Rabimodulated.xml, scanned by mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence XML sets up a Rabi-modulated pODMR measurement. It first performs adj_polarize followed by detection, then waits. Because full_expt = 0, the optional 1-level reference branch is inactive even though do_adiabatic_inversion is true. The only microwave manipulation before the second detection is:

PSeq = rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on);

with length_rabi_pulse = 5.2e-08 s, sample_rate = 250 MHz, and mod_depth = 1 in the provided sequence XML. The pulse duration rounds to 52 ns at this sample rate. Therefore readout 1 is the no-microwave/0-level reference detection after polarization, and readout 2 is the detection after the 52 ns Rabi-modulated microwave pulse.

The raw readouts both show a slow upward baseline over the frequency range and point-to-point scatter. The readout-2 minus readout-1 contrast changes sign repeatedly and does not form a consistent, reproducible resonance-shaped dip or peak. The per-average overlay also shows that excursions are not stable enough across the two averages to identify a real pODMR feature. I therefore classify this case as resonance_absent.
