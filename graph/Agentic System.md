---
related_to: [Agent, AgentOps, GenAI]
dependencies: [LLM, Tools, Planning, Memory]
components: [LLM Modules, Control Flow, External Tools, Multi-step Execution]
category: Concepts Fondamentaux
tags: [Systemes_Agentiques, GenAI, Workflow]
broader: "[[Artificial Intelligence (AI)]]"
inferred:skos:ancestor:
  - "[[AI]]"
  - "[[Artificial Intelligence (AI)]]"
inferred:skos:narrower:
  - "[[Autonomy]]"
  - "[[Human-in-the-loop]]"
  - "[[Model Context Protocol (MCP)]]"
  - "[[ReAct data agent]]"
  - "[[ReAct mode]]"
  - "[[Subagent]]"
  - "[[Tool Assignment Gate]]"
  - "[[Tool arena]]"
  - "[[Toolkits]]"
  - "[[action module]]"
  - "[[agency]]"
  - "[[agent identity]]"
  - "[[agent role type]]"
  - "[[claude code]]"
  - "[[claude managed agents]]"
  - "[[comparag agent]]"
  - "[[context mode]]"
  - "[[search module]]"
  - "[[tools]]"
---
Système GenAI qui sert les objectifs d'un utilisateur en effectuant des actions qui interagissent avec des systèmes externes au LLM. Incorpore des LLM comme modules dans un flux de contrôle conçu pour résoudre des tâches via l'utilisation d'outils externes, la planification, la mémoire et l'exécution d'étapes multiples.

**Composants clés** :
- **LLM Modules** : Modèles de langage intégrés comme composants
- **[[Control Flow]]** : Flux de contrôle orchestrant les opérations
- **External [[tools]]** : Outils externes pour l'interaction avec l'environnement
- **Multi-step Execution** : Capacité d'exécution en plusieurs étapes

**Fonctionnalités** :
- Utilisation d'outils externes
- Planification des actions
- Gestion de la mémoire
- Exécution séquentielle et complexe

**Relations** :
- Implémentation concrète du [[concept]] d'[[Agent]]
- Géré par la plateforme [[agentOps]]
- Nécessite des workflows structurés


