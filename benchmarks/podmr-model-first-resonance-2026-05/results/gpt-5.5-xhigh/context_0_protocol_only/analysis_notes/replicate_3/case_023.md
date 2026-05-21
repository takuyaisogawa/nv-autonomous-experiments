Case: podmr_008_2026-05-16-014743

I used the provided sequence XML and the raw readout export for this case only.

Active sequence and timing:
- SequenceName is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML first performs adj_polarize, detection, and wait_for_awg. This makes readout 1 the true 0-level polarized reference readout.
- full_expt is 0, so the optional 1-level reference block is inactive and contributes no extra readout role.
- The active pODMR measurement pulse is rabi_pulse_mod_wait_time with length_rabi_pulse, mod_depth, and switch_delay, followed by detection. This makes readout 2 the post-pulse signal readout.
- mod_depth is 1 in the provided XML/variable values.
- length_rabi_pulse is 5.2e-08 s. At 250 MHz sample rate this is 13 samples, so the effective pulse duration is 52 ns.

Data assessment:
Readout 2 shows a localized and repeatable loss relative to readout 1 near 3.875-3.880 GHz. In the combined data the largest contrast occurs at 3.875 GHz, where readout 1 is 42.46 and readout 2 is 31.31, giving a delta of -11.15 and a ratio of 0.737. The same feature is present in both averages at 3.875 GHz: average 1 has delta -9.81 and average 2 has delta -12.50. Readout 1 itself remains near the neighboring baseline, so the feature is not a shared reference dropout.

Decision:
A pODMR resonance is present.
