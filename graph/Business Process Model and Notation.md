---
wikidata entity id: "Q1017605"
iso-thes:broaderInstantial: "[[notation]]"
iso-thes:broaderGeneric: "[[diagram]]"
depicts: "[[business rule]]"
publisher: "[[Object Management Group]]"
skos:broader: "[[diagram]]"
skos:altLabel:
  - "BPMN"
  - "Business Process Modeling Notation"
---
Graphical notation (OMG, 2004) for specifying a [[business process]]: pools and lanes for roles, tasks, gateways for decisions, events for triggers and outcomes. BPMN 2.0 XML is the exchange format SAP Signavio imports.

In a Clarifeye process store, the AS-IS Process artifact is a BPMN diagram; task attributes it cannot hold (A/C/I, systems, data objects) live in the [[responsibility assignment matrix]], keyed by element id.

**Notation vs rules:** change the BPMN only when the flow changes (tasks, gateways, lanes, events). A clarification that leaves the notation unchanged, such as how a type of entry is handled or where a system entry comes from, goes in the store's mapping rules as a [[business rule]], not in a task's documentation.

Principle: [[separation of concerns]].
