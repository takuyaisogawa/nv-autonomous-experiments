Sequence inspection:

The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML has full_expt = 0, so the conditional "Acquire 1 level reference" block is not active even though do_adiabatic_inversion is true. The active sequence therefore performs an adjusted laser polarization and detection first, waits, then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the signal detection. The two readouts should be interpreted as the initial polarized/reference readout and the post-microwave-pulse readout, not as a full 0/1 reference pair.

Data assessment:

Across the frequency sweep, the two combined readouts fluctuate around roughly 50 to 52 counts with no stable, monotonic, or localized ODMR-like dip/peak in the post-pulse signal relative to the reference. The strongest excursions are isolated points and are not reproduced consistently between the two averages; the per-average traces show comparable random scatter and crossing behavior. The apparent differences between readouts are therefore consistent with noise/average-to-average variation rather than a resolved pODMR resonance.

Decision:

No pODMR resonance is present in this scan.
