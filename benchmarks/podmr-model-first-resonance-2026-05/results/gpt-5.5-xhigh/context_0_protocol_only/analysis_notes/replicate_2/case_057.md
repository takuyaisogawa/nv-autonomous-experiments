Case podmr_043_2026-05-16-231159

Sequence interpretation:
- Active sequence file: Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active variables from the provided XML are length_rabi_pulse = 5.2e-08 s, mod_depth = 1, sample_rate = 250 MHz, and full_expt = 0.
- The rounded Rabi pulse duration remains 52 ns because 52 ns is 13 samples at 250 MHz.
- Because full_expt = 0, the conditional "Acquire 1 level reference" branch is inactive even though do_adiabatic_inversion is set.

Readout roles:
- Readout 1 is the first active detection after adj_polarize, used as the true 0-level reference.
- Readout 2 is the detection after the 52 ns rabi_pulse_mod_wait_time pulse with mod_depth = 1.

Resonance assessment:
The combined post-pulse/reference comparison has scattered excursions but no coherent pODMR feature. The largest apparent dips are isolated and not reproducible across the two averages: for example the combined dip near 3.885 GHz is strong in one average but essentially absent in the other, while other negative points also move between averages. The post-pulse trace is often above the reference rather than showing a stable fluorescence reduction at a localized microwave frequency. With only noisy, non-reproducible point-to-point changes and no clear resonance-shaped contrast, I classify this scan as resonance absent.
