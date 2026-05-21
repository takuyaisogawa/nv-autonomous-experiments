Active sequence: Rabimodulated pODMR with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence/readout roles from inputs/sequence.xml:
- The first detection follows adj_polarize directly and is the true 0-level reference readout.
- full_expt is 0, so the optional 1-level reference block is skipped.
- The active measurement readout follows rabi_pulse_mod_wait_time and is therefore the modulated-pulse signal readout.
- mod_depth is 1.
- length_rabi_pulse is 5.2e-08 s; with sample_rate 250 MHz this rounds to 13 samples, still 52 ns.

Data interpretation:
The two combined raw readouts track each other only loosely. The signal-minus-reference contrast has mean near zero and alternates sign across the frequency sweep, with excursions of roughly a few percent. The strongest negative and positive differences are not localized into a clear ODMR-like dip or peak and are not reproducible between the two per-average traces. The per-average overlays show substantial opposite drift and inconsistent features, so the combined apparent structure is more consistent with noise/drift than a stable resonance.

Decision: no reliable pODMR resonance is present in this scan.
