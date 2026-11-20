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

Clarifeye exposes its stores through an [[MCP server]] (`mcp_server/server.py`), so outside agents can read and write artifacts. In the mapping store, 52 edits came this way (`edit_source` "mcp"); they are not traced in [[langfuse]].
