Case podmr_055_2026-05-17-045046.

The provided sequence XML is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active measurement path first polarizes the NV and performs a detection labeled in the sequence as the true 0 level reference. The optional 1 level reference block is inactive because full_expt is 0, so the adiabatic/rabi reference detection in that conditional block is skipped. The remaining active microwave operation is rabi_pulse_mod_wait_time followed by detection, so the two exported readouts correspond to the 0 level reference readout and the post-rabi-pulse signal readout.

The XML variables used for the active pulse give mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. With sample_rate = 250000000 samples/s, the rounded pulse duration remains 52 ns.

To decide on resonance presence, I compared the signal readout against the reference readout across the scan and checked whether the per-average traces support a localized reproducible contrast feature. The combined readout difference alternates sign several times, with apparent deviations at multiple unrelated frequencies rather than a coherent dip or peak. The per-average traces show large scatter and drift-like behavior; features in one average are not consistently reproduced in the other. I therefore do not see a reliable pODMR resonance in this isolated case.
