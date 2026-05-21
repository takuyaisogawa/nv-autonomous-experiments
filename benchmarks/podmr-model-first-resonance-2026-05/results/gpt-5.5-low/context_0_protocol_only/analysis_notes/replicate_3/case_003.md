Active sequence and parameters:

- SequenceName is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active microwave pulse is rabi_pulse_mod_wait_time using length_rabi_pulse = 52 ns and mod_depth = 1.
- full_expt = 0, so the optional 1-level reference block is skipped even though do_adiabatic_inversion is true.
- Readout 1 is the initial true 0-level reference after polarization and before the swept Rabi pulse.
- Readout 2 is the final signal readout after the swept modulated 52 ns Rabi pulse.

Assessment:

The final signal readout shows a pronounced dip around 3.875-3.880 GHz, reaching about 40.5 counts for two adjacent scan points. The same feature is present in both averages and is substantially deeper in the signal readout than in the initial reference readout, which has only a smaller single-point depression nearby. This behavior is consistent with a pODMR resonance being present.
