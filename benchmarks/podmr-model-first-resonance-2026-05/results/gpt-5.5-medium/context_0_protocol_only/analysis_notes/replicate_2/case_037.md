Sequence review:
- Active sequence: Rabimodulated.xml, swept variable mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active microwave operation is rabi_pulse_mod_wait_time followed by detection.
- full_expt is 0, so the optional 1-level reference block is inactive.
- Readout roles from the instruction order: the first detection after adj_polarize is the true 0 level reference with no preceding microwave pulse; the later detection after rabi_pulse_mod_wait_time is the microwave-modulated signal readout.
- mod_depth is 1 in the provided sequence values, and length_rabi_pulse is 5.2e-08 s, i.e. 52 ns.

Data assessment:
The two combined raw readouts fluctuate over the scan but do not show a clear, localized, reproducible dip or peak consistent with a pODMR resonance. The per-average overlay shows strong average-to-average drift: one average trends downward at higher frequencies while the other trends upward, and this drift largely cancels in the combined traces. Because the apparent structure is not consistent between averages and the combined signal lacks a distinct resonance feature, I classify this case as resonance absent.
