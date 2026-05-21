Sequence review:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional "Acquire 1 level reference" block is not active.
- readout 1 role: true 0-level reference acquired after polarization and detection before the microwave pulse.
- readout 2 role: signal readout after rabi_pulse_mod_wait_time using length_rabi_pulse.
- mod_depth: 1.
- pulse duration: length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s, i.e. 52 ns.

Data assessment:
The combined readouts and the two per-average traces are noisy over the scan. The post-pulse readout is generally offset below the initial reference, but there is no localized, repeatable dip or peak across the two averages that stands out as a pODMR resonance. Several extrema appear in only one readout or one average and are comparable to the point-to-point scatter. Because the expected resonance should be a coherent frequency-dependent feature in the signal/contrast rather than a broad noisy offset, I classify this case as resonance absent.
