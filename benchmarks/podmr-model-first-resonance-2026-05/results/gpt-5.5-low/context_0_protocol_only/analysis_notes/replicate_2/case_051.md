Sequence inspection:
- Active sequence: Rabimodulated.xml / Rabimodulated sequence varying mw_freq.
- Scan range: 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Readout roles: readout 1 is the initial polarized/true-0 reference detection after adj_polarize; readout 2 is the detection after the modulated Rabi microwave pulse. The optional 1-level reference block is inactive because full_expt = 0.
- Pulse settings used for the active microwave pulse: length_rabi_pulse = 52 ns, mod_depth = 1, mw_ampl = -5 dBm, ampIQ = 5 dBm, freqIQ = 50 MHz.

Resonance assessment:
The relevant pODMR contrast should appear as a reproducible frequency-dependent change in the post-pulse readout relative to the reference. The raw traces fluctuate at the few-count level across the scan, but there is no coherent dip or peak with a stable line shape. The notable excursion near 3.900 GHz is mostly associated with a low reference readout, while the post-pulse readout remains within the same noisy band as neighboring points. The two averages also show substantial scatter rather than a consistent resonance feature.

Decision: resonance_absent.
