---
dcterms:type: "Concept"
skos:broader: "[[Test]]"
skos:definition: "A test that exercises the real system along the full path a user takes, with no mocks."
tags:
  - "testing"
---
Where [[Unit tests]] check one function in isolation and [[Integration tests]] check a few parts wired together, an end-to-end (E2E) test runs the real chain: real platform, real events, real permissions.

It catches what the other levels cannot see: configuration (rulesets, tokens, triggers), and assumptions about how the platform behaves.

Cost: slow, sometimes needs real humans or accounts, and must not pollute production (use throwaway data, cancel side effects).

**Example (equium-wiki, 2026-11-16):** throwaway PR #159 (empty commit on a `capture/…` branch): check it is BLOCKED → 2 colleagues click Approve → `relecture-croisee` turns green → the merge button works. Paired with 6 unit tests on the counting rule ([[pull request approval]]).

**Result (2026-11-16 16:49):** 1 approval → workflow "none 1/2", still BLOCKED; 2nd approval → status `success`, PR CLEAN → merged (44c62b8), and `push: main` workflows fired normally (see [[workflow recursion guard]]).
