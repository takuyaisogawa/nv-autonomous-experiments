# Dataset Card

## Dataset

The benchmark contains 96 pODMR measurements from a single NV center workflow.
All cases use `Rabimodulated.xml` with a 100 MHz microwave-frequency sweep,
21 points, 5 MHz step, and two stored averages.

## Labels

Labels are constructed from the physical measurement configuration, not from
case-by-case visual inspection of each trace. Resonance-present cases were
measured on NV centers aligned with the static magnetic field, for which the
targeted `mS=0 -> +1` transition lies inside the scanned microwave-frequency
window. Resonance-absent cases were measured on NV centers with a different
crystallographic orientation, for which the corresponding transition is outside
the scanned window. Failed acquisitions, tracking failures, and records without
the intended raw pODMR measurement were excluded rather than labeled as
resonance absent.

The labels are used only for offline scoring and are not present in the
agent-visible input folder.

## Agent-Visible Inputs

Each case provides:

- a raw export JSON file
- a raw-readout diagnostic PNG with combined and per-average raw readouts
- embedded sequence XML and runtime variable values inside the raw export JSON
