Sequence context from inputs/sequence.xml:

- Active sequence: Rabimodulated.xml style sequence, scanning mw_freq from 3.825 GHz to 3.925 GHz.
- full_expt = 0, so the optional 1-level reference block is skipped.
- Readout 1 role: detection immediately after adj_polarize, giving the polarized/0-level reference.
- Readout 2 role: detection after rabi_pulse_mod_wait_time, giving the microwave-pulse-affected signal.
- mod_depth = 1.
- length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz, rounding leaves this at 52 ns.

Data assessment:

The relevant contrast is the post-pulse signal relative to the preceding polarized reference. In the combined readouts, readout 2 minus readout 1 is most negative at 3.875 GHz, about -3.87 counts, with readout2/readout1 about 0.908. The adjacent 3.870 GHz point is also depressed. Both individual averages show readout 2 below readout 1 around 3.870-3.875 GHz, although the scan has substantial baseline drift between averages.

Decision:

A localized post-pulse fluorescence reduction relative to the reference is present near 3.875 GHz, so this is best classified as resonance_present despite modest noise and drift.
