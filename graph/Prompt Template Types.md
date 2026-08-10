---
related_to: [Prompt Templates, Conversation Patterns, Instruction Patterns]
dependencies: []
components: [Chat-style prompts, Instruct-style prompts]
category: Prompt Management
tags: [Types_Prompts, Templates, Conversation, Instructions]
broader: "[[AI prompt]]"
inferred:skos:ancestor:
  - "[[AI prompt]]"
  - "[[Language modeling]]"
  - "[[Large Language Model]]"
---

# Prompt Template Types

**Définition** : Classification des modèles de prompts selon leur structure et usage, optimisés pour différents types d'interactions avec les agents.

## Chat-style prompts
**Définition** : Conçus pour agents conversationnels, acceptent une liste de messages en entrée et répondent avec un message de style assistant.

**Caractéristiques** :
- Format conversationnel multi-tours
- Gestion de l'historique de conversation
- Rôles définis (user, assistant, system)
- Contexte maintenu entre les échanges

**Structure** :
```
[
  {"role": "system", "content": "Instructions système"},
  {"role": "user", "content": "Message utilisateur"},
  {"role": "assistant", "content": "Réponse agent"}
]
```

**Cas d'usage** :
- Assistants conversationnels
- Support client
- Consultations interactives
- Sessions de brainstorming

## Instruct-style prompts
**Définition** : Formatent une chaîne d'entrée unique, typiquement utilisés pour des tâches plus simples et directes.

**Caractéristiques** :
- Format instruction unique
- Tâche définie clairement
- Réponse attendue spécifique
- Exécution directe

**Structure** :
```
Instruction: [Tâche à accomplir]
Input: [Données d'entrée]
Output: [Format de sortie attendu]
```

**Cas d'usage** :
- Traitement de données
- Transformations simples
- Classification
- Extraction d'informations

**Choix du type** :
- Chat-style pour interactions complexes
- Instruct-style pour tâches unitaires
- Hybrid selon les besoins spécifiques
