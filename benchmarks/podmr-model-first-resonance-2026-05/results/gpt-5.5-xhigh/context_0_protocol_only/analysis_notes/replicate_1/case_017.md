Active sequence: Rabimodulated.xml with mw_freq swept from 3.825 to 3.925 GHz. The provided sequence XML has full_expt = 0, so the optional 1-level reference branch is inactive. The active acquisitions are:

- First detection after polarization: true 0-level/bright reference readout.
- Second detection after rabi_pulse_mod_wait_time: microwave-pulsed signal readout.

The active XML values used for the pulse are mod_depth = 1 and length_rabi_pulse = 5.2e-08 s, i.e. 52 ns. At the 250 MS/s sample rate this remains 52 ns after sample-grid rounding.

Decision: pODMR resonance is present. The microwave-pulsed readout has a pronounced and repeatable fluorescence dip centered near 3.875-3.880 GHz, dropping from the mid/high 30s to about 27 counts in the combined trace. The reference readout does not show a matching dip there, and both averages show the pulsed-readout depression in the same frequency region, supporting a real resonance rather than isolated scan noise.
