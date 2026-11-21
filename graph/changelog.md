---
wikidata entity id: Q255135
subclass of: "[[logbook]]"
skos:altLabel: ["change log", "knowledge changelog"]
inferred:skos:ancestor:
  - "[[logbook]]"
---
**Changelog**: log or record of all notable changes made to a project.

A Clarifeye store keeps one per store: each entry gives the artifact, its version number, the source of the edit (the agent, an MCP client or the UI), the user and the conversation it came from. That makes it the way to watch an [[AI agent]]: you can rebuild what Clara did in a session without reading the chat, then compare it with what the chat says it did. It is the store-level form of [[agent observability]] and of [[Version control]].

Each entry records one [[changeset]]. Taken together, they form the store's [[audit trail]] under [[change control]].
