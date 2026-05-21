Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence XML has full_expt = 0, so the optional 1-level reference block is inactive. The two active detections are:

- readout 1: initial polarize/detect 0-level reference before the swept microwave pulse.
- readout 2: detection after rabi_pulse_mod_wait_time using length_rabi_pulse.

The active pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on). With sample_rate = 250 MHz and length_rabi_pulse = 5.2e-08 s, the pulse is 52 ns (13 samples). The provided sequence XML gives mod_depth = 1.

The combined readout 2 trace has a clear local minimum at about 3.910 GHz: it drops to about 50.9 counts while adjacent points are about 53.9 and 53.7. Readout 1 does not show a corresponding dip at that frequency. In the per-average data, the same point is low in the MW-applied readout for both averages relative to nearby points, so this is more consistent with an ODMR contrast feature than a shared reference fluctuation.

Decision: resonance_present.
