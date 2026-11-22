#!/usr/bin/env python3
"""PreToolUse hook (Write|Edit|MultiEdit): runs `reason.py gate` on the future
content of a note in $KG_VAULT/graph/ before Claude writes it.

KG_GATE=warn (default, crawl) : warns Claude, never blocks.
KG_GATE=block (walk)          : refuses the write (exit 2) with the proof.
KG_GATE=off                   : escape hatch, logged.
Every decision is appended to $KG_VAULT/stats/gate-log.md.
Infra failure (no venv, crash, timeout) fails open: a broken gate never blocks you.
"""
import json
import os
import subprocess
import sys
import time
from pathlib import Path

VAULT = Path(os.environ.get("KG_VAULT", "/Users/asarazin/Documents/knowledge_glossary"))
MODE = os.environ.get("KG_GATE", "warn")


def future_content(tool, inp, path):
    if tool == "Write":
        return inp.get("content", "")
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    edits = inp.get("edits") if tool == "MultiEdit" else [inp]
    for e in edits:
        old, new = e.get("old_string", ""), e.get("new_string", "")
        text = text.replace(old, new) if e.get("replace_all") else text.replace(old, new, 1)
    return text


def log(session, verdict, note, detail=""):
    with open(VAULT / "stats" / "gate-log.md", "a", encoding="utf-8") as f:
        f.write(f"- {time.strftime('%Y-%m-%d %H:%M:%S')} · `{session[:8]}` · {MODE} · **{verdict}** · [[{note}]]\n")
        if detail:
            f.write("".join(f"    {line}\n" for line in detail.strip().splitlines()))


def main():
    event = json.load(sys.stdin)
    tool, inp = event.get("tool_name"), event.get("tool_input", {})
    path = Path(inp.get("file_path", "")).expanduser().resolve()
    if path.suffix != ".md" or path.parent != (VAULT / "graph").resolve():
        return
    session, note = event.get("session_id", "?"), path.stem
    if MODE == "off":
        return log(session, "contourné", note)

    try:
        r = subprocess.run(
            [str(VAULT / ".venv-gate/bin/python"), str(VAULT / "scripts/reason.py"), "gate",
             "--overlay", f"{note}={future_content(tool, inp, path)}"],
            capture_output=True, text=True, timeout=60)
    except Exception as e:
        return log(session, f"erreur ({e.__class__.__name__})", note)
    if r.returncode == 0:
        return log(session, "acceptée", note)
    if r.returncode != 2:
        return log(session, f"erreur (exit {r.returncode})", note, r.stderr[-500:])

    log(session, "refusée" if MODE == "block" else "avertie", note, r.stdout)
    msg = f"Garde-fou logique du PKG, note [[{note}]] :\n{r.stdout}"
    if MODE == "block":
        print(msg + "\nÉcriture refusée. Révise les relations (KG_GATE=off pour forcer, journalisé).",
              file=sys.stderr)
        sys.exit(2)
    print(json.dumps({
        "systemMessage": f"⚠ kg-gate (avertissement) : [[{note}]] introduit une incohérence logique.",
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "additionalContext": msg + "\n(Mode avertissement : l'écriture passe, mais corrige les relations.)",
        },
    }))


if __name__ == "__main__":
    main()
