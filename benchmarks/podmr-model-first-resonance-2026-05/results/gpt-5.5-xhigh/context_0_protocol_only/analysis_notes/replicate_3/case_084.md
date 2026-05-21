Active sequence review:

- Sequence file: Rabimodulated.xml / Rabi-modulated microwave pulse sequence.
- Sweep variable: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "1 level reference" block is inactive.
- Active readouts:
  - readout 1 is the true 0-level/reference detection after laser polarization and before the microwave pulse.
  - readout 2 is the detection after the Rabi-modulated microwave pulse.
- mod_depth = 1 in the provided sequence XML variable values.
- length_rabi_pulse = 5.2e-08 s; at 250 MS/s this is already 13 samples, so the active microwave pulse duration is 52 ns.

Data assessment:

Both raw readouts show a broad downward drift across the high-frequency side of the scan, including the readout that is taken before the microwave pulse. A pODMR resonance should appear as a frequency-localized change in the post-pulse readout relative to the pre-pulse reference. The readout2/readout1 contrast has scattered negative points near 3.865, 3.885, and 3.905 GHz, but these are not a clean, reproducible resonance feature across the two averages, and the absolute depression is strongly entangled with baseline drift visible in readout 1. I therefore classify this scan as not showing a reliable pODMR resonance.
