Sequence inspection:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first performs polarization and detection to acquire the true 0-level reference, then because full_expt = 0 it skips the optional 1-level reference block. It then applies rabi_pulse_mod_wait_time using length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection. Thus readout 1 is the pre-pulse 0-level reference and readout 2 is the post-pulse measurement after the modulated Rabi pulse.

The combined readouts and the per-average overlay do not show a clear, repeatable ODMR-like resonance feature across the microwave-frequency sweep. The apparent extrema are isolated and inconsistent between the two readouts and between averages, with substantial average-to-average baseline offset and point-to-point scatter. There is no stable dip or peak in the signal relative to the reference that would support identifying a pODMR resonance in this single-NV measurement.

Decision: resonance_absent.
