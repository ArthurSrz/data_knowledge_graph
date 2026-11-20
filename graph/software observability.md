---
wikidata entity id: Q115800581
skos:related:
  - "[[agent observability]]"
  - "[[tracing]]"
---
**Software observability**: ability to collect data about program execution.

For Clarifeye agents it comes from two records: [[langfuse]] traces (`conversation: <id>` → `conversation_turn` → `agent_llm_call` / `tool_execution`, tagged by surface and `project:<uuid>`) and the store's [[changelog]]. Gap seen in the mapping build: MCP calls appear only in `mcp_tool_calls`, not in Langfuse. [[agent observability]] is this applied to agents.
