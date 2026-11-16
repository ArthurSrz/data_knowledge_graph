---
rdf:type: Concept
broader: "[[Github]]"
partOf: "[[GitHub ruleset]]"
description: A named green/red light on a commit that a ruleset demands before merge.
tags:
  - github
  - ci
timestamp: 2026-11-16T00:00:00Z
inferred:skos:ancestor:
  - "[[Github]]"
---
A commit status is a small label (`context`, `state` = success / pending / failure, `description`) attached to one commit SHA through the GitHub API. Anyone with the right token can post it — a [[GitHub Actions]] workflow, an external server, a bot.

A *required* status check is a context the [[GitHub ruleset]] insists must be `success` on the PR's latest commit. It is a contract on a **name**, not on who computes it: several producers can post the same context, each encoding a different path to "OK".

Pitfall: the status is tied to a SHA. A new push = new commit = the light disappears until someone posts it again.

**Example (equium-wiki):** `relecture-croisee` is posted by three producers — the MCP server after mail validation, `relecture-hors-capture.yml` for non-capture PRs, and since 2026-11-16 `relecture-approbations-github.yml` after 2 [[pull request approval]]s.
