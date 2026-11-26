---
dcterms:type: Pattern
kg:appliesIn: "[[agent-generated deliverable in an organisation's brand]]"
kg:achieves: "[[on-brand deliverable in two exchanges]]"
role:template: "[[document template]]"
role:output: "[[slide deck]]"
role:builder: "[[agent]]"
kg:requiresRole:
  - "template"
  - "builder"
kg:hasCondition: "[[document template]]"
kg:hasLimitation: "[[draft document]]"
---
The agent writes the text of every slide in one reply, in deck order and tagged with the layout each will use, and ends with a single question (« go, or corrections? »). After one round of corrections it builds the file in one run from the template, then checks that no placeholder is left.

Condition: the [[document template]] is in the store and its notes map each layout to its shapes; without that, the build step guesses and the second exchange becomes five.

Limitation: the user reviews text, not the rendered slides, so overflow and layout problems appear only after the build; keep the text short in the draft to compensate.
