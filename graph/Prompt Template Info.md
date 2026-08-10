---
related_to: [Prompt Templates, Context Management, Output Formatting]
dependencies: [User Goal, Tools, Chat History]
components: [User Goal, Instruction, Input Query, Context Doc, Few-shot Example, Output Format, Tools, Chat History]
category: Prompt Management
tags: [Templates_Prompt, Contexte, Exemples, Format_Sortie]
broader: "[[AI prompt]]"
inferred:skos:ancestor:
  - "[[AI prompt]]"
  - "[[Large Language Model]]"
---

# Prompt Template Info

**Définition** : Structure détaillée des informations composant un template de prompt, incluant tous les éléments nécessaires à l'exécution efficace d'une tâche par l'agent.

**Composants** :

## User Goal
**Définition** : Objectif spécifique que l'utilisateur souhaite atteindre avec cette requête.

## Instruction
**Définition** : Instructions détaillées pour guider l'agent dans l'accomplissement de la tâche.

## Input Query
**Définition** : Question ou demande d'entrée formulée par l'utilisateur.

## Context Doc
**Définition** : Information contextuelle pertinente pour l'exécution de la tâche.

## Few-shot Example
**Définition** : Exemples concrets pour guider le format de sortie et le comportement attendu.

## Output Format
**Définition** : Format de sortie désiré (JSON, texte structuré, markdown, etc.).

## Tools
**Définition** : Liste des outils que l'agent peut utiliser pour accomplir la tâche.

## Chat History
**Définition** : Historique de conversation précédent pour maintenir le contexte.

**Architecture du template** :
- Structure modulaire et réutilisable
- Paramètres configurables
- Validation des inputs
- Optimisation pour différents modèles

**Bénéfices** :
- Consistance des interactions
- Réutilisabilité des patterns
- Optimisation des performances
- Facilité de maintenance

**Relations** :
- Base pour la génération de prompts
- Lié à l'identité des prompts
- Connecté aux techniques d'optimisation
