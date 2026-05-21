Active sequence: Rabimodulated.xml. The provided XML sets full_expt = 0, so the optional 1-level reference block is skipped. The executed readouts are therefore: readout 1 after polarization/detection, acting as the zero-level reference; readout 2 after a modulated Rabi pulse followed by detection, acting as the microwave-sensitive signal readout.

The provided XML uses mod_depth = 1 and length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate, so the active pulse duration is 52 ns. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The raw readouts are noisy and have average-to-average offsets, but the relevant comparison is readout 2 relative to readout 1 at each frequency. The combined trace shows a negative contrast region around 3.88-3.91 GHz: readout 2 is lower than readout 1 by about 2-3 counts at 3.880, 3.885, 3.890, and 3.910 GHz. This depression is also visible in both individual averages around 3.88-3.89 GHz, though there are noisy excursions including a positive point near 3.875 GHz and at the high-frequency edge.

Because the microwave-sensitive readout shows a reproducible dip relative to the reference over several neighboring frequency points, I classify this case as resonance_present, with limited confidence due to the small number of averages and noisy baseline.
