---
dcterms:type: "Concept"
skos:related:
  - "[[git]]"
  - "[[Pull request]]"
skos:scopeNote: "A situation that arises in git, not a kind of git: related, not broader."
skos:definition: "Two branches changed the same lines of a file; git cannot pick one version on its own."
tags:
  - "git"
  - "github"
---
A merge conflict happens when two branches started from the same commit and both edited the same lines of a file. The first [[Pull request]] merges without trouble. The others become conflicting, because their base no longer matches `main`.

Files where every branch adds a line at the same spot (an index, an append-only log) produce a conflict almost every time, even when the content has nothing in common.

Resolving a conflict rewrites the branch, so it creates a new commit. Any [[required status check]] posted on the old commit no longer covers it.

**Example:** five pull requests opened the same day all add a line to the same index and the same log file. The first one merges, the other four conflict. A branch that a human also edited by hand cannot simply be regenerated, because that would erase their edits.
