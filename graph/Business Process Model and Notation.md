---
skos:exactMatch: "wd:Q1017605"
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

## Splitting a shared role lane

A flow node sits in exactly one lane, so when one lane "Role (A or B)" must become two lanes (same work, different portfolio):
- duplicate the role's sequence in the new lane, with suffixed ids, keeping the original ids in the first lane so links from other diagrams survive;
- add an exclusive gateway after the start event that routes by the criterion ("which portfolio?"), documented as TO DEFINE when the routing rule is not written anywhere;
- keep partner lanes single (whoever receives a handover does the same work whatever its origin) and put a gateway "original portfolio?" on each flow that returns to the role, rather than duplicating the partners;
- ends of the flow that never return (an escalation handed over) need no gateway.
Then update the [[responsibility assignment matrix]] (rows per lane) and any text that describes the old single lane.
