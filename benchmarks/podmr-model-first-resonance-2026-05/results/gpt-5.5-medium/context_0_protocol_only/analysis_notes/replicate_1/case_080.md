Sequence inspection:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active pulse path uses adj_polarize followed by detection for the true 0-level reference, then a wait, then rabi_pulse_mod_wait_time followed by detection for the microwave-driven signal. The optional 1-level reference block is inactive because full_expt = 0. The provided sequence variables show length_rabi_pulse = 52 ns and mod_depth = 1, with sample_rate = 250 MHz. The pulse duration is rounded to the sample grid, and 52 ns remains compatible with the 4 ns sample period.

Readout roles:

Readout 1 is the initial 0-level reference detection after polarization. Readout 2 is the detection after the modulated Rabi pulse. Since the scan varies mw_freq, a pODMR resonance should appear as a frequency-dependent change in the post-pulse readout relative to the reference, rather than as a feature in either raw channel alone.

Data assessment:

The raw readouts are noisy with only two averages, but the combined contrast readout2 - readout1 becomes consistently negative across the central/high-frequency portion of the sweep, especially around 3.88-3.91 GHz. The ratio readout2/readout1 drops to about 0.94 near 3.88, 3.89, and 3.91 GHz, while neighboring points outside this region return closer to unity or above. This is not a clean isolated Lorentzian dip, but it is a contiguous microwave-frequency-dependent contrast feature in the expected direction for the active post-pulse signal.

Decision:

A weak pODMR resonance is present.
