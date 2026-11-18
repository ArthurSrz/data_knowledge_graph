#!/usr/bin/env python3
"""MCP server exposing the personal knowledge graph (mini GraphRAG). Stdio transport."""
from mcp.server.fastmcp import FastMCP

import kg_rag

mcp = FastMCP("pkg")


@mcp.tool()
def kg_retrieve(query: str, k: int = 3, hops: int = 1) -> str:
    """GraphRAG over Arthur's personal knowledge graph: finds the k most relevant concept notes
    (name, aliases, body) and returns their typed relations, backlinks, body excerpt and n-hop
    neighbourhood. Call this BEFORE answering any conceptual question, to use Arthur's own
    definitions and vocabulary. Empty result = concept is 'hors graphe'."""
    return kg_rag.retrieve(query, k, hops) or "Aucun concept trouvé : hors graphe."


@mcp.tool()
def kg_concept(name: str) -> str:
    """Full note for one concept (exact file name, case-insensitive): frontmatter relations,
    backlinks and whole body."""
    notes = kg_rag.load()
    real = {n.lower(): n for n in notes}.get(name.lower())
    if not real:
        hits = kg_rag.search(name, 5, notes)
        return f"'{name}' hors graphe. Candidats proches : " + ", ".join(hits) if hits else f"'{name}' hors graphe."
    return kg_rag.render(notes[real], excerpt=20000)


@mcp.tool()
def kg_neighbors(name: str, depth: int = 1) -> str:
    """Typed edges around a concept up to `depth` hops, both directions (broader, subclass of,
    skos:*, inferred:skos:*…)."""
    return kg_rag.neighbors(name, depth)


@mcp.tool()
def kg_search(query: str, k: int = 10) -> str:
    """Ranked list of concept names matching a query (names, aliases, bodies)."""
    return "\n".join(kg_rag.search(query, k)) or "Aucun résultat."


if __name__ == "__main__":
    mcp.run()
