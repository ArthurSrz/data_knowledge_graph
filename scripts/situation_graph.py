"""Build site/patterns.json for the Situation Graph (GitHub Pages) from the Pattern notes in graph/.

Usage: python scripts/situation_graph.py [out.json]   (default: site/patterns.json)
The repo is the database: every push to graph/ rebuilds the JSON (.github/workflows/situation-graph.yml).
"""
import json, os, re, sys
from pathlib import Path
PKG = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PKG / 'scripts'))
from reason import extract_frontmatter, parse_targets

notes = {p.stem: p.read_text() for p in (PKG / 'graph').glob('*.md')}
fm = {k: extract_frontmatter(t) or {} for k, t in notes.items()}
body = lambda t: re.sub(r'^---\n.*?\n---\n?', '', t, flags=re.S).strip()

pats = []
for name, f in fm.items():
    if f.get('dcterms:type') != 'Pattern':
        continue
    text = body(notes[name])
    method, _, cond = text.partition('Condition:')
    pats.append({
        'name': name,
        'situation': (parse_targets(f.get('kg:appliesIn')) or [None])[0],
        'goal': (parse_targets(f.get('kg:achieves')) or [None])[0],
        'roles': {k[5:]: parse_targets(v)[0] for k, v in f.items() if k.startswith('role:') and parse_targets(v)},
        'required': f.get('kg:requiresRole') or [],
        'condition': parse_targets(f.get('kg:hasCondition')),
        'limitation': parse_targets(f.get('kg:hasLimitation')),
        'steps': [s.strip() for s in re.split(r'(?<=[.;])\s+(?=[A-Z«])', method.strip().replace('\n', ' ')) if s.strip()],
        'conditionText': cond.strip(),
    })

touched = {c for p in pats for c in list(p['roles'].values()) + p['condition'] + p['limitation']}
rel = []
for a in touched:
    for k, v in fm.get(a, {}).items():
        if k.startswith(('skos:', 'iso-thes:', 'kg:')) and k not in ('skos:scopeNote', 'skos:definition'):
            rel += [[a, k, b] for b in parse_targets(v) if b in touched and b != a]
stub = {c: c not in notes or len(body(notes[c])) < 40 for c in touched | {p['situation'] for p in pats} | {p['goal'] for p in pats}}
def snip(name, n=2, cap=300):
    t = body(notes.get(name, ''))
    t = re.sub(r'^#.*$', '', t, flags=re.M)
    t = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', r'\2', t)
    t = re.sub(r'\[\[([^\]]+)\]\]', r'\1', t)
    t = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', t)
    t = re.sub(r'[*_`>]', '', t).replace('\n', ' ').strip()
    out = ' '.join(re.split(r'(?<=[.!?])\s+', t)[:n])
    return out[:cap] + ('…' if len(out) > cap else '')

SKIP = ('role:', 'dcterms:', 'skos:scopeNote', 'skos:definition', 'kg:requiresRole')
def links_of(n):
    return [(k, b) for k, v in fm.get(n, {}).items() if not k.startswith(SKIP) for b in parse_targets(v) if b != n]
incoming = {}
for a in fm:
    for k, b in links_of(a):
        incoming.setdefault(b, []).append((k, a))
nbrs = {}
hubs = touched | {p['situation'] for p in pats} | {p['goal'] for p in pats} | {p['name'] for p in pats}
for c in hubs:
    out = [(c, k, b) for k, b in links_of(c)] + [(a, k, c) for k, a in incoming.get(c, []) if fm.get(a, {}).get('dcterms:type') != 'Pattern']
    out.sort(key=lambda e: (not e[1].startswith(('iso-thes', 'has part')), e[1]))
    nbrs[c] = out[:6]
named = touched | {p['situation'] for p in pats} | {p['goal'] for p in pats} | {e[0] for v in nbrs.values() for e in v} | {e[2] for v in nbrs.values() for e in v}
text = {k: snip(k) for k in named}
out = {'patterns': sorted(pats, key=lambda p: p['situation'] or ''), 'relations': rel, 'stub': stub, 'neighbors': nbrs, 'text': text,
       'built': {'commit': os.environ.get('GITHUB_SHA', '')[:7], 'repo': os.environ.get('GITHUB_REPOSITORY', '')}}
dest = Path(sys.argv[1]) if len(sys.argv) > 1 else PKG / 'site' / 'patterns.json'
dest.write_text(json.dumps(out, ensure_ascii=False))
print(f"{len(pats)} patterns -> {dest}")
