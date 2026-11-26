---
dcterms:type: Case
kg:applied: "[[draft in one turn, build in one run]]"
kg:inSituation: "[[agent-generated deliverable in an organisation's brand]]"
kg:outcome: failure
kg:measuredBy: "[[end-to-end test]]"
kg:value: "4 builder errors before the template and its notes were fixed"
---
First build run against a freshly made template, before its notes had been tested with the builder. Four failures: the title put in the shape map was refused; labels left unfilled were emptied; table text came out white on white; the cover title overflowed.

Each failure became a template fix or a build rule in the notes (title in its own field, fill every shape, one text colour per table, shorter cover title), and a small [[end-to-end test]] now builds a sample deck and checks for placeholders and unreadable text. Lesson: a template is not done until the builder has used it.
