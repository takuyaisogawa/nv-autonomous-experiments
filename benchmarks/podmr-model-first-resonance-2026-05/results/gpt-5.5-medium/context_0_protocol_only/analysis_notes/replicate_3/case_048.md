Active sequence assessment:

- Sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML instructions first polarize and detect a true 0-level reference.
- full_expt is 0, so the optional 1-level reference block is skipped even though do_adiabatic_inversion is true.
- The active microwave manipulation is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the final detection.
- Therefore readout 1 is the 0-level reference and readout 2 is the pulse-modulated measurement readout.

Data assessment:

The pulse readout does not show a stable, localized ODMR-like contrast feature relative to the reference. The two readouts cross and fluctuate over the scan, and the per-average overlays show that apparent excursions are not reproducible between the two averages. With only two averages and no consistent dip or peak tied to the pulsed readout contrast, the observed structure is better explained as noise/drift than a pODMR resonance.

Decision: resonance absent.
