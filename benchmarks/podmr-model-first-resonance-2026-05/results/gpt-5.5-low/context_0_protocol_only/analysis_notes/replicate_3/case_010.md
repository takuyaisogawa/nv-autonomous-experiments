Sequence/data review for podmr_017_2026-05-12-134151.

The provided sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to
3.925 GHz in 5 MHz steps. The active pulse sequence polarizes and detects a
true 0-level reference, waits, then applies rabi_pulse_mod_wait_time followed
by a detection. The conditional 1-level reference block is inactive because
full_expt = 0, so the relevant readout roles are:

- readout 1: initial reference after polarization, before the microwave pulse.
- readout 2: signal after the modulated Rabi microwave pulse.

The relevant pulse parameters are mod_depth = 1 and length_rabi_pulse = 52 ns
(rounded at 250 MS/s, still 52 ns). The sequence also has mw_freq swept and
freqIQ = 50 MHz.

The combined raw readouts are noisy and the signal readout does not form a
clear localized ODMR-like contrast feature against the reference. Readout 2 is
higher than readout 1 at several frequencies, lower at others, and the largest
excursions are not a consistent narrow dip or reproducible feature in the
per-average overlay. The per-average traces show substantial opposing drift
between averages, so apparent changes in the combined traces are not reliable
evidence of a resonance.

Decision: resonance_absent.
