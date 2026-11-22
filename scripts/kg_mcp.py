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


@mcp.tool()
def kg_upsert_concept(name: str, frontmatter: str, body: str) -> str:
    """Create or replace a concept note, ONLY if it keeps the graph logically coherent.
    `frontmatter`: YAML relations without the --- fences (e.g. 'subclass of: "[[person]]"').
    The note is checked in memory by the logic gate (cycles, SKOS S27, opposites, disjointness,
    instance/subclass crossing, part-whole cycles); refused with the proof chains otherwise.
    Before any `subclass of`/`broader`: decide occurrent vs continuant."""
    import subprocess, time, yaml
    from reason import GRAPH_DIR, STATS_DIR, VAULT
    if not name.strip() or any(c in name for c in "/\\\0") or name.startswith("."):
        return f"Refusé : nom de note invalide {name!r}."
    try:
        if not isinstance(yaml.safe_load(frontmatter) or {}, dict):
            return "Refusé : le frontmatter doit être un mapping YAML."
    except yaml.YAMLError as e:
        return f"Refusé : frontmatter YAML invalide ({e})."
    text = f"---\n{frontmatter.strip()}\n---\n{body.strip()}\n"
    r = subprocess.run([str(VAULT / ".venv-gate/bin/python"), str(VAULT / "scripts/reason.py"), "gate",
                        "--overlay", f"{name}={text}"], capture_output=True, text=True, timeout=60)
    verdict = {0: "acceptée", 2: "refusée"}.get(r.returncode, f"erreur (exit {r.returncode})")
    with open(STATS_DIR / "gate-log.md", "a", encoding="utf-8") as f:
        f.write(f"- {time.strftime('%Y-%m-%d %H:%M:%S')} · `mcp` · upsert · **{verdict}** · [[{name}]]\n")
        if r.returncode == 2:
            f.write("".join(f"    {l}\n" for l in r.stdout.strip().splitlines()))
    if r.returncode != 0:
        return f"Non écrit ({verdict}).\n{r.stdout or r.stderr[-800:]}"
    (GRAPH_DIR / f"{name}.md").write_text(text, encoding="utf-8")
    return f"Écrit : graph/{name}.md\n{r.stdout}"


if __name__ == "__main__":
    mcp.run()
