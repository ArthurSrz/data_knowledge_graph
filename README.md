<div align="center">

# 🧠 [[Data]] [[knowledge graph]]

**A living [[ontology]] of [[data]] science, ML, and AI built as an Obsidian vault with typed semantic relationships.**

[![Concepts](https://img.shields.io/badge/concepts-873-blue?style=flat-square)](#)
[![Wikilinks](https://img.shields.io/badge/wikilinks-7%2C800%2B-green?style=flat-square)](#)
[![SKOS Coverage](https://img.shields.io/badge/SKOS_coverage-80.9%25-orange?style=flat-square)](#)
[![Datalog Rules](https://img.shields.io/badge/datalog_rules-9-purple?style=flat-square)](#formal-reasoning)

</div>

---

<br>

> **Not a glossary, a graph.** Each concept carries typed relationships in YAML frontmatter (`broader`, `uses`, `subclass of`, …), forming a navigable semantic network. 73 root concepts branch into 8 nesting levels, connected by 7,800+ wikilinks.

<br>

## 📈 Growth

![Knowledge Graph Growth](stats/chart.png)

|  | Count |
|---|---:|
| **Rich** (200+ words) | 109 |
| **Medium** (50–199 words) | 112 |
| **Stubs** (< 50 words) | 359 |
| **Empty** (link targets) | 292 |

<br>

## 🏗️ Structure

Each concept is a markdown file with YAML frontmatter defining typed relationships and wiki-links connecting to related terms:

```yaml
# Knowledge graph.md
---
uses:
  - "[[Ontology]]"
  - "[[Taxonomy]]"
subclass of:
  - "[[knowledge base]]"
  - "[[labeled directed graph]]"
studied in:
  - "[[Ontology engineering]]"
---
A knowledge graph represents structured domain knowledge
as entities connected by typed relationships...
```

<br>

## 🗺️ Topics

<table>
<tr>
<td width="33%">

**🤖 AI & LLMs**
<br><sub>Agents, RAG, transformers, prompt engineering, LLM evaluation</sub>

</td>
<td width="33%">

**📊 Machine Learning**
<br><sub>Algorithms, training, evaluation metrics, feature engineering</sub>

</td>
<td width="33%">

**🔧 Data Engineering**
<br><sub>Pipelines, data lineage, ETL, data quality</sub>

</td>
</tr>
<tr>
<td>

**🧬 Deep Learning**
<br><sub>Neural networks, CNNs, transformers, attention, backpropagation</sub>

</td>
<td>

**🔗 Knowledge Representation**
<br><sub>Ontologies, taxonomies, knowledge graphs, SKOS</sub>

</td>
<td>

**⚖️ Fairness & Privacy**
<br><sub>Bias, FERPA, PII management, interpretability</sub>

</td>
</tr>
<tr>
<td>

**🏛️ Infrastructure**
<br><sub>Cloud, containers, HTTP, authentication, databases</sub>

</td>
<td>

**📐 Math & Statistics**
<br><sub>Probability, graph theory, vector spaces, combinatorics</sub>

</td>
<td>

**💼 Process & Product**
<br><sub>Design thinking, CRISP-DM, agile, management</sub>

</td>
</tr>
</table>

<br>

## 🎯 Use as a Data Ontology

| Use case | How |
|---|---|
| **GraphRAG** | Navigate concepts through semantic connections instead of keyword matching |
| **Data catalog enrichment** | Import as standardized terminology for hierarchical classification |
| **LLM grounding** | Reduce hallucination through explicit relationship constraints |
| **Onboarding** | Interactive learning with concept definitions and relationship paths |
| **Metadata schema design** | Use `partOf`, `uses`, `subclass of` as schema blueprints |
| **Knowledge graph construction** | Export to Neo4j / RDF by parsing frontmatter into typed edges |
| **Concept disambiguation** | Canonical definitions that resolve cross-team terminology drift |

<br>

## 🔬 Formal Reasoning

`scripts/reason.py` uses [Semantica](https://github.com/semantica-agi/semantica)'s Datalog engine for purely logical inference — no LLM involved.

```bash
pip install -r requirements.txt

python scripts/reason.py infer          # derived ancestor chains, symmetric related, inverses
python scripts/reason.py check          # cycles, broken links, S27 violations, orphans
python scripts/reason.py query "ancestor(AI agent, ?X)"   # query with real note titles
python scripts/reason.py report         # write stats/reasoning_report.md
```

9 Datalog rules encode SKOS semantics: transitive `broader` closure, `broader`↔`narrower` inverses, `related` symmetry, cycle detection, and [SKOS S27](https://www.w3.org/TR/skos-reference/#L2422) disjointness.

<br>

## 🌳 Taxonomy — SKOS Broader/Narrower Hierarchy

The graph encodes [SKOS](https://www.w3.org/2004/02/skos/)-style hierarchical relationships via `broader:` in YAML frontmatter. **701 of 866 concepts** (80.9%) are classified — 73 root concepts, up to 8 nesting levels.

<details>
<summary><strong>Browse full taxonomy</strong> (73 root concepts → 701 classified concepts)</summary>

<br>

- [agent observability](graph/agent%20observability.md)
  - [agentOps](agentOps.md)
  - [LLM Observability](graph/LLM%20Observability.md)
    - [Langfuse](graph/Langfuse.md)
- [Agile approach](graph/Agile%20approach.md)
  - [Daily stand-ups](graph/Daily%20stand-ups.md)
  - [Demo sessions](graph/Demo%20sessions.md)
  - [Product owner](graph/Product%20owner.md)
  - [Sprint planning](graph/Sprint%20planning.md)
- [AI](graph/AI.md)
  - [AI engineering](graph/AI%20engineering.md)
  - [AI Hierarchy of needs](graph/AI%20Hierarchy%20of%20needs.md)
  - [AI Proof detection model](graph/AI%20Proof%20detection%20model.md)
  - [AI stack](graph/AI%20stack.md)
  - [Artificial Intelligence (AI)](graph/Artificial%20Intelligence%20%28AI%29.md)
    - [agentic System](agentic%20System.md)
      - [action module](graph/action%20module.md) · [agency](graph/agency.md) · [agent harness](graph/agent%20harness.md) · [agent identity](graph/agent%20identity.md) · [agent role type](graph/agent%20role%20type.md) · [Autonomy](graph/Autonomy.md) · [claude code](graph/claude%20code.md) · [claude managed agents](graph/claude%20managed%20agents.md) · [comparag agent](graph/comparag%20agent.md) · [context mode](graph/context%20mode.md) · [Human-in-the-loop](graph/Human-in-the-loop.md) · [ReAct data agent](graph/ReAct%20data%20agent.md) · [ReAct mode](graph/ReAct%20mode.md) · [search module](graph/search%20module.md) · [Subagent](graph/Subagent.md) · [Tool arena](graph/Tool%20arena.md) · [Tool Assignment Gate](graph/Tool%20Assignment%20Gate.md) · [Toolkits](graph/Toolkits.md) · [tools](tools.md)
      - [Model Context Protocol (MCP)](graph/Model%20Context%20Protocol%20%28MCP%29.md) → [MCP host](graph/MCP%20host.md) · [MCP server](graph/MCP%20server.md)
    - [compound AI system](compound%20AI%20system.md)
    - [computer vision](graph/computer%20vision.md) → [Facial recognition](graph/Facial%20recognition.md)
    - [connexionism](graph/connexionism.md) · [Expert systems](graph/Expert%20systems.md) · [Narrow AI](graph/Narrow%20AI.md) · [Symbolism](graph/Symbolism.md)
    - [Natural Language Processing](graph/Natural%20Language%20Processing.md)
      - [bag of words](bag%20of%20words.md) · [Sentiment analysis](graph/Sentiment%20analysis.md) · [token](graph/token.md) · [Tokenizer](graph/Tokenizer.md)
      - [Embeddings](graph/Embeddings.md) → [embedding](graph/embedding.md) · [Embeddings models](graph/Embeddings%20models.md) · [latent space](graph/latent%20space.md) · [vectorization](graph/vectorization.md) · [Word embeddings](graph/Word%20embeddings.md)
      - [Language modeling](graph/Language%20modeling.md)
        - [autoregressive language models](graph/autoregressive%20language%20models.md) → [GPT2](graph/GPT2.md)
        - [Large Language Model](graph/Large%20Language%20Model.md)
          - [AI prompt](graph/AI%20prompt.md) → [chain-of-thought](graph/chain-of-thought.md) · [Prompt Identity](graph/Prompt%20Identity.md) · [Prompt Optimization Techniques](graph/Prompt%20Optimization%20Techniques.md) · [Prompt templates](graph/Prompt%20templates.md) · [system prompt](graph/system%20prompt.md) · …
          - [RAG (Retrieval-Augmented Generation)](graph/RAG%20%28Retrieval-Augmented%20Generation%29.md) → [Retriever](graph/Retriever.md) · [HyDE](graph/Hypothetical%20Document%20Embeddings%20%28HyDE%29.md) · …
          - [chat engines](graph/chat%20engines.md) · [Hallucination](graph/Hallucination.md) · [In-Context Learning](graph/In-Context%20Learning.md) · [LLaMA](graph/LLaMA.md) · [Ollama](graph/Ollama.md) · …
        - [masked language models](graph/masked%20language%20models.md) → [BERT](graph/BERT.md) → [camemBERT](graph/camemBERT.md)
  - [claude cowork](graph/claude%20cowork.md) · [Man-Computer Symbiosis](graph/Man-Computer%20Symbiosis.md) · [The Shift from Models to Compound AI Systems](graph/The%20Shift%20from%20Models%20to%20Compound%20AI%20Systems.md) · …
- [algorithm](algorithm.md)
  - [algorithm selection](algorithm%20selection.md) · [Greediness](graph/Greediness.md) · [Non-parametric algorithms](graph/Non-parametric%20algorithms.md) · [selection](graph/selection.md)
- [automation](automation.md)
  - [automation framework](automation%20framework.md) · [office automation](graph/office%20automation.md)
- [Business understanding](graph/Business%20understanding.md)
  - [define success](graph/define%20success.md) · [Problem framing](graph/Problem%20framing.md)
- [Centrality](graph/Centrality.md)
  - [betweenness centrality](graph/betweenness%20centrality.md) · [closeness centrality](graph/closeness%20centrality.md) · [Degree centrality](graph/Degree%20centrality.md) · [Eigenvector centrality](graph/Eigenvector%20centrality.md)
- [clause](graph/clause.md)
  - [clause classification heuristic](graph/clause%20classification%20heuristic.md) · [exclusion clause](graph/exclusion%20clause.md) · [force majeure](graph/force%20majeure.md) · [non-compete clause](graph/non-compete%20clause.md)
- [Clustering](graph/Clustering.md)
  - [Elbow method](graph/Elbow%20method.md) · [K-Means Clustering](graph/K-Means%20Clustering.md)
- [Combinatorics](graph/Combinatorics.md) · [combinatorics](graph/combinatorics.md)
  - [graph theory](graph/graph%20theory.md) · [probability](graph/probability.md) · [combination](graph/combination.md) · [Unary operation](graph/Unary%20operation.md)
- [Confusion Matrix](graph/Confusion%20Matrix.md)
  - [False Negative (FN)](graph/False%20Negative%20%28FN%29.md) · [False Positive (FP)](graph/False%20Positive%20%28FP%29.md) · [True Negative (TN)](graph/True%20Negative%20%28TN%29.md) · [True Positive (TP)](graph/True%20Positive%20%28TP%29.md)
- [Containerization (computing)](graph/Containerization%20%28computing%29.md)
  - [container](graph/container.md) · [Docker](graph/Docker.md) → [Docker images](graph/Docker%20images.md)
- [contract](graph/contract.md)
  - [compliant privacy policy](graph/compliant%20privacy%20policy.md) · [liability](graph/liability.md) · [model contract](graph/model%20contract.md) · [Rider](graph/Rider.md)
- [control theory](graph/control%20theory.md)
  - [Damping](graph/Damping.md) · [Inertia](graph/Inertia.md) · [James Clerk Maxwell](graph/James%20Clerk%20Maxwell.md) · [state observer](graph/state%20observer.md)
- [Deep learning](graph/Deep%20learning.md)
  - [artificial neural network](graph/artificial%20neural%20network.md) → [artificial neuron](graph/artificial%20neuron.md) · [autoencoder](graph/autoencoder.md) · [backpropagation](backpropagation.md) · [CNN](graph/Convolutional%20neural%20networks.md) · [multilayer perceptron](graph/multilayer%20perceptron.md) · [ReLU](graph/ReLU%20activation%20function.md) · [Sigmoid](graph/Sigmoid%20function.md) · [Weights](graph/Weights.md) · …
  - [foundation model](graph/foundation%20model.md) → [multimodal model](graph/multimodal%20model.md) · [tabular foundation model](graph/tabular%20foundation%20model.md) → [TabPFN](graph/TabPFN.md)
  - [Keras](graph/Keras.md) · [Transfer learning](graph/Transfer%20learning.md)
  - [Transformers](graph/Transformers.md) → [attention weights](graph/attention%20weights.md) · [Decoder-only](graph/Decoder-only.md) · [Encoder-only](graph/Encoder-only.md)
- [elicitation](graph/elicitation.md)
  - [Dialogue](graph/Dialogue.md) · [elicitation interview](graph/elicitation%20interview.md) · [Socratic](graph/Socratic.md) → [Socrates](graph/Socrates.md)
- [evaluation](graph/evaluation.md)
  - [Cross validation](graph/Cross%20validation.md) · [Evaluation metrics](graph/Evaluation%20metrics.md) → [accuracy](graph/accuracy.md) · [F1 Score](graph/F1%20Score.md) · [Precision](graph/Precision.md) · [Recall](graph/Recall.md) · [ROC](graph/Receiver%20Operating%20Characteristic%20curve.md) · [Regression Error Metrics](graph/Regression%20Error%20Metrics.md) · …
- [Fairness](graph/Fairness.md)
  - [bias](graph/bias.md) → [Feedback loop bias](graph/Feedback%20loop%20bias.md) · [Historical bias](graph/Historical%20bias.md)
  - [Data privacy](graph/Data%20privacy.md) → [Data privacy laws](graph/Data%20privacy%20laws.md) · [Privacy by design](graph/Privacy%20by%20design.md) · [Sensitive Information](graph/Sensitive%20Information.md) · …
  - [Transparency](graph/Transparency.md) → [Interpretability](graph/Interpretability.md) → [LIME](graph/Local%20Interpretable%20Model-Agnostic%20Explanations%20%28LIME%29.md) · [SHAP](graph/Shapley%20Additive%20Explanations%20%28SHAP%29.md)
- [Graph theory](graph/Graph%20theory.md)
  - [adjacency matrix](graph/adjacency%20matrix.md) · [Edges](graph/Edges.md) · [node](graph/node.md) · [Heterogeneous graph](graph/Heterogeneous%20graph.md) · [Network graph](graph/Network%20graph.md) · …
- [Infrastructure](graph/Infrastructure.md)
  - [authentication protocol](graph/authentication%20protocol.md) → [OAuth](graph/OAuth.md) · [SSH Key](graph/SSH%20Key.md)
  - [cloud computing](graph/cloud%20computing.md) · [Datawarehouse](graph/Datawarehouse.md) · [Deploy](graph/Deploy.md) · [Docker](graph/Docker.md) · [HTTP](graph/HTTP.md) · [NoSQL database](graph/NoSQL%20database.md) · [Virtualization](graph/Virtualization.md) · …
- [knowledge graph](graph/knowledge%20graph.md)
  - [CYPHER](graph/CYPHER.md) · [context graph](graph/context%20graph.md) · [graph hop](graph/graph%20hop.md) · [Properties](graph/Properties.md) · [Text2Cypher](graph/Text2Cypher.md) · …
- [knowledge organization system](graph/knowledge%20organization%20system.md)
  - [concept](graph/concept.md) · [controlled vocabulary](graph/controlled%20vocabulary.md) · [Ontology](graph/Ontology.md) · [taxonomy](graph/taxonomy.md) · [thesaurus](graph/thesaurus.md) · …
- [machine learning](graph/machine%20learning.md)
  - [supervised learning](graph/supervised%20learning.md) → [Decision tree](graph/Decision%20tree.md) · [KNN](graph/K-Nearest%20Neighbor%20algorithm.md) · [Naive Bayes](graph/Naive%20Bayes%20Classifier.md) · [SVM](graph/Support%20Vector%20Machine.md)
  - [Unsupervised Learning](graph/Unsupervised%20Learning.md) · [Reinforcement Learning](graph/Reinforcement%20Learning.md) · [Federated learning](graph/Federated%20learning.md)
  - [Hyperparameters](graph/Hyperparameters.md) · [loss function](graph/loss%20function.md) · [Regularization](graph/Regularization.md)
  - [Optimizer algorithm](graph/Optimizer%20algorithm.md) → [Gradient descent](graph/Gradient%20descent.md)
  - [ML system](graph/ML%20system.md) → [cold start problem](graph/cold%20start%20problem.md) · [Reproducibility](graph/Reproducibility.md) · …
- [machine learning projects](graph/machine%20learning%20projects.md)
  - [CRISP-DM Process](graph/CRISP-DM%20Process.md) → [Data preparation](graph/Data%20preparation.md) · [Deployment](graph/Deployment.md) · [modeling](graph/modeling.md) · [Problem definition](graph/Problem%20definition.md) · …
- [ML models](graph/ML%20models.md)
  - [Linear models](graph/Linear%20models.md) · [Neural network models](graph/Neural%20network%20models.md) · [feature](graph/feature.md) · [prediction](graph/prediction.md) · …
- [Model fit](graph/Model%20fit.md) → [Overfitting](graph/Overfitting.md) · [Underfitting](graph/Underfitting.md)
- [Model maintenance](graph/Model%20maintenance.md) → [concept drift](graph/concept%20drift.md) · [Data drift](graph/Data%20drift.md) · [Model registry](graph/Model%20registry.md) · [Retraining](graph/Retraining.md) · …
- [Model tuning](graph/Model%20tuning.md) → [Fine-tuning](graph/Fine-tuning.md) · [LoRA](graph/Low-Rank%20Adaptation.md) · [Pruning](graph/Pruning.md) · [Quantization](graph/Quantization.md)
- [Probability](graph/Probability.md) → [bayes' theorem](bayes'%20theorem.md) · [confidence interval](graph/confidence%20interval.md) · [variance](graph/variance.md) · …
- [Process](graph/Process.md)
  - [application development](application%20development.md) → [backend](backend.md) · [Frontend](graph/Frontend.md) · [Programming language](graph/Programming%20language.md) · [DevOps](graph/DevOps.md) · …
  - [data](graph/data.md) → [Data quality](graph/Data%20quality.md) · [data type](graph/data%20type.md) · [metadata](graph/metadata.md) · …
  - [Design thinking](graph/Design%20thinking.md) · [knowledge](graph/knowledge.md) · [Management](graph/Management.md) · …
- [Shareholders agreement](graph/Shareholders%20agreement.md) · [contract](graph/contract.md) · [negotiation](graph/negotiation.md)
- [spreadsheet](graph/spreadsheet.md) → [excel](graph/excel.md) · [google sheet](graph/google%20sheet.md) · [named-ranges](graph/named-ranges.md) · …
- [Vector space](graph/Vector%20space.md) → [Distance](graph/Distance.md) · [Cosine similarity](graph/Cosine%20similarity.md) · [Tensors](graph/Tensors.md) · [vector](graph/vector.md) · …
- [version control](graph/version%20control.md) → [Git](graph/Git.md) · [Repository](graph/Repository.md) · …
- *+ 20 more root concepts: [Data augmentation](graph/Data%20augmentation.md), [Data science team](graph/Data%20science%20team.md), [Decision support](graph/Decision%20support.md), [Dividual](graph/Dividual.md), [Graph algorithm](graph/Graph%20algorithm.md), [heuristic](graph/heuristic.md), [Kernel](graph/Kernel.md), [Metric](graph/Metric.md), [Modeling](graph/Modeling.md), [pattern](graph/pattern.md), [Pipelines](graph/Pipelines.md), [Product](graph/Product.md), [Prototyping](graph/Prototyping.md), [regression](graph/regression.md), [risk](graph/risk.md), [Schema design](graph/Schema%20design.md), [Search](graph/Search.md), [semantics](graph/semantics.md), [Stochastic processes](graph/Stochastic%20processes.md), [systems theory](graph/systems%20theory.md), …*

</details>

<br>

## 🚀 Getting Started

**Explore** — Open the `graph/` folder in [Obsidian](https://obsidian.md/) and use Graph View to navigate visually.

**Export** — Convert to other formats:

| Target | Method |
|---|---|
| **Neo4j** | Parse frontmatter into Cypher `CREATE` statements |
| **RDF/OWL** | Map `broader:` → `skos:broader`, relationship types → predicates |
| **JSON-LD** | Export as linked data for web interoperability |

<br>

---

<div align="center">
<sub>Built with <a href="https://obsidian.md/">Obsidian</a> · Reasoned with <a href="https://github.com/semantica-agi/semantica">Semantica</a> · Stats updated daily via [[GitHub]] Actions</sub>
</div>
