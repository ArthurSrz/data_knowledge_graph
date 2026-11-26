---
dcterms:type: Situation
skos:related:
  - "[[document template]]"
  - "[[slide deck]]"
  - "[[agent]]"
---
An [[agent]] produces a client-facing [[slide deck]] (or another document) that must look like the organisation's own, without a designer in the loop.

Constraints:
- The agent sees only what the [[document template]] gives it: without a build file holding one sample slide per layout, plus notes mapping each shape to its content, it falls back on whatever template it has, often another organisation's.
- The builder clones sample slides and fills shapes by id: every text shape must be filled (one left out is emptied), and placeholder text must not survive.
- Brand rules (colours, fonts, footer, density) belong in the template notes, written so a renderer cannot hide them.
- Text must be short enough to fit: split a slide rather than shrink the font; tables have a row limit.
- Draft the content first and build once: each extra round with the agent costs the user minutes.
