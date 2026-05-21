Sequence review:

- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active pulse block: after polarization and a first detection, the sequence applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, then performs the final detection.
- Readout roles: readout 1 is the true 0-level/reference detection acquired after optical polarization before the microwave pulse; readout 2 is the detection after the Rabi-modulated microwave pulse. The optional 1-level reference branch is inactive because full_expt is 0.
- Parameters used for interpretation: length_rabi_pulse is 52 ns, mod_depth is 1, sample_rate is 250 MHz, and the final wait is 1 us.

Data assessment:

Both raw readouts show a similar broad decrease toward the high-frequency end of the scan, especially near 3.92 to 3.925 GHz. Because the reference readout falls along with the post-pulse readout, this is not a localized microwave-dependent loss unique to the post-pulse signal. The readout-2/readout-1 ratio fluctuates from point to point with several isolated positive and negative excursions, but there is no clear, reproducible dip or resonance-shaped feature that stands out from the average-to-average scatter. The largest apparent differences are isolated and not supported by a coherent line shape.

Decision:

No pODMR resonance is evident in this scan.
