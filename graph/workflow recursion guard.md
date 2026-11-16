---
rdf:type: Concept
broader: "[[GitHub Actions]]"
description: GitHub's rule that actions performed with GITHUB_TOKEN do not trigger other workflows.
tags:
  - github
  - ci
  - pitfall
timestamp: 2026-11-16T00:00:00Z
inferred:skos:ancestor:
  - "[[GitHub Actions]]"
  - "[[Github]]"
---
To prevent infinite loops, a push, merge or PR event made with the automatic `GITHUB_TOKEN` of [[GitHub Actions]] fires **no** new workflow run (except `workflow_dispatch` / `repository_dispatch`).

Consequence: if a workflow merges a [[Pull request]] itself, every workflow listening to `push: main` (deploy, conflict rebuild…) silently stays idle.

**Example (equium-wiki, 2026-11-16):** the "2 approvals" workflow only posts the [[required status check]] and leaves the merge click to a human, so `reingest-on-conflict.yml` and `deploy-mcp.yml` still run after the merge.
