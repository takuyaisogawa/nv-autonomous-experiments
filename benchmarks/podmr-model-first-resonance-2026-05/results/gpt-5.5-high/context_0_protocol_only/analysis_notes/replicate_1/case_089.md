Active sequence: Rabimodulated.xml.

The provided sequence sweeps mw_freq and applies a modulated Rabi pulse before the final detection. The reference block for the 1 level is inactive because full_expt = 0, so the first detection is the true 0 level reference after optical polarization and before the microwave pulse. The second detection is the readout after rabi_pulse_mod_wait_time.

Relevant pulse parameters from the provided XML:
- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s, i.e. 52 ns
- sample_rate = 250 MHz, so the 52 ns pulse is already aligned to a 4 ns sample grid
- delay_wrt_1mus = 0.2 us

The raw data span 3.825 to 3.925 GHz in 5 MHz steps with two averages. A pODMR resonance in this sequence should appear as a frequency-localized change in the post-pulse readout relative to the pre-pulse reference, ideally reproducible between averages. Here the two readouts mainly show shared slow upward drift plus noisy point-to-point variation. The readout2-readout1 difference changes sign repeatedly and lacks a stable localized dip or peak. The per-average overlay also does not show a consistent feature at one frequency.

Decision: resonance_absent.
