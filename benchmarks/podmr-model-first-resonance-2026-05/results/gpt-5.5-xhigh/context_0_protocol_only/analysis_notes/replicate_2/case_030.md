Sequence context:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to
3.925 GHz. The XML sets full_expt = 0, so the optional 1-level reference block is
not active. The acquired readouts are therefore:

- readout 1: true 0-level reference, acquired after optical polarization and
  before the microwave test pulse.
- readout 2: signal readout after rabi_pulse_mod_wait_time with the swept
  microwave frequency.

The active modulation depth is mod_depth = 1. The rabi pulse duration is
length_rabi_pulse = 52 ns; at the 250 MHz sample rate this is exactly 13 samples,
so the rounded duration remains 52 ns.

Data interpretation:

The reference readout remains relatively flat across the sweep, while the
post-pulse readout has a pronounced, localized dip around 3.875 GHz. The dip is
visible in the combined averages and is supported by the per-average overlay,
with readout 2 falling well below its neighboring baseline points and below the
reference. For this Rabimodulated pODMR sequence, that frequency-localized loss
in the post-microwave readout indicates an ODMR resonance.

Decision: resonance_present.
