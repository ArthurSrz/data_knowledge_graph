---
subclassOf:
  - "[[agent]]"
usedIn:
  - "[[comparag]]"
aliases:
  - evaluator
  - random_picker
  - blind_folded_mechanism
broader: "[[agentic System]]"
inferred:skos:ancestor:
  - "[[agentic System]]"
---
The entity that selects which RAG [[tools]] to compare and judges the result. In CompaRAG, two agents act: 
1. the MCPDispatcher (selects [[tools]] via registry.pick_two())
2. the human user (votes on results). 

The [[agent]] does not change the goal — it selects the [[path]] and judges the [[outcome]].

We use this term to refer to the autonomous systems part inside comparag, performing autonomous actions 