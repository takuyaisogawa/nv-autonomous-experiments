Active pulse sequence: Rabimodulated.xml, with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence details from inputs/sequence.xml:
- sample_rate = 250 MHz.
- length_rabi_pulse = 5.2e-08 s; after rounding to the sample clock this remains 52 ns.
- mod_depth = 1.
- full_expt = 0, so the optional 1-level reference branch is inactive.
- The active body is: polarize, detect, wait, apply rabi_pulse_mod_wait_time, detect, wait.

Readout roles:
- Readout 1 is the detection immediately after polarization, used as the 0-level/reference readout.
- Readout 2 is the detection after the modulated microwave Rabi pulse, used as the pODMR signal readout.

Decision reasoning:
The raw readouts are noisy, but the signal/reference ratio has a clear dip around 3.880 GHz. At 3.880 GHz readout 2 is 41.673 versus readout 1 at 44.538, giving a ratio of about 0.936 and contrast of about 6.4 percent. The two individual averages both show reduced signal/reference ratios near this frequency, about 0.932 and 0.940, so the feature is not only from one average. Nearby points around 3.870 to 3.885 GHz also stay below baseline, while many off-feature points are closer to unity or above. This is consistent with a pODMR resonance being present.
