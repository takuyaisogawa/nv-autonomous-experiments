Sequence inspection:

The saved experiment uses Rabimodulated.xml while sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active variables show length_rabi_pulse = 52 ns and mod_depth = 1. The instructions first polarize and detect, then wait; because full_expt = 0, the optional 1-level reference block is skipped. The only active microwave manipulation before the second detection is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection.

Readout roles:

Readout 1 is the initial polarized detection/reference readout before the microwave pulse. Readout 2 is the post-Rabi-pulse signal detection. The pODMR contrast should therefore be judged primarily by whether readout 2 shows a frequency-dependent dip relative to readout 1, not by treating both traces as equivalent signals.

Data assessment:

The combined readout 2 trace drops sharply around 3.87 to 3.875 GHz, reaching about 31.2 counts while adjacent and low-frequency points are near 39 to 40 counts. Readout 1 does not show a comparable local dip at that point and remains near 40 to 41 counts before declining more gradually at higher frequency. The per-average overlay shows the readout 2 depression in both averages, with the same local contrast feature near the middle of the scan, so it is not just a single-average spike. This is consistent with a pODMR resonance being present.
