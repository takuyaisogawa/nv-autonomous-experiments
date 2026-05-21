Case podmr_042_2026-05-16-225623.

The provided sequence XML is Rabimodulated.xml. It scans mw_freq and uses a modulated Rabi pulse before the final detection. The first detection occurs immediately after adj_polarize and is the true 0-level reference/bright readout. The optional 1-level reference block is inactive because full_expt is 0, so the second recorded readout is the microwave-affected signal after rabi_pulse_mod_wait_time. The active pulse uses length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate, with mod_depth = 1; this is a 52 ns pulse.

For a pODMR resonance, the microwave-affected readout should show a frequency-localized decrease relative to the 0-level reference. The combined readout 2 trace has a low point near 3.875 GHz, but readout 1 also drops there and the reference-normalized signal is not uniquely low; comparable negative readout2-readout1 excursions occur at other scan points. The two individual averages are noisy and do not show a consistent, reproducible resonance-shaped dip at one frequency. The dominant feature is common-mode drift/noise across both readouts rather than a clear microwave-frequency-dependent contrast feature.

Decision: resonance_absent.
