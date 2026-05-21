Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz. The sequence first performs polarization and detection to acquire the true 0-level reference, then skips the 1-level reference because full_expt = 0, then applies rabi_pulse_mod_wait_time followed by detection for the signal readout. From the provided sequence XML, mod_depth is 1 and length_rabi_pulse is 5.2e-08 s, which is already on the 250 MHz sample grid as a 52 ns pulse.

Readout role interpretation: readout 1 is the true 0-level reference detection, and readout 2 is the post-modulated-Rabi-pulse detection. A pODMR resonance would normally appear as a coherent frequency-localized change in the signal readout relative to the reference, most likely a dip in the post-pulse fluorescence/contrast near resonance for this NV measurement.

The combined traces are noisy over only two averages. Readout 2 crosses above and below readout 1 several times, with large point-to-point excursions and no stable, reproducible line shape. The strongest deviations are not a clean isolated dip and the per-average overlay shows substantial average-to-average scatter comparable to or larger than the apparent contrast features. There is no convincing frequency-localized resonance feature across the sweep.

Decision: resonance_absent.
