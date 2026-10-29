# Memory And Knowledge

The agent stores operating instructions in `memory` and lessons from earlier
experiments in `knowledge`.

## Memory

Memory contains the instructions read at the start of each agent run. It
describes the agent's role, operating rules, safety constraints, project
selection, and how to find relevant knowledge sections.

Memory should stay small and stable. It is not meant to be a full laboratory
notebook.

## Knowledge

Knowledge contains lessons from previous runs, analysis methods, known failure
modes, and guidance for measurements. The agent is instructed to read only
the sections relevant to its current task.

## Updating the Documents

The agent is instructed to add reusable experimental lessons to knowledge
and rules that apply to every run to memory. An outdated lesson can be
corrected in knowledge without changing the operating instructions.

The case folders under `cases/<case>/project/` preserve records of these updates.

See also:

- `docs/nv_research_memory.md`
- `docs/nv_research_knowledge_index.md`
- `docs/nv_research_knowledge_excerpt.md`
