Sequence interpretation:

The provided sequence is Rabimodulated.xml. The active sweep parameter is mw_freq, with a scan from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active microwave operation is a modulated Rabi pulse:

PSeq = rabi_pulse_mod_wait_time(PSeq,sample_rate,length_rabi_pulse,mod_depth,switch_delay,ch_on);

The listed variable values give length_rabi_pulse = 5.2e-08 s, i.e. 52 ns, and mod_depth = 1. The sequence rounds the duration to the sample grid at 250 MS/s, which leaves 52 ns unchanged.

Readout roles:

1. The first detection occurs after adj_polarize and before the Rabi pulse. This is the true 0 level reference.
2. The optional 1 level reference block is inactive because full_expt = 0, so it is skipped.
3. The second detection occurs after the 52 ns modulated Rabi pulse. This is the signal readout to compare against the 0 reference.

Resonance assessment:

The combined readouts fluctuate by roughly one to a few counts across the sweep. The signal-minus-reference contrast has several isolated negative excursions, for example near 3.830, 3.850, 3.870, 3.900, and 3.905 GHz, but these do not form a single reproducible dip or line shape. The per-average overlay shows that the larger excursions are not consistent between the two averages: one average has stronger dips near 3.850 and 3.905 GHz, while the other has stronger dips near 3.830 and 3.870 GHz. The readout traces also cross and wander without a coherent resonance feature.

Decision:

I do not identify a reliable pODMR resonance in this scan. The apparent dips are comparable to the average-to-average scatter and do not persist at a consistent frequency.
