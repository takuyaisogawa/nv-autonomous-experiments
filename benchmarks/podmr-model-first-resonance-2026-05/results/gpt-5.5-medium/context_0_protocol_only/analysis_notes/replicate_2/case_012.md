Case podmr_030_2026-05-13-160024.

I used inputs/sequence.xml as the sequence source. The active sequence is Rabimodulated.xml / Rabimodulated, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The microwave is applied with a modulated Rabi pulse:

- sample_rate: 250 MHz
- mw_freq variable: swept by the scan
- detuning: 0
- freqIQ: 50 MHz
- length_rabi_pulse: 52 ns, rounded to the sample clock
- mod_depth: 1
- mw_ampl: -5 dBm
- ampIQ: 5 dBm
- full_expt: 0
- do_adiabatic_inversion: true, but the adiabatic/full-experiment branch is skipped because full_expt is zero

Readout roles from the instruction order:

1. The first detection occurs after adj_polarize and is the true 0-level / bright reference readout.
2. The optional 1-level reference block is skipped because full_expt = 0.
3. The second active detection occurs after rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, so it is the microwave-pulse signal readout.

Decision:

The combined raw readouts do not show a convincing pODMR resonance. The two readouts are noisy and their difference changes sign repeatedly across the frequency sweep, with large excursions at several unrelated points rather than a localized, reproducible dip or peak. The per-average overlay also shows substantial average-to-average variation, so the apparent extrema are not stable enough to call a resonance.

Prediction: resonance_absent.
