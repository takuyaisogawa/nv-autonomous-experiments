Active sequence identified from inputs/sequence.xml and raw_export.json: Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The pulse program first polarizes and detects the bright/0-level reference, waits, then because full_expt = 0 it skips the optional 1-level reference block. The active experimental readout is the later detection after rabi_pulse_mod_wait_time using length_rabi_pulse = 52 ns and mod_depth = 1, with switch_delay = 100 ns.

Readout roles: readout 1 is the direct polarized 0-level reference detection; readout 2 is the post-microwave-pulse detection. A pODMR resonance should appear as a reproducible frequency-dependent reduction in the post-pulse readout relative to the reference, not merely a common drift in both raw channels.

The combined raw traces show substantial scan-dependent drift in both readouts. The readout2/readout1 ratio has local dips near 3.88 and 3.89 GHz, but the two averages are not reproducible: the per-average overlays show large baseline shifts and inconsistent point-to-point structure, with feature amplitudes comparable to noise/drift. There is no coherent resonance-shaped contrast across the averages over the scanned microwave frequency range.

Decision: resonance_absent. Confidence: 1.
