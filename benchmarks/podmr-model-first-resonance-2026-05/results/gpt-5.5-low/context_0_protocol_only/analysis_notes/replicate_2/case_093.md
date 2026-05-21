Sequence inspection:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz.
- full_expt is 0, so the optional 1-level reference block is not active.
- The active sequence first polarizes and detects the true 0-level reference, then applies a rabi_pulse_mod_wait_time pulse and detects again.
- Readout 1 is therefore the pre-microwave reference detection; readout 2 is the post-microwave signal detection.
- mod_depth is 1 in the exported variable values used for this run.
- length_rabi_pulse is 5.2e-08 s, rounded at 250 MS/s to 52 ns.

Data assessment:
The two-readout traces fluctuate around roughly the same level across the sweep. A pODMR resonance should appear as a reproducible frequency-localized change in the post-pulse signal relative to the reference, but the readout difference changes sign several times and the large excursions are not consistent across the two averages. The apparent high-frequency point near 3.92 GHz is isolated and not supported by a coherent dip or peak pattern relative to the reference. With only two averages and substantial point-to-point scatter, the data do not show a defensible resonance feature.

Decision: resonance_absent.
