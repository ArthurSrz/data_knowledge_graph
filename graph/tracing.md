---
skos:exactMatch: "wd:Q322229"
iso-thes:broaderGeneric:
  - "[[debugging]]"
  - "[[logging]]"
skos:broader: "[[software engineering]]"
skos:related:
  - "[[LLM Observability]]"
  - "[[langfuse]]"
---
a specialized form of [[logging]] that records a program's execution step by step. Each trace is a tree of [[observations]] (spans, generations, tool calls).

In [[LLM Observability]], a trace covers one conversation and each turn is a span. [[langfuse]] filters traces by `userId`, so one user's activity can be followed across conversations