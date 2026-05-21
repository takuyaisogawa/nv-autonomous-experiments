Sequence inspection:

- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active instructions acquire a true 0-level reference first with adj_polarize followed by detection, then wait.
- The "Acquire 1 level reference" block is inactive because full_expt = 0, so no additional 1-level reference readout is included.
- The active measurement pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns.
- mod_depth is 1 from the provided sequence XML and the exported variable values.
- Readout role interpretation: readout 1 is the pre-pulse 0-level/reference detection; readout 2 is the post-Rabi-pulse signal detection.

Data assessment:

Readout 1 stays relatively flat around the mid-30 count level across the sweep. Readout 2 has a strong localized fluorescence decrease centered around 3.875-3.880 GHz, dropping from a baseline near 35-37 counts to about 28 counts, and this feature appears in both averages. Because the dip is in the pulse-affected signal readout and not mirrored as a comparable feature in the reference readout, this is consistent with a pODMR resonance from the single NV center.

Decision: resonance_present.
