---
related_to:
  - "[[Multi-agent systems]]"
  - "[[Agent orchestration]]"
dependencies: []
components:
  - Worker
  - Coordinator
  - Supervisor
category: Agent Creation Registry
tags:
  - Rôles_Agent
  - Hiérarchie
  - Multi_Agent
broader: "[[agentic System]]"
inferred:skos:ancestor: "[[agentic System]]"
---
**Définition** : [[classification]] des agents selon leur fonction et position dans la hiérarchie du système multi-[[agent]].

# **Types principaux** :

### Worker

Agents avec des rôles spécifiques comme "Researcher" ou "Writer", fonctionnant comme partie d'une équipe avec des compétences et responsabilités spécifiques.

**Caractéristiques** :
- Spécialisation fonctionnelle
- Compétences dédiées
- Responsabilités définies
- Collaboration en équipe

### Coordinator/Supervisor

Agents sous lesquels opèrent plusieurs agents workers, suivant les [[instructions]] du superviseur.

**Caractéristiques** :
- Gestion d'équipe d'agents
- Coordination des tâches
- Distribution des responsabilités
- Supervision des exécutions

**Architecture multi-[[agent]]** :
- Hiérarchie claire des rôles
- Communication inter-agents
- [[Delegation]] et supervision
- Orchestration des workflows

**Bénéfices** :
- Spécialisation et efficacité
- Scalabilité horizontale
- Parallélisation des tâches
- Résilience du système
