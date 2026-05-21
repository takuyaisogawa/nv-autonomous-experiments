Sequence inspection:
- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz.
- full_expt is 0, so the optional "1 level reference" block is skipped.
- Readout 1 is the initial detection after adj_polarize, serving as the bright/0-level reference.
- Readout 2 is the detection after the microwave Rabi pulse, serving as the driven signal readout.
- The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

Data assessment:
The two-average combined data show readout 2 tracking near readout 1 over much of the scan, then falling below the reference in the upper-frequency region. The most notable contrast is around 3.910-3.925 GHz, where readout 2 remains depressed while readout 1 stays near 49 counts. This produces a frequency-dependent signal/reference separation consistent with a weak pODMR resonance rather than only uncorrelated readout noise. The feature is broad and noisy with only two averages, so confidence should be limited, but the driven signal dip relative to the reference is sufficient to call a resonance present.
