# Memory And Knowledge

The autonomous NV workflow separates `memory` and `knowledge` so that a
self-updating research agent can remain auditable as it accumulates experience.

## Memory

Memory is the compact wake-start contract. It describes the agent role, the
current operating rules, hard safety boundaries, project routing, and the index
for selecting relevant knowledge sections.

In practice, memory answers questions such as:

- What role is this wake running?
- Which project files must be read first?
- What boundaries are hard constraints?
- Which knowledge sections are likely relevant?
- What must be written before the wake is complete?

Memory should stay small and stable. It is not meant to be a full laboratory
notebook.

## Knowledge

Knowledge is the accumulated reusable research notebook. It contains lessons
from previous runs, analysis practices, known failure modes, measurement
patterns, and experiment-operation guidance that may help future project wakes.

Knowledge is read selectively. A wake should pull in only the sections that are
called for by the current project state, evidence, or memory index.

## Why This Split Matters

The split makes the system easier to inspect and safer to revise.

- Every wake starts from a compact, comparable contract.
- Old lessons do not silently dominate every new decision.
- A wrong or stale lesson can be corrected in knowledge without rewriting the
  wake contract.
- A new hard rule can be promoted into memory when it should apply to every
  wake.
- The difference between current operating rules and accumulated lessons is
  visible to reviewers.

For the research claim, this matters because the agent is not only running a
fixed script. It can update project artifacts and accumulate reusable
experimental knowledge, while the public record still shows where those updates
entered the loop.

## Update Pattern

The intended update pattern is:

1. Scheduler writes a wake record.
2. Agent reads memory, project brief, advice, state, and evidence pointers.
3. Agent reads selected knowledge sections only when relevant.
4. Agent performs analysis, writes an experiment intent, or closes out a branch.
5. Agent appends evidence and updates project state.
6. Reusable lessons go to knowledge; durable rules or routing changes go to
   memory.

This pattern is visible in the case folders under `cases/<case>/project/`.

See also:

- `docs/nv_research_memory.md`
- `docs/nv_research_knowledge_index.md`
- `docs/nv_research_knowledge_excerpt.md`
