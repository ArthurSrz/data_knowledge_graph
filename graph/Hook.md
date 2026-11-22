---
wikidata entity id: Q1203383
skos:related:
  - "[[trigger]]"
  - "[[claude code]]"
skos:scopeNote: "Wikidata: hooking ⊂ software feature, a class not in the graph, so no hierarchical link here."
---
Point where a program lets you attach your own code, which then runs automatically when a given event happens (a [[trigger]]): before a [[commit]] ([[git]] hooks), before a tool call, at the end of a [[session]].

In [[claude code]], a hook is a shell command declared in `settings.json` for an event (`UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `Stop`…). Exit code 2 blocks the [[action]] and its message goes back to the [[agent]]; otherwise the hook can [[add]] [[context]].

**Example ([[knowledge]] glossary, 2026-11-22):** `kg-ground.py` injects [[graph]] [[context]] on every prompt; `kg-gate.py` refuses any note that would make the [[graph]] incoherent, with the proof chains, before [[Claude]] writes it.
