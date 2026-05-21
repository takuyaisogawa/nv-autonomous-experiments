Sequence review:

- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Provided sequence variables give length_rabi_pulse = 5.2e-08 s (52 ns) and mod_depth = 1.
- full_expt = 0, so the optional 1-level reference block is inactive even though do_adiabatic_inversion is true.
- Active readout roles: readout 1 is the detection immediately after optical polarization, serving as the true 0-level/bright reference; readout 2 is the detection after the modulated Rabi pulse and is the MW-affected signal.

Data assessment:

Both raw readouts show similar broad drift over the sweep, especially a gradual lower-count region near the middle of the scan. The MW-affected signal does not show a clean, reproducible dip or peak relative to the 0-level reference. The combined contrast has isolated negative excursions, including near 3.900 GHz, but adjacent points do not support a resonance-shaped feature and the two averages do not consistently reproduce a localized line. Because the apparent structure is comparable to readout drift and point-to-point noise, I do not identify a pODMR resonance in this case.
