Case: podmr_081_2026-05-17-110558

I used the provided sequence XML before deciding. The active sequence is
Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz
steps. The sequence first polarizes and takes a detection readout labeled in the
XML as the true 0 level reference. Because full_expt = 0, the optional 1 level
reference block is skipped. The sequence then applies
rabi_pulse_mod_wait_time using length_rabi_pulse = 52 ns and mod_depth = 1, then
takes the signal detection readout. Thus readout 1 is the 0-level reference and
readout 2 is the post-microwave signal readout.

The two averages have a large common brightness offset, so I compared the signal
readout against the reference readout rather than relying on absolute raw counts.
Both combined readouts share a broad downward drift across the scan. The
readout2/readout1 contrast has several isolated negative points, but they are
interleaved with positive points and do not form a coherent resonance line shape.
The candidate dips are not stable enough across the two averages to distinguish
them from point-to-point noise and drift.

Decision: resonance_absent.
