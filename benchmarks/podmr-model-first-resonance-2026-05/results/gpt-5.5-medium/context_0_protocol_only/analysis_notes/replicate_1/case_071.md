Sequence and roles:
- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz.
- full_expt is 0, so the optional 1-level reference block is skipped.
- readout 1 is the initial detection after optical polarization, serving as the 0-level/reference readout.
- readout 2 is the detection after the rabi_pulse_mod_wait_time microwave pulse, serving as the signal readout for pODMR contrast.
- mod_depth is 1 from Variable_values, and length_rabi_pulse is 5.2e-08 s, i.e. 52 ns.

Assessment:
The raw readouts are noisy with only two averages, and there is no broad smooth ODMR lineshape across the full scan. However, the relevant contrast is the post-pulse signal relative to the pre-pulse reference. Around 3.910 GHz, readout 2 is lower than readout 1 in both averages, and the combined signal/reference ratio reaches a local minimum near that point. Neighboring points are mixed and the edge point at 3.925 GHz is also low, so the evidence is not strong, but the repeated local negative contrast near 3.91 GHz is enough to call a pODMR resonance present with low confidence.
