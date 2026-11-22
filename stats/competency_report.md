# Competency Report

## Questions your graph can answer


### `broader` — 415 edges across 310 notes (strong)

- What is the parent domain of {X}?
- What are all subtypes of {X}?
- What is the full ancestor chain from {X} to the root?
- Which concepts are root concepts (no broader parent)?
- What concepts share the same parent domain as {X}?

### `depends_on` — 5 edges across 3 notes (weak)

- What are the dependencies of {X}?

### `has_use` — 13 edges across 11 notes (strong)

- What are the practical applications of {X}?

### `narrower` — 23 edges across 8 notes (strong)

- What are the direct children of {X}?

### `opposite_of` — 23 edges across 20 notes (strong)

- What is the opposite of {X}?

### `related` — 84 edges across 37 notes (strong)

- What concepts are semantically related to {X}?

### `studied_in` — 24 edges across 15 notes (strong)

- In what field is {X} studied?

### `uses` — 28 edges across 18 notes (strong)

- What tools or techniques does {X} use?
- Which concepts use {X}?

### Inferred predicates (via 24 Datalog rules)


**`ancestor`** — 830 derived facts

- Is {X} a (transitive) specialization of {Y}?
- What are all ancestors of {X} up to the root?

**`related_s`** — 164 derived facts

- What concepts are related to {X} (including symmetric)?

## User-defined competency questions


**9/21** answerable


### Answerable (9)

- [hierarchy] What is the parent domain of a given concept?
- [hierarchy] What are all the subtypes of a given concept?
- [hierarchy] What is the full ancestor chain from a concept up to a root?
- [hierarchy] Which concepts are root concepts (no broader parent)?
- [association] What concepts are semantically related to a given concept?
- [association] What is the opposite of a given concept?
- [dependency] What tools or techniques does a given concept use?
- [cross-cutting] Given an ML technique, what tools does it use and what domain is it part of?
- [cross-cutting] What concepts share the same parent domain?

### Not answerable (12)

- [dependency] What are the dependencies of a given concept?
  - **Gap**: depends_on (only 3 notes, need 5+)
- [dependency] What can a given concept be constructed with?
  - **Gap**: constructed_with (not found)
- [applicability] Which concepts are applicable in situation S (inherited by sub-situations)?
  - **Gap**: appliesIn (not found), broaderGeneric (not found), Situation (not found), Pattern (not found)
- [applicability] Under which conditions should C be used, and when should it be avoided?
  - **Gap**: hasCondition (not found), hasLimitation (not found)
- [combination] Which concepts does C combine with, and in which role?
  - **Gap**: role (not found), Pattern (not found)
- [success] Which combinations succeeded in S, and by which measure?
  - **Gap**: applied (not found), inSituation (not found), outcome (not found), measuredBy (not found), Case (not found)
- [provenance] What is the evidence, and how much trust does it deserve?
  - **Gap**: wasAttributedTo (not found), wasGeneratedBy (not found)
- [combination] What can replace C in a role (any kindOf the concept filling it)?
  - **Gap**: role (not found), broaderGeneric (not found)
- [success] What is missing to reach goal G (required role left unfilled)?
  - **Gap**: achieves (not found), requiresRole (not found), Goal (not found)
- [success] Which combinations failed, and why?
  - **Gap**: applied (not found), outcome (not found), hasLimitation (not found), Case (not found)
- [provenance] Who invented a given algorithm?
  - **Gap**: invented_by (not found)
- [provenance] When was a given concept first described?
  - **Gap**: first_described (not found)

## Coverage gaps


### Unused relation types

- `constructed_with`
- `contributing_factor`

### Thin coverage (<5 notes)

- `disjoint_with`: 2 edges across 2 notes
- `depends_on`: 5 edges across 3 notes
