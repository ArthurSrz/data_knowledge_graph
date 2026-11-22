---
skos:exactMatch: "wd:Q907375"
skos:broader: "[[Test]]"
---
Test of one unit of code (a function, a rule) in isolation, with small hand-made inputs: fast, run on every change. The lowest level of the three described in [[end-to-end test]], below [[Integration tests]].

Good habit: a **positive control** (an injected error must be caught) and a **negative control** (a legitimate case must not be flagged), otherwise a test that never fires looks the same as a test that passes.

**Example (knowledge glossary, 2026-11-22):** `scripts/test_gate.py` builds a tiny two-class ontology in a temporary folder and checks each violation of the logic gate (cycle, S27, opposites, disjointness, instance/subclass crossing, part–whole cycle) with both controls. 8 unit tests run in about 8 s.
