# NV Research Knowledge Index

This is the public index for the reusable NV research knowledge used by
the project-execution agent.

The full live knowledge file is long and accumulates dated lessons. In this
release, full wake-local copies are preserved inside case wake records under
`cases/<case>/project/.manager/wake_records/*/md/`. This document
summarizes the current section map and the intended use of each section.

## Read Policy

Knowledge is not loaded wholesale into every wake. The agent first reads the
compact memory contract, project state, current advice, and evidence pointers.
It then reads only the knowledge sections relevant to the current decision.

This is the core memory/knowledge split:

- memory: compact startup contract and routing rules;
- knowledge: reusable experiment practice, dated lessons, and interpretation
  guidance.

## Sections

| Section | Strength | Used For |
| --- | --- | --- |
| `Shared Literature` | `DEFAULT` for practice, `PROVENANCE` for sources | Literature search, papers, DOI/arXiv/publisher pages, prior-result comparison, Hamiltonian/model interpretation, coupling extraction, old hardware assumptions. |
| `Experiment Defaults` | Mostly `DEFAULT`; caveats often `SOFT` | Sequence defaults, strong-pi/weak-pi pulsed ODMR, resonance validity, Rabi, CPMG/Hahn/XY8/DDRF, XML/protocol inspection, weak-signal follow-up. |
| `Drift, Tracking, And Environment` | Mostly `PROVENANCE` / `SOFT`; hard only for tracking loss, count collapse, safety uncertainty, or explicit stop conditions | Imaging, TrackCenter, usual NV/NV23 identity, nearby-NV recovery, position freshness, environment drift, count/tracking interpretation. |
| `Shot Budget And Data Quality` | `DEFAULT` analysis practice plus `SOFT` interpretation guidance | Shot credit, SEM scaling, stored averages, visual review, fit validity, snake scan, recent-average drift. |
| `Project Operation` | Hard for queue/verifier/execute/state handoffs; default for pacing and bridge-free work | Route policy, same-wake work, running-execute bridge-free work, project layout, advice inbox, verifier verdicts, canonical state, queue staging, completion markers. |
| `Research Practice And Closeout` | `DEFAULT` for synthesis and closeout | Literature/prior-result comparison, non-experiment findings that affect design, closeout reports, manual experiment evidence. |

## How The Agent Uses The Index

1. Read memory and current project state.
2. Identify the current decision: interpretation, measurement design,
   verification, closeout, or bridge-free analysis.
3. Select only the relevant knowledge sections.
4. Use knowledge as guidance and provenance, not as a substitute for current
   evidence.
5. Record which evidence, calculations, literature, or prior lessons affected
   the decision.
6. If the wake produces a reusable lesson, add a concise dated note to the
   relevant knowledge section.

## Public Copies

The case folders include wake-local copies of the memory and knowledge files
used during real project wakes. For example:

```text
cases/<case>/project/.manager/wake_records/<wake_id>/md/NV_RESEARCH_MEMORY.md
cases/<case>/project/.manager/wake_records/<wake_id>/md/NV_RESEARCH_KNOWLEDGE.md
```

Those files show what the agent could see at a particular wake. This index gives
the shorter reader-facing map.
