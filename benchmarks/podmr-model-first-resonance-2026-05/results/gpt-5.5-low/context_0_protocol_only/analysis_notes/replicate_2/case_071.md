Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence interpretation from inputs/sequence.xml and raw_export.json:
- sample_rate = 250 MHz.
- length_rabi_pulse = 5.2e-08 s, rounded to 52 ns at the sample rate.
- mod_depth = 1 in Variable_values for this run.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive.
- Readout 1 is the true 0-level reference after adj_polarize and detection.
- Readout 2 is the detection after the modulated Rabi pulse.

Data assessment:
The two combined raw readouts fluctuate by roughly a few counts across the sweep, but the apparent dips and peaks are not cleanly aligned between the reference and post-pulse readout in a way that supports a reproducible pODMR resonance. The per-average overlay also shows substantial average-to-average scatter, especially around the low points, so the visible structure is not clearly distinguishable from noise or baseline variation. I therefore classify this case as resonance absent.
