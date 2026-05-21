Sequence and readout assessment:

The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The relevant variables are length_rabi_pulse = 5.2e-08 s, mod_depth = 1, and full_expt = 0. Because full_expt is zero, the optional 1-level reference block is not executed. The executed sequence is polarization, first detection, wait, modulated Rabi pulse, second detection, then final wait.

Readout roles:

Readout 1 is the true 0-level/reference fluorescence detection before the microwave pulse. Readout 2 is the fluorescence detection after the 52 ns rabi_pulse_mod_wait_time pulse with modulation depth 1.

Resonance decision:

The combined readouts both fluctuate at roughly the same scale as the per-average scatter. There is no clean, reproducible dip or peak in the post-pulse readout relative to the pre-pulse reference across the scan. Candidate local excursions, such as around 3.84 GHz or 3.89-3.90 GHz, are not stable across the two averages and are comparable to noise/baseline variation. I therefore do not identify a pODMR resonance in this dataset.
