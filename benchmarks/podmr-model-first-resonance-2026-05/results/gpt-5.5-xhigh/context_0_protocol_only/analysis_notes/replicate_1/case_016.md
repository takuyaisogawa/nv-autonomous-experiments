Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence/readout interpretation from inputs/sequence.xml:
- sample_rate = 250 MHz.
- length_rabi_pulse = 5.2e-08 s, which rounds to 52 ns at this sample rate.
- mod_depth = 1.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive.
- Readout 1 is the detection immediately after adj_polarize and is the true 0-level reference.
- Readout 2 is the detection after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay), so it is the microwave-pulse pODMR signal readout.

Data assessment:
Readout 2 has a large, localized fluorescence dip around 3.875-3.880 GHz: combined readout 2 reaches 30.0 at 3.875 GHz and 28.98 at 3.880 GHz, while readout 1 at those points is 38.21 and 37.13. The ratio readout2/readout1 is about 0.78 at the minimum. Both averages independently show their minimum ratio at 3.880 GHz, near 0.78, so the feature is repeatable across averages. Readout 1 has some point-to-point variation, including a lower point near 3.885 GHz, but it does not show the same deep, coherent dip seen in the post-pulse readout.

Decision:
A pODMR resonance is present.
