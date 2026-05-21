Sequence XML review:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz. The active microwave operation before the signal readout is rabi_pulse_mod_wait_time using length_rabi_pulse = 52 ns and mod_depth = 1, with switch_delay = 100 ns. The full_expt flag is 0, so the optional 1-level reference block is not executed even though do_adiabatic_inversion is true.

Readout roles:

Readout 1 is the true 0-level reference acquired after optical polarization and before the microwave pulse. Readout 2 is the pODMR signal acquired after the modulated 52 ns microwave pulse. Since the 1-level reference branch is inactive, there are only the reference and signal readouts.

Data assessment:

The raw readouts are noisy across the 21-point microwave-frequency scan. Readout 2 does not show a stable, isolated ODMR-like dip relative to the reference; instead it has alternating point-to-point highs and lows, including isolated peaks near 3.835, 3.895, and 3.910 GHz and a single low near 3.885 GHz that is not supported by a coherent contrast trend. The per-average traces show large average-to-average offsets and fluctuations comparable to the apparent features in the combined readouts.

Decision:

I do not see a reliable pODMR resonance in this scan. The apparent extrema are not sufficiently coherent across readout roles or averages to call a resonance present.
