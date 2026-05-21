Case podmr_066_2026-05-17-072831.

I used only inputs/sequence.xml, inputs/raw_export.json, and the provided raw readout plot. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The pulse program first performs polarization and detection for a true 0/reference readout, waits, then because full_expt is 0 it skips the optional 1-level reference block. It then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by the second detection. Thus the two readouts are reference-before-drive and signal-after-rabi-drive for the swept microwave frequency.

The relevant parameters are mod_depth = 1 and length_rabi_pulse = 5.2e-08 s, rounded at the 250 MHz sample rate, i.e. 52 ns. The sequence also has do_adiabatic_inversion enabled as a boolean, but that block is not active because the full_expt branch is skipped.

The combined raw readouts do not show a stable localized pODMR contrast feature. Readout 2, the post-pulse signal, trends upward across the scan and fluctuates, while readout 1 also fluctuates with a sharp high point near the upper side of the sweep. The per-average overlay shows large average-to-average offsets and no frequency-localized dip or peak reproduced consistently between averages. Any apparent excursions are comparable to the raw scatter and baseline drift rather than a coherent resonance.

Decision: resonance absent.
