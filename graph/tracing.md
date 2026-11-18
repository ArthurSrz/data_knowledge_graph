---
wikidata entity id: Q322229
subclass of:
  - "[[debugging]]"
  - "[[logging]]"
facet of: "[[software engineering]]"
skos:related:
  - "[[LLM Observability]]"
  - "[[Langfuse]]"
---
a specialized form of [[logging]] that records a program's execution step by step. Each trace is a tree of [[observations]] (spans, generations, tool calls).

In [[LLM Observability]], a trace covers one conversation and each turn is a span. [[Langfuse]] filters traces by `userId`, so one user's activity can be followed across conversations