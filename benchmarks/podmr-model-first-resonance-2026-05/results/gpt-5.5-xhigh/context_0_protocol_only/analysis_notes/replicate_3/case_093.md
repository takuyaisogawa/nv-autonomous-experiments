The sequence XML defines a Rabimodulated frequency scan with mw_freq varied from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active readout structure is:

- First detection: after adj_polarize, before the microwave pulse. This is the bright/0-level reference readout.
- The optional 1-level reference block is skipped because full_expt = 0, even though do_adiabatic_inversion is true in the variables.
- Second detection: after rabi_pulse_mod_wait_time using length_rabi_pulse = 5.2e-08 s and mod_depth = 1. This is the microwave-affected signal readout.

The pulse duration is 52 ns after sample-rate rounding at 250 MHz, and the modulation depth is full scale (1). A resonance should appear as a coherent frequency-dependent change in the post-pulse signal relative to the pre-pulse reference, most naturally a dip in readout 2 relative to readout 1.

The combined raw readouts fluctuate around 50 counts, with readout 1 mean about 50.72 and readout 2 mean about 50.78. The paired difference readout2 - readout1 has mean about +0.06 counts and a standard deviation about 1.26 counts. The largest negative contrast points, such as near 3.870 GHz and 3.905 GHz, are isolated rather than forming a smooth or repeatable resonance feature across neighboring frequency points. The per-average overlays also show substantial average-to-average offsets and point noise rather than a stable post-pulse depression tied to a single frequency.

Decision: resonance_absent. The active pODMR signal readout does not show a convincing resonance line shape above the observed readout fluctuations.
