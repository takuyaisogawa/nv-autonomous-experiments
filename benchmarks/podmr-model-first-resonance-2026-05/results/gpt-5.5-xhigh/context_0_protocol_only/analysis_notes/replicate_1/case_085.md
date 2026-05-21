Active sequence review:

- The provided sequence is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- sample_rate is 250 MHz, so length_rabi_pulse = 52 ns is already aligned to the 4 ns sample grid.
- mod_depth is 1 in the provided sequence/variable values.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped. do_adiabatic_inversion is not part of the active path.
- The active path is: polarize, detection, wait, modulated Rabi pulse, detection, final wait.

Readout roles:

- readout 1 is the true 0-level reference acquired immediately after optical polarization and before the microwave Rabi pulse.
- readout 2 is the post-pulse signal acquired after rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).

Resonance assessment:

For a pODMR resonance in this sequence, I expect a frequency-localized change in the post-pulse signal relative to the 0-level reference, preferably visible as a consistent dip or contrast feature across the scan/averages. The combined readouts mainly show slow drift plus point-to-point noise. The readout-2 minus readout-1 contrast alternates sign across neighboring points; the largest negative excursion is near 3.860 GHz, while a similarly large positive excursion appears nearby around 3.840-3.855 GHz. Other negative points are scattered rather than forming a clean resonance line. The per-average overlay also does not show a reproducible localized contrast feature shared by the averages.

Decision: resonance_absent.
