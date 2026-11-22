#!/usr/bin/env python3
"""Claude Code hook: runs `reason.py gate` (the single judge) on notes in $KG_VAULT/graph/.

PreToolUse (Write|Edit|MultiEdit): gates the future content of the note.
Stop: gates the whole session changeset (catches sed/scripts run via Bash),
      against the vault commit that existed when the session started — not HEAD,
      since Obsidian's auto-backup commits to main every few minutes.

KG_GATE=warn (default, crawl) : warns, never blocks.
KG_GATE=block (walk)          : refuses (PreToolUse exit 2 / Stop decision=block).
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

VAULT = Path(os.environ.get("KG_VAULT", "/Users/asarazin/Documents/pkg"))
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
        f.write(f"- {time.strftime('%Y-%m-%d %H:%M:%S')} · `{session[:8]}` · {MODE} · **{verdict}** · {note}\n")
        if detail:
            f.write("".join(f"    {line}\n" for line in detail.strip().splitlines()))


def run_gate(*args):
    return subprocess.run([str(VAULT / ".venv-gate/bin/python"), str(VAULT / "scripts/reason.py"),
                           "gate", *args], capture_output=True, text=True, timeout=60)


def git(*args):
    return subprocess.run(["git", "-C", str(VAULT), *args], capture_output=True, text=True).stdout.strip()


def pre_tool_use(event, session):
    tool, inp = event.get("tool_name"), event.get("tool_input", {})
    path = Path(inp.get("file_path", "")).expanduser().resolve()
    if path.suffix != ".md" or path.parent != (VAULT / "graph").resolve():
        return
    note = f"[[{path.stem}]]"
    if MODE == "off":
        return log(session, "contourné", note)
    r = run_gate("--overlay", f"{path.stem}={future_content(tool, inp, path)}")
    if r.returncode == 0:
        return log(session, "acceptée", note)
    if r.returncode != 2:
        return log(session, f"erreur (exit {r.returncode})", note, r.stderr[-500:])
    log(session, "refusée" if MODE == "block" else "avertie", note, r.stdout)
    msg = f"Garde-fou logique du PKG, note {note} :\n{r.stdout}"
    if MODE == "block":
        print(msg + "\nÉcriture refusée. Révise les relations (KG_GATE=off pour forcer, journalisé).",
              file=sys.stderr)
        sys.exit(2)
    print(json.dumps({
        "systemMessage": f"⚠ kg-gate (avertissement) : {note} introduit une incohérence logique.",
        "hookSpecificOutput": {"hookEventName": "PreToolUse", "additionalContext":
                               msg + "\n(Mode avertissement : l'écriture passe, mais corrige les relations.)"},
    }))


def stop(event, session):
    transcript = Path(event.get("transcript_path", ""))
    # ponytail: "touched the vault" = transcript mentions its path; cheap, skips other sessions' Stops
    if not transcript.is_file() or str(VAULT) not in transcript.read_text(errors="ignore"):
        return
    started = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(transcript.stat().st_birthtime))
    base = git("rev-list", "-1", f"--before={started}", "HEAD")
    if not base:
        return
    if not git("diff", "--name-only", base, "--", "graph/") and not git(
            "ls-files", "--others", "--exclude-standard", "graph/"):
        return
    if MODE == "off":
        return log(session, "contourné (Stop)", f"changeset depuis {base[:7]}")
    r = run_gate("--base", base)
    label = f"changeset depuis {base[:7]}"
    if r.returncode == 0:
        return log(session, "acceptée (Stop)", label)
    if r.returncode != 2:
        return log(session, f"erreur Stop (exit {r.returncode})", label, r.stderr[-500:])
    # stop_hook_active: we already blocked once this turn; don't loop forever if Claude can't fix it
    blocking = MODE == "block" and not event.get("stop_hook_active")
    log(session, "refusée (Stop)" if blocking else "avertie (Stop)", label, r.stdout)
    msg = f"Garde-fou logique du PKG, changeset de la session (depuis {base[:7]}) :\n{r.stdout}"
    if blocking:
        print(json.dumps({"decision": "block", "reason": msg + "\nRévise les relations avant de terminer."}))
    else:
        print(json.dumps({"systemMessage": "⚠ kg-gate (Stop) : la session laisse une incohérence logique "
                                           "dans le vault. Voir stats/gate-log.md."}))


def main():
    event = json.load(sys.stdin)
    session = event.get("session_id", "?")
    handler = stop if event.get("hook_event_name") == "Stop" else pre_tool_use
    try:
        handler(event, session)
    except subprocess.TimeoutExpired:
        log(session, "erreur (timeout)", event.get("hook_event_name", "?"))


if __name__ == "__main__":
    main()
