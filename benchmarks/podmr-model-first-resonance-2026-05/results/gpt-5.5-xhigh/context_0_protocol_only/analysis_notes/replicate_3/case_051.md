Active sequence and roles

The sequence is Rabimodulated.xml with mw_freq swept from 3.825e9 to 3.925e9 in 5 MHz steps, with 2 averages. In the active instructions, full_expt=0, so the optional "Acquire 1 level reference" branch is skipped.

Active readouts:

1. adj_polarize followed by detection before the microwave pulse: readout 1, the true 0-level/reference readout.
2. rabi_pulse_mod_wait_time followed by detection: readout 2, the driven signal readout after the microwave pulse.

The modulation depth is mod_depth=1. The driven pulse duration is length_rabi_pulse=5.2e-8 s; at sample_rate=250 MHz this is 13 samples, or 52 ns.

Data assessment

For a pODMR resonance, I would expect the driven signal readout to show a localized frequency-dependent contrast relative to the reference, preferably consistent across the two averages. The combined readout 2 minus readout 1 contrast changes sign across the scan and is dominated by isolated excursions rather than a stable line shape. The large apparent contrast around 3.900 GHz is driven mainly by a dip in the reference readout, not by a reproducible feature in the driven readout. The per-average traces also do not show the same feature at the same frequency.

Decision

I classify this scan as resonance_absent because the active driven readout does not show a clear, reproducible pODMR resonance relative to the reference.
