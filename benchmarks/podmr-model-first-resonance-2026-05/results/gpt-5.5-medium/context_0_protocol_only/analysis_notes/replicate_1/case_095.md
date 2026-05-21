Active sequence inspection:

- Sequence: Rabimodulated.xml.
- The XML sets full_expt = 0, so the optional 1-level reference branch is not active.
- The active detections are therefore:
  - readout 1: true 0-level/reference readout after optical polarization and before the microwave pulse.
  - readout 2: signal readout after the modulated Rabi microwave pulse.
- mod_depth = 1.
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns.

Data assessment:

The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. A pODMR resonance should appear as a frequency-localized reduction in the post-pulse signal relative to the reference, ideally persisting over neighboring scan points and being reasonably consistent between averages.

The raw readouts show a slow downward drift in both channels across the scan, and the signal/reference contrast alternates between positive and negative excursions. The strongest negative contrast points are isolated or not consistently supported by both averages; adjacent points often rebound or change sign. The per-average traces also have a large offset between averages, indicating that much of the structure is average-to-average baseline variation rather than a stable spectral feature.

Decision: no clear pODMR resonance is present in this scan.
