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
- 2026-11-22 20:37:48 · `mcp` · upsert · **acceptée** · [[Unit tests]]
- 2026-11-22 20:37:52 · `mcp` · upsert · **acceptée** · [[Integration tests]]
- 2026-11-22 20:37:56 · `mcp` · upsert · **acceptée** · [[Deployment]]
- 2026-11-22 20:38:13 · `mcp` · upsert · **acceptée** · [[crawl-walk-run]]
- 2026-11-22 20:38:17 · `mcp` · upsert · **acceptée** · [[claude code]]
- 2026-11-22 20:38:22 · `mcp` · upsert · **acceptée** · [[hook]]
- 2026-11-22 20:38:59 · `d251c4ed` · block · **acceptée (Stop)** · changeset depuis 105e702
- 2026-11-22 20:43:58 · `d251c4ed` · block · **acceptée (Stop)** · changeset depuis 105e702
- 2026-11-22 20:51:31 · `d251c4ed` · block · **acceptée (Stop)** · changeset depuis 105e702
- 2026-11-22 21:02:07 · `d251c4ed` · block · **acceptée (Stop)** · changeset depuis 105e702
- 2026-11-22 21:04:51 · `d251c4ed` · block · **acceptée (Stop)** · changeset depuis 105e702
- 2026-11-22 21:11:21 · `d251c4ed` · block · **acceptée (Stop)** · changeset depuis 105e702
- 2026-11-22 21:16:40 · `d251c4ed` · block · **acceptée (Stop)** · changeset depuis 105e702
- 2026-11-22 21:17:51 · `d251c4ed` · block · **acceptée (Stop)** · changeset depuis 105e702
- 2026-11-22 21:21:09 · `d251c4ed` · block · **acceptée (Stop)** · changeset depuis 105e702
- 2026-11-22 21:47:33 · `354d34c4` · block · **acceptée (Stop)** · changeset depuis 469922f
- 2026-11-22 21:47:41 · `mcp` · upsert · **acceptée** · [[clarifeye]]
- 2026-11-22 21:47:52 · `da3d6722` · block · **acceptée (Stop)** · changeset depuis d3f03ec
- 2026-11-22 21:50:02 · `mcp` · upsert · **refusée** · [[person]]
    ✗ gate: 6 nouvelle(s) violation(s) logique(s).
    
    • disjonction : Judea Pearl ↔ continuant
        Judea Pearl —instance_of→ person —broader→ independent continuant —broader→ continuant
        Judea Pearl —instance_of→ person —broader→ process —broader→ occurrent
        continuant —disjoint with— occurrent
      → Supprimer la relation entre deux concepts disjoints (un concept ne peut pas être lié à un concept qu'il exclut).
    
    • disjonction : person ↔ continuant
        person —broader→ independent continuant —broader→ continuant
        person —broader→ process —broader→ occurrent
        continuant —disjoint with— occurrent
      → Supprimer la relation entre deux concepts disjoints (un concept ne peut pas être lié à un concept qu'il exclut).
    
    • disjonction : process owner ↔ continuant
        process owner —broader→ person —broader→ independent continuant —broader→ continuant
        process owner —broader→ person —broader→ process —broader→ occurrent
        continuant —disjoint with— occurrent
      → Supprimer la relation entre deux concepts disjoints (un concept ne peut pas être lié à un concept qu'il exclut).
- 2026-11-23 09:30:08 · `eebed3d4` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 09:31:58 · `6e3e9954` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 09:33:01 · `6e3e9954` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 09:33:52 · `eebed3d4` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 09:33:59 · `6e3e9954` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 09:34:36 · `6e3e9954` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 09:35:59 · `6e3e9954` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 09:36:11 · `eebed3d4` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 09:36:21 · `eebed3d4` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 09:37:22 · `6e3e9954` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 09:38:19 · `6e3e9954` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 09:40:52 · `eebed3d4` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 09:42:19 · `6e3e9954` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 09:44:30 · `eebed3d4` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 09:45:15 · `eebed3d4` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 09:50:25 · `eebed3d4` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 09:52:32 · `e253a35e` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 09:53:07 · `e253a35e` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 09:53:33 · `e253a35e` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 09:55:28 · `eebed3d4` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 09:56:29 · `eebed3d4` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 09:58:31 · `e253a35e` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 09:59:20 · `e253a35e` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 10:00:49 · `e253a35e` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 10:02:22 · `e253a35e` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 10:03:56 · `e253a35e` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 10:08:34 · `e253a35e` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 10:08:46 · `e253a35e` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 10:10:50 · `e253a35e` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 11:39:02 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 11:39:49 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 11:41:04 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 11:42:57 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 11:45:09 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 13:13:41 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 13:16:19 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 13:18:38 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 13:21:54 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 13:37:18 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 13:42:10 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 13:43:48 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 13:44:48 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 14:11:57 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 14:18:57 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 14:27:12 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 14:49:08 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 18:23:54 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 18:26:25 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 18:27:16 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 18:29:12 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 18:31:18 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 18:33:19 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 18:33:56 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 18:34:32 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 18:36:20 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 18:37:35 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 18:39:46 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 18:41:37 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 18:42:45 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 18:52:21 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 18:53:50 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 18:55:24 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 19:28:46 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 19:31:17 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 19:31:54 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 19:36:55 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 19:38:51 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 19:42:29 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 20:14:11 · `e253a35e` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 20:16:11 · `e253a35e` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 20:19:18 · `e253a35e` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 20:22:04 · `e253a35e` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 20:24:01 · `e253a35e` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 20:29:00 · `e253a35e` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 20:29:32 · `7291ec85` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 20:33:20 · `e253a35e` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 20:33:46 · `7291ec85` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 20:45:09 · `7291ec85` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 20:47:04 · `8d7b2774` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 20:47:59 · `7291ec85` · block · **acceptée** · [[merge conflict]]
- 2026-11-23 20:48:05 · `mcp` · upsert · **acceptée** · [[data lineage]]
- 2026-11-23 20:48:10 · `mcp` · upsert · **acceptée** · [[Provenance]]
- 2026-11-23 20:48:15 · `mcp` · upsert · **acceptée** · [[single source of truth]]
- 2026-11-23 20:48:18 · `7291ec85` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 20:48:20 · `mcp` · upsert · **acceptée** · [[OAuth]]
- 2026-11-23 20:48:46 · `e253a35e` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 20:48:59 · `8d7b2774` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 20:50:14 · `7291ec85` · block · **acceptée** · [[explicit knowledge]]
- 2026-11-23 20:50:19 · `7291ec85` · block · **acceptée** · [[explicit knowledge]]
- 2026-11-23 20:50:37 · `7291ec85` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 20:51:29 · `mcp` · upsert · **acceptée** · [[digital identity]]
- 2026-11-23 20:51:34 · `mcp` · upsert · **acceptée** · [[service account]]
- 2026-11-23 20:51:39 · `mcp` · upsert · **acceptée** · [[event sourcing]]
- 2026-11-23 20:51:53 · `e253a35e` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 20:56:18 · `7291ec85` · block · **acceptée** · [[merge conflict]]
- 2026-11-23 20:56:23 · `7291ec85` · block · **acceptée** · [[explicit knowledge]]
- 2026-11-23 20:56:36 · `mcp` · upsert · **acceptée** · [[data lineage]]
- 2026-11-23 20:56:41 · `mcp` · upsert · **acceptée** · [[Provenance]]
- 2026-11-23 20:56:45 · `7291ec85` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 20:56:46 · `8d7b2774` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 20:56:47 · `mcp` · upsert · **acceptée** · [[single source of truth]]
- 2026-11-23 20:56:52 · `mcp` · upsert · **acceptée** · [[OAuth]]
- 2026-11-23 20:57:06 · `e253a35e` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 20:59:10 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 21:03:25 · `4a333d96` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 21:05:01 · `mcp` · upsert · **acceptée** · [[algorithm]]
- 2026-11-23 21:05:06 · `mcp` · upsert · **acceptée** · [[algorithm execution]]
- 2026-11-23 21:05:19 · `8d7b2774` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-23 21:05:48 · `8d7b2774` · block · **acceptée (Stop)** · changeset depuis 2a88a81
- 2026-11-24 12:02:44 · `cf1765e3` · block · **acceptée (Stop)** · changeset depuis eab27c8
- 2026-11-24 12:05:53 · `mcp` · upsert · **acceptée** · [[hypothesis]]
- 2026-11-24 12:05:58 · `mcp` · upsert · **acceptée** · [[falsifiability]]
- 2026-11-24 12:06:03 · `mcp` · upsert · **acceptée** · [[bias]]
- 2026-11-24 12:06:07 · `mcp` · upsert · **acceptée** · [[cognitive bias]]
- 2026-11-24 12:06:12 · `mcp` · upsert · **acceptée** · [[recall bias]]
- 2026-11-24 12:06:17 · `mcp` · upsert · **acceptée** · [[measurement bias]]
- 2026-11-24 12:06:22 · `mcp` · upsert · **acceptée** · [[selection bias]]
- 2026-11-24 12:06:26 · `mcp` · upsert · **acceptée** · [[sampling bias]]
- 2026-11-24 12:07:12 · `mcp` · upsert · **acceptée** · [[research interview]]
- 2026-11-24 12:07:17 · `mcp` · upsert · **refusée** · [[elicitation interview]]
    ✗ gate: 1 nouvelle(s) violation(s) logique(s).
    
    • SKOS S27 (related + hiérarchique) : elicitation interview ↔ research interview
        elicitation interview —broader→ research interview
        elicitation interview —related— research interview
      → Supprimer la relation entre deux concepts liés hiérarchiquement (un concept ne peut pas être lié à un de ses ancêtres).
- 2026-11-24 12:07:22 · `mcp` · upsert · **acceptée** · [[critical incident technique]]
- 2026-11-24 12:07:26 · `mcp` · upsert · **acceptée** · [[member check]]
- 2026-11-24 12:07:31 · `mcp` · upsert · **acceptée** · [[qualitative coding]]
- 2026-11-24 12:07:36 · `mcp` · upsert · **acceptée** · [[codebook]]
- 2026-11-24 12:07:41 · `mcp` · upsert · **acceptée** · [[triangulation (social science)]]
- 2026-11-24 12:07:46 · `mcp` · upsert · **acceptée** · [[glossary]]
- 2026-11-24 12:07:52 · `mcp` · upsert · **acceptée** · [[emic and etic]]
- 2026-11-24 12:07:57 · `mcp` · upsert · **acceptée** · [[gap analysis]]
- 2026-11-24 12:08:13 · `mcp` · upsert · **acceptée** · [[elicitation interview]]
- 2026-11-24 12:08:33 · `cf1765e3` · block · **acceptée (Stop)** · changeset depuis eab27c8
- 2026-11-26 16:41:44 · `mcp` · upsert · **acceptée** · [[artifact]]
- 2026-11-26 16:41:50 · `mcp` · upsert · **acceptée** · [[interview guide]]
- 2026-11-26 16:42:03 · `064cbe0e` · block · **acceptée (Stop)** · changeset depuis 4e12c15
- 2026-11-26 16:42:06 · `6087c610` · block · **acceptée (Stop)** · changeset depuis 4e12c15
- 2026-11-26 16:49:24 · `6087c610` · block · **acceptée (Stop)** · changeset depuis 4e12c15
- 2026-11-26 16:49:33 · `064cbe0e` · block · **acceptée (Stop)** · changeset depuis 4e12c15
- 2026-11-26 16:51:52 · `mcp` · upsert · **acceptée** · [[content curation]]
- 2026-11-26 16:51:57 · `mcp` · upsert · **acceptée** · [[brief]]
- 2026-11-26 16:52:03 · `mcp` · upsert · **acceptée** · [[concept map]]
- 2026-11-26 16:52:08 · `mcp` · upsert · **acceptée** · [[document template]]
- 2026-11-26 16:52:14 · `mcp` · upsert · **acceptée** · [[process mining]]
- 2026-11-26 16:52:19 · `mcp` · upsert · **acceptée** · [[benchmarking]]
- 2026-11-26 16:52:25 · `mcp` · upsert · **acceptée** · [[goal]]
- 2026-11-26 16:52:30 · `mcp` · upsert · **acceptée** · [[enterprise architecture]]
- 2026-11-26 16:52:35 · `mcp` · upsert · **acceptée** · [[order to cash]]
- 2026-11-26 16:52:54 · `mcp` · upsert · **acceptée** · [[cash collection]]
- 2026-11-26 16:52:58 · `6087c610` · block · **acceptée (Stop)** · changeset depuis 4e12c15
- 2026-11-26 16:52:59 · `mcp` · upsert · **acceptée** · [[conformance checking]]
- 2026-11-26 16:53:05 · `mcp` · upsert · **acceptée** · [[sandbox]]
- 2026-11-26 16:53:10 · `mcp` · upsert · **acceptée** · [[clarifeye]]
- 2026-11-26 16:53:16 · `mcp` · upsert · **acceptée** · [[feedback]]
- 2026-11-26 16:53:54 · `mcp` · upsert · **acceptée** · [[knowledge worker]]
- 2026-11-26 16:54:00 · `mcp` · upsert · **acceptée** · [[member check]]
- 2026-11-26 16:54:05 · `mcp` · upsert · **acceptée** · [[audit]]
- 2026-11-26 16:54:11 · `mcp` · upsert · **acceptée** · [[skills]]
- 2026-11-26 16:54:16 · `mcp` · upsert · **acceptée** · [[controlled vocabulary]]
- 2026-11-26 16:54:29 · `mcp` · upsert · **acceptée** · [[draft document]]
- 2026-11-26 16:54:35 · `mcp` · upsert · **acceptée** · [[knowledge base]]
- 2026-11-26 16:54:46 · `6087c610` · block · **acceptée (Stop)** · changeset depuis 4e12c15
- 2026-11-26 16:54:47 · `064cbe0e` · block · **acceptée (Stop)** · changeset depuis 4e12c15
- 2026-11-26 16:57:14 · `6087c610` · block · **acceptée (Stop)** · changeset depuis 4e12c15
