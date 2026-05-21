Sequence review:
- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz.
- full_expt is 0, so the conditional "Acquire 1 level reference" block is not active.
- Readout 1 is the true 0-level reference acquired immediately after optical polarization.
- Readout 2 is acquired after the active rabi_pulse_mod_wait_time block.
- The active pulse uses length_rabi_pulse = 52 ns and mod_depth = 1, with switch_delay = 100 ns.

Data assessment:
Readout 1 stays near the high-30s to low-40s without a matching central dip. Readout 2 shows a pronounced, localized reduction around 3.875-3.880 GHz, dropping to about 31 raw counts while neighboring points recover toward the high-30s. The dip is visible in the combined trace and is repeated in both per-average traces, so it is not just a single-average artifact. Because the dip occurs in the post-pulse signal readout while the reference readout does not show the same feature, this is consistent with a pODMR resonance.

Decision: resonance_present.
