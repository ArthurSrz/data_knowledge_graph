---
partOf: "[[Retrieval Augmented Generation]]"
relatedTo:
  - "[[Retriever Orchestration]]"
  - "[[Filtered vector search]]"
broader: "[[RAG (Retrieval-Augmented Generation)]]"
inferred:skos:ancestor:
  - "[[Language modeling]]"
  - "[[Large Language Model]]"
  - "[[RAG (Retrieval-Augmented Generation)]]"
---

# Retrieval Depth

The number of chunks or objects a retriever returns per query, controlled by
the `n_objects` parameter. Acts as a coverage ceiling: if the document requires
more chunks than `n_objects` allows, the excess is silently dropped.

## Calibrating n_objects

Match `n_objects` to the expected document length and query breadth:
- Short focused queries on dense docs: 5–10 sufficient
- Full checklist or multi-section document coverage: 20–30+

Setting `force_n_objects: true` returns exactly n results even when fewer
match — useful for debugging but can introduce low-quality padding.

## Interaction with reranking

High `n_objects` + `rerank: true` is a common pattern: retrieve broadly,
then let the reranker surface the most relevant subset. This avoids the
coverage loss of a low `n_objects` ceiling while maintaining output quality.
