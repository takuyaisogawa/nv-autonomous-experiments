Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence interpretation from inputs/sequence.xml:
- full_expt = 0, so the optional 1-level reference block is inactive.
- Readout 1 is the detection immediately after adj_polarize, so it is the polarized/0-level bright reference.
- Readout 2 is the detection after rabi_pulse_mod_wait_time while sweeping mw_freq, so it is the microwave-pulse readout used to look for pODMR contrast.
- mod_depth = 1.
- length_rabi_pulse = 5.2e-08 s, rounded at the 250 MHz sample rate, so the active microwave pulse duration is 52 ns.

Decision:
For a pODMR resonance, I expect a repeatable frequency-localized reduction in the post-pulse readout relative to the 0-level reference. The combined readout 2 trace has isolated low points, but the readout2-readout1 contrast changes sign across the scan and has comparable positive and negative excursions. The largest combined negative contrast is near 3.835 GHz, but the two per-average traces do not show a stable shared dip at one frequency: one average has its largest contrast near 3.865 GHz, while the other has its largest contrast near 3.835 GHz, with other excursions of similar scale elsewhere.

The data therefore looks dominated by average-to-average scatter and slow drift rather than a coherent pODMR line. I classify this case as resonance absent.
