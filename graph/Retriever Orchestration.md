---
partOf: "[[Retrieval Augmented Generation]]"
relatedTo:
  - "[[Filtered vector search]]"
  - "[[Tool Assignment Gate]]"
broader: "[[RAG (Retrieval-Augmented Generation)]]"
inferred:skos:ancestor:
  - "[[Large Language Model]]"
  - "[[RAG (Retrieval-Augmented Generation)]]"
---

# Retriever Orchestration

A RAG architecture pattern where multiple retrieval tools are assigned to a single
agent, each with independent configuration. The agent routes queries to the
appropriate retriever based on tool descriptions and system prompt instructions.

## Why use multiple retrievers

Different document types benefit from different retrieval strategies:
- **Semantic chunks**: prose documents, contracts, reports
- **Structured objects**: KBIS sheets, forms, typed records
- **Checklist documents**: sequential items requiring full coverage

A single retriever with averaged settings will underperform on all types.
Dedicated retrievers, each tuned for their document type, allow the agent to
retrieve optimally across a heterogeneous knowledge base.

## Failure mode

If a retriever is not assigned to the agent, it is never called — regardless
of how well it is configured. See [[Tool Assignment Gate]].
