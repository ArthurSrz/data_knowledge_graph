---
wikidata entity id: "Q133436854"
skos:altLabel:
  - "MCP"
compatible with:
  - "[[large language model]]"
---
**Model Context Protocol**: protocol for applications to provide context to LLMs.

Clarifeye exposes its stores through an [[MCP server]], so outside agents can read and write artifacts. Such edits are recorded in the store's [[changelog]] as MCP edits, but they are not traced in [[langfuse]].
