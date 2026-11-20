---
rdf:type: Concept
broader: "[[github]]"
partOf: "[[automation framework]]"
description: GitHub's built-in CI/automation runner — YAML workflows launched by repository events.
tags:
  - github
  - ci
  - automation
timestamp: 2026-11-16T00:00:00Z
inferred:skos:ancestor:
  - "[[github]]"
inferred:skos:narrower:
  - "[[workflow recursion guard]]"
---
A workflow is a YAML file in `.github/workflows/` with an `on:` block listing the [[trigger]]s (push, pull_request, pull_request_review, schedule, manual dispatch…) and jobs that run shell steps on a fresh machine.

Each run receives a short-lived `GITHUB_TOKEN` whose rights are set by `permissions:` (e.g. `statuses: write` to post a [[required status check]]).

Security habit: when a workflow runs code from the repo on behalf of a PR, check out the **base** branch (trusted) rather than the PR branch, so the PR cannot rewrite the rule that judges it.

See also [[workflow recursion guard]].
