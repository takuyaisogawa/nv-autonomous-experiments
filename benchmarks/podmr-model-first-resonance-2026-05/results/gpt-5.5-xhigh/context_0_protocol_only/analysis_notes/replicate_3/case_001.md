Provided sequence XML:

- Active sequence: Rabimodulated.xml / rabi_pulse_mod_wait_time while sweeping mw_freq.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- Readout roles: readout 1 is the true 0-level reference after polarization; readout 2 is the post-Rabi-pulse signal detection.
- Active pulse settings: mod_depth = 1, length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz, this is already 13 samples, so the rounded pulse duration remains 52 ns.

Data assessment:

The combined signal-minus-reference contrast is negative at several scan points, with the most convincing repeatable localized dip at about 3.855 GHz: both averages have readout 2 below readout 1 there. Another repeatable negative point appears near 3.830 GHz, while the large positive features and the endpoint negative swing are less consistent between averages. Because the active signal readout shows frequency-localized reductions relative to the 0-level reference under the Rabi pulse, I classify this case as resonance present.
