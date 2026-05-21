I used inputs/sequence.xml as the sequence source. The active sequence is Rabimodulated with mw_freq swept from 3.825 GHz to 3.925 GHz. The active variables set sample_rate to 250 MHz, length_rabi_pulse to 5.2e-08 s, and mod_depth to 1. The pulse duration is already on the sample grid: 52 ns equals 13 samples at 250 MHz.

In the instruction flow, full_expt is 0, so the optional 1-level reference block is skipped. The two active detections are therefore:

1. Readout 1: the reference detection after adj_polarize, before the microwave pulse.
2. Readout 2: the signal detection after rabi_pulse_mod_wait_time using the 52 ns pulse at mod_depth 1.

For a pODMR resonance I would expect the post-pulse signal readout, or the contrast between signal and reference, to show a localized and repeatable frequency-dependent feature. The combined signal readout varies weakly and irregularly, and the signal-reference contrast changes sign across neighboring points. The largest apparent excursions are not reproducible between the two averages and are strongly affected by reference fluctuations, especially around 3.900 GHz. I therefore do not see a reliable pODMR resonance in this measurement.
