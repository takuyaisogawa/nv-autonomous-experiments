Sequence inspection:

- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active microwave manipulation before the signal detection is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- length_rabi_pulse is 5.2e-08 s, i.e. 52 ns. With sample_rate 250 MHz, this remains 52 ns after rounding.
- mod_depth in the provided sequence XML is 1.
- full_expt is 0, so the "Acquire 1 level reference" block is inactive and does not contribute a readout.

Readout roles:

- readout 1 is the detection immediately after adj_polarize, so it is the bright/0-level reference.
- readout 2 is the detection after the modulated 52 ns Rabi pulse, so it is the pODMR signal channel.

Resonance assessment:

The signal readout is noisy, with only two averages, but the signal/reference contrast is not random across the whole sweep. The combined readout 2 trace is depressed relative to readout 1 across a clustered region around roughly 3.865-3.900 GHz, including pronounced negative differences near 3.875, 3.880, 3.890, and 3.900 GHz. The per-average data are not perfectly consistent, but one average shows the same central trough structure strongly and the combined trace preserves a broad dip-like feature. This supports a weak/noisy pODMR resonance being present rather than a clearly flat or absent response.
