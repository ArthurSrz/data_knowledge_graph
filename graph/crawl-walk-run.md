---
broader: "[[process]]"
skos:related:
  - "[[Deployment]]"
  - "[[human-in-the-loop]]"
skos:scopeNote: "Not in Wikidata. Read here as a staged process (occurrent); strictly, the plan describing the stages would be a continuant."
inferred:skos:ancestor:
  - "[[occurrent]]"
  - "[[process]]"
---
Staged way to bring in something new: **crawl** (observe without consequences), **walk** (enforce on a limited scope), **run** (automate everywhere). Each stage only starts once the previous one has shown it can be trusted.

It is the [[Deployment]] form of [[human-in-the-loop]]: people judge the system's verdicts before it is allowed to act on its own.

**Example (knowledge glossary, 2026-11-22):** the logic gate first only *warned* Claude (crawl, verdicts logged in `stats/gate-log.md`), then *refused* incoherent writes (walk, `KG_GATE=block`), then validated writes from the MCP tool and the CI (run).
