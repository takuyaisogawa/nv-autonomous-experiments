Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

From inputs/sequence.xml, the active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s. At sample_rate = 250 MHz this is 13 samples, so the rounded pulse duration remains 52 ns. The modulation depth is mod_depth = 1.

Readout roles: full_expt = 0, so the optional 1-level reference block is skipped. Readout 1 is the detection immediately after adj_polarize, the polarized true-0 reference. Readout 2 is the detection after the 52 ns modulated Rabi pulse, so it is the microwave-pulse signal readout.

The signal-reference contrast has a localized negative feature at 3.895 GHz. Combined readout2 - readout1 is -2.769 there, compared with a scan mean of about -0.080 and standard deviation of about 1.263. The same point is negative in both averages (-3.731 and -1.808), while the reference readout alone does not show an equally isolated collapse. This supports a pODMR resonance being present.
