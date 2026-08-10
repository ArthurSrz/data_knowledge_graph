---
partOf: "[[Retriever Orchestration]]"
failureMode: "[[Tool Assignment Gate]]"
relatedTo: "[[Filtered vector search]]"
broader: "[[agentic System]]"
inferred:skos:ancestor: "[[agentic System]]"
---

# Tool Assignment Gate

The first gate in a multi-retriever RAG pipeline: a retrieval tool must be
explicitly assigned to an agent before it can be called. An unassigned tool
is invisible to the agent at inference time.

## Why this matters

Tool assignment failures are silent — the agent produces output using only
the tools it has, with no indication that other tools exist. This makes
coverage gaps hard to diagnose: the output looks complete but is missing
entire document classes.

## Relationship to other gates

| Gate | Type | Effect |
|------|------|--------|
| Tool Assignment Gate | Hard | Unassigned tool never runs |
| [[Filtered vector search]] pre-filter | Hard | Wrong tag → zero results |
| Reranking | Soft | Ranks results, never excludes |

Fix: verify tool assignment before tuning retrieval parameters.
