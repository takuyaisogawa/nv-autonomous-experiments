Active sequence inspection:

The scan uses Rabimodulated.xml while varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The provided sequence performs an initial polarize and detection block before the microwave pulse, then skips the optional "Acquire 1 level reference" branch because full_expt is 0. It then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s and mod_depth = 1, followed by the second detection block.

Readout roles:

Readout 1 is the pre-microwave bright/reference detection after polarization. Readout 2 is the post-Rabi-pulse detection and is the microwave-frequency-dependent readout to compare against the reference. The pulse duration is 52 ns.

Resonance assessment:

The combined readouts do not show a convincing pODMR resonance. The post-pulse readout does not form a reproducible dip against the reference over the frequency sweep; the readout-2 minus readout-1 contrast changes sign repeatedly, and the largest excursions are isolated. The two per-average overlays have strong opposite baseline drift and inconsistent pointwise contrast, so the combined trace appears dominated by noise/drift rather than a stable resonance feature.

Decision: resonance_absent.
