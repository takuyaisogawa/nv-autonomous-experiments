Sequence review:

The active sequence is Rabimodulated.xml. In the provided sequence XML, sample_rate is 250 MHz, length_rabi_pulse is 5.2e-08 s, mod_depth is 1, and the microwave frequency is the swept parameter. The pulse duration rounds to 52 ns at this sample rate.

Readout roles:

The first active detection occurs immediately after adj_polarize and is labeled in the sequence comments as the true 0 level reference. The full_expt variable is 0, so the optional 1 level reference block is skipped. The second active detection follows rabi_pulse_mod_wait_time using length_rabi_pulse and mod_depth, so it is the microwave-pulsed signal readout.

Data assessment:

The raw readouts are noisy, but the microwave-pulsed signal compared with the reference shows its strongest local negative contrast near 3.885 GHz. This minimum is present in both stored averages, whereas many other excursions are either smaller, broad drift, or inconsistent between averages. Given the active 52 ns modulated pulse and the replicated local signal suppression, I interpret this as a pODMR resonance being present, with only moderate confidence because the scan has two averages and visible point-to-point noise.
