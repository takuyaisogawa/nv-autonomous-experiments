Active sequence: Rabimodulated.xml with mw_freq swept across the scan. The executed path polarizes the NV, performs an immediate detection as the no-MW reference, waits, skips the optional 1-level reference because full_expt = 0, then applies rabi_pulse_mod_wait_time with the active Rabi pulse and detects again. I therefore treat the first readout as the reference and the second readout as the MW-pulse signal.

The provided sequence uses mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. With the 250 MHz sample rate, the pulse is already aligned to 13 samples, so the active microwave pulse duration is 52 ns.

The raw readouts have common brightness drift, so I compared the second readout against the first rather than looking at either trace alone. The normalized signal/reference contrast is not flat: the MW-pulse signal is depressed relative to the reference near 3.855 GHz and again across the upper-middle portion of the sweep, especially around 3.885 to 3.895 GHz where the combined contrast reaches about 5 to 7 percent. The feature is noisy with only two averages, but the localized contrast deficits are consistent with a pODMR resonance being present.

Decision: resonance_present.
