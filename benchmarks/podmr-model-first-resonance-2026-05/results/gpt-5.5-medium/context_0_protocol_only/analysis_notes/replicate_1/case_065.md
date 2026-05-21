Active sequence: Rabimodulated.xml, sweeping mw_freq over 3.825 to 3.925 GHz in 5 MHz steps.

Sequence/readout interpretation:
- sample_rate is 250 MHz.
- length_rabi_pulse is 52 ns after rounding.
- mod_depth is 1 from the recorded variable values.
- full_expt is 0, so the optional "Acquire 1 level reference" block is inactive.
- Readout 1 is the initial detection after adj_polarize, serving as the bright/0 reference.
- Readout 2 is the detection after the modulated Rabi microwave pulse, so this is the pODMR signal readout.

Data assessment:
The raw readouts are noisy, but the post-pulse readout shows a clear local minimum at 3.895 GHz. At that point readout 2 is 45.38 while the reference readout is 50.00, giving about -9.2% contrast. The per-average traces also both show low post-pulse values at this frequency, so the feature is not only from one average. Neighboring points are less deep, and the scan is sparse, but the localized negative contrast in the signal readout relative to the reference is consistent with a pODMR resonance.

Decision: resonance_present.
