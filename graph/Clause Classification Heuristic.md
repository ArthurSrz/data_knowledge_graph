---
subclass of:
  - "[[heuristic]]"
  - "[[Provenance]]"
uses:
  - "[[Bargaining power]]"
  - "[[de facto standard]]"
  - "[[categorization]]"
part of:
  - "[[pre-contractual phase]]"
outputs:
  - "[[boilerplate]]"
  - "[[model contract]]"
  - "[[bespoke]]"
related to:
  - "[[term sheet]]"
  - "[[negotiation]]"
broader: "[[clause]]"
inferred:skos:ancestor:
  - "[[Application development]]"
  - "[[Dialogue]]"
  - "[[Documentation]]"
  - "[[Process]]"
  - "[[Provenance]]"
  - "[[algorithm]]"
  - "[[clause]]"
  - "[[elicitation]]"
  - "[[heuristic]]"
---
The decision process a legal practitioner applies to assign a clause to a [[Provenance]] type. It is a [[heuristic]] — not an algorithm — because it relies on experience and tacit market knowledge rather than a computable rule.
## Two axes

**Axis 1 — Market practice signal**
Is this clause present verbatim in an institutional model (LMA, ISDA, ICC)? Does it appear with near-identical wording in the majority of comparable transactions? If yes → [[boilerplate]] or [[model contract]]. The relevant Wikidata concept is [[de facto standard]] (Q385853): a norm that holds dominant position by market acceptance, as opposed to a de jure standard imposed by law.

**Axis 2 — Bargaining power signal**
Do the parties have genuine room to negotiate this clause? Is there asymmetry in leverage that would prevent one side from pushing back? [[Bargaining power]] (Q2625018) is the relative ability to influence the counterparty. High leverage + deal-specific facts → [[bespoke]]. Low leverage or high switching cost → [[boilerplate]].

## The ambiguous zone
[[model contract]] sits at the intersection: the clause has institutional authority (market signal is present) but negotiation is still possible (bargaining power is non-zero). This is where most practitioner judgment is exercised and where the heuristic is hardest to formalise.

## Wikidata gap

No Wikidata node currently encodes this decision procedure for legal clause classification. The process is implied by the combination of Q5748245 + Q2625018 + Q385853 but has no dedicated QID. A candidate contribution: propose a node for "legal clause provenance classification" as a subclass of Q912550 (categorization).
