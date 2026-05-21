Sequence XML and raw-export review for case podmr_030_2026-05-16-194429.

The active sequence is Rabimodulated.xml with mw_freq as the scanned variable. The scan runs from 3.825 GHz to 3.925 GHz in 5 MHz steps for 21 points. The XML sets mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. With the 250 MHz sample rate the pulse duration remains 52 ns after rounding.

Readout roles from the active XML:
- Readout 1 is the "true 0 level reference": adj_polarize, detection, then wait_for_awg.
- The optional "1 level reference" block is inactive because full_expt = 0, even though do_adiabatic_inversion is true.
- Readout 2 is the measurement after rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection.

I therefore compare readout 2 against readout 1 as the microwave-pulse signal relative to the pumped reference. The combined contrast r2 - r1 has its most negative point at 3.895 GHz: readout 1 = 52.577, readout 2 = 49.808, contrast = -2.769 counts or about -5.27 percent. The adjacent 3.900 GHz point is also negative, and both individual averages have negative contrast at 3.895 GHz (about -6.56 percent and -3.74 percent). There are noisy point-to-point fluctuations elsewhere, but the 3.895 GHz dip is the clearest frequency-localized microwave-dependent feature in the normalized readout comparison.

Decision: resonance_present. The evidence is modest rather than high-SNR, but the correct readout comparison shows a repeatable negative contrast feature at the scanned pulse frequency.
