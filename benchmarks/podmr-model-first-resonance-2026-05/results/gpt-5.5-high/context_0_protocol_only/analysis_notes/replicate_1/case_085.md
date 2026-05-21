Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

From the provided sequence XML, full_expt is 0, so the optional 1-level reference block is inactive. The executed readouts are therefore:
- readout 1: detection immediately after adj_polarize, serving as the polarized/0-level reference before the microwave Rabi pulse.
- readout 2: detection after rabi_pulse_mod_wait_time, serving as the microwave-affected pODMR readout.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns. The XML variable mod_depth is 1.

The raw readouts mostly share a broad upward drift across the scan. The relative contrast between the post-pulse readout and the reference readout alternates sign across neighboring frequency points, with positive and negative excursions of similar size and an average difference near zero. There is no stable, frequency-localized dip or peak that stands out from the two-average scatter. The apparent fluctuations around 3.85-3.90 GHz are not coherent enough to identify a pODMR resonance.

Decision: resonance absent.
