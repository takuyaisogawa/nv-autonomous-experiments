Sequence inspection:

- Active sequence: Rabimodulated.xml / Rabimodulated pulse sequence while sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided sequence sets length_rabi_pulse to 5.2e-08 s, which is rounded at 250 MS/s and remains 52 ns.
- The provided sequence sets mod_depth to 1.
- full_expt is 0, so the optional one-level reference block is skipped.
- Readout roles: readout 1 is the detection immediately after optical polarization, acting as the polarized 0-level reference. readout 2 is the detection after the 52 ns modulated Rabi pulse, acting as the microwave-on signal readout.

Data assessment:

I compare readout 2 against readout 1 because the sequence provides a reference detection followed by the microwave-pulse signal detection at each swept microwave frequency. The combined ratio readout2/readout1 has its lowest value at 3.900 GHz, about 0.923, corresponding to a suppression of roughly 7.7 percent relative to the reference. There is also a neighboring low point at 3.895 GHz, about 0.942. In the two individual averages, the deepest low appears at 3.900 GHz for one average and at 3.895 GHz for the other, so the feature is not just a single isolated combined-readout fluctuation.

The trace is noisy and only has two averages, but the microwave-on readout shows a localized dip near 3.895-3.900 GHz relative to the reference readout. This is consistent with a pODMR resonance being present.
