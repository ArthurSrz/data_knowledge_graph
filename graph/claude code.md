---
wikidata entity id: Q138457287
instance of: "[[agent harness]]"
skos:scopeNote: "Wikidata: instance of agent harness (and of command-line interface). An individual tool, so `instance of`, not `subclass of`; the older broader → [[agentic System]] link was dropped for that reason."
inferred:skos:related:
  - "[[hook]]"
---
Anthropic's coding agent, used from the terminal, IDEs, the desktop app and the web. It reads and edits files, runs commands and calls tools ([[MCP server]]s), inside a harness that the user configures: [[claude.md]] files for rules, [[skills]] for packaged procedures, and [[hook]]s for automatic checks.

Its settings follow the same levels as `CLAUDE.md`: organization, user, project, local. A setting at the user level applies to every session, whatever folder it is opened in.

**Example (knowledge glossary, 2026-11-22):** a user-level `PreToolUse` hook runs the logic gate before any Claude Code session writes a note to the vault, and a `Stop` hook checks the whole session's changes.
