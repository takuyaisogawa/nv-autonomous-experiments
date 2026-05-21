Active sequence identification from inputs/sequence.xml:

The pulse program is Rabimodulated-style pODMR with mw_freq swept. It first sets the microwave and enabled channels, then performs adj_polarize followed by detection. This first detection is the true 0-level reference/readout. The optional "Acquire 1 level reference" block is inactive because full_expt is set to 0, so that branch does not contribute a readout. The active microwave manipulation is then rabi_pulse_mod_wait_time using length_rabi_pulse = 5.2e-08 s, i.e. 52 ns, with mod_depth = 1 and switch_delay = 1e-07 s, followed by the second detection. Thus readout 1 is the pre-pulse polarized reference and readout 2 is the microwave-pulse signal readout.

Data assessment:

The scan varies mw_freq from 3.825e9 to 3.925e9 in 5 MHz steps. Readout 1 stays relatively flat around 40 to 42 counts without a matching central feature. Readout 2 shows a strong, localized, repeatable drop around 3.875e9 to 3.880e9, falling from roughly 40 counts to about 32 counts in the combined data. The same depression appears in both per-average traces, so it is not just a single-average artifact. Because the dip is specific to the microwave-pulse signal readout and is localized in the frequency sweep, this is consistent with a pODMR resonance.
