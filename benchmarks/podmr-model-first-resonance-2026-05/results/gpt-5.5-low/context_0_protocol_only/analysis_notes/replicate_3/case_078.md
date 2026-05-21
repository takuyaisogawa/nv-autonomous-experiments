Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

Sequence/readout interpretation:
- The sequence first performs optical polarization and detection, which is the true 0-level reference readout.
- The optional 1-level reference block is disabled because full_expt = 0, so that intermediate reference is not active.
- The active microwave operation is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the signal detection readout.
- Thus the two plotted readouts are the 0-level reference and the microwave-pulse signal readout, not a full three-readout reference experiment.

Assessment:
The raw readouts fluctuate around roughly the same level across the sweep. The signal/reference difference changes sign repeatedly and the largest features are isolated single-point deviations, including a high signal point near 3.915 GHz rather than a consistent ODMR fluorescence dip. The per-average overlay also shows that these deviations are not stable across averages. I do not see a reproducible resonance-like contrast feature tied to the microwave frequency sweep.

Decision: resonance_absent.
