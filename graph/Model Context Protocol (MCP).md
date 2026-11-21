---
wikidata entity id: Q133436854
skos:altLabel: ["MCP"]
compatible with:
  - "[[large language model]]"
inferred:skos:narrower:
  - "[[MCP host]]"
  - "[[MCP server]]"
---
**Model Context Protocol**: protocol for applications to provide context to LLMs.

Clarifeye exposes its stores through an [[MCP server]] (`mcp_server/server.py`), so outside agents can read and write artifacts. Such edits are recorded in the store's [[changelog]] with `edit_source` "mcp", but they are not traced in [[langfuse]].
