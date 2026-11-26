---
dcterms:type: Pattern
kg:appliesIn: "[[new user blocked from a shared workspace]]"
kg:achieves: "[[access granted without a detour through IT]]"
role:mechanism: "[[access control]]"
role:channel: "[[draft document]]"
kg:requiresRole:
  - "mechanism"
kg:hasCondition: "[[access control]]"
kg:hasLimitation: "[[change management]]"
---
First check whether the blocked user was invited to that workspace; the usual cause is a missing membership, not a security rule. Reply in a few lines: why the link fails, that an invitation is enough on the vendor's side, and ask whether the client's policy requires IT approval for a new tool. Invite only after the account owner agrees; go through IT only if the client confirms its policy requires it.

Condition: someone on the vendor side has the rights to invite users to the workspace.

Limitation: the vendor cannot see the client's policy (single sign-on, procurement rules); if the client says IT is mandatory, the invitation route is closed and the delay is the client's [[change management]] process.
