---
dcterms:type: "Concept"
skos:broader: "[[git]]"
skos:related: "[[Pull request]]"
skos:definition: "Two branches changed the same lines of a file; git cannot pick one version on its own."
tags:
  - "git"
  - "github"
---
A merge conflict happens when two branches started from the same commit and both edited the same lines of a file. The first [[Pull request]] merges without trouble. The others become conflicting, because their base no longer matches `main`.

Files where every branch adds a line at the same spot (an index, an append-only log) produce a conflict almost every time, even when the content has nothing in common.

Resolving a conflict rewrites the branch, so it creates a new commit. Any [[required status check]] posted on the old commit no longer covers it.

**Example (equium-wiki, 2026-11-23):** five captures from the same author (#162–#166) all edit `index.md`, `log.md` and `DESP Categorie IV.md`. The first merge makes the other four conflict. The PRs where the author pushed his own fixes cannot be rebuilt automatically (label `conflit-manuel`).
