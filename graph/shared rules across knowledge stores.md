---
dcterms:type: Situation
skos:related:
  - "[[knowledge base]]"
  - "[[single source of truth]]"
  - "[[skills]]"
  - "[[clarifeye]]"
---
Several [[knowledge base]]s run the same method on different topics (one store per process, for instance), and the method's rules, templates and reference vocabulary are kept in one master store that the others link to read-only.

Constraints:
- The rules must stay a [[single source of truth]]: a reusable instruction (a skill) reads them live from the master store instead of copying them, or the copies drift.
- A linked store exposes only what is shared: its search, not necessarily its tools or its templates. Assets such as a design template must be added to each store explicitly; being organisation-wide does not make them visible by default.
- Reading through a link is slower than reading locally: a task that consults the master often needs the master's navigation tools shared too.
- A finding made in one store (a missing rule, a vocabulary gap) belongs in the master, where every store benefits.
