Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The XML sets full_expt = 0, so the optional 1-level reference block is inactive despite do_adiabatic_inversion being true. The executed sequence is: polarize, detect the true 0-level/reference readout, wait, apply rabi_pulse_mod_wait_time using length_rabi_pulse = 52 ns and mod_depth = 1, then detect the microwave-affected readout. The first readout is therefore the no-microwave/reference fluorescence and the second readout is the pODMR signal after the modulated microwave pulse.

The two combined readouts fluctuate around 50-52 counts with comparable point-to-point noise. There are isolated excursions, including a high point in the second readout near the high-frequency end and a high point in the first readout near 3.87 GHz, but these do not form a clear, reproducible ODMR-like dip or peak in the signal readout relative to the reference. The per-average overlay shows substantial average-to-average scatter and no stable resonance-shaped feature across the scan.

Decision: resonance_absent. Confidence is low-to-moderate because the scan is noisy with only two averages, but the data do not show a convincing pODMR resonance.
