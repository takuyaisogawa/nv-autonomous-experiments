Sequence inspection:

The active sequence is Rabimodulated.xml / Rabimodulated, with mw_freq swept from 3.825e9 to 3.925e9 Hz in 5 MHz steps. The active pulse path has full_expt = 0, so the optional 1-level reference block is skipped. The executed readouts are therefore the first detection after optical polarization, serving as the true 0-level/reference readout, followed by a rabi_pulse_mod_wait_time pulse and a second detection serving as the microwave-pulse readout. The exported variable values give length_rabi_pulse = 5.2e-08 s (52 ns), mod_depth = 1, switch_delay = 1e-07 s, and delay_wrt_1mus = 2e-07 s.

Data assessment:

For a pODMR resonance I would expect a reproducible microwave-frequency-dependent contrast feature, typically a dip in the microwave-pulse readout relative to the reference or a consistent feature in the readout difference/ratio across averages. Here the combined traces fluctuate around the low-to-mid 40 count range. Readout 2 has isolated high excursions near 3.84 GHz and 3.91-3.915 GHz, while readout 1 stays comparatively smooth and does not show a matching resonance-like feature. The per-average overlay shows substantial disagreement between averages, including baseline drift and opposite/uncorrelated excursions, rather than a stable dip or contrast centered at a plausible frequency.

Decision:

No reliable pODMR resonance is present in this scan.
