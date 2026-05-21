Sequence inspection:

- Active sequence: Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the "Acquire 1 level reference" branch is skipped.
- The active readouts are therefore:
  - readout 1: detection immediately after optical polarization, the true 0-level/reference readout.
  - readout 2: detection after rabi_pulse_mod_wait_time using length_rabi_pulse and mod_depth, the microwave-applied signal readout.
- mod_depth is 1.
- length_rabi_pulse is 5.2e-08 s, i.e. 52 ns.

Data assessment:

For a pODMR resonance in this active sequence, the post-pulse signal readout should show a coherent frequency-localized change relative to the 0-level reference, typically a dark dip when the pulse transfers population out of the bright state. The combined readout2-readout1 contrast has isolated negative points near 3.830 GHz and 3.855 GHz, but these are single-point features rather than a consistent pulse-width-scale resonance. The same trace also has comparably large positive excursions, especially near 3.840 GHz and 3.910-3.915 GHz. The two per-average contrast traces do not show a stable shared resonance shape across the scan.

Decision:

I do not see a convincing pODMR resonance in this case. The frequency dependence is dominated by noisy point-to-point excursions rather than a coherent resonance feature.
