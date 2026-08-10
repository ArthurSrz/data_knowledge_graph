---
related_to: [Agent Observability, Observability 2.0, Logging]
dependencies: [Trace ID, Span ID, Structured Events]
components: [Development Artifacts, Production Artifacts, Trace Events, Span Events]
category: Concepts Fondamentaux
tags: [Artefacts_Traçables, Observability_2.0, Logging]
broader: "[[version control]]"
inferred:skos:ancestor: "[[version control]]"
---

# Traceable Artifacts

**Définition** : Données sous-produit générées tout au long du cycle de vie de développement à production de l'agent. Dans l'ère Observability 2.0, ces données sont stockées dans des événements de log structurés avec des IDs de trace et span.

**Caractéristiques** :
- **Cycle de vie complet** : Du développement à la production
- **Structured Logging** : Événements de log structurés
- **Identification unique** : Trace ID et Span ID pour la traçabilité
- **Observability 2.0** : Nouvelle génération d'observabilité

**Types d'artefacts** :
- Artefacts de développement
- Artefacts de production
- Événements de trace
- Événements de span
- Métriques et logs

**Structure des données** :
- IDs de trace pour la corrélation
- IDs de span pour la granularité
- Métadonnées contextuelles
- Timestamps et statuts

**Utilisation** :
- Debugging et troubleshooting
- Analyse de performance
- Audit et compliance
- Amélioration continue
