Active sequence and parameters:
- The active pulse sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML sets length_rabi_pulse to 5.2e-08 s, which rounds to 52 ns at the 250 MHz sample rate.
- mod_depth is 1 in the variable values used for this run.
- full_expt is 0, so the conditional "Acquire 1 level reference" block is skipped.

Readout roles:
- The first detection occurs immediately after adj_polarize and is the true 0-level/polarized reference.
- The second active detection occurs after rabi_pulse_mod_wait_time using the 52 ns pulse and mod_depth 1, so it is the microwave-pulse readout.
- Because full_expt is 0, there is no active intermediate 1-level reference readout in this measurement.

Resonance assessment:
The two combined raw readouts are noisy and show a mild overall upward drift across the microwave-frequency scan. A pODMR resonance would normally appear as a localized dip or contrast feature in the post-pulse readout relative to the reference. Here the post-pulse readout does not show a coherent localized resonance feature; the largest excursions are isolated point-to-point fluctuations and the endpoint rise, while the per-average overlays are not consistent enough to support a resonance call.

Decision: resonance absent.
