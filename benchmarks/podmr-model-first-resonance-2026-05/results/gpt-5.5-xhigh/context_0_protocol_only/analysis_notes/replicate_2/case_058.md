Sequence inspection:

- Active sequence: Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional 1-level reference branch is inactive despite do_adiabatic_inversion being true.
- Readout 1 is the "true 0 level reference" after optical polarization and before the microwave Rabi-modulated pulse.
- Readout 2 is the detection after rabi_pulse_mod_wait_time using length_rabi_pulse.
- mod_depth is 1.
- length_rabi_pulse is 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns.

Data assessment:

The relevant pODMR contrast is the post-pulse readout relative to the 0-level reference, not the raw trace labels. The averaged readout2-readout1 difference has its strongest negative excursion at 3.865 GHz, where readout 2 is about 2.42 counts below readout 1, corresponding to about 4.8% contrast. This point is also supported by both individual averages: average 1 has about 3.9% contrast and average 2 has about 5.8% contrast at 3.865 GHz. The data are noisy and there are other point-to-point fluctuations, but the consistent localized deficit in the microwave-pulsed readout is sufficient evidence for a weak pODMR resonance.
