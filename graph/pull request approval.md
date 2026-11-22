---
dcterms:type: "Concept"
skos:broader: "[[Pull request]]"
skos:definition: "A reviewer's \"Approve\" verdict on a pull request, as recorded by GitHub."
tags:
  - "github"
  - "code-review"
---
Each review has a state: APPROVED, CHANGES_REQUESTED, COMMENTED or DISMISSED. GitHub keeps only the **latest non-comment review per person**: a later comment does not cancel an approval, a later "Request changes" does, a dismissal removes it.

The author of a [[Pull request]] can never approve it. So a PR opened by a bot or shared token can be approved by everyone except that account.

Counting approvals yourself (outside the [[github ruleset]]) must reproduce this "latest per person" rule, otherwise one person approving twice counts as two.

**Example (equium-wiki):** `tools/approbations_github.py` applies exactly this rule to decide whether to turn the [[required status check]] `relecture-croisee` green.
