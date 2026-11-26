---
dcterms:type: Pattern
kg:appliesIn: "[[interview campaign run by an AI interviewer]]"
kg:achieves: "[[interview guide that improves after each interview]]"
role:interviewer: "[[agent]]"
role:framing: "[[brief]]"
role:guide: "[[interview guide]]"
role:memory: "[[artifact]]"
kg:requiresRole:
  - "interviewer"
  - "framing"
  - "memory"
kg:hasCondition: "[[brief]]"
kg:hasLimitation: "[[access control]]"
---
One conversation per task. Before each interview, build its [[brief]] from the guide and validate it explicitly; the AI agent joins only interviews marked as prepared. Tell the call's host in advance that an AI interviewer will join. After the interview, analyse it (technique, unanswered questions) and carry the result back into the [[interview guide]]. Keep the guide, its profile variants, its short version (derived from the full one, never rewritten) and one sheet per interview as [[artifact]]s, so each new conversation starts from them.

Condition: the brief can be validated before the meeting starts; a brief prepared but never confirmed is as good as none.

Limitation: the agent is a guest in someone else's call; if the host removes it or the meeting platform blocks bots, the interview is lost and must be run or recorded by a person.
