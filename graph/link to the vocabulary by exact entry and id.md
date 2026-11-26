---
dcterms:type: Pattern
kg:appliesIn: "[[process capture for a BPM repository]]"
kg:achieves: "[[process models importable into the BPM repository]]"
role:vocabulary: "[[controlled vocabulary]]"
role:matching: "[[record linkage]]"
role:localName: "[[non-preferred term]]"
role:decider: "[[process owner]]"
kg:requiresRole:
  - "vocabulary"
  - "matching"
kg:hasCondition: "[[preferred term]]"
kg:hasLimitation: "[[sandbox]]"
---
Each model element is linked to the repository's vocabulary by writing the entry's exact title and its identifier, and the name used locally is kept as an alias. Matching runs on the title first, then on the identifier; a weak match is shown with its confidence and left to the [[process owner]], never applied silently. An element with no entry becomes a request (a proposed term in the [[sandbox]], or an IT system asked from [[enterprise architecture]]), not an invented entry.

Condition: a current export of the vocabulary is readable from the store.

Limitation: when the import tool drops structured extensions, the link must also be written in the element's documentation, where it survives; and a proposed term stays unusable until the vocabulary's own review cycle accepts it.
