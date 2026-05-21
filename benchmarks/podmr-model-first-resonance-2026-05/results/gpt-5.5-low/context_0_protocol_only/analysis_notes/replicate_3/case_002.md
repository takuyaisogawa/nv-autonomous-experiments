Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Relevant XML/run settings:
- length_rabi_pulse: 52 ns
- mod_depth: 1 from the run variable values
- full_expt: 0, so the conditional 1-level reference block is inactive
- active readouts are the initial post-polarization true-0 reference detection and the final detection after the Rabi-modulated microwave pulse

Readout interpretation:
- readout 1 is the reference-like detection before the scanned pulse effect and is comparatively flat/noisy.
- readout 2 is the post-pulse signal readout and shows a clear fluorescence decrease near the middle of the scan, reaching its minimum around 3.875-3.880 GHz before recovering near 3.890 GHz.

Decision:
The post-pulse readout has a coherent dip relative to neighboring frequencies and relative to the reference behavior, consistent with a pODMR resonance being present.
