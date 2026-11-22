# Gate log

Décisions du garde-fou logique (`reason.py gate`) : acceptée, avertie, refusée, contournée.

- 2026-11-22 20:18:12 · `d251c4ed` · warn · **acceptée (Stop)** · changeset depuis 105e702
- 2026-11-22 20:24:52 · `d251c4ed` · warn · **acceptée (Stop)** · changeset depuis 105e702
- 2026-11-22 20:25:45 · `d251c4ed` · warn · **acceptée (Stop)** · changeset depuis 105e702
- 2026-11-22 20:28:39 · `d251c4ed` · warn · **acceptée (Stop)** · changeset depuis 105e702
- 2026-11-22 20:31:45 · `d251c4ed` · block · **refusée** · [[zz gate block test]]
    ✗ gate: 2 nouvelle(s) violation(s) logique(s).
    
    • disjonction : zz gate block test ↔ continuant
        zz gate block test —broader→ person —broader→ independent continuant —broader→ continuant
        zz gate block test —broader→ business process —broader→ process —broader→ occurrent
        continuant —disjoint with— occurrent
      → Supprimer la relation entre deux concepts disjoints (un concept ne peut pas être lié à un concept qu'il exclut).
- 2026-11-22 20:31:53 · `d251c4ed` · block · **acceptée** · [[zz gate block test]]
- 2026-11-22 20:32:11 · `d251c4ed` · block · **refusée (Stop)** · changeset depuis 105e702
    ✗ gate: 2 nouvelle(s) violation(s) logique(s).
    
    • disjonction : zz gate block test ↔ continuant
        zz gate block test —broader→ person —broader→ independent continuant —broader→ continuant
        zz gate block test —broader→ business process —broader→ process —broader→ occurrent
        continuant —disjoint with— occurrent
      → Supprimer la relation entre deux concepts disjoints (un concept ne peut pas être lié à un concept qu'il exclut).
- 2026-11-22 20:32:27 · `d251c4ed` · block · **acceptée (Stop)** · changeset depuis 105e702
- 2026-11-22 20:33:18 · `mcp` · upsert · **refusée** · [[zz mcp gate test]]
    ✗ gate: 2 nouvelle(s) violation(s) logique(s).
    
    • disjonction : zz mcp gate test ↔ continuant
        zz mcp gate test —broader→ person —broader→ independent continuant —broader→ continuant
        zz mcp gate test —broader→ business process —broader→ process —broader→ occurrent
        continuant —disjoint with— occurrent
      → Supprimer la relation entre deux concepts disjoints (un concept ne peut pas être lié à un concept qu'il exclut).
- 2026-11-22 20:33:27 · `mcp` · upsert · **acceptée** · [[zz mcp gate test]]
- 2026-11-22 20:33:38 · `d251c4ed` · block · **acceptée (Stop)** · changeset depuis 105e702
