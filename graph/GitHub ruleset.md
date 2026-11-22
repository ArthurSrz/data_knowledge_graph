---
dcterms:type: "Concept"
broader: "[[github]]"
description: "Set of rules GitHub enforces on a branch (e.g. main) before anything can land on it."
tags:
  - "github"
  - "governance"
timestamp: 2026-11-16T00:00:00+00:00
---
A ruleset is the "law" of a [[branch]]: no deletion, no force-push, merge only through a [[Pull request]], and a list of [[required status check]]s and/or a minimum number of [[pull request approval]]s.

Two independent gates can coexist: "N approvals" and "status X must be green". If the ruleset asks for 0 approvals but requires a status, approvals alone never unlock the merge — only whatever posts the status does.

**Example (equium-wiki, 2026-11-16):** ruleset `review-wiki` on `main` = 0 approvals + required status `relecture-croisee`. That is why two GitHub approvals did not unblock capture PRs.
