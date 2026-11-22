# Rapport de migration (à blanc)

Produit par `scripts/migrate.py --dry-run`. **Aucune note n'a été modifiée.** La migration réelle attend ta validation, puis tourne sur une branche, un commit par type de changement.

## Synthèse

| Changement | Occurrences |
|---|---|
| clé renommée vers le schéma | 1094 |
| clé déjà conforme | 130 |
| bloc `inferred:` sorti vers `inferred/` | 1029 |
| identifiant externe → `skos:closeMatch` | 42 |
| fait sur le monde → cache Wikidata | 120 |
| supprimé (maintenance, média, dérivé) | 96 |
| **hors schéma, à décider** | 299 |
| `skos:narrower` inversé en `skos:broader` sur la cible | 23 |

Notes touchées : **1000** / 1030.

## File de revue des arêtes `broader` (184)

Par défaut chaque arête devient `skos:broader` (rangement thématique). Pré-classement : à classer : 171, iso-thes:broaderGeneric : 9, iso-thes:broaderPartitive : 2, iso-thes:broaderInstantial : 1, kg:methodFor : 1.

| Source | Cible | Proposition | Fondement |
|---|---|---|---|
| [[recursive tree building]] | [[decision tree]] | kg:methodFor | verdict utilisateur |
| [[trainer]] | [[hugging face]] | iso-thes:broaderPartitive | verdict utilisateur |
| [[vanilla RAG design]] | [[RAG (Retrieval-Augmented Generation)]] | iso-thes:broaderGeneric | verdict utilisateur |
| [[active cell]] | [[spreadsheet]] | iso-thes:broaderPartitive | Wikidata Q59154568→Q183197 |
| [[backward chaining]] | [[Inference]] | iso-thes:broaderGeneric | Wikidata Q1141183→Q408386 |
| [[business process]] | [[process]] | iso-thes:broaderGeneric | Wikidata Q851587→Q3249551 |
| [[business process mapping]] | [[business process]] | iso-thes:broaderInstantial | Wikidata Q3298296→Q851587 |
| [[Business Process Model and Notation]] | [[diagram]] | iso-thes:broaderGeneric | Wikidata Q1017605→Q959962 |
| [[learning]] | [[process]] | iso-thes:broaderGeneric | Wikidata Q133500→Q3249551 |
| [[model contract]] | [[contract]] | iso-thes:broaderGeneric | Wikidata Q63032908→Q93288 |
| [[onboarding]] | [[process]] | iso-thes:broaderGeneric | Wikidata Q7091744→Q3249551 |
| [[thesaurus]] | [[knowledge organization system]] | iso-thes:broaderGeneric | Wikidata Q17152639→Q6423319 |
| [[training]] | [[learning]] | iso-thes:broaderGeneric | Wikidata Q918385→Q133500 |
| [[agent Role Type]] | [[agentic System]] | à classer | pas de Q-id aux deux extrémités |
| [[AI prompt]] | [[large language model]] | à classer | Wikidata Q117217619→Q115305900 : aucun lien P279/P31/P361 |
| [[AI stack]] | [[AI]] | à classer | pas de Q-id aux deux extrémités |
| [[application programming interface]] | [[application development]] | à classer | pas de Q-id aux deux extrémités |
| [[artifact management]] | [[Version control]] | à classer | pas de Q-id aux deux extrémités |
| [[artifact management]] | [[artifact]] | à classer | pas de Q-id aux deux extrémités |
| [[artificial neural network]] | [[deep learning]] | à classer | pas de Q-id aux deux extrémités |
| [[artificial neuron]] | [[artificial neural network]] | à classer | pas de Q-id aux deux extrémités |
| [[attention weights]] | [[Transformers]] | à classer | pas de Q-id aux deux extrémités |
| [[autoencoder]] | [[artificial neural network]] | à classer | pas de Q-id aux deux extrémités |
| [[autoML]] | [[machine learning]] | à classer | pas de Q-id aux deux extrémités |
| [[autoModel]] | [[hugging face]] | à classer | pas de Q-id aux deux extrémités |
| [[autotokenizer]] | [[hugging face]] | à classer | pas de Q-id aux deux extrémités |
| [[bag of words]] | [[Natural Language Processing]] | à classer | pas de Q-id aux deux extrémités |
| [[bargaining power]] | [[negotiation]] | à classer | pas de Q-id aux deux extrémités |
| [[batch prediction]] | [[Inference]] | à classer | pas de Q-id aux deux extrémités |
| [[bayesian epistemology]] | [[bayesian inference]] | à classer | pas de Q-id aux deux extrémités |
| [[bayesian inference]] | [[bayes' theorem]] | à classer | pas de Q-id aux deux extrémités |
| [[bayesian network]] | [[bayesian inference]] | à classer | pas de Q-id aux deux extrémités |
| [[best-classification-rate AI detection system]] | [[ML system]] | à classer | pas de Q-id aux deux extrémités |
| [[biological neural network]] | [[artificial neural network]] | à classer | pas de Q-id aux deux extrémités |
| [[boilerplate]] | [[application development]] | à classer | pas de Q-id aux deux extrémités |
| [[bundle]] | [[application development]] | à classer | pas de Q-id aux deux extrémités |
| [[calibration]] | [[model fit]] | à classer | pas de Q-id aux deux extrémités |
| [[Celery]] | [[backend]] | à classer | pas de Q-id aux deux extrémités |
| [[chain-of-thought]] | [[AI prompt]] | à classer | pas de Q-id aux deux extrémités |
| [[chainrings]] | [[combination]] | à classer | pas de Q-id aux deux extrémités |
| [[clause classification heuristic]] | [[clause]] | à classer | pas de Q-id aux deux extrémités |
| [[cold start problem]] | [[ML system]] | à classer | pas de Q-id aux deux extrémités |
| [[combination]] | [[combinatorics]] | à classer | pas de Q-id aux deux extrémités |
| [[comparag agent]] | [[agentic System]] | à classer | pas de Q-id aux deux extrémités |
| [[conceptual modeling]] | [[process]] | à classer | pas de Q-id aux deux extrémités |
| [[context]] | [[process]] | à classer | pas de Q-id aux deux extrémités |
| [[cosine similarity]] | [[similarity measure]] | à classer | pas de Q-id aux deux extrémités |
| [[countVectorizer]] | [[Python]] | à classer | pas de Q-id aux deux extrémités |
| [[crawl-walk-run]] | [[process]] | à classer | pas de Q-id aux deux extrémités |
| [[daily stand-ups]] | [[Agile approach]] | à classer | pas de Q-id aux deux extrémités |
| [[data leakage]] | [[Overfitting]] | à classer | pas de Q-id aux deux extrémités |
| [[data leakage]] | [[feature selection]] | à classer | pas de Q-id aux deux extrémités |
| [[data lineage]] | [[data]] | à classer | pas de Q-id aux deux extrémités |
| [[data preparation]] | [[CRISP-DM Process]] | à classer | pas de Q-id aux deux extrémités |
| [[data silos]] | [[data]] | à classer | pas de Q-id aux deux extrémités |
| [[datasetDict]] | [[hugging face]] | à classer | pas de Q-id aux deux extrémités |
| [[datasets]] | [[hugging face]] | à classer | pas de Q-id aux deux extrémités |
| [[decision tree]] | [[supervised learning]] | à classer | pas de Q-id aux deux extrémités |
| [[Decoder-only]] | [[Transformers]] | à classer | pas de Q-id aux deux extrémités |
| [[deep learning]] | [[machine learning]] | à classer | pas de Q-id aux deux extrémités |
| [[default]] | [[application development]] | à classer | pas de Q-id aux deux extrémités |
| [[delegation]] | [[management]] | à classer | pas de Q-id aux deux extrémités |
| [[Django]] | [[backend]] | à classer | pas de Q-id aux deux extrémités |
| [[Elixir]] | [[Programming language]] | à classer | pas de Q-id aux deux extrémités |
| [[Embedded methods]] | [[feature selection]] | à classer | pas de Q-id aux deux extrémités |
| [[Embedding network]] | [[artificial neural network]] | à classer | pas de Q-id aux deux extrémités |
| [[Embeddings]] | [[Natural Language Processing]] | à classer | pas de Q-id aux deux extrémités |
| [[Embeddings models]] | [[Embeddings]] | à classer | pas de Q-id aux deux extrémités |
| [[Encoder-only]] | [[Transformers]] | à classer | pas de Q-id aux deux extrémités |
| [[end-to-end test]] | [[Test]] | à classer | pas de Q-id aux deux extrémités |
| [[evaluate results]] | [[CRISP-DM Process]] | à classer | pas de Q-id aux deux extrémités |
| [[Excessive latency]] | [[ML system]] | à classer | pas de Q-id aux deux extrémités |
| [[Expert systems]] | [[Artificial Intelligence (AI)]] | à classer | pas de Q-id aux deux extrémités |
| [[facial recognition]] | [[computer vision]] | à classer | pas de Q-id aux deux extrémités |
| [[federated learning]] | [[machine learning]] | à classer | pas de Q-id aux deux extrémités |
| [[forward propagation]] | [[artificial neural network]] | à classer | pas de Q-id aux deux extrémités |
| [[Gilles Deleuze]] | [[dividual]] | à classer | pas de Q-id aux deux extrémités |
| [[gitHub actions]] | [[github]] | à classer | pas de Q-id aux deux extrémités |
| [[github ruleset]] | [[github]] | à classer | pas de Q-id aux deux extrémités |
| [[gouvernance]] | [[management]] | à classer | pas de Q-id aux deux extrémités |
| [[gramm-leach-bliley act (GLBA)]] | [[data privacy laws]] | à classer | pas de Q-id aux deux extrémités |
| [[Group K-Fold Cross Validation]] | [[cross validation]] | à classer | pas de Q-id aux deux extrémités |
| [[Hallucination]] | [[large language model]] | à classer | pas de Q-id aux deux extrémités |
| [[heuristics]] | [[heuristic]] | à classer | pas de Q-id aux deux extrémités |
| [[hugging face]] | [[Python]] | à classer | pas de Q-id aux deux extrémités |
| [[human-in-the-loop]] | [[agentic System]] | à classer | pas de Q-id aux deux extrémités |
| [[hypothetical document embeddings (HyDE)]] | [[RAG (Retrieval-Augmented Generation)]] | à classer | pas de Q-id aux deux extrémités |
| [[Identify factors]] | [[CRISP-DM Process]] | à classer | pas de Q-id aux deux extrémités |
| [[inference pipeline]] | [[Inference]] | à classer | pas de Q-id aux deux extrémités |
| [[instruction dataset]] | [[fine-tuning]] | à classer | pas de Q-id aux deux extrémités |
| [[Integration tests]] | [[Test]] | à classer | pas de Q-id aux deux extrémités |
| [[Jupyter notebooks]] | [[Python]] | à classer | pas de Q-id aux deux extrémités |
| [[K-Nearest neighbor regressor]] | [[K-Nearest Neighbor algorithm]] | à classer | pas de Q-id aux deux extrémités |
| [[Keras]] | [[deep learning]] | à classer | pas de Q-id aux deux extrémités |
| [[label encoding]] | [[data preparation]] | à classer | pas de Q-id aux deux extrémités |
| [[latent space]] | [[Embeddings]] | à classer | pas de Q-id aux deux extrémités |
| [[Logistic regression]] | [[Linear models]] | à classer | pas de Q-id aux deux extrémités |
| [[loss function]] | [[machine learning]] | à classer | pas de Q-id aux deux extrémités |
| [[Low-Rank Adaptation]] | [[fine-tuning]] | à classer | pas de Q-id aux deux extrémités |
| [[machine learning systems]] | [[ML system]] | à classer | pas de Q-id aux deux extrémités |
| [[management]] | [[process]] | à classer | pas de Q-id aux deux extrémités |
| [[management of PII]] | [[data privacy]] | à classer | pas de Q-id aux deux extrémités |
| [[matplotlib]] | [[Python]] | à classer | pas de Q-id aux deux extrémités |
| [[MCP host]] | [[Model Context Protocol (MCP)]] | à classer | pas de Q-id aux deux extrémités |
| [[MCP server]] | [[Model Context Protocol (MCP)]] | à classer | pas de Q-id aux deux extrémités |
| [[Min-max normalization]] | [[data preparation]] | à classer | pas de Q-id aux deux extrémités |
| [[ML system]] | [[machine learning]] | à classer | pas de Q-id aux deux extrémités |
| [[ML system design process]] | [[ML system]] | à classer | pas de Q-id aux deux extrémités |
| [[ML System failures]] | [[ML system]] | à classer | pas de Q-id aux deux extrémités |
| [[Modeling]] | [[CRISP-DM Process]] | à classer | pas de Q-id aux deux extrémités |
| [[multilayer perceptron]] | [[artificial neural network]] | à classer | pas de Q-id aux deux extrémités |
| [[Naive Bayes Classifier]] | [[supervised learning]] | à classer | pas de Q-id aux deux extrémités |
| [[Nano-precision detection system]] | [[ML system]] | à classer | pas de Q-id aux deux extrémités |
| [[Narrow AI]] | [[Artificial Intelligence (AI)]] | à classer | pas de Q-id aux deux extrémités |
| [[Natural Language Processing]] | [[Artificial Intelligence (AI)]] | à classer | pas de Q-id aux deux extrémités |
| [[neuron layer]] | [[artificial neural network]] | à classer | pas de Q-id aux deux extrémités |
| [[Numpy]] | [[Python]] | à classer | pas de Q-id aux deux extrémités |
| [[One-hot encoding]] | [[data preparation]] | à classer | pas de Q-id aux deux extrémités |
| [[Online prediction]] | [[Inference]] | à classer | pas de Q-id aux deux extrémités |
| [[openpyxl]] | [[Python]] | à classer | pas de Q-id aux deux extrémités |
| [[Pandas]] | [[Python]] | à classer | pas de Q-id aux deux extrémités |
| [[parsing]] | [[application development]] | à classer | pas de Q-id aux deux extrémités |
| [[performance indicator]] | [[performance metric]] | à classer | pas de Q-id aux deux extrémités |
| [[PostgreSQL]] | [[backend]] | à classer | pas de Q-id aux deux extrémités |
| [[prepare for modeling]] | [[CRISP-DM Process]] | à classer | pas de Q-id aux deux extrémités |
| [[price index]] | [[index]] | à classer | pas de Q-id aux deux extrémités |
| [[Prompt Identity]] | [[AI prompt]] | à classer | pas de Q-id aux deux extrémités |
| [[Prompt Optimization Techniques]] | [[AI prompt]] | à classer | pas de Q-id aux deux extrémités |
| [[Prompt Template Info]] | [[AI prompt]] | à classer | pas de Q-id aux deux extrémités |
| [[Prompt Template Types]] | [[AI prompt]] | à classer | pas de Q-id aux deux extrémités |
| [[prompt templates]] | [[AI prompt]] | à classer | pas de Q-id aux deux extrémités |
| [[prompt-based techniques]] | [[AI prompt]] | à classer | pas de Q-id aux deux extrémités |
| [[prompts]] | [[AI prompt]] | à classer | pas de Q-id aux deux extrémités |
| [[property]] | [[knowledge graph]] | à classer | pas de Q-id aux deux extrémités |
| [[pull request approval]] | [[Pull request]] | à classer | pas de Q-id aux deux extrémités |
| [[pydantic]] | [[Python]] | à classer | pas de Q-id aux deux extrémités |
| [[pypi]] | [[Python]] | à classer | pas de Q-id aux deux extrémités |
| [[Python]] | [[Programming language]] | à classer | pas de Q-id aux deux extrémités |
| [[PyTorch]] | [[Python]] | à classer | pas de Q-id aux deux extrémités |
| [[Quantile binning]] | [[Threshold value]] | à classer | pas de Q-id aux deux extrémités |
| [[Quantile binning]] | [[feature engineering]] | à classer | pas de Q-id aux deux extrémités |
| [[ReAct data agent]] | [[agentic System]] | à classer | pas de Q-id aux deux extrémités |
| [[Redis]] | [[backend]] | à classer | pas de Q-id aux deux extrémités |
| [[Regression trees]] | [[decision tree]] | à classer | pas de Q-id aux deux extrémités |
| [[Regularization]] | [[machine learning]] | à classer | pas de Q-id aux deux extrémités |
| [[Reinforcement Learning]] | [[machine learning]] | à classer | pas de Q-id aux deux extrémités |
| [[ReLU activation function]] | [[artificial neural network]] | à classer | pas de Q-id aux deux extrémités |
| [[reproducibility]] | [[ML system]] | à classer | pas de Q-id aux deux extrémités |
| [[required status check]] | [[github]] | à classer | pas de Q-id aux deux extrémités |
| [[sci-kit Learn]] | [[Python]] | à classer | pas de Q-id aux deux extrémités |
| [[sentiment analysis]] | [[Natural Language Processing]] | à classer | pas de Q-id aux deux extrémités |
| [[Shifter]] | [[combination]] | à classer | pas de Q-id aux deux extrémités |
| [[Sigmoid function]] | [[artificial neural network]] | à classer | pas de Q-id aux deux extrémités |
| [[SpaCy]] | [[Python]] | à classer | pas de Q-id aux deux extrémités |
| [[sparkline]] | [[spreadsheet]] | à classer | Wikidata Q2307841→Q183197 : aucun lien P279/P31/P361 |
| [[SSH Agent]] | [[infrastructure]] | à classer | pas de Q-id aux deux extrémités |
| [[stateless protocol]] | [[stateless]] | à classer | pas de Q-id aux deux extrémités |
| [[supervised learning]] | [[machine learning]] | à classer | pas de Q-id aux deux extrémités |
| [[Support Vector Machine]] | [[supervised learning]] | à classer | pas de Q-id aux deux extrémités |
| [[system prompt]] | [[AI prompt]] | à classer | pas de Q-id aux deux extrémités |
| [[Target's pregnancy prediction]] | [[prediction]] | à classer | pas de Q-id aux deux extrémités |
| [[Théorie du cerveau bayésien]] | [[bayesian inference]] | à classer | pas de Q-id aux deux extrémités |
| [[Tidy Data]] | [[data preparation]] | à classer | pas de Q-id aux deux extrémités |
| [[Time-shifted scoring]] | [[feature engineering]] | à classer | pas de Q-id aux deux extrémités |
| [[token]] | [[Natural Language Processing]] | à classer | pas de Q-id aux deux extrémités |
| [[Tokenizer]] | [[Natural Language Processing]] | à classer | pas de Q-id aux deux extrémités |
| [[Toolkits]] | [[agentic System]] | à classer | pas de Q-id aux deux extrémités |
| [[Tooth]] | [[combination]] | à classer | pas de Q-id aux deux extrémités |
| [[Training algorithm]] | [[machine learning]] | à classer | pas de Q-id aux deux extrémités |
| [[TrainingAguments]] | [[hugging face]] | à classer | pas de Q-id aux deux extrémités |
| [[Transfer learning]] | [[deep learning]] | à classer | pas de Q-id aux deux extrémités |
| [[Transformers]] | [[deep learning]] | à classer | pas de Q-id aux deux extrémités |
| [[tree depth]] | [[decision tree]] | à classer | pas de Q-id aux deux extrémités |
| [[truncation]] | [[data preparation]] | à classer | pas de Q-id aux deux extrémités |
| [[Unit tests]] | [[Test]] | à classer | pas de Q-id aux deux extrémités |
| [[Unsloth]] | [[fine-tuning]] | à classer | pas de Q-id aux deux extrémités |
| [[Unsupervised Learning]] | [[machine learning]] | à classer | pas de Q-id aux deux extrémités |
| [[vector index]] | [[index]] | à classer | pas de Q-id aux deux extrémités |
| [[vectorization]] | [[Embeddings]] | à classer | pas de Q-id aux deux extrémités |
| [[Virtual Environment]] | [[Python]] | à classer | pas de Q-id aux deux extrémités |
| [[Weights]] | [[artificial neural network]] | à classer | pas de Q-id aux deux extrémités |
| [[Word embeddings]] | [[Embeddings]] | à classer | pas de Q-id aux deux extrémités |
| [[workflow recursion guard]] | [[gitHub actions]] | à classer | pas de Q-id aux deux extrémités |
| [[Z-Score normalization]] | [[data preparation]] | à classer | pas de Q-id aux deux extrémités |

## Clés hors schéma (236 clés)

Décision par clé : la projeter sur une propriété, la mettre en cache, ou la supprimer. Règle validée : une clé rare n'entre au schéma que si une question de compétence en a besoin.

| Clé | Notes |
|---|---|
| `inspiredBy` | 4 : [[Inference engine]], [[Reinforcement Learning]], [[Support Vector Machine]], [[artificial neuron]] |
| `algorithms` | 3 : [[Reinforcement Learning]], [[decision tree]], [[federated learning]] |
| `applies to jurisdiction` | 3 : [[french commercial code]], [[société anonyme]], [[société par actions simplifiée]] |
| `Commons gallery` | 3 : [[control theory]], [[lawyer]], [[periodic table]] |
| `country` | 3 : [[action de préférence]], [[cease and desist]], [[french commercial code]] |
| `enables` | 3 : [[Pipelines]], [[federated learning]], [[multilayer perceptron]] |
| `has goal` | 3 : [[access control]], [[shareholder]], [[thesaurus]] |
| `influenced by` | 3 : [[Elixir]], [[Gilles Deleuze]], [[Markdown]] |
| `official website` | 3 : [[Elixir]], [[Ollama]], [[pypi]] |
| `originatesFrom` | 3 : [[Expert systems]], [[deep learning]], [[graph]] |
| `PhilPapers topic` | 3 : [[Gilles Deleuze]], [[Inference]], [[semantics]] |
| `properties` | 3 : [[Embeddings]], [[Word embeddings]], [[loss function]] |
| `properties for this type` | 3 : [[knowledge organization system]], [[occurrence]], [[process]] |
| `UMLS CUI` | 3 : [[intention]], [[lawyer]], [[problem solving]] |
| `usedFor` | 3 : [[PyTorch]], [[Support Vector Machine]], [[decision tree]] |
| `Wolfram Language entity code` | 3 : [[Gilles Deleuze]], [[bipartite graph]], [[classification scheme]] |
| `author` | 2 : [[Domain-Driven Design]], [[The Book of Why]] |
| `based on` | 2 : [[knowledge organization system]], [[periodic table]] |
| `builtOnTopOf` | 2 : [[Query engine]], [[Théorie du cerveau bayésien]] |
| `copyright license` | 2 : [[Elixir]], [[Ollama]] |
| `copyright status` | 2 : [[Elixir]], [[Ollama]] |
| `depicts` | 2 : [[Business Process Model and Notation]], [[periodic table]] |
| `described at URL` | 2 : [[classification scheme]], [[thesaurus]] |
| `does not have part` | 2 : [[bipartite graph]], [[periodic table]] |
| `entity` | 2 : [[Embeddings]], [[push_to_comet]] |
| `fabrication method` | 2 : [[AI prompt]], [[management]] |
| `female form of label` | 2 : [[business analyst]], [[lawyer]] |
| `field of this occupation` | 2 : [[lawyer]], [[statutory auditor]] |
| `followed by` | 2 : [[control theory]], [[draft document]] |
| `GitHub account` | 2 : [[Elixir]], [[Ollama]] |
| `handled, mitigated, or managed by` | 2 : [[conflict of interest]], [[problem]] |
| `history of topic` | 2 : [[Physics]], [[periodic table]] |
| `ISCO-08 occupation class` | 2 : [[business analyst]], [[lawyer]] |
| `language of work or name` | 2 : [[Domain-Driven Design]], [[International (Nice) Classification of Goods and Services]] |
| `literal translation` | 2 : [[backward chaining]], [[share purchase agreement]] |
| `MacPorts port` | 2 : [[Elixir]], [[Ollama]] |
| `male form of label` | 2 : [[business analyst]], [[lawyer]] |
| `name` | 2 : [[application programming interface]], [[thesaurus]] |
| `platform` | 2 : [[Elixir]], [[Ollama]] |
| `Provenio UUID` | 2 : [[lawyer]], [[semiotics]] |
| `same` | 2 : [[One-hot encoding]], [[label encoding]] |
| `software version identifier` | 2 : [[Elixir]], [[Ollama]] |
| `source code repository URL` | 2 : [[Elixir]], [[Ollama]] |
| `subreddit` | 2 : [[Gilles Deleuze]], [[application programming interface]] |
| `techniques` | 2 : [[Natural Language Processing]], [[Word embeddings]] |
| `topic's main template` | 2 : [[control theory]], [[management]] |
| `3D model` | 1 : [[periodic table]] |
| `academic degree` | 1 : [[Gilles Deleuze]] |
| `accelerates` | 1 : [[Transfer learning]] |
| `ACM Classification Code (2012)` | 1 : [[use case]] |
| `advantages` | 1 : [[ReLU activation function]] |
| `affecte` | 1 : [[Hallucination]] |
| `alternativeTo` | 1 : [[PyTorch]] |
| `applications` | 1 : [[Natural Language Processing]] |
| `Arch Linux package` | 1 : [[Elixir]] |
| `ArchWiki article` | 1 : [[Elixir]] |
| `articulates` | 1 : [[vanilla RAG design]] |
| `assessment` | 1 : [[Gilles Deleuze]] |
| `atWorkWithin` | 1 : [[empirical evidence]] |
| `AUR package` | 1 : [[Elixir]] |
| `Baidu Tieba name` | 1 : [[lawyer]] |
| `benefitFrom` | 1 : [[Transfer learning]] |
| `BHCL UUID` | 1 : [[Gilles Deleuze]] |
| `calculationUnder` | 1 : [[cosine similarity]] |
| `category for eponymous categories` | 1 : [[lawyer]] |
| `challenges` | 1 : [[federated learning]] |
| `Changes` | 1 : [[Shifter]] |
| `child` | 1 : [[Gilles Deleuze]] |
| `class of object(s) of occurrence` | 1 : [[management]] |
| `Colon Classification` | 1 : [[periodic table]] |
| `communicatesWith` | 1 : [[Observations]] |
| `compatible with` | 1 : [[Model Context Protocol (MCP)]] |
| `ComplementaryWith` | 1 : [[training data set]] |
| `complementedBy` | 1 : [[forward propagation]] |
| `computedBy` | 1 : [[attention weights]] |
| `concepts` | 1 : [[accountability]] |
| `connectsFrom` | 1 : [[prompt templates]] |
| `connectsThrough` | 1 : [[Layer]] |
| `connectsTo` | 1 : [[prompt templates]] |
| `country of citizenship` | 1 : [[Gilles Deleuze]] |
| `country of origin` | 1 : [[periodic table]] |
| `creates` | 1 : [[vectorization]] |
| `date of birth` | 1 : [[Gilles Deleuze]] |
| `date of death` | 1 : [[Gilles Deleuze]] |
| `Debian stable package` | 1 : [[Elixir]] |
| `depicted by` | 1 : [[periodic table]] |
| `developer` | 1 : [[Elixir]] |
| `disjoint union of` | 1 : [[change]] |
| `Docker Hub repository` | 1 : [[Elixir]] |
| `doctoral student` | 1 : [[Gilles Deleuze]] |
| `does not have characteristic` | 1 : [[primary commodity]] |
| `does not use` | 1 : [[modular programming]] |
| `educated at` | 1 : [[Gilles Deleuze]] |
| `EmbodiementOf` | 1 : [[latent space]] |
| `employer` | 1 : [[Gilles Deleuze]] |
| `enablesArchitecture` | 1 : [[Transformers]] |
| `Europeana entity` | 1 : [[Gilles Deleuze]] |
| `example` | 1 : [[model contract]] |
| `example in` | 1 : [[boilerplate]] |
| `exampleOf` | 1 : [[Best]] |
| `examples` | 1 : [[loss function]] |
| `extendedBy` | 1 : [[decision tree]] |
| `family name` | 1 : [[Gilles Deleuze]] |
| `featureOf` | 1 : [[model lineage]] |
| `Fedora package` | 1 : [[Elixir]] |
| `file extension` | 1 : [[Elixir]] |
| `firstDescribedby` | 1 : [[control theory]] |
| `firstStepOf` | 1 : [[Virtual Environment]] |
| `foundationFor` | 1 : [[Transformers]] |
| `FreeBSD port` | 1 : [[Elixir]] |
| `fundamentalTo` | 1 : [[accountability]] |
| `Gentoo package` | 1 : [[Elixir]] |
| `Gentoo Wiki article` | 1 : [[Elixir]] |
| `given name` | 1 : [[Gilles Deleuze]] |
| `goesOnInside` | 1 : [[attention weights]] |
| `Gujarati Vishwakosh entry` | 1 : [[periodic table]] |
| `Harper's tag` | 1 : [[logical contradiction]] |
| `has contributing factor` | 1 : [[contract]] |
| `has list` | 1 : [[commodity]] |
| `has version, edition or translation` | 1 : [[Domain-Driven Design]] |
| `hasUse` | 1 : [[PostgreSQL]] |
| `HeuristicFor` | 1 : [[Tidy Data]] |
| `Homebrew formula name` | 1 : [[Elixir]] |
| `IAB code` | 1 : [[commodity]] |
| `IdenticalTo` | 1 : [[chainrings]] |
| `IEV number` | 1 : [[discrimination threshold]] |
| `implementations` | 1 : [[Pipelines]] |
| `implements` | 1 : [[Transfer learning]] |
| `importPartOf` | 1 : [[Identify factors]] |
| `integratesWith` | 1 : [[PyTorch]] |
| `InterlockWith` | 1 : [[Tooth]] |
| `introducedin` | 1 : [[Transformers]] |
| `inventedBy` | 1 : [[artificial neuron]] |
| `involves` | 1 : [[management]] |
| `IRC channel URL` | 1 : [[Elixir]] |
| `ISCO-88 occupation class` | 1 : [[lawyer]] |
| `ISNI` | 1 : [[Gilles Deleuze]] |
| `items classified` | 1 : [[periodic table]] |
| `keyComponents` | 1 : [[Reinforcement Learning]] |
| `label in sign language` | 1 : [[lawyer]] |
| `languages spoken, written or signed` | 1 : [[Gilles Deleuze]] |
| `Libris-URI` | 1 : [[Gilles Deleuze]] |
| `location of creation` | 1 : [[periodic table]] |
| `made from material` | 1 : [[blueprint]] |
| `madeOf` | 1 : [[AI stack]] |
| `main regulatory text` | 1 : [[preferred stock]] |
| `maintained by` | 1 : [[pypi]] |
| `manner of death` | 1 : [[Gilles Deleuze]] |
| `media type` | 1 : [[Elixir]] |
| `MethodInside` | 1 : [[push_to_comet]] |
| `minimizedBy` | 1 : [[loss function]] |
| `mitigated_by` | 1 : [[Hallucination]] |
| `MountedInParallel` | 1 : [[chainrings]] |
| `movement` | 1 : [[Gilles Deleuze]] |
| `name in native language` | 1 : [[Gilles Deleuze]] |
| `native language` | 1 : [[Gilles Deleuze]] |
| `needs` | 1 : [[gouvernance]] |
| `Nomenclature for Museum Cataloging` | 1 : [[spreadsheet]] |
| `notable work` | 1 : [[Gilles Deleuze]] |
| `notation` | 1 : [[tautology]] |
| `number of children` | 1 : [[Gilles Deleuze]] |
| `O*NET OnLine code` | 1 : [[lawyer]] |
| `occupation` | 1 : [[Gilles Deleuze]] |
| `official blog URL` | 1 : [[Elixir]] |
| `on focus list of Wikimedia project` | 1 : [[AI prompt]] |
| `OpenBSD port` | 1 : [[Elixir]] |
| `OpenStreetMap key` | 1 : [[lawyer]] |
| `OpenStreetMap tag` | 1 : [[lawyer]] |
| `openSUSE package` | 1 : [[Elixir]] |
| `operatesOn` | 1 : [[PyTorch]] |
| `operating system` | 1 : [[Elixir]] |
| `outputs` | 1 : [[clause classification heuristic]] |
| `owner of` | 1 : [[shareholder]] |
| `participant` | 1 : [[contract]] |
| `partner in business or sport` | 1 : [[Gilles Deleuze]] |
| `patron saint` | 1 : [[lawyer]] |
| `permanent duplicated item` | 1 : [[periodic table]] |
| `place of birth` | 1 : [[Gilles Deleuze]] |
| `place of burial` | 1 : [[Gilles Deleuze]] |
| `place of death` | 1 : [[Gilles Deleuze]] |
| `position held by head of the organization` | 1 : [[board of directors]] |
| `prevents` | 1 : [[Regularization]] |
| `processes` | 1 : [[Transformers]] |
| `produces` | 1 : [[forward propagation]] |
| `product of` | 1 : [[conceptual model]] |
| `programming paradigm` | 1 : [[Elixir]] |
| `protects` | 1 : [[federated learning]] |
| `publicationDate` | 1 : [[PostgreSQL]] |
| `publisher` | 1 : [[Business Process Model and Notation]] |
| `readable file format` | 1 : [[Elixir]] |
| `reduces` | 1 : [[Regularization]] |
| `reducesNeedFor` | 1 : [[Transfer learning]] |
| `related image` | 1 : [[application programming interface]] |
| `related Wikidata property` | 1 : [[occurrence]] |
| `relative` | 1 : [[Gilles Deleuze]] |
| `relevant qualification` | 1 : [[business analyst]] |
| `religion or worldview` | 1 : [[Gilles Deleuze]] |
| `reliéA` | 1 : [[Hallucination]] |
| `Repology project name` | 1 : [[Elixir]] |
| `represents` | 1 : [[Embeddings]] |
| `resultsIn` | 1 : [[AI]] |
| `ROME Occupation Code` | 1 : [[lawyer]] |
| `sex or gender` | 1 : [[Gilles Deleuze]] |
| `shouldPayAttentionTo` | 1 : [[ML system design process]] |
| `shouldTakeIntoAccount` | 1 : [[false positives and false negatives]] |
| `signature` | 1 : [[Gilles Deleuze]] |
| `significant person` | 1 : [[data visualization]] |
| `SlackBuilds package` | 1 : [[Elixir]] |
| `SOC Code (2010)` | 1 : [[lawyer]] |
| `social media followers` | 1 : [[Elixir]] |
| `software engine` | 1 : [[pypi]] |
| `specificInstanceOf` | 1 : [[ReAct data agent]] |
| `spouse` | 1 : [[Gilles Deleuze]] |
| `SSYK 2012 The Swedish Standard Classification of Occupations` | 1 : [[lawyer]] |
| `storedInto` | 1 : [[Embeddings]] |
| `student of` | 1 : [[Gilles Deleuze]] |
| `subject has role` | 1 : [[knowledge organization system]] |
| `subtitle` | 1 : [[Domain-Driven Design]] |
| `supports` | 1 : [[PyTorch]] |
| `time period` | 1 : [[Gilles Deleuze]] |
| `trainedBy` | 1 : [[multilayer perceptron]] |
| `trainingTechnique` | 1 : [[forward propagation]] |
| `typing discipline` | 1 : [[Elixir]] |
| `U.S. National Archives Identifier` | 1 : [[lawyer]] |
| `Ubuntu package` | 1 : [[Elixir]] |
| `Unicode character` | 1 : [[lawyer]] |
| `union of` | 1 : [[process]] |
| `usedBy` | 1 : [[pydantic]] |
| `useTechniques` | 1 : [[Natural Language Processing]] |
| `variants` | 1 : [[ReLU activation function]] |
| `wears` | 1 : [[lawyer]] |
| `Wikimedia outline` | 1 : [[semiotics]] |
| `WordLift URL` | 1 : [[management]] |
| `writable file format` | 1 : [[Elixir]] |
| `writing language` | 1 : [[Gilles Deleuze]] |
| `X (Twitter) username` | 1 : [[Elixir]] |

## Détail par note

- **[[_.claude]]** : `inferred:skos:ancestor` → `inferred/_.claude.json`
- **[[_.claude.json.mcpServers]]** : `inferred:skos:ancestor` → `inferred/_.claude.json.mcpServers.json`
- **[[abstract entity]]** : `inferred:skos:narrower` → `inferred/abstract entity.json`
- **[[abuse of majority]]** : `inferred:skos:ancestor` → `inferred/abuse of majority.json`
- **[[access control]]** : `wikidata entity id: Q228502` → `skos:exactMatch: wd:Q228502` ; `subclass of` → `iso-thes:broaderGeneric` ; `has goal` → **à décider** (hors schéma)
- **[[accountability]]** : `foundationalPaper` → `dcterms:isReferencedBy` ; `relatedTo` → `skos:related` ; `fundamentalTo` → **à décider** (hors schéma) ; `concepts` → **à décider** (hors schéma)
- **[[accountable AI]]** : `inferred:skos:ancestor` → `inferred/accountable AI.json`
- **[[accounts receivable]]** : `wikidata entity id: Q328554` → `skos:exactMatch: wd:Q328554` ; `subclass of` → `iso-thes:broaderGeneric` ; `used by` → `kg:usedBy`
- **[[accuracy]]** : `inferred:skos:ancestor` → `inferred/accuracy.json`
- **[[action]]** : `studied by` → `cache/wikidata.jsonl` (fait sur le monde) ; `different from` → `skos:scopeNote` (« différent de … ») ; `has effect` → `cache/wikidata.jsonl` (fait sur le monde) ; `subclass of` → `iso-thes:broaderGeneric` ; `part of` → `iso-thes:broaderPartitive` ; `described by source` → `dcterms:isReferencedBy` ; `has characteristic` → `cache/wikidata.jsonl` (fait sur le monde) ; `instance of` → `iso-thes:broaderInstantial` ; `OmegaWiki Defined Meaning` → `skos:closeMatch` ; `pronunciation audio` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `equivalent class` → `skos:closeMatch` ; `wikidata entity id: Q4026292` → `skos:exactMatch: wd:Q4026292` ; `inferred:skos:ancestor` → `inferred/action.json`
- **[[action de préférence]]** : `country` → **à décider** (hors schéma) ; `different from` → `skos:scopeNote` (« différent de … ») ; `subclass of` → `iso-thes:broaderGeneric` ; `wikidata entity id: Q2823672` → `skos:exactMatch: wd:Q2823672`
- **[[action module]]** : `inferred:skos:ancestor` → `inferred/action module.json`
- **[[activatesShifter]]** : `inferred:skos:ancestor` → `inferred/activatesShifter.json`
- **[[active cell]]** : `part of` → `iso-thes:broaderPartitive` ; `has characteristic` → `cache/wikidata.jsonl` (fait sur le monde) ; `subclass of` → `iso-thes:broaderGeneric` ; `wikidata entity id: Q59154568` → `skos:exactMatch: wd:Q59154568` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/active cell.json`
- **[[activity log]]** : `wikidata entity id: Q107343483` → `skos:exactMatch: wd:Q107343483` ; `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/activity log.json` ; `inferred:skos:narrower` → `inferred/activity log.json`
- **[[adar-Adamic index]]** : `inferred:skos:ancestor` → `inferred/adar-Adamic index.json`
- **[[add]]** : `inferred:skos:ancestor` → `inferred/add.json`
- **[[adjacency matrix]]** : `inferred:skos:ancestor` → `inferred/adjacency matrix.json` ; `inferred:skos:broader` → `inferred/adjacency matrix.json`
- **[[agency]]** : `inferred:skos:narrower` → `inferred/agency.json`
- **[[agent]]** : `dependencies` → `kg:dependsOn` ; `rdf:type: skos:Concept` → `dcterms:type: Concept` ; `skos:narrower` → retiré ; chaque cible reçoit `skos:broader: [[agent]]` ; `inferred:skos:narrower` → `inferred/agent.json`
- **[[agent harness]]** : `inferred:skos:ancestor` → `inferred/agent harness.json` ; `inferred:skos:broader` → `inferred/agent harness.json`
- **[[agent identity]]** : `inferred:skos:ancestor` → `inferred/agent identity.json`
- **[[agent observability]]** : `inferred:skos:related` → `inferred/agent observability.json`
- **[[agent Role Type]]** : `related_to` → `skos:related` ; `dependencies` → `kg:dependsOn` ; `components` → `has part` ; `category` → `dcterms:subject` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/agent Role Type.json`
- **[[agentic System]]** : `inferred:skos:narrower` → `inferred/agentic System.json`
- **[[agentOps]]** : `inferred:skos:ancestor` → `inferred/agentOps.json`
- **[[agents.md]]** : `wikidata entity id: Q136229882` → `skos:exactMatch: wd:Q136229882` ; `subclass of` → `iso-thes:broaderGeneric` ; `has use` → `kg:hasUse` ; `inferred:skos:ancestor` → `inferred/agents.md.json`
- **[[Agile approach]]** : `inferred:skos:narrower` → `inferred/Agile approach.json`
- **[[AI]]** : `resultsIn` → **à décider** (hors schéma) ; `inferred:skos:narrower` → `inferred/AI.json`
- **[[AI agent]]** : `inferred:skos:ancestor` → `inferred/AI agent.json` ; `inferred:skos:broader` → `inferred/AI agent.json` ; `inferred:skos:related` → `inferred/AI agent.json`
- **[[AI engineering]]** : `inferred:skos:ancestor` → `inferred/AI engineering.json`
- **[[AI Hierarchy of needs]]** : `inferred:skos:ancestor` → `inferred/AI Hierarchy of needs.json`
- **[[AI prompt]]** : `subclass of` → `iso-thes:broaderGeneric` ; `facet of` → `skos:broader` ; `fabrication method` → **à décider** (hors schéma) ; `on focus list of Wikimedia project` → **à décider** (hors schéma) ; `used by` → `kg:usedBy` ; `has part(s)` → `has part` ; `main Wikidata property` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `wikidata entity id: Q117217619` → `skos:exactMatch: wd:Q117217619` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/AI prompt.json` ; `inferred:skos:narrower` → `inferred/AI prompt.json` ; `inferred:skos:related` → `inferred/AI prompt.json`
- **[[AI Proof detection model]]** : `inferred:skos:ancestor` → `inferred/AI Proof detection model.json`
- **[[AI stack]]** : `madeOf` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/AI stack.json`
- **[[algorithm]]** : `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/algorithm.json`
- **[[algorithm selection]]** : `inferred:skos:ancestor` → `inferred/algorithm selection.json` ; `inferred:skos:broader` → `inferred/algorithm selection.json`
- **[[alias]]** : `inferred:skos:ancestor` → `inferred/alias.json`
- **[[API toolset]]** : `inferred:skos:narrower` → `inferred/API toolset.json`
- **[[app script]]** : `inferred:skos:ancestor` → `inferred/app script.json`
- **[[application development]]** : `inferred:skos:narrower` → `inferred/application development.json`
- **[[application programming interface]]** : `field of work` → `cache/wikidata.jsonl` (fait sur le monde) ; `facet of` → `skos:broader` ; `subclass of` → `iso-thes:broaderGeneric` ; `instance of` → `iso-thes:broaderInstantial` ; `has use` → `kg:hasUse` ; `used by` → `kg:usedBy` ; `described by source` → `dcterms:isReferencedBy` ; `OmegaWiki Defined Meaning` → `skos:closeMatch` ; `subreddit` → **à décider** (hors schéma) ; `GitHub topic` → `skos:closeMatch` ; `short name` → `skos:altLabel` ; `related image` → **à décider** (hors schéma) ; `exact match` → `skos:exactMatch` ; `Stack Exchange tag` → `skos:closeMatch` ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `name` → **à décider** (hors schéma) ; `wikidata entity id: Q165194` → `skos:exactMatch: wd:Q165194` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/application programming interface.json`
- **[[araph algorithm]]** : `inferred:skos:narrower` → `inferred/araph algorithm.json`
- **[[arc]]** : `inferred:skos:ancestor` → `inferred/arc.json` ; `inferred:skos:broader` → `inferred/arc.json`
- **[[articles of association]]** : `described by source` → `dcterms:isReferencedBy` ; `different from` → `skos:scopeNote` (« différent de … ») ; `facet of` → `skos:broader` ; `named after` → `cache/wikidata.jsonl` (fait sur le monde) ; `subclass of` → `iso-thes:broaderGeneric` ; `wikidata entity id: Q3497659` → `skos:exactMatch: wd:Q3497659` ; `inferred:skos:ancestor` → `inferred/articles of association.json`
- **[[artifact]]** : `inferred:skos:narrower` → `inferred/artifact.json`
- **[[artifact management]]** : `inferred:skos:ancestor` → `inferred/artifact management.json` ; `inferred:skos:broader` → `inferred/artifact management.json`
- **[[Artificial Intelligence (AI)]]** : `inferred:skos:narrower` → `inferred/Artificial Intelligence (AI).json`
- **[[artificial neural network]]** : `has part(s)` → `has part` ; `instance of` → `iso-thes:broaderInstantial` ; `different from` → `skos:scopeNote` (« différent de … ») ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/artificial neural network.json` ; `inferred:skos:narrower` → `inferred/artificial neural network.json`
- **[[artificial neuron]]** : `foundationalPaper` → `dcterms:isReferencedBy` ; `keyPapers` → `dcterms:isReferencedBy` ; `inventedBy` → **à décider** (hors schéma) ; `inspiredBy` → **à décider** (hors schéma) ; `components` → `has part` ; `usedIn` → `kg:usedBy` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/artificial neuron.json`
- **[[attention weights]]** : `foundationalPaper` → `dcterms:isReferencedBy` ; `keyPapers` → `dcterms:isReferencedBy` ; `goesOnInside` → **à décider** (hors schéma) ; `usedIn` → `kg:usedBy` ; `computedBy` → **à décider** (hors schéma) ; `relatedTo` → `skos:related` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/attention weights.json`
- **[[audit]]** : `wikidata entity id: Q181487` → `skos:exactMatch: wd:Q181487` ; `part of` → `iso-thes:broaderPartitive`
- **[[audit trail]]** : `wikidata entity id: Q1047174` → `skos:exactMatch: wd:Q1047174` ; `subclass of` → `iso-thes:broaderGeneric` ; `facet of` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/audit trail.json`
- **[[audit-notes]]** : `rdf:type: Research Note` → `dcterms:type: Concept` (à confirmer : note de recherche) ; `title` → `skos:prefLabel` ; `description` → `skos:definition` ; `timestamp` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `instanceOf` → `iso-thes:broaderInstantial`
- **[[augmentation]]** : `inferred:skos:narrower` → `inferred/augmentation.json`
- **[[authentication]]** : `wikidata entity id: Q212108` → `skos:exactMatch: wd:Q212108`
- **[[authentication protocol]]** : `inferred:skos:narrower` → `inferred/authentication protocol.json`
- **[[autoencoder]]** : `subclass of` → `iso-thes:broaderGeneric` ; `facet of` → `skos:broader` ; `foundationalPaper` → `dcterms:isReferencedBy` ; `keyPapers` → `dcterms:isReferencedBy` ; `relatedTo` → `skos:related` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/autoencoder.json`
- **[[Automation]]** : `inferred:skos:narrower` → `inferred/Automation.json`
- **[[automation framework]]** : `inferred:skos:ancestor` → `inferred/automation framework.json`
- **[[autoML]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/autoML.json`
- **[[autoModel]]** : `partOf` → `iso-thes:broaderPartitive` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/autoModel.json`
- **[[autonomy]]** : `inferred:skos:ancestor` → `inferred/autonomy.json`
- **[[autopilot]]** : `wikidata entity id: Q220858` → `skos:exactMatch: wd:Q220858`
- **[[autoregressive language models]]** : `inferred:skos:narrower` → `inferred/autoregressive language models.json`
- **[[autotokenizer]]** : `partOf` → `iso-thes:broaderPartitive` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/autotokenizer.json`
- **[[backend]]** : `inferred:skos:narrower` → `inferred/backend.json`
- **[[backpropagation]]** : `inferred:skos:narrower` → `inferred/backpropagation.json`
- **[[backward chaining]]** : `subclass of` → `iso-thes:broaderGeneric` ; `opposite of` → `kg:oppositeOf` ; `instance of` → `iso-thes:broaderInstantial` ; `literal translation` → **à décider** (hors schéma) ; `wikidata entity id: Q1141183` → `skos:exactMatch: wd:Q1141183` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/backward chaining.json` ; `inferred:skos:broader` → `inferred/backward chaining.json`
- **[[bag of words]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/bag of words.json`
- **[[bargaining power]]** : `facet of` → `skos:broader` ; `subclass of` → `iso-thes:broaderGeneric` ; `wikidata entity id: Q2625018` → `skos:exactMatch: wd:Q2625018` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/bargaining power.json`
- **[[batch gradient descent]]** : `inferred:skos:ancestor` → `inferred/batch gradient descent.json`
- **[[batch prediction]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/batch prediction.json` ; `inferred:skos:broader` → `inferred/batch prediction.json`
- **[[bayes' theorem]]** : `inferred:skos:narrower` → `inferred/bayes' theorem.json`
- **[[bayesian epistemology]]** : `uses` → `kg:uses` ; `subclass of` → `iso-thes:broaderGeneric` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/bayesian epistemology.json`
- **[[bayesian inference]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/bayesian inference.json` ; `inferred:skos:narrower` → `inferred/bayesian inference.json`
- **[[bayesian network]]** : `named after` → `cache/wikidata.jsonl` (fait sur le monde) ; `instance of` → `iso-thes:broaderInstantial` ; `OmegaWiki Defined Meaning` → `skos:closeMatch` ; `image` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `GitHub topic` → `skos:closeMatch` ; `Dewey Decimal Classification` → `dcterms:subject` ; `wikidata entity id: Q812540` → `skos:exactMatch: wd:Q812540` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/bayesian network.json`
- **[[belief revision]]** : `wikidata entity id: Q3566063` → `skos:exactMatch: wd:Q3566063` ; `part of` → `iso-thes:broaderPartitive`
- **[[BERT]]** : `inferred:skos:narrower` → `inferred/BERT.json`
- **[[bespoke]]** : `inferred:skos:ancestor` → `inferred/bespoke.json`
- **[[Best]]** : `exampleOf` → **à décider** (hors schéma)
- **[[best practice]]** : `wikidata entity id: Q830382` → `skos:exactMatch: wd:Q830382` ; `facet of` → `skos:broader`
- **[[best-classification-rate AI detection system]]** : `instanceof` → `iso-thes:broaderInstantial` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/best-classification-rate AI detection system.json`
- **[[beta testing]]** : `inferred:skos:ancestor` → `inferred/beta testing.json`
- **[[betweenness centrality]]** : `inferred:skos:ancestor` → `inferred/betweenness centrality.json` ; `inferred:skos:broader` → `inferred/betweenness centrality.json`
- **[[bias]]** : `inferred:skos:narrower` → `inferred/bias.json`
- **[[bijectivity]]** : `inferred:skos:ancestor` → `inferred/bijectivity.json`
- **[[biological neural network]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/biological neural network.json`
- **[[bipartite graph]]** : `studied by` → `cache/wikidata.jsonl` (fait sur le monde) ; `has part(s) of the class` → `cache/wikidata.jsonl` (fait sur le monde) ; `subclass of` → `iso-thes:broaderGeneric` ; `has characteristic` → `cache/wikidata.jsonl` (fait sur le monde) ; `maintained by WikiProject` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `does not have part` → **à décider** (hors schéma) ; `instance of` → `iso-thes:broaderInstantial` ; `opposite of` → `kg:oppositeOf` ; `image` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `Wolfram Language entity code` → **à décider** (hors schéma) ; `wikidata entity id: Q174733` → `skos:exactMatch: wd:Q174733` ; `inferred:skos:ancestor` → `inferred/bipartite graph.json` ; `inferred:skos:broader` → `inferred/bipartite graph.json`
- **[[Blocking minority]]** : `inferred:skos:ancestor` → `inferred/Blocking minority.json`
- **[[blueprint]]** : `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `subclass of` → `iso-thes:broaderGeneric` ; `different from` → `skos:scopeNote` (« différent de … ») ; `made from material` → **à décider** (hors schéma) ; `partOf` → `iso-thes:broaderPartitive`
- **[[board of directors]]** : `described by source` → `dcterms:isReferencedBy` ; `different from` → `skos:scopeNote` (« différent de … ») ; `facet of` → `skos:broader` ; `has part(s)` → `has part` ; `position held by head of the organization` → **à décider** (hors schéma) ; `subclass of` → `iso-thes:broaderGeneric` ; `wikidata entity id: Q188628` → `skos:exactMatch: wd:Q188628`
- **[[boilerplate]]** : `wikidata entity id: Q1651672` → `skos:exactMatch: wd:Q1651672` ; `subclass of` → `iso-thes:broaderGeneric` ; `opposite of` → `kg:oppositeOf` ; `different from` → `skos:scopeNote` (« différent de … ») ; `example in` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/boilerplate.json` ; `inferred:skos:broader` → `inferred/boilerplate.json`
- **[[bootstrap aggregating (bagging)]]** : `inferred:skos:ancestor` → `inferred/bootstrap aggregating (bagging).json`
- **[[branch]]** : `partOf` → `iso-thes:broaderPartitive`
- **[[branch -vv]]** : `inferred:skos:ancestor` → `inferred/branch -vv.json`
- **[[break error]]** : `inferred:skos:ancestor` → `inferred/break error.json`
- **[[brief mission]]** : `inferred:skos:ancestor` → `inferred/brief mission.json`
- **[[bundle]]** : `subclass of` → `iso-thes:broaderGeneric` ; `has part(s)` → `has part` ; `has cause` → `cache/wikidata.jsonl` (fait sur le monde) ; `different from` → `skos:scopeNote` (« différent de … ») ; `image` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `wikidata entity id: Q83808937` → `skos:exactMatch: wd:Q83808937` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/bundle.json`
- **[[business]]** : `wikidata entity id: Q4830453` → `skos:exactMatch: wd:Q4830453` ; `inferred:skos:narrower` → `inferred/business.json`
- **[[business activity]]** : `wikidata entity id: Q19862406` → `skos:exactMatch: wd:Q19862406`
- **[[business analyst]]** : `relevant qualification` → **à décider** (hors schéma) ; `subclass of` → `iso-thes:broaderGeneric` ; `instance of` → `iso-thes:broaderInstantial` ; `ISCO-08 occupation class` → **à décider** (hors schéma) ; `female form of label` → **à décider** (hors schéma) ; `male form of label` → **à décider** (hors schéma) ; `wikidata entity id: Q1017553` → `skos:exactMatch: wd:Q1017553`
- **[[business impact]]** : `inferred:skos:ancestor` → `inferred/business impact.json`
- **[[business process]]** : `wikidata entity id: Q851587` → `skos:exactMatch: wd:Q851587` ; `instance of` → `iso-thes:broaderInstantial` ; `subclass of` → `iso-thes:broaderGeneric` ; `manifestation of` → `cache/wikidata.jsonl` (fait sur le monde) ; `uses` → `kg:uses` ; `used by` → `kg:usedBy` ; `different from` → `skos:scopeNote` (« différent de … ») ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/business process.json` ; `inferred:skos:narrower` → `inferred/business process.json`
- **[[business process mapping]]** : `wikidata entity id: Q3298296` → `skos:exactMatch: wd:Q3298296` ; `instance of` → `iso-thes:broaderInstantial` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/business process mapping.json`
- **[[Business Process Model and Notation]]** : `wikidata entity id: Q1017605` → `skos:exactMatch: wd:Q1017605` ; `instance of` → `iso-thes:broaderInstantial` ; `subclass of` → `iso-thes:broaderGeneric` ; `depicts` → **à décider** (hors schéma) ; `publisher` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Business Process Model and Notation.json`
- **[[business rule]]** : `wikidata entity id: Q1518244` → `skos:exactMatch: wd:Q1518244` ; `subclass of` → `iso-thes:broaderGeneric` ; `characteristic of` → `cache/wikidata.jsonl` (fait sur le monde) ; `inferred:skos:ancestor` → `inferred/business rule.json`
- **[[business understanding]]** : `inferred:skos:ancestor` → `inferred/business understanding.json` ; `inferred:skos:narrower` → `inferred/business understanding.json`
- **[[cadence]]** : `inferred:skos:ancestor` → `inferred/cadence.json`
- **[[calculated-fields]]** : `inferred:skos:ancestor` → `inferred/calculated-fields.json`
- **[[calibration]]** : `rdf:type: skos:Concept` → `dcterms:type: Concept` ; `inferred:skos:ancestor` → `inferred/calibration.json` ; `inferred:skos:related` → `inferred/calibration.json`
- **[[callback]]** : `inferred:skos:ancestor` → `inferred/callback.json`
- **[[camemBERT]]** : `inferred:skos:ancestor` → `inferred/camemBERT.json`
- **[[canonicalization]]** : `wikidata entity id: Q2936505` → `skos:exactMatch: wd:Q2936505`
- **[[causal inference]]** : `instance of` → `iso-thes:broaderInstantial` ; `subclass of` → `iso-thes:broaderGeneric` ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `GitHub topic` → `skos:closeMatch` ; `wikidata entity id: Q5054566` → `skos:exactMatch: wd:Q5054566` ; `inferred:skos:related` → `inferred/causal inference.json`
- **[[causality]]** : `subclass of` → `iso-thes:broaderGeneric` ; `facet of` → `skos:broader` ; `wikidata entity id: Q1149766` → `skos:exactMatch: wd:Q1149766` ; `inferred:skos:narrower` → `inferred/causality.json`
- **[[cease and desist]]** : `country` → **à décider** (hors schéma) ; `instance of` → `iso-thes:broaderInstantial` ; `part of` → `iso-thes:broaderPartitive` ; `subclass of` → `iso-thes:broaderGeneric` ; `wikidata entity id: Q31726` → `skos:exactMatch: wd:Q31726`
- **[[Celery]]** : `instanceOf` → `iso-thes:broaderInstantial` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Celery.json`
- **[[central processing unit]]** : `inferred:skos:ancestor` → `inferred/central processing unit.json`
- **[[centrality]]** : `inferred:skos:narrower` → `inferred/centrality.json`
- **[[chain of custody]]** : `wikidata entity id: Q738898` → `skos:exactMatch: wd:Q738898` ; `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/chain of custody.json`
- **[[chain-of-thought]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/chain-of-thought.json`
- **[[chainrings]]** : `IdenticalTo` → **à décider** (hors schéma) ; `MountedInParallel` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/chainrings.json`
- **[[champion-challenger testing]]** : `inferred:skos:ancestor` → `inferred/champion-challenger testing.json`
- **[[change]]** : `manifestation of` → `cache/wikidata.jsonl` (fait sur le monde) ; `has cause` → `cache/wikidata.jsonl` (fait sur le monde) ; `described by source` → `dcterms:isReferencedBy` ; `different from` → `skos:scopeNote` (« différent de … ») ; `has characteristic` → `cache/wikidata.jsonl` (fait sur le monde) ; `opposite of` → `kg:oppositeOf` ; `disjoint union of` → **à décider** (hors schéma) ; `part of` → `iso-thes:broaderPartitive` ; `instance of` → `iso-thes:broaderInstantial` ; `subclass of` → `iso-thes:broaderGeneric` ; `has effect` → `cache/wikidata.jsonl` (fait sur le monde) ; `OmegaWiki Defined Meaning` → `skos:closeMatch` ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `IMDb keyword` → `skos:closeMatch` ; `wikidata entity id: Q1150070` → `skos:exactMatch: wd:Q1150070` ; `inferred:skos:ancestor` → `inferred/change.json`
- **[[change control]]** : `wikidata entity id: Q3625347` → `skos:exactMatch: wd:Q3625347` ; `part of` → `iso-thes:broaderPartitive` ; `instance of` → `iso-thes:broaderInstantial`
- **[[change management]]** : `inferred:skos:ancestor` → `inferred/change management.json`
- **[[changelog]]** : `wikidata entity id: Q255135` → `skos:exactMatch: wd:Q255135` ; `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/changelog.json`
- **[[changeset]]** : `wikidata entity id: Q5071951` → `skos:exactMatch: wd:Q5071951` ; `subclass of` → `iso-thes:broaderGeneric` ; `has use` → `kg:hasUse` ; `used by` → `kg:usedBy` ; `inferred:skos:ancestor` → `inferred/changeset.json`
- **[[chat engines]]** : `inferred:skos:ancestor` → `inferred/chat engines.json`
- **[[chat modes]]** : `inferred:skos:ancestor` → `inferred/chat modes.json`
- **[[checklist]]** : `wikidata entity id: Q922625` → `skos:exactMatch: wd:Q922625` ; `subclass of` → `iso-thes:broaderGeneric`
- **[[checkout]]** : `inferred:skos:ancestor` → `inferred/checkout.json`
- **[[checkout -b]]** : `inferred:skos:ancestor` → `inferred/checkout -b.json`
- **[[chronology]]** : `wikidata entity id: Q130788` → `skos:exactMatch: wd:Q130788` ; `inferred:skos:narrower` → `inferred/chronology.json`
- **[[clarifeye]]** : `inferred:skos:ancestor` → `inferred/clarifeye.json`
- **[[class imbalance]]** : `inferred:skos:ancestor` → `inferred/class imbalance.json`
- **[[classification]]** : `inferred:skos:ancestor` → `inferred/classification.json` ; `inferred:skos:broader` → `inferred/classification.json`
- **[[classification scheme]]** : `inferred:skos:ancestor` → `inferred/classification scheme.json` ; `has part(s)` → `has part` ; `studied by` → `cache/wikidata.jsonl` (fait sur le monde) ; `has part(s) of the class` → `cache/wikidata.jsonl` (fait sur le monde) ; `described by source` → `dcterms:isReferencedBy` ; `different from` → `skos:scopeNote` (« différent de … ») ; `part of` → `iso-thes:broaderPartitive` ; `subclass of` → `iso-thes:broaderGeneric` ; `facet of` → `skos:broader` ; `instance of` → `iso-thes:broaderInstantial` ; `has characteristic` → `cache/wikidata.jsonl` (fait sur le monde) ; `used by` → `kg:usedBy` ; `model item` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `image` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `exact match` → `skos:exactMatch` ; `described at URL` → **à décider** (hors schéma) ; `Library of Congress Classification` → `dcterms:subject` ; `Wolfram Language entity code` → **à décider** (hors schéma) ; `equivalent class` → `skos:closeMatch` ; `wikidata entity id: Q5962346` → `skos:exactMatch: wd:Q5962346`
- **[[claude code]]** : `wikidata entity id: Q138457287` → `skos:exactMatch: wd:Q138457287` ; `instance of` → `iso-thes:broaderInstantial` ; `inferred:skos:related` → `inferred/claude code.json`
- **[[claude cowork]]** : `inferred:skos:ancestor` → `inferred/claude cowork.json`
- **[[claude managed agents]]** : `inferred:skos:ancestor` → `inferred/claude managed agents.json`
- **[[claude.md]]** : `partOf` → `iso-thes:broaderPartitive`
- **[[clause]]** : `described by source` → `dcterms:isReferencedBy` ; `facet of` → `skos:broader` ; `instance of` → `iso-thes:broaderInstantial` ; `part of` → `iso-thes:broaderPartitive` ; `studied by` → `cache/wikidata.jsonl` (fait sur le monde) ; `subclass of` → `iso-thes:broaderGeneric` ; `wikidata entity id: Q1527956` → `skos:exactMatch: wd:Q1527956` ; `inferred:skos:narrower` → `inferred/clause.json`
- **[[clause classification heuristic]]** : `subclass of` → `iso-thes:broaderGeneric` ; `uses` → `kg:uses` ; `part of` → `iso-thes:broaderPartitive` ; `outputs` → **à décider** (hors schéma) ; `related to` → `skos:related` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/clause classification heuristic.json` ; `inferred:skos:broader` → `inferred/clause classification heuristic.json`
- **[[closeness centrality]]** : `inferred:skos:ancestor` → `inferred/closeness centrality.json` ; `inferred:skos:broader` → `inferred/closeness centrality.json`
- **[[cloud computing]]** : `inferred:skos:ancestor` → `inferred/cloud computing.json`
- **[[clustering]]** : `inferred:skos:narrower` → `inferred/clustering.json`
- **[[coefficient of determination]]** : `inferred:skos:ancestor` → `inferred/coefficient of determination.json`
- **[[cognitive bias]]** : `inferred:skos:ancestor` → `inferred/cognitive bias.json`
- **[[cold start problem]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/cold start problem.json`
- **[[collaboration tools]]** : `inferred:skos:ancestor` → `inferred/collaboration tools.json`
- **[[collaborators]]** : `inferred:skos:ancestor` → `inferred/collaborators.json`
- **[[collecting data]]** : `inferred:skos:ancestor` → `inferred/collecting data.json`
- **[[combination]]** : `studied by` → `cache/wikidata.jsonl` (fait sur le monde) ; `different from` → `skos:scopeNote` (« différent de … ») ; `instance of` → `iso-thes:broaderInstantial` ; `subclass of` → `iso-thes:broaderGeneric` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/combination.json` ; `inferred:skos:narrower` → `inferred/combination.json`
- **[[combinatorics]]** : `inferred:skos:narrower` → `inferred/combinatorics.json`
- **[[comet]]** : `inferred:skos:ancestor` → `inferred/comet.json`
- **[[commissaire aux apports]]** : `wikidata entity id: Q2986295` → `skos:exactMatch: wd:Q2986295`
- **[[commit]]** : `inferred:skos:ancestor` → `inferred/commit.json`
- **[[commit amend]]** : `inferred:skos:ancestor` → `inferred/commit amend.json`
- **[[commit message]]** : `wikidata entity id: Q135001051` → `skos:exactMatch: wd:Q135001051` ; `part of` → `iso-thes:broaderPartitive`
- **[[commodity]]** : `has characteristic` → `cache/wikidata.jsonl` (fait sur le monde) ; `manifestation of` → `cache/wikidata.jsonl` (fait sur le monde) ; `said to be the same as` → `skos:closeMatch` ; `partially coincident with` → `cache/wikidata.jsonl` (fait sur le monde) ; `different from` → `skos:scopeNote` (« différent de … ») ; `has cause` → `cache/wikidata.jsonl` (fait sur le monde) ; `has list` → **à décider** (hors schéma) ; `topic has template` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `instance of` → `iso-thes:broaderInstantial` ; `subclass of` → `iso-thes:broaderGeneric` ; `IAB code` → **à décider** (hors schéma) ; `OmegaWiki Defined Meaning` → `skos:closeMatch` ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `wikidata entity id: Q317088` → `skos:exactMatch: wd:Q317088` ; `inferred:skos:narrower` → `inferred/commodity.json`
- **[[communicate uncertainty]]** : `inferred:skos:narrower` → `inferred/communicate uncertainty.json`
- **[[communication protocol]]** : `inferred:skos:narrower` → `inferred/communication protocol.json`
- **[[community detection]]** : `inferred:skos:ancestor` → `inferred/community detection.json`
- **[[comparag agent]]** : `subclassOf` → `iso-thes:broaderGeneric` ; `usedIn` → `kg:usedBy` ; `aliases` → `skos:altLabel` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/comparag agent.json`
- **[[compatibility]]** : `rdf:type: Research Note` → `dcterms:type: Concept` (à confirmer : note de recherche) ; `title` → `skos:prefLabel` ; `description` → `skos:definition` ; `timestamp` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `instanceOf` → `iso-thes:broaderInstantial`
- **[[compilatio IA]]** : `inferred:skos:ancestor` → `inferred/compilatio IA.json`
- **[[complete graph]]** : `inferred:skos:ancestor` → `inferred/complete graph.json` ; `inferred:skos:broader` → `inferred/complete graph.json`
- **[[completeness]]** : `inferred:skos:ancestor` → `inferred/completeness.json`
- **[[compliant privacy policy]]** : `inferred:skos:ancestor` → `inferred/compliant privacy policy.json`
- **[[compound AI system]]** : `inferred:skos:related` → `inferred/compound AI system.json`
- **[[computer interface]]** : `inferred:skos:narrower` → `inferred/computer interface.json`
- **[[computer program]]** : `wikidata entity id: Q40056` → `skos:exactMatch: wd:Q40056` ; `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/computer program.json` ; `inferred:skos:narrower` → `inferred/computer program.json`
- **[[computer vision]]** : `inferred:skos:narrower` → `inferred/computer vision.json` ; `inferred:skos:related` → `inferred/computer vision.json`
- **[[concept]]** : `inferred:skos:ancestor` → `inferred/concept.json`
- **[[concept drift]]** : `inferred:skos:related` → `inferred/concept drift.json`
- **[[conceptual model]]** : `part of` → `iso-thes:broaderPartitive` ; `facet of` → `skos:broader` ; `partially coincident with` → `cache/wikidata.jsonl` (fait sur le monde) ; `subclass of` → `iso-thes:broaderGeneric` ; `opposite of` → `kg:oppositeOf` ; `different from` → `skos:scopeNote` (« différent de … ») ; `product of` → **à décider** (hors schéma) ; `inferred:skos:ancestor` → `inferred/conceptual model.json` ; `inferred:skos:broader` → `inferred/conceptual model.json` ; `inferred:skos:narrower` → `inferred/conceptual model.json`
- **[[conceptual modeling]]** : `broader` → `skos:broader` ; `different from` → `skos:scopeNote` (« différent de … ») ; `inferred:skos:ancestor` → `inferred/conceptual modeling.json` ; `inferred:skos:broader` → `inferred/conceptual modeling.json`
- **[[condense_plus_context]]** : `inferred:skos:ancestor` → `inferred/condense_plus_context.json`
- **[[condense_question]]** : `inferred:skos:ancestor` → `inferred/condense_question.json`
- **[[conditional-formatting]]** : `inferred:skos:ancestor` → `inferred/conditional-formatting.json`
- **[[confidence interval]]** : `inferred:skos:ancestor` → `inferred/confidence interval.json` ; `inferred:skos:broader` → `inferred/confidence interval.json`
- **[[confidence presentation]]** : `inferred:skos:ancestor` → `inferred/confidence presentation.json`
- **[[conflict of interest]]** : `facet of` → `skos:broader` ; `handled, mitigated, or managed by` → **à décider** (hors schéma) ; `has characteristic` → `cache/wikidata.jsonl` (fait sur le monde) ; `instance of` → `iso-thes:broaderInstantial` ; `subclass of` → `iso-thes:broaderGeneric` ; `wikidata entity id: Q211067` → `skos:exactMatch: wd:Q211067` ; `inferred:skos:ancestor` → `inferred/conflict of interest.json`
- **[[confusion matrix]]** : `inferred:skos:related` → `inferred/confusion matrix.json`
- **[[connexionism]]** : `inferred:skos:ancestor` → `inferred/connexionism.json`
- **[[connotation]]** : `inferred:skos:ancestor` → `inferred/connotation.json`
- **[[consistency]]** : `opposite of` → `kg:oppositeOf` ; `characteristic of` → `cache/wikidata.jsonl` (fait sur le monde) ; `said to be the same as` → `skos:closeMatch` ; `subclass of` → `iso-thes:broaderGeneric` ; `maintained by WikiProject` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `facet of` → `skos:broader` ; `described by source` → `dcterms:isReferencedBy` ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `wikidata entity id: Q1319773` → `skos:exactMatch: wd:Q1319773`
- **[[constancy]]** : `inferred:skos:ancestor` → `inferred/constancy.json`
- **[[constraint]]** : `subclass of` → `iso-thes:broaderGeneric` ; `instance of` → `iso-thes:broaderInstantial` ; `Stack Exchange tag` → `skos:closeMatch` ; `wikidata entity id: Q231612` → `skos:exactMatch: wd:Q231612`
- **[[container]]** : `inferred:skos:ancestor` → `inferred/container.json` ; `inferred:skos:broader` → `inferred/container.json`
- **[[containerization (computing)]]** : `inferred:skos:narrower` → `inferred/containerization (computing).json`
- **[[context]]** : `has part(s)` → `has part` ; `has use` → `kg:hasUse` ; `subclass of` → `iso-thes:broaderGeneric` ; `described by source` → `dcterms:isReferencedBy` ; `studied by` → `cache/wikidata.jsonl` (fait sur le monde) ; `facet of` → `skos:broader` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/context.json`
- **[[context engineering]]** : `instance of` → `iso-thes:broaderInstantial` ; `part of` → `iso-thes:broaderPartitive` ; `facet of` → `skos:broader` ; `wikidata entity id: Q137916163` → `skos:exactMatch: wd:Q137916163` ; `inferred:skos:related` → `inferred/context engineering.json`
- **[[context graph]]** : `inferred:skos:ancestor` → `inferred/context graph.json`
- **[[context mode]]** : `inferred:skos:ancestor` → `inferred/context mode.json`
- **[[continuant]]** : `disjoint with` → `kg:disjointWith` ; `inferred:skos:narrower` → `inferred/continuant.json`
- **[[continuity]]** : `inferred:skos:ancestor` → `inferred/continuity.json`
- **[[continuous learning]]** : `inferred:skos:ancestor` → `inferred/continuous learning.json`
- **[[continuum data]]** : `inferred:skos:ancestor` → `inferred/continuum data.json`
- **[[contract]]** : `described by source` → `dcterms:isReferencedBy` ; `different from` → `skos:scopeNote` (« différent de … ») ; `facet of` → `skos:broader` ; `has characteristic` → `cache/wikidata.jsonl` (fait sur le monde) ; `has contributing factor` → **à décider** (hors schéma) ; `has effect` → `cache/wikidata.jsonl` (fait sur le monde) ; `has part(s)` → `has part` ; `has part(s) of the class` → `cache/wikidata.jsonl` (fait sur le monde) ; `instance of` → `iso-thes:broaderInstantial` ; `part of` → `iso-thes:broaderPartitive` ; `participant` → **à décider** (hors schéma) ; `said to be the same as` → `skos:closeMatch` ; `subclass of` → `iso-thes:broaderGeneric` ; `wikidata entity id: Q93288` → `skos:exactMatch: wd:Q93288` ; `inferred:skos:ancestor` → `inferred/contract.json` ; `inferred:skos:narrower` → `inferred/contract.json`
- **[[control]]** : `inferred:skos:narrower` → `inferred/control.json`
- **[[control (L.233-3)]]** : `uses` → `kg:uses` ; `subclass of` → `iso-thes:broaderGeneric`
- **[[control flow]]** : `inferred:skos:narrower` → `inferred/control flow.json`
- **[[control theory]]** : `followed by` → **à décider** (hors schéma) ; `is the study of` → `cache/wikidata.jsonl` (fait sur le monde) ; `instance of` → `iso-thes:broaderInstantial` ; `topic's main template` → **à décider** (hors schéma) ; `maintained by WikiProject` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `subclass of` → `iso-thes:broaderGeneric` ; `part of` → `iso-thes:broaderPartitive` ; `Stack Exchange tag` → `skos:closeMatch` ; `Commons gallery` → **à décider** (hors schéma) ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `wikidata entity id: Q6501221` → `skos:exactMatch: wd:Q6501221` ; `firstDescribedby` → **à décider** (hors schéma) ; `inferred:skos:narrower` → `inferred/control theory.json`
- **[[controlled vocabulary]]** : `wikidata entity id: Q1469824` → `skos:exactMatch: wd:Q1469824` ; `subclass of` → `iso-thes:broaderGeneric` ; `exact match` → `skos:exactMatch` ; `inferred:skos:ancestor` → `inferred/controlled vocabulary.json` ; `inferred:skos:narrower` → `inferred/controlled vocabulary.json`
- **[[convolutional layers]]** : `inferred:skos:ancestor` → `inferred/convolutional layers.json`
- **[[convolutional neural networks]]** : `inferred:skos:narrower` → `inferred/convolutional neural networks.json`
- **[[cosine similarity]]** : `calculationUnder` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/cosine similarity.json`
- **[[counterfactual explanations]]** : `inferred:skos:ancestor` → `inferred/counterfactual explanations.json`
- **[[countVectorizer]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/countVectorizer.json`
- **[[crawl-walk-run]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/crawl-walk-run.json`
- **[[creative work]]** : `inferred:skos:narrower` → `inferred/creative work.json`
- **[[credit note]]** : `wikidata entity id: Q317955` → `skos:exactMatch: wd:Q317955` ; `subclass of` → `iso-thes:broaderGeneric` ; `different from` → `skos:scopeNote` (« différent de … ») ; `inferred:skos:related` → `inferred/credit note.json`
- **[[CRISP-DM Process]]** : `inferred:skos:narrower` → `inferred/CRISP-DM Process.json`
- **[[cross validation]]** : `inferred:skos:narrower` → `inferred/cross validation.json`
- **[[cross-sheet source references]]** : `inferred:skos:ancestor` → `inferred/cross-sheet source references.json`
- **[[customization]]** : `inferred:skos:ancestor` → `inferred/customization.json`
- **[[CYPHER]]** : `inferred:skos:ancestor` → `inferred/CYPHER.json`
- **[[daily stand-ups]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/daily stand-ups.json`
- **[[damping]]** : `inferred:skos:ancestor` → `inferred/damping.json`
- **[[dangerousness]]** : `inferred:skos:ancestor` → `inferred/dangerousness.json`
- **[[dashboard]]** : `inferred:skos:ancestor` → `inferred/dashboard.json`
- **[[data]]** : `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/data.json` ; `inferred:skos:narrower` → `inferred/data.json`
- **[[data augmentation]]** : `inferred:skos:narrower` → `inferred/data augmentation.json`
- **[[data catalog]]** : `inferred:skos:ancestor` → `inferred/data catalog.json`
- **[[data deduplication]]** : `wikidata entity id: Q1182260` → `skos:exactMatch: wd:Q1182260`
- **[[data drift]]** : `inferred:skos:ancestor` → `inferred/data drift.json`
- **[[data engineer]]** : `inferred:skos:ancestor` → `inferred/data engineer.json`
- **[[data leakage]]** : `rdf:type: skos:Concept` → `dcterms:type: Concept` ; `inferred:skos:ancestor` → `inferred/data leakage.json` ; `inferred:skos:related` → `inferred/data leakage.json`
- **[[data lineage]]** : `subclass of` → `iso-thes:broaderGeneric` ; `wikidata entity id: Q1172162` → `skos:exactMatch: wd:Q1172162` ; `inferred:skos:ancestor` → `inferred/data lineage.json`
- **[[data management]]** : `wikidata entity id: Q1149776` → `skos:exactMatch: wd:Q1149776`
- **[[data mapping]]** : `inferred:skos:ancestor` → `inferred/data mapping.json`
- **[[data model]]** : `inferred:skos:ancestor` → `inferred/data model.json`
- **[[data object]]** : `inferred:skos:ancestor` → `inferred/data object.json` ; `inferred:skos:broader` → `inferred/data object.json`
- **[[data oriented design]]** : `different from` → `skos:scopeNote` (« différent de … ») ; `subclass of` → `iso-thes:broaderGeneric` ; `short name` → `skos:altLabel` ; `wikidata entity id: Q24882785` → `skos:exactMatch: wd:Q24882785`
- **[[data preparation]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/data preparation.json` ; `inferred:skos:narrower` → `inferred/data preparation.json`
- **[[data privacy]]** : `inferred:skos:narrower` → `inferred/data privacy.json`
- **[[data privacy laws]]** : `inferred:skos:narrower` → `inferred/data privacy laws.json`
- **[[data processing toolset]]** : `inferred:skos:ancestor` → `inferred/data processing toolset.json`
- **[[data quality]]** : `inferred:skos:related` → `inferred/data quality.json`
- **[[data quantity]]** : `inferred:skos:ancestor` → `inferred/data quantity.json`
- **[[data science team]]** : `inferred:skos:narrower` → `inferred/data science team.json`
- **[[data scientist]]** : `inferred:skos:ancestor` → `inferred/data scientist.json`
- **[[data set]]** : `wikidata entity id: Q1172284` → `skos:exactMatch: wd:Q1172284` ; `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/data set.json` ; `inferred:skos:narrower` → `inferred/data set.json`
- **[[data silos]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/data silos.json`
- **[[data type]]** : `inferred:skos:narrower` → `inferred/data type.json`
- **[[data understanding]]** : `inferred:skos:ancestor` → `inferred/data understanding.json`
- **[[data visualization]]** : `significant person` → **à décider** (hors schéma) ; `subclass of` → `iso-thes:broaderGeneric` ; `product or material produced` → `cache/wikidata.jsonl` (fait sur le monde) ; `part of` → `iso-thes:broaderPartitive` ; `said to be the same as` → `skos:closeMatch` ; `uses` → `kg:uses` ; `partially coincident with` → `cache/wikidata.jsonl` (fait sur le monde) ; `wikidata entity id: Q6504956` → `skos:exactMatch: wd:Q6504956` ; `inferred:skos:narrower` → `inferred/data visualization.json`
- **[[datasetDict]]** : `partOf` → `iso-thes:broaderPartitive` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/datasetDict.json`
- **[[datasets]]** : `partOf` → `iso-thes:broaderPartitive` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/datasets.json`
- **[[datawarehouse]]** : `inferred:skos:ancestor` → `inferred/datawarehouse.json`
- **[[datum]]** : `inferred:skos:ancestor` → `inferred/datum.json`
- **[[de facto]]** : `inferred:skos:narrower` → `inferred/de facto.json`
- **[[de facto standard]]** : `inferred:skos:ancestor` → `inferred/de facto standard.json`
- **[[decision making]]** : `inferred:skos:ancestor` → `inferred/decision making.json`
- **[[Decision support]]** : `inferred:skos:narrower` → `inferred/Decision support.json`
- **[[decision tree]]** : `foundationalPaper` → `dcterms:isReferencedBy` ; `subclass of` → `iso-thes:broaderGeneric` ; `usedFor` → **à décider** (hors schéma) ; `components` → `has part` ; `algorithms` → **à décider** (hors schéma) ; `extendedBy` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/decision tree.json` ; `inferred:skos:narrower` → `inferred/decision tree.json`
- **[[declarative sentence]]** : `wikidata entity id: Q474328` → `skos:exactMatch: wd:Q474328` ; `inferred:skos:narrower` → `inferred/declarative sentence.json`
- **[[Decoder-only]]** : `subclass of` → `iso-thes:broaderGeneric` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Decoder-only.json`
- **[[decoders model]]** : `inferred:skos:ancestor` → `inferred/decoders model.json`
- **[[dedicated server]]** : `inferred:skos:ancestor` → `inferred/dedicated server.json`
- **[[deep learning]]** : `originatesFrom` → **à décider** (hors schéma) ; `inferred:skos:ancestor` → `inferred/deep learning.json` ; `inferred:skos:narrower` → `inferred/deep learning.json`
- **[[default]]** : `subclass of` → `iso-thes:broaderGeneric` ; `has characteristic` → `cache/wikidata.jsonl` (fait sur le monde) ; `different from` → `skos:scopeNote` (« différent de … ») ; `instance of` → `iso-thes:broaderInstantial` ; `wikidata entity id: Q67151552` → `skos:exactMatch: wd:Q67151552` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/default.json`
- **[[define success]]** : `inferred:skos:narrower` → `inferred/define success.json`
- **[[degree]]** : `inferred:skos:ancestor` → `inferred/degree.json`
- **[[degree centrality]]** : `inferred:skos:ancestor` → `inferred/degree centrality.json` ; `inferred:skos:broader` → `inferred/degree centrality.json`
- **[[delegation]]** : `facet of` → `skos:broader` ; `has effect` → `cache/wikidata.jsonl` (fait sur le monde) ; `subclass of` → `iso-thes:broaderGeneric` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/delegation.json`
- **[[delta live tables]]** : `inferred:skos:ancestor` → `inferred/delta live tables.json`
- **[[demo sessions]]** : `inferred:skos:ancestor` → `inferred/demo sessions.json`
- **[[denormalized schema]]** : `inferred:skos:ancestor` → `inferred/denormalized schema.json`
- **[[Dependency injection]]** : `inferred:skos:ancestor` → `inferred/Dependency injection.json`
- **[[deploy]]** : `inferred:skos:narrower` → `inferred/deploy.json`
- **[[Deployment]]** : `wikidata entity id: Q2297740` → `skos:exactMatch: wd:Q2297740` ; `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/Deployment.json` ; `inferred:skos:related` → `inferred/Deployment.json`
- **[[design]]** : `inferred:skos:narrower` → `inferred/design.json`
- **[[Design thinking]]** : `inferred:skos:narrower` → `inferred/Design thinking.json`
- **[[detection tool performance]]** : `inferred:skos:ancestor` → `inferred/detection tool performance.json`
- **[[determine feature set]]** : `inferred:skos:ancestor` → `inferred/determine feature set.json`
- **[[DevOps]]** : `inferred:skos:ancestor` → `inferred/DevOps.json`
- **[[diagram]]** : `wikidata entity id: Q959962` → `skos:exactMatch: wd:Q959962` ; `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/diagram.json` ; `inferred:skos:narrower` → `inferred/diagram.json`
- **[[dialogue]]** : `inferred:skos:ancestor` → `inferred/dialogue.json`
- **[[differences]]** : `rdf:type: Research Note` → `dcterms:type: Concept` (à confirmer : note de recherche) ; `title` → `skos:prefLabel` ; `description` → `skos:definition` ; `timestamp` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `instanceOf` → `iso-thes:broaderInstantial`
- **[[dijkstra's shortest path]]** : `inferred:skos:ancestor` → `inferred/dijkstra's shortest path.json`
- **[[dimensional modeling]]** : `instanceOf` → `iso-thes:broaderInstantial`
- **[[discourse topic]]** : `inferred:skos:ancestor` → `inferred/discourse topic.json`
- **[[discrimination threshold]]** : `subclass of` → `iso-thes:broaderGeneric` ; `IEV number` → **à décider** (hors schéma) ; `wikidata entity id: Q111024610` → `skos:exactMatch: wd:Q111024610` ; `inferred:skos:related` → `inferred/discrimination threshold.json`
- **[[Distance]]** : `inferred:skos:narrower` → `inferred/Distance.json`
- **[[dividual]]** : `inferred:skos:narrower` → `inferred/dividual.json`
- **[[Django]]** : `creator` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `programmed in` → `kg:programmedIn` ; `named after` → `cache/wikidata.jsonl` (fait sur le monde) ; `wikidata entity id: Q842014` → `skos:exactMatch: wd:Q842014` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Django.json`
- **[[Docker]]** : `inferred:skos:narrower` → `inferred/Docker.json`
- **[[Docker images]]** : `inferred:skos:ancestor` → `inferred/Docker images.json`
- **[[documentary evidence]]** : `wikidata entity id: Q5287668` → `skos:exactMatch: wd:Q5287668` ; `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/documentary evidence.json` ; `inferred:skos:narrower` → `inferred/documentary evidence.json`
- **[[Documentation]]** : `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/Documentation.json` ; `inferred:skos:narrower` → `inferred/Documentation.json`
- **[[Domain]]** : `inferred:skos:narrower` → `inferred/Domain.json`
- **[[domain driven design]]** : `subclass of` → `iso-thes:broaderGeneric` ; `instance of` → `iso-thes:broaderInstantial` ; `has use` → `kg:hasUse` ; `different from` → `skos:scopeNote` (« différent de … ») ; `described by source` → `dcterms:isReferencedBy` ; `discoverer or inventor` → `cache/wikidata.jsonl` (fait sur le monde) ; `short name` → `skos:altLabel` ; `OmegaWiki Defined Meaning` → `skos:closeMatch` ; `Stack Exchange tag` → `skos:closeMatch` ; `GitHub topic` → `skos:closeMatch` ; `wikidata entity id: Q524367` → `skos:exactMatch: wd:Q524367`
- **[[domain knowledge]]** : `facet of` → `skos:broader` ; `subclass of` → `iso-thes:broaderGeneric` ; `instance of` → `iso-thes:broaderInstantial` ; `wikidata entity id: Q2088941` → `skos:exactMatch: wd:Q2088941` ; `inferred:skos:ancestor` → `inferred/domain knowledge.json` ; `inferred:skos:related` → `inferred/domain knowledge.json`
- **[[Domain-Driven Design]]** : `main subject` → `dcterms:subject` ; `instance of` → `iso-thes:broaderInstantial` ; `has version, edition or translation` → **à décider** (hors schéma) ; `author` → **à décider** (hors schéma) ; `language of work or name` → **à décider** (hors schéma) ; `title` → `skos:prefLabel` ; `subtitle` → **à décider** (hors schéma) ; `publication date` → `cache/wikidata.jsonl` (fait sur le monde) ; `wikidata entity id: Q100742558` → `skos:exactMatch: wd:Q100742558`
- **[[Don Norman's principles of Interaction Design]]** : `inferred:skos:ancestor` → `inferred/Don Norman's principles of Interaction Design.json`
- **[[draft document]]** : `subclass of` → `iso-thes:broaderGeneric` ; `followed by` → **à décider** (hors schéma) ; `different from` → `skos:scopeNote` (« différent de … ») ; `partially coincident with` → `cache/wikidata.jsonl` (fait sur le monde) ; `has characteristic` → `cache/wikidata.jsonl` (fait sur le monde) ; `wikidata entity id: Q560361` → `skos:exactMatch: wd:Q560361` ; `aliases` → `skos:altLabel` ; `inferred:skos:ancestor` → `inferred/draft document.json`
- **[[drag-along right]]** : `instance of` → `iso-thes:broaderInstantial` ; `wikidata entity id: Q5304788` → `skos:exactMatch: wd:Q5304788`
- **[[economic taxonomy]]** : `inferred:skos:ancestor` → `inferred/economic taxonomy.json`
- **[[Edge ML]]** : `inferred:skos:ancestor` → `inferred/Edge ML.json`
- **[[Edges]]** : `inferred:skos:ancestor` → `inferred/Edges.json` ; `inferred:skos:broader` → `inferred/Edges.json`
- **[[Eigenvector centrality]]** : `inferred:skos:ancestor` → `inferred/Eigenvector centrality.json` ; `inferred:skos:broader` → `inferred/Eigenvector centrality.json`
- **[[Elbow method]]** : `inferred:skos:ancestor` → `inferred/Elbow method.json` ; `inferred:skos:broader` → `inferred/Elbow method.json`
- **[[elicitation interview]]** : `inferred:skos:related` → `inferred/elicitation interview.json`
- **[[Elixir]]** : `programming paradigm` → **à décider** (hors schéma) ; `influenced by` → **à décider** (hors schéma) ; `operating system` → **à décider** (hors schéma) ; `typing discipline` → **à décider** (hors schéma) ; `instance of` → `iso-thes:broaderInstantial` ; `programmed in` → `kg:programmedIn` ; `copyright license` → **à décider** (hors schéma) ; `depends on software` → `kg:dependsOn` ; `platform` → **à décider** (hors schéma) ; `developer` → **à décider** (hors schéma) ; `creator` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `copyright status` → **à décider** (hors schéma) ; `writable file format` → **à décider** (hors schéma) ; `readable file format` → **à décider** (hors schéma) ; `social media followers` → **à décider** (hors schéma) ; `MacPorts port` → **à décider** (hors schéma) ; `GitHub topic` → `skos:closeMatch` ; `Homebrew formula name` → **à décider** (hors schéma) ; `openSUSE package` → **à décider** (hors schéma) ; `Repology project name` → **à décider** (hors schéma) ; `Ubuntu package` → **à décider** (hors schéma) ; `Fedora package` → **à décider** (hors schéma) ; `Arch Linux package` → **à décider** (hors schéma) ; `Debian stable package` → **à décider** (hors schéma) ; `file extension` → **à décider** (hors schéma) ; `software version identifier` → **à décider** (hors schéma) ; `source code repository URL` → **à décider** (hors schéma) ; `ArchWiki article` → **à décider** (hors schéma) ; `Gentoo Wiki article` → **à décider** (hors schéma) ; `media type` → **à décider** (hors schéma) ; `inception` → `cache/wikidata.jsonl` (fait sur le monde) ; `logo image` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `official website` → **à décider** (hors schéma) ; `official blog URL` → **à décider** (hors schéma) ; `Stack Exchange tag` → `skos:closeMatch` ; `IRC channel URL` → **à décider** (hors schéma) ; `Gentoo package` → **à décider** (hors schéma) ; `SlackBuilds package` → **à décider** (hors schéma) ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `AUR package` → **à décider** (hors schéma) ; `GitHub account` → **à décider** (hors schéma) ; `X (Twitter) username` → **à décider** (hors schéma) ; `OpenBSD port` → **à décider** (hors schéma) ; `FreeBSD port` → **à décider** (hors schéma) ; `Docker Hub repository` → **à décider** (hors schéma) ; `publication date` → `cache/wikidata.jsonl` (fait sur le monde) ; `wikidata entity id: Q5362035` → `skos:exactMatch: wd:Q5362035` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Elixir.json` ; `inferred:skos:broader` → `inferred/Elixir.json`
- **[[Embedded methods]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Embedded methods.json`
- **[[embedding]]** : `wikidata entity id: Q133284072` → `skos:exactMatch: wd:Q133284072` ; `part of` → `iso-thes:broaderPartitive` ; `inferred:skos:narrower` → `inferred/embedding.json`
- **[[Embedding network]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Embedding network.json`
- **[[Embeddings]]** : `foundationalPaper` → `dcterms:isReferencedBy` ; `keyPapers` → `dcterms:isReferencedBy` ; `entity` → **à décider** (hors schéma) ; `storedInto` → **à décider** (hors schéma) ; `represents` → **à décider** (hors schéma) ; `properties` → **à décider** (hors schéma) ; `skos:narrower` → retiré ; chaque cible reçoit `skos:broader: [[Embeddings]]` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Embeddings.json` ; `inferred:skos:narrower` → `inferred/Embeddings.json`
- **[[Embeddings models]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Embeddings models.json`
- **[[Empathy]]** : `inferred:skos:narrower` → `inferred/Empathy.json`
- **[[empirical evidence]]** : `atWorkWithin` → **à décider** (hors schéma)
- **[[Encoder-only]]** : `subclass of` → `iso-thes:broaderGeneric` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Encoder-only.json`
- **[[end-to-end test]]** : `rdf:type: Concept` → `dcterms:type: Concept` ; `broader` → `skos:broader` ; `description` → `skos:definition` ; `timestamp` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `inferred:skos:ancestor` → `inferred/end-to-end test.json`
- **[[engineering concept]]** : `wikidata entity id: Q137430548` → `skos:exactMatch: wd:Q137430548`
- **[[engineering team]]** : `inferred:skos:ancestor` → `inferred/engineering team.json`
- **[[environment]]** : `inferred:skos:ancestor` → `inferred/environment.json`
- **[[equifinality]]** : `inferred:skos:ancestor` → `inferred/equifinality.json`
- **[[escrow]]** : `different from` → `skos:scopeNote` (« différent de … ») ; `said to be the same as` → `skos:closeMatch` ; `subclass of` → `iso-thes:broaderGeneric` ; `wikidata entity id: Q338451` → `skos:exactMatch: wd:Q338451`
- **[[ethical checklist]]** : `inferred:skos:ancestor` → `inferred/ethical checklist.json`
- **[[ethical risks]]** : `inferred:skos:ancestor` → `inferred/ethical risks.json`
- **[[evaluate results]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/evaluate results.json`
- **[[evaluation]]** : `inferred:skos:narrower` → `inferred/evaluation.json`
- **[[evaluation dataset]]** : `inferred:skos:ancestor` → `inferred/evaluation dataset.json`
- **[[evaluation metrics]]** : `inferred:skos:narrower` → `inferred/evaluation metrics.json`
- **[[evaluation task]]** : `partOf` → `iso-thes:broaderPartitive`
- **[[evidence]]** : `wikidata entity id: Q176763` → `skos:exactMatch: wd:Q176763` ; `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/evidence.json` ; `inferred:skos:narrower` → `inferred/evidence.json`
- **[[excel]]** : `inferred:skos:ancestor` → `inferred/excel.json`
- **[[excel vs. gsheet problem]]** : `inferred:skos:ancestor` → `inferred/excel vs. gsheet problem.json`
- **[[exception handling]]** : `inferred:skos:narrower` → `inferred/exception handling.json`
- **[[Excessive latency]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Excessive latency.json`
- **[[excitement]]** : `inferred:skos:ancestor` → `inferred/excitement.json`
- **[[exclusion clause]]** : `inferred:skos:ancestor` → `inferred/exclusion clause.json`
- **[[experimentation]]** : `inferred:skos:ancestor` → `inferred/experimentation.json`
- **[[Expert systems]]** : `originatesFrom` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Expert systems.json`
- **[[explicit knowledge]]** : `wikidata entity id: Q1323686` → `skos:exactMatch: wd:Q1323686` ; `subclass of` → `iso-thes:broaderGeneric` ; `instance of` → `iso-thes:broaderInstantial` ; `opposite of` → `kg:oppositeOf` ; `has cause` → `cache/wikidata.jsonl` (fait sur le monde) ; `inferred:skos:ancestor` → `inferred/explicit knowledge.json` ; `inferred:skos:related` → `inferred/explicit knowledge.json`
- **[[exploratory data analysis]]** : `inferred:skos:narrower` → `inferred/exploratory data analysis.json`
- **[[explore the data]]** : `inferred:skos:ancestor` → `inferred/explore the data.json` ; `inferred:skos:broader` → `inferred/explore the data.json`
- **[[F1 Score]]** : `inferred:skos:ancestor` → `inferred/F1 Score.json`
- **[[facial recognition]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/facial recognition.json`
- **[[fair AI]]** : `inferred:skos:ancestor` → `inferred/fair AI.json`
- **[[fair information practices]]** : `inferred:skos:ancestor` → `inferred/fair information practices.json` ; `inferred:skos:broader` → `inferred/fair information practices.json`
- **[[fairness]]** : `inferred:skos:narrower` → `inferred/fairness.json`
- **[[false negative (FN)]]** : `inferred:skos:ancestor` → `inferred/false negative (FN).json` ; `inferred:skos:broader` → `inferred/false negative (FN).json`
- **[[false positive (FP)]]** : `inferred:skos:ancestor` → `inferred/false positive (FP).json` ; `inferred:skos:broader` → `inferred/false positive (FP).json`
- **[[false positive rate]]** : `inferred:skos:ancestor` → `inferred/false positive rate.json`
- **[[false positives and false negatives]]** : `shouldTakeIntoAccount` → **à décider** (hors schéma)
- **[[family educational rights and privacy act (FERPA)]]** : `inferred:skos:ancestor` → `inferred/family educational rights and privacy act (FERPA).json`
- **[[fault tolerance]]** : `inferred:skos:ancestor` → `inferred/fault tolerance.json`
- **[[feasability]]** : `inferred:skos:ancestor` → `inferred/feasability.json`
- **[[feature]]** : `inferred:skos:ancestor` → `inferred/feature.json`
- **[[feature bagging]]** : `inferred:skos:ancestor` → `inferred/feature bagging.json`
- **[[feature engineering]]** : `inferred:skos:narrower` → `inferred/feature engineering.json`
- **[[feature pipeline]]** : `inferred:skos:ancestor` → `inferred/feature pipeline.json`
- **[[feature selection]]** : `inferred:skos:narrower` → `inferred/feature selection.json`
- **[[feature-list]]** : `inferred:skos:ancestor` → `inferred/feature-list.json`
- **[[federated learning]]** : `foundationalPaper` → `dcterms:isReferencedBy` ; `keyPapers` → `dcterms:isReferencedBy` ; `protects` → **à décider** (hors schéma) ; `enables` → **à décider** (hors schéma) ; `challenges` → **à décider** (hors schéma) ; `algorithms` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/federated learning.json`
- **[[feedback]]** : `inferred:skos:ancestor` → `inferred/feedback.json`
- **[[feedback loop bias]]** : `inferred:skos:related` → `inferred/feedback loop bias.json`
- **[[feedback loops]]** : `inferred:skos:related` → `inferred/feedback loops.json`
- **[[field of study (education)]]** : `inferred:skos:ancestor` → `inferred/field of study (education).json`
- **[[filter methods]]** : `inferred:skos:ancestor` → `inferred/filter methods.json`
- **[[filtered vector search]]** : `inferred:skos:ancestor` → `inferred/filtered vector search.json`
- **[[financial privacy]]** : `inferred:skos:ancestor` → `inferred/financial privacy.json`
- **[[fine-tuning]]** : `inferred:skos:narrower` → `inferred/fine-tuning.json`
- **[[flywheel effect]]** : `inferred:skos:ancestor` → `inferred/flywheel effect.json`
- **[[force majeure]]** : `inferred:skos:ancestor` → `inferred/force majeure.json`
- **[[forward propagation]]** : `foundationalPaper` → `dcterms:isReferencedBy` ; `keyPapers` → `dcterms:isReferencedBy` ; `trainingTechnique` → **à décider** (hors schéma) ; `partOf` → `iso-thes:broaderPartitive` ; `complementedBy` → **à décider** (hors schéma) ; `consists_of` → `has part` ; `produces` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/forward propagation.json`
- **[[foundation model]]** : `inferred:skos:narrower` → `inferred/foundation model.json`
- **[[french commercial code]]** : `applies to jurisdiction` → **à décider** (hors schéma) ; `country` → **à décider** (hors schéma) ; `instance of` → `iso-thes:broaderInstantial` ; `wikidata entity id: Q2981466` → `skos:exactMatch: wd:Q2981466`
- **[[frontend]]** : `inferred:skos:ancestor` → `inferred/frontend.json`
- **[[functional programming]]** : `inferred:skos:narrower` → `inferred/functional programming.json`
- **[[functional requirement]]** : `subclass of` → `iso-thes:broaderGeneric` ; `facet of` → `skos:broader` ; `has characteristic` → `cache/wikidata.jsonl` (fait sur le monde) ; `opposite of` → `kg:oppositeOf` ; `OmegaWiki Defined Meaning` → `skos:closeMatch` ; `wikidata entity id: Q3264234` → `skos:exactMatch: wd:Q3264234` ; `inferred:skos:narrower` → `inferred/functional requirement.json`
- **[[functions]]** : `inferred:skos:narrower` → `inferred/functions.json`
- **[[gather data]]** : `inferred:skos:ancestor` → `inferred/gather data.json` ; `inferred:skos:broader` → `inferred/gather data.json`
- **[[generation]]** : `wikidata entity id:  Q3123154` → `skos:exactMatch: wd: Q3123154` ; `has characteristic` → `cache/wikidata.jsonl` (fait sur le monde)
- **[[generically dependent continuant]]** : `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/generically dependent continuant.json` ; `inferred:skos:narrower` → `inferred/generically dependent continuant.json`
- **[[geometric concept]]** : `inferred:skos:ancestor` → `inferred/geometric concept.json`
- **[[GGUF]]** : `inferred:skos:ancestor` → `inferred/GGUF.json`
- **[[Gilles Deleuze]]** : `influenced by` → **à décider** (hors schéma) ; `place of birth` → **à décider** (hors schéma) ; `place of death` → **à décider** (hors schéma) ; `occupation` → **à décider** (hors schéma) ; `educated at` → **à décider** (hors schéma) ; `employer` → **à décider** (hors schéma) ; `movement` → **à décider** (hors schéma) ; `partner in business or sport` → **à décider** (hors schéma) ; `student of` → **à décider** (hors schéma) ; `academic degree` → **à décider** (hors schéma) ; `time period` → **à décider** (hors schéma) ; `described by source` → `dcterms:isReferencedBy` ; `notable work` → **à décider** (hors schéma) ; `given name` → **à décider** (hors schéma) ; `assessment` → **à décider** (hors schéma) ; `doctoral student` → **à décider** (hors schéma) ; `child` → **à décider** (hors schéma) ; `part of` → `iso-thes:broaderPartitive` ; `sex or gender` → **à décider** (hors schéma) ; `maintained by WikiProject` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `family name` → **à décider** (hors schéma) ; `place of burial` → **à décider** (hors schéma) ; `spouse` → **à décider** (hors schéma) ; `relative` → **à décider** (hors schéma) ; `field of work` → `cache/wikidata.jsonl` (fait sur le monde) ; `religion or worldview` → **à décider** (hors schéma) ; `manner of death` → **à décider** (hors schéma) ; `instance of` → `iso-thes:broaderInstantial` ; `country of citizenship` → **à décider** (hors schéma) ; `native language` → **à décider** (hors schéma) ; `languages spoken, written or signed` → **à décider** (hors schéma) ; `writing language` → **à décider** (hors schéma) ; `number of children` → **à décider** (hors schéma) ; `Europeana entity` → **à décider** (hors schéma) ; `Wolfram Language entity code` → **à décider** (hors schéma) ; `Libris-URI` → **à décider** (hors schéma) ; `Krugosvet article (archived)` → `skos:closeMatch` ; `name in native language` → **à décider** (hors schéma) ; `date of death` → **à décider** (hors schéma) ; `date of birth` → **à décider** (hors schéma) ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `BHCL UUID` → **à décider** (hors schéma) ; `PhilPapers topic` → **à décider** (hors schéma) ; `subreddit` → **à décider** (hors schéma) ; `image` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `signature` → **à décider** (hors schéma) ; `Stack Exchange tag` → `skos:closeMatch` ; `ISNI` → **à décider** (hors schéma) ; `wikidata entity id: Q184226` → `skos:exactMatch: wd:Q184226` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Gilles Deleuze.json`
- **[[git]]** : `inferred:skos:narrower` → `inferred/git.json`
- **[[git worktree]]** : `inferred:skos:ancestor` → `inferred/git worktree.json`
- **[[github]]** : `inferred:skos:narrower` → `inferred/github.json`
- **[[gitHub actions]]** : `rdf:type: Concept` → `dcterms:type: Concept` ; `broader` → `skos:broader` ; `partOf` → `iso-thes:broaderPartitive` ; `description` → `skos:definition` ; `timestamp` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `inferred:skos:ancestor` → `inferred/gitHub actions.json` ; `inferred:skos:narrower` → `inferred/gitHub actions.json`
- **[[github ruleset]]** : `rdf:type: Concept` → `dcterms:type: Concept` ; `broader` → `skos:broader` ; `description` → `skos:definition` ; `timestamp` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `inferred:skos:ancestor` → `inferred/github ruleset.json`
- **[[goals]]** : `inferred:skos:ancestor` → `inferred/goals.json`
- **[[good and services classes]]** : `inferred:skos:ancestor` → `inferred/good and services classes.json` ; `inferred:skos:broader` → `inferred/good and services classes.json`
- **[[google sheet]]** : `inferred:skos:ancestor` → `inferred/google sheet.json`
- **[[gouvernance]]** : `needs` → **à décider** (hors schéma) ; `partOf` → `iso-thes:broaderPartitive` ; `product or material produced` → `cache/wikidata.jsonl` (fait sur le monde) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/gouvernance.json`
- **[[GPT2]]** : `inferred:skos:ancestor` → `inferred/GPT2.json`
- **[[gradient]]** : `inferred:skos:ancestor` → `inferred/gradient.json`
- **[[gradient descent]]** : `inferred:skos:narrower` → `inferred/gradient descent.json`
- **[[gramm-leach-bliley act (GLBA)]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/gramm-leach-bliley act (GLBA).json`
- **[[graph]]** : `originatesFrom` → **à décider** (hors schéma) ; `facet of` → `skos:broader` ; `studied by` → `cache/wikidata.jsonl` (fait sur le monde) ; `subclass of` → `iso-thes:broaderGeneric` ; `has part(s)` → `has part` ; `inferred:skos:narrower` → `inferred/graph.json`
- **[[graph hop]]** : `inferred:skos:ancestor` → `inferred/graph hop.json`
- **[[graph network analysis]]** : `inferred:skos:narrower` → `inferred/graph network analysis.json`
- **[[graph projection]]** : `inferred:skos:ancestor` → `inferred/graph projection.json` ; `inferred:skos:broader` → `inferred/graph projection.json`
- **[[graph theory]]** : `inferred:skos:narrower` → `inferred/graph theory.json`
- **[[graphics processing unit]]** : `inferred:skos:ancestor` → `inferred/graphics processing unit.json`
- **[[greediness]]** : `inferred:skos:ancestor` → `inferred/greediness.json`
- **[[ground truth]]** : `facet of` → `skos:broader` ; `subclass of` → `iso-thes:broaderGeneric` ; `instance of` → `iso-thes:broaderInstantial`
- **[[Group K-Fold Cross Validation]]** : `rdf:type: skos:Concept` → `dcterms:type: Concept` ; `inferred:skos:ancestor` → `inferred/Group K-Fold Cross Validation.json`
- **[[Hallucination]]** : `foundationalPaper` → `dcterms:isReferencedBy` ; `keyPapers` → `dcterms:isReferencedBy` ; `reliéA` → **à décider** (hors schéma) ; `affecte` → **à décider** (hors schéma) ; `mitigated_by` → **à décider** (hors schéma) ; `skos:narrower` → retiré ; chaque cible reçoit `skos:broader: [[Hallucination]]` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Hallucination.json`
- **[[handled-vs-gaps]]** : `inferred:skos:ancestor` → `inferred/handled-vs-gaps.json`
- **[[heterogeneous graph]]** : `inferred:skos:ancestor` → `inferred/heterogeneous graph.json` ; `inferred:skos:broader` → `inferred/heterogeneous graph.json`
- **[[heuristics]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/heuristics.json`
- **[[HGR-AI-1]]** : `inferred:skos:ancestor` → `inferred/HGR-AI-1.json`
- **[[hidden states]]** : `sameAs` → `skos:exactMatch` ; `partOf` → `iso-thes:broaderPartitive` ; `inferred:skos:ancestor` → `inferred/hidden states.json`
- **[[high-intent data discovery]]** : `inferred:skos:ancestor` → `inferred/high-intent data discovery.json`
- **[[hindsight scenario testing]]** : `inferred:skos:ancestor` → `inferred/hindsight scenario testing.json` ; `inferred:skos:broader` → `inferred/hindsight scenario testing.json`
- **[[historical bias]]** : `inferred:skos:ancestor` → `inferred/historical bias.json`
- **[[homebrew]]** : `inferred:skos:ancestor` → `inferred/homebrew.json`
- **[[hook]]** : `wikidata entity id: Q1203383` → `skos:exactMatch: wd:Q1203383`
- **[[horizontal scaling]]** : `inferred:skos:ancestor` → `inferred/horizontal scaling.json`
- **[[how-to-use]]** : `inferred:skos:ancestor` → `inferred/how-to-use.json`
- **[[html]]** : `inferred:skos:ancestor` → `inferred/html.json`
- **[[HTTP]]** : `inferred:skos:narrower` → `inferred/HTTP.json`
- **[[HTTP 403]]** : `inferred:skos:ancestor` → `inferred/HTTP 403.json`
- **[[hugging face]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/hugging face.json` ; `inferred:skos:narrower` → `inferred/hugging face.json`
- **[[human prediction]]** : `inferred:skos:ancestor` → `inferred/human prediction.json`
- **[[human-in-the-loop]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/human-in-the-loop.json` ; `inferred:skos:related` → `inferred/human-in-the-loop.json`
- **[[hybrid search]]** : `inferred:skos:ancestor` → `inferred/hybrid search.json`
- **[[hyperparameters]]** : `inferred:skos:related` → `inferred/hyperparameters.json`
- **[[hypothetical document embeddings (HyDE)]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/hypothetical document embeddings (HyDE).json`
- **[[IAM execution role]]** : `inferred:skos:ancestor` → `inferred/IAM execution role.json`
- **[[ideate]]** : `inferred:skos:ancestor` → `inferred/ideate.json`
- **[[idempotence]]** : `inferred:skos:ancestor` → `inferred/idempotence.json`
- **[[Identify factors]]** : `partOf` → `iso-thes:broaderPartitive` ; `importPartOf` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Identify factors.json`
- **[[impermanence]]** : `inferred:skos:ancestor` → `inferred/impermanence.json`
- **[[implementation detail]]** : `inferred:skos:ancestor` → `inferred/implementation detail.json`
- **[[implicature]]** : `inferred:skos:ancestor` → `inferred/implicature.json`
- **[[implicitness]]** : `inferred:skos:ancestor` → `inferred/implicitness.json`
- **[[in-context learning]]** : `inferred:skos:ancestor` → `inferred/in-context learning.json`
- **[[Independent Cascade Model]]** : `inferred:skos:ancestor` → `inferred/Independent Cascade Model.json`
- **[[independent continuant]]** : `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/independent continuant.json` ; `inferred:skos:narrower` → `inferred/independent continuant.json`
- **[[index]]** : `inferred:skos:narrower` → `inferred/index.json`
- **[[individual fairness]]** : `inferred:skos:ancestor` → `inferred/individual fairness.json`
- **[[inertia]]** : `inferred:skos:ancestor` → `inferred/inertia.json`
- **[[Inference]]** : `wikidata entity id: Q408386` → `skos:exactMatch: wd:Q408386` ; `model item` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `has part(s)` → `has part` ; `partially coincident with` → `cache/wikidata.jsonl` (fait sur le monde) ; `subclass of` → `iso-thes:broaderGeneric` ; `different from` → `skos:scopeNote` (« différent de … ») ; `instance of` → `iso-thes:broaderInstantial` ; `has characteristic` → `cache/wikidata.jsonl` (fait sur le monde) ; `main Wikidata property` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `Dewey Decimal Classification` → `dcterms:subject` ; `Library of Congress Classification` → `dcterms:subject` ; `PhilPapers topic` → **à décider** (hors schéma) ; `Stack Exchange tag` → `skos:closeMatch` ; `inferred:skos:ancestor` → `inferred/Inference.json` ; `inferred:skos:narrower` → `inferred/Inference.json`
- **[[Inference engine]]** : `wikidata entity id: Q1341685` → `skos:exactMatch: wd:Q1341685` ; `inspiredBy` → **à décider** (hors schéma) ; `subclass of` → `iso-thes:broaderGeneric` ; `has use` → `kg:hasUse` ; `inferred:skos:ancestor` → `inferred/Inference engine.json`
- **[[inference pipeline]]** : `partOf` → `iso-thes:broaderPartitive` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/inference pipeline.json` ; `inferred:skos:broader` → `inferred/inference pipeline.json`
- **[[inferred from attribute of entity]]** : `inferred:skos:ancestor` → `inferred/inferred from attribute of entity.json`
- **[[information content entity]]** : `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/information content entity.json` ; `inferred:skos:narrower` → `inferred/information content entity.json`
- **[[Information Gain (IG)]]** : `inferred:skos:ancestor` → `inferred/Information Gain (IG).json`
- **[[information integration]]** : `wikidata entity id: Q17092450` → `skos:exactMatch: wd:Q17092450`
- **[[information retrieval]]** : `wikidata entity id: Q816826` → `skos:exactMatch: wd:Q816826` ; `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/information retrieval.json` ; `inferred:skos:narrower` → `inferred/information retrieval.json`
- **[[infrastructure]]** : `inferred:skos:narrower` → `inferred/infrastructure.json`
- **[[ingestion]]** : `inferred:skos:ancestor` → `inferred/ingestion.json`
- **[[ingoing relationships]]** : `inferred:skos:ancestor` → `inferred/ingoing relationships.json`
- **[[inherent error]]** : `inferred:skos:ancestor` → `inferred/inherent error.json`
- **[[inputs]]** : `partOf` → `iso-thes:broaderPartitive`
- **[[instruction dataset]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/instruction dataset.json`
- **[[instructions]]** : `inferred:skos:ancestor` → `inferred/instructions.json`
- **[[Instructor model]]** : `inferred:skos:ancestor` → `inferred/Instructor model.json`
- **[[Integration tests]]** : `wikidata entity id: Q782466` → `skos:exactMatch: wd:Q782466` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Integration tests.json`
- **[[intellectual work]]** : `inferred:skos:narrower` → `inferred/intellectual work.json`
- **[[intention]]** : `instance of` → `iso-thes:broaderInstantial` ; `said to be the same as` → `skos:closeMatch` ; `has part(s)` → `has part` ; `has effect` → `cache/wikidata.jsonl` (fait sur le monde) ; `described by source` → `dcterms:isReferencedBy` ; `subclass of` → `iso-thes:broaderGeneric` ; `has cause` → `cache/wikidata.jsonl` (fait sur le monde) ; `facet of` → `skos:broader` ; `different from` → `skos:scopeNote` (« différent de … ») ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `IMDb keyword` → `skos:closeMatch` ; `pronunciation audio` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `UMLS CUI` → **à décider** (hors schéma) ; `MeSH tree code` → `dcterms:subject` ; `Krugosvet article (archived)` → `skos:closeMatch` ; `wikidata entity id: Q706622` → `skos:exactMatch: wd:Q706622` ; `inferred:skos:narrower` → `inferred/intention.json`
- **[[intentional human activity]]** : `inferred:skos:narrower` → `inferred/intentional human activity.json`
- **[[International (Nice) Classification of Goods and Services]]** : `wikidata entity id: Q193988` → `skos:exactMatch: wd:Q193988` ; `instance of` → `iso-thes:broaderInstantial` ; `main subject` → `dcterms:subject` ; `subclass of` → `iso-thes:broaderGeneric` ; `language of work or name` → **à décider** (hors schéma) ; `skos:narrower` → retiré ; chaque cible reçoit `skos:broader: [[International (Nice) Classification of Goods and Services]]`
- **[[Interpretability]]** : `inferred:skos:narrower` → `inferred/Interpretability.json`
- **[[Interpretation]]** : `inferred:skos:narrower` → `inferred/Interpretation.json`
- **[[Iron law of oligarchy]]** : `has cause` → `cache/wikidata.jsonl` (fait sur le monde) ; `facet of` → `skos:broader` ; `instance of` → `iso-thes:broaderInstantial` ; `image` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `wikidata entity id: Q1299608` → `skos:exactMatch: wd:Q1299608` ; `main subject` → `dcterms:subject`
- **[[James Clerk Maxwell]]** : `inferred:skos:ancestor` → `inferred/James Clerk Maxwell.json`
- **[[Java]]** : `inferred:skos:ancestor` → `inferred/Java.json`
- **[[joint venture]]** : `different from` → `skos:scopeNote` (« différent de … ») ; `instance of` → `iso-thes:broaderInstantial` ; `subclass of` → `iso-thes:broaderGeneric` ; `wikidata entity id: Q489209` → `skos:exactMatch: wd:Q489209` ; `inferred:skos:ancestor` → `inferred/joint venture.json`
- **[[JSON]]** : `inferred:skos:ancestor` → `inferred/JSON.json`
- **[[Judea Pearl]]** : `wikidata entity id: Q92824` → `skos:exactMatch: wd:Q92824` ; `instance of` → `iso-thes:broaderInstantial` ; `field of work` → `cache/wikidata.jsonl` (fait sur le monde)
- **[[judgment]]** : `inferred:skos:ancestor` → `inferred/judgment.json`
- **[[Jupyter notebooks]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Jupyter notebooks.json`
- **[[K-Means Clustering]]** : `inferred:skos:ancestor` → `inferred/K-Means Clustering.json` ; `inferred:skos:broader` → `inferred/K-Means Clustering.json`
- **[[K-Nearest Neighbor algorithm]]** : `inferred:skos:narrower` → `inferred/K-Nearest Neighbor algorithm.json`
- **[[K-Nearest neighbor regressor]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/K-Nearest neighbor regressor.json`
- **[[Keras]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Keras.json`
- **[[Kernel]]** : `inferred:skos:narrower` → `inferred/Kernel.json`
- **[[knowledge]]** : `inferred:skos:narrower` → `inferred/knowledge.json`
- **[[knowledge base]]** : `wikidata entity id: Q593744` → `skos:exactMatch: wd:Q593744` ; `subclass of` → `iso-thes:broaderGeneric` ; `has part(s)` → `has part` ; `inferred:skos:ancestor` → `inferred/knowledge base.json` ; `inferred:skos:related` → `inferred/knowledge base.json`
- **[[knowledge extraction]]** : `wikidata entity id: Q1582085` → `skos:exactMatch: wd:Q1582085`
- **[[knowledge graph]]** : `inferred:skos:narrower` → `inferred/knowledge graph.json`
- **[[knowledge management]]** : `wikidata entity id: Q192060` → `skos:exactMatch: wd:Q192060` ; `subclass of` → `iso-thes:broaderGeneric` ; `instance of` → `iso-thes:broaderInstantial` ; `facet of` → `skos:broader` ; `uses` → `kg:uses` ; `practiced by` → `cache/wikidata.jsonl` (fait sur le monde) ; `different from` → `skos:scopeNote` (« différent de … ») ; `inferred:skos:related` → `inferred/knowledge management.json`
- **[[knowledge organization system]]** : `has part(s)` → `has part` ; `based on` → **à décider** (hors schéma) ; `studied by` → `cache/wikidata.jsonl` (fait sur le monde) ; `subject has role` → **à décider** (hors schéma) ; `subclass of` → `iso-thes:broaderGeneric` ; `maintained by WikiProject` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `instance of` → `iso-thes:broaderInstantial` ; `properties for this type` → **à décider** (hors schéma) ; `exact match` → `skos:exactMatch` ; `wikidata entity id: Q6423319` → `skos:exactMatch: wd:Q6423319` ; `inferred:skos:ancestor` → `inferred/knowledge organization system.json` ; `inferred:skos:narrower` → `inferred/knowledge organization system.json` ; `inferred:skos:related` → `inferred/knowledge organization system.json`
- **[[knowledge transfer]]** : `wikidata entity id: Q2586354` → `skos:exactMatch: wd:Q2586354` ; `subclass of` → `iso-thes:broaderGeneric` ; `different from` → `skos:scopeNote` (« différent de … »)
- **[[knowledge type]]** : `wikidata entity id: Q110403031` → `skos:exactMatch: wd:Q110403031`
- **[[knowledge worker]]** : `inferred:skos:ancestor` → `inferred/knowledge worker.json`
- **[[La bibliothèque de Babel]]** : `inferred:skos:related` → `inferred/La bibliothèque de Babel.json`
- **[[La Société de Connaissance]]** : `inferred:skos:ancestor` → `inferred/La Société de Connaissance.json`
- **[[label]]** : `inferred:skos:ancestor` → `inferred/label.json`
- **[[label encoding]]** : `same` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/label encoding.json`
- **[[langfuse]]** : `inferred:skos:related` → `inferred/langfuse.json`
- **[[language modeling]]** : `inferred:skos:narrower` → `inferred/language modeling.json`
- **[[large language model]]** : `wikidata entity id: Q115305900` → `skos:exactMatch: wd:Q115305900` ; `uses` → `kg:uses` ; `facet of` → `skos:broader` ; `inferred:skos:narrower` → `inferred/large language model.json`
- **[[latent]]** : `inferred:skos:ancestor` → `inferred/latent.json`
- **[[latent space]]** : `uses` → `kg:uses` ; `subclass of` → `iso-thes:broaderGeneric` ; `facet of` → `skos:broader` ; `wikidata entity id: Q107154297` → `skos:exactMatch: wd:Q107154297` ; `EmbodiementOf` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/latent space.json`
- **[[latent travel]]** : `inferred:skos:ancestor` → `inferred/latent travel.json`
- **[[lawyer]]** : `wears` → **à décider** (hors schéma) ; `patron saint` → **à décider** (hors schéma) ; `different from` → `skos:scopeNote` (« différent de … ») ; `subclass of` → `iso-thes:broaderGeneric` ; `said to be the same as` → `skos:closeMatch` ; `described by source` → `dcterms:isReferencedBy` ; `field of this occupation` → **à décider** (hors schéma) ; `instance of` → `iso-thes:broaderInstantial` ; `topic has template` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `category for eponymous categories` → **à décider** (hors schéma) ; `ROME Occupation Code` → **à décider** (hors schéma) ; `SSYK 2012 The Swedish Standard Classification of Occupations` → **à décider** (hors schéma) ; `ISCO-08 occupation class` → **à décider** (hors schéma) ; `ISCO-88 occupation class` → **à décider** (hors schéma) ; `Commons gallery` → **à décider** (hors schéma) ; `male form of label` → **à décider** (hors schéma) ; `female form of label` → **à décider** (hors schéma) ; `image` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `IMDb keyword` → `skos:closeMatch` ; `OpenStreetMap key` → **à décider** (hors schéma) ; `Unicode character` → **à décider** (hors schéma) ; `short name` → `skos:altLabel` ; `Dewey Decimal Classification` → `dcterms:subject` ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `pronunciation audio` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `label in sign language` → **à décider** (hors schéma) ; `equivalent class` → `skos:closeMatch` ; `U.S. National Archives Identifier` → **à décider** (hors schéma) ; `SOC Code (2010)` → **à décider** (hors schéma) ; `O*NET OnLine code` → **à décider** (hors schéma) ; `Provenio UUID` → **à décider** (hors schéma) ; `UMLS CUI` → **à décider** (hors schéma) ; `MeSH tree code` → `dcterms:subject` ; `Baidu Tieba name` → **à décider** (hors schéma) ; `OpenStreetMap tag` → **à décider** (hors schéma) ; `wikidata entity id: Q40348` → `skos:exactMatch: wd:Q40348`
- **[[Layer]]** : `foundationalPaper` → `dcterms:isReferencedBy` ; `keyPapers` → `dcterms:isReferencedBy` ; `composedOf` → `has part` ; `skos:narrower` → retiré ; chaque cible reçoit `skos:broader: [[Layer]]` ; `connectsThrough` → **à décider** (hors schéma) ; `formsPartOf` → `iso-thes:broaderPartitive`
- **[[layered architecture]]** : `inferred:skos:ancestor` → `inferred/layered architecture.json`
- **[[Le Bateau Ivre des données]]** : `instanceOf` → `iso-thes:broaderInstantial`
- **[[lean logic]]** : `inferred:skos:ancestor` → `inferred/lean logic.json`
- **[[learning]]** : `wikidata entity id: Q133500` → `skos:exactMatch: wd:Q133500` ; `instance of` → `iso-thes:broaderInstantial` ; `subclass of` → `iso-thes:broaderGeneric` ; `has effect` → `cache/wikidata.jsonl` (fait sur le monde) ; `has cause` → `cache/wikidata.jsonl` (fait sur le monde) ; `facet of` → `skos:broader` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/learning.json` ; `inferred:skos:narrower` → `inferred/learning.json`
- **[[learning bias]]** : `inferred:skos:ancestor` → `inferred/learning bias.json`
- **[[Learning curve]]** : `inferred:skos:ancestor` → `inferred/Learning curve.json`
- **[[Learning rate]]** : `inferred:skos:ancestor` → `inferred/Learning rate.json`
- **[[legal opinion]]** : `instance of` → `iso-thes:broaderInstantial` ; `subclass of` → `iso-thes:broaderGeneric` ; `wikidata entity id: Q1911852` → `skos:exactMatch: wd:Q1911852`
- **[[Levenshtein]]** : `inferred:skos:ancestor` → `inferred/Levenshtein.json`
- **[[liability]]** : `inferred:skos:ancestor` → `inferred/liability.json`
- **[[License]]** : `inferred:skos:ancestor` → `inferred/License.json`
- **[[Linear models]]** : `inferred:skos:narrower` → `inferred/Linear models.json`
- **[[Linear regression models]]** : `inferred:skos:ancestor` → `inferred/Linear regression models.json`
- **[[list of values as qualifiers]]** : `inferred:skos:ancestor` → `inferred/list of values as qualifiers.json`
- **[[LLaMA]]** : `inferred:skos:ancestor` → `inferred/LLaMA.json`
- **[[LLM Metrics]]** : `inferred:skos:ancestor` → `inferred/LLM Metrics.json`
- **[[LLM Models]]** : `inferred:skos:ancestor` → `inferred/LLM Models.json`
- **[[LLM Observability]]** : `inferred:skos:related` → `inferred/LLM Observability.json`
- **[[LLM output evaluation]]** : `inferred:skos:narrower` → `inferred/LLM output evaluation.json`
- **[[LLM Path Extractors]]** : `inferred:skos:ancestor` → `inferred/LLM Path Extractors.json`
- **[[LLM-as-a-judge]]** : `instance of` → `iso-thes:broaderInstantial` ; `uses` → `kg:uses` ; `studied by` → `cache/wikidata.jsonl` (fait sur le monde) ; `wikidata entity id: Q134468621` → `skos:exactMatch: wd:Q134468621`
- **[[LLM-as-judges]]** : `inferred:skos:ancestor` → `inferred/LLM-as-judges.json`
- **[[Local Interpretable Model-Agnostic Explanations (LIME)]]** : `inferred:skos:ancestor` → `inferred/Local Interpretable Model-Agnostic Explanations (LIME).json`
- **[[Log]]** : `inferred:skos:ancestor` → `inferred/Log.json`
- **[[logbook]]** : `wikidata entity id: Q1414013` → `skos:exactMatch: wd:Q1414013` ; `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/logbook.json` ; `inferred:skos:narrower` → `inferred/logbook.json`
- **[[logical contradiction]]** : `has part(s)` → `has part` ; `opposite of` → `kg:oppositeOf` ; `subclass of` → `iso-thes:broaderGeneric` ; `described by source` → `dcterms:isReferencedBy` ; `instance of` → `iso-thes:broaderInstantial` ; `characteristic of` → `cache/wikidata.jsonl` (fait sur le monde) ; `Dewey Decimal Classification` → `dcterms:subject` ; `OmegaWiki Defined Meaning` → `skos:closeMatch` ; `Harper's tag` → **à décider** (hors schéma) ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `wikidata entity id: Q363948` → `skos:exactMatch: wd:Q363948`
- **[[Logistic regression]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Logistic regression.json`
- **[[Logit link function]]** : `inferred:skos:related` → `inferred/Logit link function.json`
- **[[loss function]]** : `foundationalPaper` → `dcterms:isReferencedBy` ; `keyPapers` → `dcterms:isReferencedBy` ; `minimizedBy` → **à décider** (hors schéma) ; `examples` → **à décider** (hors schéma) ; `properties` → **à décider** (hors schéma) ; `usedIn` → `kg:usedBy` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/loss function.json`
- **[[Louvain algorithm]]** : `inferred:skos:ancestor` → `inferred/Louvain algorithm.json`
- **[[Low-Rank Adaptation]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Low-Rank Adaptation.json`
- **[[Machine Leaning Baseline]]** : `inferred:skos:related` → `inferred/Machine Leaning Baseline.json`
- **[[machine learning]]** : `inferred:skos:narrower` → `inferred/machine learning.json`
- **[[Machine learning engineer]]** : `inferred:skos:ancestor` → `inferred/Machine learning engineer.json`
- **[[machine learning projects]]** : `inferred:skos:narrower` → `inferred/machine learning projects.json`
- **[[machine learning systems]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/machine learning systems.json`
- **[[macros]]** : `inferred:skos:ancestor` → `inferred/macros.json`
- **[[man-Computer Symbiosis]]** : `inferred:skos:ancestor` → `inferred/man-Computer Symbiosis.json`
- **[[management]]** : `fabrication method` → **à décider** (hors schéma) ; `subclass of` → `iso-thes:broaderGeneric` ; `has characteristic` → `cache/wikidata.jsonl` (fait sur le monde) ; `class of object(s) of occurrence` → **à décider** (hors schéma) ; `facet of` → `skos:broader` ; `studied by` → `cache/wikidata.jsonl` (fait sur le monde) ; `different from` → `skos:scopeNote` (« différent de … ») ; `practiced by` → `cache/wikidata.jsonl` (fait sur le monde) ; `said to be the same as` → `skos:closeMatch` ; `topic's main template` → **à décider** (hors schéma) ; `instance of` → `iso-thes:broaderInstantial` ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `image` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `WordLift URL` → **à décider** (hors schéma) ; `involves` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/management.json` ; `inferred:skos:narrower` → `inferred/management.json`
- **[[management of PII]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/management of PII.json`
- **[[manifold]]** : `inferred:skos:ancestor` → `inferred/manifold.json`
- **[[manual operation]]** : `inferred:skos:ancestor` → `inferred/manual operation.json`
- **[[manual override]]** : `wikidata entity id: Q6752322` → `skos:exactMatch: wd:Q6752322` ; `opposite of` → `kg:oppositeOf`
- **[[mapping]]** : `wikidata entity id: Q370502` → `skos:exactMatch: wd:Q370502` ; `instance of` → `iso-thes:broaderInstantial` ; `has characteristic` → `cache/wikidata.jsonl` (fait sur le monde) ; `uses` → `kg:uses` ; `different from` → `skos:scopeNote` (« différent de … ») ; `inferred:skos:narrower` → `inferred/mapping.json`
- **[[Margin]]** : `inferred:skos:related` → `inferred/Margin.json`
- **[[Mark-up language]]** : `inferred:skos:narrower` → `inferred/Mark-up language.json`
- **[[Markdown]]** : `wikidata entity id: Q1193600` → `skos:exactMatch: wd:Q1193600` ; `influenced by` → **à décider** (hors schéma) ; `inferred:skos:ancestor` → `inferred/Markdown.json`
- **[[masked language models]]** : `inferred:skos:narrower` → `inferred/masked language models.json`
- **[[master data]]** : `wikidata entity id: Q384093` → `skos:exactMatch: wd:Q384093` ; `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/master data.json` ; `inferred:skos:related` → `inferred/master data.json`
- **[[matplotlib]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/matplotlib.json`
- **[[MCP host]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/MCP host.json`
- **[[MCP server]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/MCP server.json`
- **[[mean absolute error]]** : `inferred:skos:ancestor` → `inferred/mean absolute error.json`
- **[[mean Absolute Percent Error]]** : `inferred:skos:ancestor` → `inferred/mean Absolute Percent Error.json`
- **[[meaning]]** : `inferred:skos:ancestor` → `inferred/meaning.json`
- **[[measure]]** : `inferred:skos:ancestor` → `inferred/measure.json`
- **[[measurement bias]]** : `inferred:skos:related` → `inferred/measurement bias.json`
- **[[medical data privacy]]** : `inferred:skos:narrower` → `inferred/medical data privacy.json`
- **[[Memory]]** : `inferred:skos:ancestor` → `inferred/Memory.json`
- **[[mergers and acquisitions]]** : `has part(s)` → `has part` ; `opposite of` → `kg:oppositeOf` ; `subclass of` → `iso-thes:broaderGeneric` ; `wikidata entity id: Q731112` → `skos:exactMatch: wd:Q731112` ; `inferred:skos:ancestor` → `inferred/mergers and acquisitions.json`
- **[[message-oriented middleware]]** : `inferred:skos:ancestor` → `inferred/message-oriented middleware.json`
- **[[metadata]]** : `inferred:skos:ancestor` → `inferred/metadata.json`
- **[[Metadata management]]** : `inferred:skos:narrower` → `inferred/Metadata management.json`
- **[[metric]]** : `inferred:skos:narrower` → `inferred/metric.json`
- **[[Michael Polanyi]]** : `wikidata entity id: Q163087` → `skos:exactMatch: wd:Q163087`
- **[[Min-max normalization]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Min-max normalization.json`
- **[[Mini-batch gradient descent]]** : `inferred:skos:ancestor` → `inferred/Mini-batch gradient descent.json`
- **[[minority interest vs full ownership]]** : `inferred:skos:ancestor` → `inferred/minority interest vs full ownership.json`
- **[[minority shareholder]]** : `subclass of` → `iso-thes:broaderGeneric` ; `wikidata entity id: Q117049212` → `skos:exactMatch: wd:Q117049212` ; `inferred:skos:ancestor` → `inferred/minority shareholder.json`
- **[[missing at random]]** : `inferred:skos:ancestor` → `inferred/missing at random.json`
- **[[missing completely at random]]** : `inferred:skos:ancestor` → `inferred/missing completely at random.json`
- **[[missing not at random]]** : `inferred:skos:ancestor` → `inferred/missing not at random.json`
- **[[mistral agents]]** : `inferred:skos:ancestor` → `inferred/mistral agents.json`
- **[[ML models]]** : `inferred:skos:narrower` → `inferred/ML models.json`
- **[[ML system]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/ML system.json` ; `inferred:skos:narrower` → `inferred/ML system.json`
- **[[ML system design process]]** : `shouldPayAttentionTo` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/ML system design process.json`
- **[[ML System failures]]** : `studied by` → `cache/wikidata.jsonl` (fait sur le monde) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/ML System failures.json`
- **[[ML system monitoring]]** : `inferred:skos:narrower` → `inferred/ML system monitoring.json`
- **[[mockups]]** : `inferred:skos:ancestor` → `inferred/mockups.json`
- **[[model]]** : `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/model.json`
- **[[Model Context Protocol (MCP)]]** : `wikidata entity id: Q133436854` → `skos:exactMatch: wd:Q133436854` ; `compatible with` → **à décider** (hors schéma) ; `inferred:skos:narrower` → `inferred/Model Context Protocol (MCP).json`
- **[[model contract]]** : `wikidata entity id: Q63032908` → `skos:exactMatch: wd:Q63032908` ; `subclass of` → `iso-thes:broaderGeneric` ; `different from` → `skos:scopeNote` (« différent de … ») ; `partially coincident with` → `cache/wikidata.jsonl` (fait sur le monde) ; `example` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/model contract.json` ; `inferred:skos:broader` → `inferred/model contract.json`
- **[[model decay]]** : `inferred:skos:ancestor` → `inferred/model decay.json`
- **[[model evaluation]]** : `inferred:skos:narrower` → `inferred/model evaluation.json`
- **[[model fit]]** : `inferred:skos:narrower` → `inferred/model fit.json`
- **[[model lineage]]** : `featureOf` → **à décider** (hors schéma)
- **[[model maintenance]]** : `inferred:skos:narrower` → `inferred/model maintenance.json`
- **[[model registry]]** : `inferred:skos:ancestor` → `inferred/model registry.json`
- **[[model selection]]** : `inferred:skos:narrower` → `inferred/model selection.json`
- **[[model tuning]]** : `inferred:skos:narrower` → `inferred/model tuning.json`
- **[[model versioning]]** : `inferred:skos:ancestor` → `inferred/model versioning.json`
- **[[model vocabulary]]** : `inferred:skos:ancestor` → `inferred/model vocabulary.json`
- **[[Modeling]]** : `partOf` → `iso-thes:broaderPartitive` ; `sameAs` → `skos:exactMatch` ; `broader` → `skos:broader` ; `different from` → `skos:scopeNote` (« différent de … ») ; `inferred:skos:ancestor` → `inferred/Modeling.json`
- **[[moderation]]** : `inferred:skos:ancestor` → `inferred/moderation.json`
- **[[modular programming]]** : `subclass of` → `iso-thes:broaderGeneric` ; `part of` → `iso-thes:broaderPartitive` ; `uses` → `kg:uses` ; `instance of` → `iso-thes:broaderInstantial` ; `has characteristic` → `cache/wikidata.jsonl` (fait sur le monde) ; `does not use` → **à décider** (hors schéma) ; `Stack Exchange tag` → `skos:closeMatch` ; `wikidata entity id: Q6453666` → `skos:exactMatch: wd:Q6453666` ; `inferred:skos:ancestor` → `inferred/modular programming.json`
- **[[modularity]]** : `inferred:skos:ancestor` → `inferred/modularity.json`
- **[[modélisation]]** : `partOf` → `iso-thes:broaderPartitive`
- **[[monitor]]** : `inferred:skos:ancestor` → `inferred/monitor.json`
- **[[monopartite graph]]** : `inferred:skos:ancestor` → `inferred/monopartite graph.json`
- **[[multiclass confusion matrix]]** : `inferred:skos:ancestor` → `inferred/multiclass confusion matrix.json`
- **[[multilayer perceptron]]** : `foundationalPaper` → `dcterms:isReferencedBy` ; `keyPapers` → `dcterms:isReferencedBy` ; `subclass of` → `iso-thes:broaderGeneric` ; `composedOf` → `has part` ; `enables` → **à décider** (hors schéma) ; `trainedBy` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/multilayer perceptron.json`
- **[[multimodal model]]** : `inferred:skos:ancestor` → `inferred/multimodal model.json`
- **[[Multipartite graph]]** : `inferred:skos:narrower` → `inferred/Multipartite graph.json`
- **[[N-Fold Cross Validation]]** : `inferred:skos:related` → `inferred/N-Fold Cross Validation.json`
- **[[Naive Bayes Classifier]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Naive Bayes Classifier.json`
- **[[named-ranges]]** : `inferred:skos:ancestor` → `inferred/named-ranges.json`
- **[[Nano-precision detection system]]** : `instance of` → `iso-thes:broaderInstantial` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Nano-precision detection system.json`
- **[[Narrow AI]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Narrow AI.json`
- **[[Natural Language Processing]]** : `subFieldOf` → `iso-thes:broaderGeneric` ; `useTechniques` → **à décider** (hors schéma) ; `relatedTo` → `skos:related` ; `applications` → **à décider** (hors schéma) ; `techniques` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Natural Language Processing.json` ; `inferred:skos:narrower` → `inferred/Natural Language Processing.json`
- **[[negotiation]]** : `inferred:skos:narrower` → `inferred/negotiation.json`
- **[[Nested schema]]** : `inferred:skos:ancestor` → `inferred/Nested schema.json`
- **[[Network graph]]** : `inferred:skos:ancestor` → `inferred/Network graph.json` ; `inferred:skos:broader` → `inferred/Network graph.json`
- **[[Neural network models]]** : `inferred:skos:narrower` → `inferred/Neural network models.json`
- **[[neuron layer]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/neuron layer.json`
- **[[newsletter]]** : `inferred:skos:ancestor` → `inferred/newsletter.json`
- **[[node]]** : `inferred:skos:ancestor` → `inferred/node.json` ; `inferred:skos:broader` → `inferred/node.json`
- **[[node similarity]]** : `inferred:skos:ancestor` → `inferred/node similarity.json`
- **[[non-compete clause]]** : `inferred:skos:ancestor` → `inferred/non-compete clause.json`
- **[[non-parametric algorithms]]** : `inferred:skos:ancestor` → `inferred/non-parametric algorithms.json`
- **[[non-preferred term]]** : `wikidata entity id: Q115778157` → `skos:exactMatch: wd:Q115778157` ; `part of` → `iso-thes:broaderPartitive` ; `opposite of` → `kg:oppositeOf`
- **[[normalized schema]]** : `inferred:skos:ancestor` → `inferred/normalized schema.json`
- **[[normative statement]]** : `wikidata entity id: Q7053129` → `skos:exactMatch: wd:Q7053129` ; `subclass of` → `iso-thes:broaderGeneric` ; `opposite of` → `kg:oppositeOf` ; `inferred:skos:ancestor` → `inferred/normative statement.json`
- **[[NoSQL database]]** : `inferred:skos:ancestor` → `inferred/NoSQL database.json`
- **[[notation]]** : `wikidata entity id: Q2001982` → `skos:exactMatch: wd:Q2001982` ; `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/notation.json`
- **[[null morpheme]]** : `inferred:skos:ancestor` → `inferred/null morpheme.json`
- **[[Numpy]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Numpy.json`
- **[[OAuth]]** : `inferred:skos:ancestor` → `inferred/OAuth.json`
- **[[Object]]** : `inferred:skos:narrower` → `inferred/Object.json`
- **[[Object Management Group]]** : `wikidata entity id: Q252733` → `skos:exactMatch: wd:Q252733`
- **[[Observations]]** : `communicatesWith` → **à décider** (hors schéma)
- **[[Occam's rasor]]** : `inferred:skos:ancestor` → `inferred/Occam's rasor.json`
- **[[occurrence]]** : `has characteristic` → `cache/wikidata.jsonl` (fait sur le monde) ; `has effect` → `cache/wikidata.jsonl` (fait sur le monde) ; `different from` → `skos:scopeNote` (« différent de … ») ; `characteristic of` → `cache/wikidata.jsonl` (fait sur le monde) ; `has cause` → `cache/wikidata.jsonl` (fait sur le monde) ; `model item` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `said to be the same as` → `skos:closeMatch` ; `topic has template` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `described by source` → `dcterms:isReferencedBy` ; `maintained by WikiProject` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `subclass of` → `iso-thes:broaderGeneric` ; `instance of` → `iso-thes:broaderInstantial` ; `properties for this type` → **à décider** (hors schéma) ; `related Wikidata property` → **à décider** (hors schéma) ; `OmegaWiki Defined Meaning` → `skos:closeMatch` ; `equivalent class` → `skos:closeMatch` ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `wikidata entity id: Q1190554` → `skos:exactMatch: wd:Q1190554` ; `inferred:skos:ancestor` → `inferred/occurrence.json` ; `inferred:skos:narrower` → `inferred/occurrence.json`
- **[[occurrent]]** : `disjoint with` → `kg:disjointWith` ; `inferred:skos:narrower` → `inferred/occurrent.json`
- **[[Odds]]** : `inferred:skos:related` → `inferred/Odds.json`
- **[[office automation]]** : `inferred:skos:ancestor` → `inferred/office automation.json`
- **[[Offline models]]** : `inferred:skos:ancestor` → `inferred/Offline models.json`
- **[[Ollama]]** : `has use` → `kg:hasUse` ; `copyright license` → **à décider** (hors schéma) ; `instance of` → `iso-thes:broaderInstantial` ; `copyright status` → **à décider** (hors schéma) ; `uses` → `kg:uses` ; `named after` → `cache/wikidata.jsonl` (fait sur le monde) ; `platform` → **à décider** (hors schéma) ; `programmed in` → `kg:programmedIn` ; `source code repository URL` → **à décider** (hors schéma) ; `software version identifier` → **à décider** (hors schéma) ; `official website` → **à décider** (hors schéma) ; `MacPorts port` → **à décider** (hors schéma) ; `GitHub account` → **à décider** (hors schéma) ; `logo image` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `wikidata entity id: Q124636097` → `skos:exactMatch: wd:Q124636097` ; `instanceOf` → `iso-thes:broaderInstantial`
- **[[onboarding]]** : `wikidata entity id: Q7091744` → `skos:exactMatch: wd:Q7091744` ; `instance of` → `iso-thes:broaderInstantial` ; `subclass of` → `iso-thes:broaderGeneric` ; `said to be the same as` → `skos:closeMatch` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/onboarding.json`
- **[[One-hot encoding]]** : `same` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/One-hot encoding.json`
- **[[Online models]]** : `inferred:skos:ancestor` → `inferred/Online models.json`
- **[[Online prediction]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Online prediction.json` ; `inferred:skos:broader` → `inferred/Online prediction.json`
- **[[Ontology]]** : `inferred:skos:narrower` → `inferred/Ontology.json`
- **[[ontology engineering]]** : `inferred:skos:ancestor` → `inferred/ontology engineering.json`
- **[[open data]]** : `inferred:skos:ancestor` → `inferred/open data.json`
- **[[Open source software]]** : `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/Open source software.json`
- **[[openpyxl]]** : `rdf:type: Research Note` → `dcterms:type: Concept` (à confirmer : note de recherche) ; `title` → `skos:prefLabel` ; `description` → `skos:definition` ; `timestamp` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `instanceOf` → `iso-thes:broaderInstantial` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/openpyxl.json`
- **[[operating characteristic curve]]** : `described by source` → `dcterms:isReferencedBy` ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `wikidata entity id: Q1517752` → `skos:exactMatch: wd:Q1517752` ; `inferred:skos:narrower` → `inferred/operating characteristic curve.json`
- **[[Optimizer algorithm]]** : `inferred:skos:narrower` → `inferred/Optimizer algorithm.json`
- **[[organizing principles]]** : `inferred:skos:narrower` → `inferred/organizing principles.json`
- **[[orientation]]** : `facet of` → `skos:broader` ; `different from` → `skos:scopeNote` (« différent de … ») ; `has part(s)` → `has part` ; `subclass of` → `iso-thes:broaderGeneric` ; `main Wikidata property` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `part of` → `iso-thes:broaderPartitive` ; `wikidata entity id: Q2235286` → `skos:exactMatch: wd:Q2235286`
- **[[other-losses]]** : `inferred:skos:ancestor` → `inferred/other-losses.json`
- **[[outcome]]** : `inferred:skos:ancestor` → `inferred/outcome.json`
- **[[Outgoing relationships]]** : `inferred:skos:ancestor` → `inferred/Outgoing relationships.json`
- **[[Outliers]]** : `inferred:skos:ancestor` → `inferred/Outliers.json`
- **[[output]]** : `inferred:skos:ancestor` → `inferred/output.json`
- **[[Overfitting]]** : `inferred:skos:narrower` → `inferred/Overfitting.json` ; `inferred:skos:related` → `inferred/Overfitting.json`
- **[[Package installer]]** : `inferred:skos:ancestor` → `inferred/Package installer.json`
- **[[Pandas]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Pandas.json`
- **[[parameter]]** : `inferred:skos:ancestor` → `inferred/parameter.json`
- **[[parsing]]** : `studied by` → `cache/wikidata.jsonl` (fait sur le monde) ; `subclass of` → `iso-thes:broaderGeneric` ; `partOf` → `iso-thes:broaderPartitive` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/parsing.json` ; `inferred:skos:broader` → `inferred/parsing.json`
- **[[partial column range]]** : `inferred:skos:ancestor` → `inferred/partial column range.json`
- **[[path]]** : `inferred:skos:ancestor` → `inferred/path.json` ; `inferred:skos:broader` → `inferred/path.json`
- **[[pattern]]** : `inferred:skos:ancestor` → `inferred/pattern.json`
- **[[Peppol]]** : `wikidata entity id: Q1585098` → `skos:exactMatch: wd:Q1585098` ; `instance of` → `iso-thes:broaderInstantial`
- **[[Perception]]** : `inferred:skos:ancestor` → `inferred/Perception.json` ; `inferred:skos:broader` → `inferred/Perception.json`
- **[[performance indicator]]** : `wikidata entity id: Q860554` → `skos:exactMatch: wd:Q860554` ; `subclass of` → `iso-thes:broaderGeneric` ; `has use` → `kg:hasUse` ; `broader` → `skos:broader`
- **[[periodic table]]** : `short name` → `skos:altLabel` ; `Stack Exchange tag` → `skos:closeMatch` ; `has part(s)` → `has part` ; `named after` → `cache/wikidata.jsonl` (fait sur le monde) ; `part of` → `iso-thes:broaderPartitive` ; `subclass of` → `iso-thes:broaderGeneric` ; `described by source` → `dcterms:isReferencedBy` ; `instance of` → `iso-thes:broaderInstantial` ; `based on` → **à décider** (hors schéma) ; `topic has template` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `maintained by WikiProject` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `history of topic` → **à décider** (hors schéma) ; `permanent duplicated item` → **à décider** (hors schéma) ; `depicted by` → **à décider** (hors schéma) ; `inception` → `cache/wikidata.jsonl` (fait sur le monde) ; `location of creation` → **à décider** (hors schéma) ; `discoverer or inventor` → `cache/wikidata.jsonl` (fait sur le monde) ; `items classified` → **à décider** (hors schéma) ; `depicts` → **à décider** (hors schéma) ; `does not have part` → **à décider** (hors schéma) ; `country of origin` → **à décider** (hors schéma) ; `OmegaWiki Defined Meaning` → `skos:closeMatch` ; `Dewey Decimal Classification` → `dcterms:subject` ; `video` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `pronunciation audio` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `3D model` → **à décider** (hors schéma) ; `image` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `Colon Classification` → **à décider** (hors schéma) ; `Krugosvet article (archived)` → `skos:closeMatch` ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `Commons gallery` → **à décider** (hors schéma) ; `Gujarati Vishwakosh entry` → **à décider** (hors schéma) ; `wikidata entity id: Q10693` → `skos:exactMatch: wd:Q10693`
- **[[permanence]]** : `inferred:skos:ancestor` → `inferred/permanence.json`
- **[[Perplexity]]** : `inferred:skos:ancestor` → `inferred/Perplexity.json`
- **[[persistence]]** : `inferred:skos:ancestor` → `inferred/persistence.json`
- **[[person]]** : `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/person.json` ; `inferred:skos:narrower` → `inferred/person.json`
- **[[personal computing resources]]** : `inferred:skos:ancestor` → `inferred/personal computing resources.json`
- **[[Personalization]]** : `inferred:skos:ancestor` → `inferred/Personalization.json`
- **[[philosophical concept]]** : `wikidata entity id: Q33104279` → `skos:exactMatch: wd:Q33104279`
- **[[Physics]]** : `has part(s)` → `has part` ; `practiced by` → `cache/wikidata.jsonl` (fait sur le monde) ; `history of topic` → **à décider** (hors schéma) ; `instance of` → `iso-thes:broaderInstantial` ; `different from` → `skos:scopeNote` (« différent de … ») ; `subclass of` → `iso-thes:broaderGeneric` ; `is the study of` → `cache/wikidata.jsonl` (fait sur le monde) ; `model item` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `wikidata entity id: Q413` → `skos:exactMatch: wd:Q413`
- **[[pictorial fraction chart]]** : `inferred:skos:ancestor` → `inferred/pictorial fraction chart.json`
- **[[pierre vermersch]]** : `inferred:skos:ancestor` → `inferred/pierre vermersch.json`
- **[[Pipe function]]** : `inferred:skos:ancestor` → `inferred/Pipe function.json`
- **[[Pipelines]]** : `foundationalPaper` → `dcterms:isReferencedBy` ; `keyPapers` → `dcterms:isReferencedBy` ; `enables` → **à décider** (hors schéma) ; `components` → `has part` ; `implementations` → **à décider** (hors schéma) ; `skos:narrower` → retiré ; chaque cible reçoit `skos:broader: [[Pipelines]]` ; `inferred:skos:narrower` → `inferred/Pipelines.json`
- **[[platform-limits]]** : `inferred:skos:ancestor` → `inferred/platform-limits.json`
- **[[Plugins]]** : `inferred:skos:ancestor` → `inferred/Plugins.json`
- **[[Polynomial regression]]** : `inferred:skos:ancestor` → `inferred/Polynomial regression.json`
- **[[positive statement]]** : `wikidata entity id: Q7233295` → `skos:exactMatch: wd:Q7233295` ; `subclass of` → `iso-thes:broaderGeneric` ; `opposite of` → `kg:oppositeOf` ; `inferred:skos:ancestor` → `inferred/positive statement.json`
- **[[Post-training]]** : `inferred:skos:ancestor` → `inferred/Post-training.json` ; `inferred:skos:broader` → `inferred/Post-training.json`
- **[[PostgreSQL]]** : `publicationDate` → **à décider** (hors schéma) ; `creator` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `hasUse` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/PostgreSQL.json`
- **[[power]]** : `inferred:skos:narrower` → `inferred/power.json`
- **[[Powerpoint]]** : `inferred:skos:ancestor` → `inferred/Powerpoint.json`
- **[[Precision]]** : `inferred:skos:ancestor` → `inferred/Precision.json`
- **[[prediction]]** : `inferred:skos:narrower` → `inferred/prediction.json`
- **[[preferred stock]]** : `different from` → `skos:scopeNote` (« différent de … ») ; `main regulatory text` → **à décider** (hors schéma) ; `opposite of` → `kg:oppositeOf` ; `subclass of` → `iso-thes:broaderGeneric` ; `wikidata entity id: Q622588` → `skos:exactMatch: wd:Q622588` ; `inferred:skos:ancestor` → `inferred/preferred stock.json`
- **[[preferred term]]** : `wikidata entity id: Q115778090` → `skos:exactMatch: wd:Q115778090` ; `part of` → `iso-thes:broaderPartitive` ; `opposite of` → `kg:oppositeOf`
- **[[prepare for modeling]]** : `partOf` → `iso-thes:broaderPartitive` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/prepare for modeling.json`
- **[[preston curve]]** : `inferred:skos:ancestor` → `inferred/preston curve.json`
- **[[pretotyping]]** : `inferred:skos:ancestor` → `inferred/pretotyping.json`
- **[[pretraining]]** : `inferred:skos:narrower` → `inferred/pretraining.json`
- **[[price index]]** : `wikidata entity id: Q631360` → `skos:exactMatch: wd:Q631360` ; `subclass of` → `iso-thes:broaderGeneric` ; `broader` → `skos:broader` ; `has part(s)` → `has part` ; `inferred:skos:ancestor` → `inferred/price index.json`
- **[[primary commodity]]** : `subclass of` → `iso-thes:broaderGeneric` ; `does not have characteristic` → **à décider** (hors schéma) ; `instance of` → `iso-thes:broaderInstantial` ; `wikidata entity id: Q1550712` → `skos:exactMatch: wd:Q1550712` ; `inferred:skos:ancestor` → `inferred/primary commodity.json`
- **[[principal component analysis]]** : `inferred:skos:ancestor` → `inferred/principal component analysis.json`
- **[[privacy by design]]** : `inferred:skos:ancestor` → `inferred/privacy by design.json`
- **[[Probability]]** : `inferred:skos:related` → `inferred/Probability.json`
- **[[probability measure]]** : `inferred:skos:ancestor` → `inferred/probability measure.json` ; `inferred:skos:broader` → `inferred/probability measure.json`
- **[[problem]]** : `handled, mitigated, or managed by` → **à décider** (hors schéma) ; `subclass of` → `iso-thes:broaderGeneric` ; `studied by` → `cache/wikidata.jsonl` (fait sur le monde) ; `described by source` → `dcterms:isReferencedBy` ; `partially coincident with` → `cache/wikidata.jsonl` (fait sur le monde) ; `opposite of` → `kg:oppositeOf` ; `has characteristic` → `cache/wikidata.jsonl` (fait sur le monde) ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `pronunciation audio` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `wikidata entity id: Q621184` → `skos:exactMatch: wd:Q621184` ; `inferred:skos:ancestor` → `inferred/problem.json`
- **[[problem definition]]** : `inferred:skos:ancestor` → `inferred/problem definition.json`
- **[[problem framing]]** : `inferred:skos:ancestor` → `inferred/problem framing.json` ; `inferred:skos:broader` → `inferred/problem framing.json`
- **[[problem shaping]]** : `part of` → `iso-thes:broaderPartitive` ; `wikidata entity id: Q13604401` → `skos:exactMatch: wd:Q13604401`
- **[[problem solving]]** : `uses` → `kg:uses` ; `has cause` → `cache/wikidata.jsonl` (fait sur le monde) ; `subclass of` → `iso-thes:broaderGeneric` ; `has characteristic` → `cache/wikidata.jsonl` (fait sur le monde) ; `instance of` → `iso-thes:broaderInstantial` ; `has effect` → `cache/wikidata.jsonl` (fait sur le monde) ; `part of` → `iso-thes:broaderPartitive` ; `topic has template` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `main Wikidata property` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `Library of Congress Classification` → `dcterms:subject` ; `IMDb keyword` → `skos:closeMatch` ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `spoken text audio` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `UMLS CUI` → **à décider** (hors schéma) ; `MeSH tree code` → `dcterms:subject` ; `Dewey Decimal Classification` → `dcterms:subject` ; `wikidata entity id: Q730920` → `skos:exactMatch: wd:Q730920` ; `inferred:skos:ancestor` → `inferred/problem solving.json`
- **[[process]]** : `manifestation of` → `cache/wikidata.jsonl` (fait sur le monde) ; `different from` → `skos:scopeNote` (« différent de … ») ; `has effect` → `cache/wikidata.jsonl` (fait sur le monde) ; `facet of` → `skos:broader` ; `has characteristic` → `cache/wikidata.jsonl` (fait sur le monde) ; `has cause` → `cache/wikidata.jsonl` (fait sur le monde) ; `has part(s)` → `has part` ; `studied by` → `cache/wikidata.jsonl` (fait sur le monde) ; `part of` → `iso-thes:broaderPartitive` ; `said to be the same as` → `skos:closeMatch` ; `union of` → **à décider** (hors schéma) ; `subclass of` → `iso-thes:broaderGeneric` ; `instance of` → `iso-thes:broaderInstantial` ; `properties for this type` → **à décider** (hors schéma) ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `equivalent class` → `skos:closeMatch` ; `exact match` → `skos:exactMatch` ; `wikidata entity id: Q3249551` → `skos:exactMatch: wd:Q3249551` ; `inferred:skos:ancestor` → `inferred/process.json` ; `inferred:skos:narrower` → `inferred/process.json`
- **[[process owner]]** : `wikidata entity id: Q1418701` → `skos:exactMatch: wd:Q1418701` ; `subclass of` → `iso-thes:broaderGeneric` ; `accountable for` → `kg:accountableFor` ; `inferred:skos:ancestor` → `inferred/process owner.json`
- **[[process philosophy]]** : `inferred:skos:ancestor` → `inferred/process philosophy.json`
- **[[process-oriented programming]]** : `inferred:skos:ancestor` → `inferred/process-oriented programming.json` ; `inferred:skos:broader` → `inferred/process-oriented programming.json`
- **[[Product]]** : `inferred:skos:narrower` → `inferred/Product.json`
- **[[Product owner]]** : `inferred:skos:ancestor` → `inferred/Product owner.json`
- **[[product packaging]]** : `inferred:skos:narrower` → `inferred/product packaging.json`
- **[[Programming language]]** : `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/Programming language.json` ; `inferred:skos:narrower` → `inferred/Programming language.json`
- **[[programming paradigm]]** : `wikidata entity id: Q188267` → `skos:exactMatch: wd:Q188267` ; `inferred:skos:narrower` → `inferred/programming paradigm.json`
- **[[programming principle]]** : `wikidata entity id: Q39487140` → `skos:exactMatch: wd:Q39487140`
- **[[project description]]** : `inferred:skos:ancestor` → `inferred/project description.json`
- **[[project title]]** : `inferred:skos:ancestor` → `inferred/project title.json`
- **[[prompt engineering]]** : `wikidata entity id: Q108941486` → `skos:exactMatch: wd:Q108941486` ; `subclass of` → `iso-thes:broaderGeneric` ; `product or material produced` → `cache/wikidata.jsonl` (fait sur le monde) ; `facet of` → `skos:broader` ; `inferred:skos:related` → `inferred/prompt engineering.json`
- **[[Prompt Identity]]** : `related_to` → `skos:related` ; `dependencies` → `kg:dependsOn` ; `components` → `has part` ; `category` → `dcterms:subject` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Prompt Identity.json`
- **[[Prompt Optimization Techniques]]** : `related_to` → `skos:related` ; `dependencies` → `kg:dependsOn` ; `components` → `has part` ; `category` → `dcterms:subject` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Prompt Optimization Techniques.json` ; `inferred:skos:related` → `inferred/Prompt Optimization Techniques.json`
- **[[Prompt Template Info]]** : `related_to` → `skos:related` ; `dependencies` → `kg:dependsOn` ; `components` → `has part` ; `category` → `dcterms:subject` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Prompt Template Info.json` ; `inferred:skos:related` → `inferred/Prompt Template Info.json`
- **[[Prompt Template Types]]** : `related_to` → `skos:related` ; `dependencies` → `kg:dependsOn` ; `components` → `has part` ; `category` → `dcterms:subject` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Prompt Template Types.json` ; `inferred:skos:related` → `inferred/Prompt Template Types.json`
- **[[prompt templates]]** : `connectsFrom` → **à décider** (hors schéma) ; `connectsTo` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/prompt templates.json` ; `inferred:skos:related` → `inferred/prompt templates.json`
- **[[prompt-based techniques]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/prompt-based techniques.json`
- **[[prompts]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/prompts.json`
- **[[properties]]** : `inferred:skos:ancestor` → `inferred/properties.json`
- **[[property]]** : `facet of` → `skos:broader` ; `instance of` → `iso-thes:broaderInstantial` ; `said to be the same as` → `skos:closeMatch` ; `partially coincident with` → `cache/wikidata.jsonl` (fait sur le monde) ; `subclass of` → `iso-thes:broaderGeneric` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/property.json`
- **[[property graph model]]** : `inferred:skos:ancestor` → `inferred/property graph model.json` ; `inferred:skos:broader` → `inferred/property graph model.json`
- **[[protected health information (PHI)]]** : `inferred:skos:ancestor` → `inferred/protected health information (PHI).json`
- **[[prototyping]]** : `inferred:skos:narrower` → `inferred/prototyping.json`
- **[[Provenance]]** : `wikidata entity id: Q1773840` → `skos:exactMatch: wd:Q1773840` ; `subclass of` → `iso-thes:broaderGeneric` ; `partially coincident with` → `cache/wikidata.jsonl` (fait sur le monde) ; `facet of` → `skos:broader` ; `exact match` → `skos:exactMatch` ; `inferred:skos:ancestor` → `inferred/Provenance.json` ; `inferred:skos:broader` → `inferred/Provenance.json` ; `inferred:skos:narrower` → `inferred/Provenance.json`
- **[[pruning]]** : `inferred:skos:ancestor` → `inferred/pruning.json` ; `inferred:skos:broader` → `inferred/pruning.json`
- **[[psychological terminology]]** : `used by` → `kg:usedBy` ; `subclass of` → `iso-thes:broaderGeneric` ; `partially coincident with` → `cache/wikidata.jsonl` (fait sur le monde) ; `instance of` → `iso-thes:broaderInstantial` ; `facet of` → `skos:broader` ; `wikidata entity id: Q77468620` → `skos:exactMatch: wd:Q77468620` ; `inferred:skos:ancestor` → `inferred/psychological terminology.json`
- **[[Pull request]]** : `inferred:skos:narrower` → `inferred/Pull request.json`
- **[[pull request approval]]** : `rdf:type: Concept` → `dcterms:type: Concept` ; `broader` → `skos:broader` ; `description` → `skos:definition` ; `timestamp` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `inferred:skos:ancestor` → `inferred/pull request approval.json`
- **[[push_to_comet]]** : `entity` → **à décider** (hors schéma) ; `MethodInside` → **à décider** (hors schéma)
- **[[pydantic]]** : `usedBy` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/pydantic.json`
- **[[pypi]]** : `maintained by` → **à décider** (hors schéma) ; `instance of` → `iso-thes:broaderInstantial` ; `different from` → `skos:scopeNote` (« différent de … ») ; `software engine` → **à décider** (hors schéma) ; `official website` → **à décider** (hors schéma) ; `logo image` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `wikidata entity id: Q2984686` → `skos:exactMatch: wd:Q2984686` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/pypi.json`
- **[[Python]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Python.json` ; `inferred:skos:broader` → `inferred/Python.json` ; `inferred:skos:narrower` → `inferred/Python.json`
- **[[PyTorch]]** : `instance of` → `iso-thes:broaderInstantial` ; `usedFor` → **à décider** (hors schéma) ; `alternativeTo` → **à décider** (hors schéma) ; `operatesOn` → **à décider** (hors schéma) ; `supports` → **à décider** (hors schéma) ; `integratesWith` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/PyTorch.json`
- **[[Qdrant]]** : `inferred:skos:ancestor` → `inferred/Qdrant.json`
- **[[quality management]]** : `wikidata entity id: Q757012` → `skos:exactMatch: wd:Q757012` ; `inferred:skos:narrower` → `inferred/quality management.json`
- **[[Quantile binning]]** : `rdf:type: skos:Concept` → `dcterms:type: Concept` ; `inferred:skos:ancestor` → `inferred/Quantile binning.json`
- **[[Quantization]]** : `inferred:skos:narrower` → `inferred/Quantization.json`
- **[[query]]** : `inferred:skos:ancestor` → `inferred/query.json`
- **[[Query engine]]** : `builtOnTopOf` → **à décider** (hors schéma)
- **[[quorum]]** : `described by source` → `dcterms:isReferencedBy` ; `different from` → `skos:scopeNote` (« différent de … ») ; `subclass of` → `iso-thes:broaderGeneric` ; `wikidata entity id: Q526999` → `skos:exactMatch: wd:Q526999`
- **[[r2]]** : `inferred:skos:ancestor` → `inferred/r2.json`
- **[[Radial Basis Function Kernel]]** : `inferred:skos:ancestor` → `inferred/Radial Basis Function Kernel.json`
- **[[RAG (Retrieval-Augmented Generation)]]** : `wikidata entity id: Q121362277` → `skos:exactMatch: wd:Q121362277` ; `subclass of` → `iso-thes:broaderGeneric` ; `facet of` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/RAG (Retrieval-Augmented Generation).json` ; `inferred:skos:narrower` → `inferred/RAG (Retrieval-Augmented Generation).json`
- **[[Random forest]]** : `inferred:skos:narrower` → `inferred/Random forest.json`
- **[[raw data]]** : `inferred:skos:ancestor` → `inferred/raw data.json`
- **[[reach]]** : `inferred:skos:ancestor` → `inferred/reach.json`
- **[[ReAct data agent]]** : `specificInstanceOf` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/ReAct data agent.json`
- **[[ReAct mode]]** : `inferred:skos:ancestor` → `inferred/ReAct mode.json`
- **[[Readme file]]** : `inferred:skos:ancestor` → `inferred/Readme file.json`
- **[[reasoning]]** : `wikidata entity id: Q1156402` → `skos:exactMatch: wd:Q1156402`
- **[[Recall]]** : `inferred:skos:ancestor` → `inferred/Recall.json`
- **[[recall bias]]** : `inferred:skos:ancestor` → `inferred/recall bias.json`
- **[[Receiver Operating Characteristic curve]]** : `inferred:skos:ancestor` → `inferred/Receiver Operating Characteristic curve.json`
- **[[receiver operating characteristics]]** : `instance of` → `iso-thes:broaderInstantial` ; `subclass of` → `iso-thes:broaderGeneric` ; `has use` → `kg:hasUse` ; `image` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `MeSH tree code` → `dcterms:subject` ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `wikidata entity id: Q327120` → `skos:exactMatch: wd:Q327120` ; `inferred:skos:ancestor` → `inferred/receiver operating characteristics.json`
- **[[record linkage]]** : `wikidata entity id: Q1266546` → `skos:exactMatch: wd:Q1266546` ; `subclass of` → `iso-thes:broaderGeneric` ; `uses` → `kg:uses` ; `facet of` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/record linkage.json` ; `inferred:skos:related` → `inferred/record linkage.json`
- **[[recursive tree building]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/recursive tree building.json`
- **[[Redis]]** : `publication date` → `cache/wikidata.jsonl` (fait sur le monde) ; `instance of` → `iso-thes:broaderInstantial` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Redis.json`
- **[[regression]]** : `inferred:skos:narrower` → `inferred/regression.json`
- **[[Regression Error Metrics]]** : `inferred:skos:narrower` → `inferred/Regression Error Metrics.json`
- **[[Regression trees]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Regression trees.json`
- **[[Regularity]]** : `subFieldOf` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/Regularity.json`
- **[[Regularization]]** : `foundationalPaper` → `dcterms:isReferencedBy` ; `keyPapers` → `dcterms:isReferencedBy` ; `prevents` → **à décider** (hors schéma) ; `reduces` → **à décider** (hors schéma) ; `skos:narrower` → retiré ; chaque cible reçoit `skos:broader: [[Regularization]]` ; `usedIn` → `kg:usedBy` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Regularization.json`
- **[[Reinforcement Learning]]** : `foundationalPaper` → `dcterms:isReferencedBy` ; `keyPapers` → `dcterms:isReferencedBy` ; `instance of` → `iso-thes:broaderInstantial` ; `inspiredBy` → **à décider** (hors schéma) ; `keyComponents` → **à décider** (hors schéma) ; `algorithms` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Reinforcement Learning.json`
- **[[Relationship aggregation]]** : `inferred:skos:ancestor` → `inferred/Relationship aggregation.json`
- **[[relationship quality]]** : `inferred:skos:ancestor` → `inferred/relationship quality.json`
- **[[ReLU activation function]]** : `foundationalPaper` → `dcterms:isReferencedBy` ; `keyPapers` → `dcterms:isReferencedBy` ; `instance of` → `iso-thes:broaderInstantial` ; `advantages` → **à décider** (hors schéma) ; `variants` → **à décider** (hors schéma) ; `usedIn` → `kg:usedBy` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/ReLU activation function.json`
- **[[repository]]** : `inferred:skos:ancestor` → `inferred/repository.json`
- **[[reproducibility]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/reproducibility.json`
- **[[required status check]]** : `rdf:type: Concept` → `dcterms:type: Concept` ; `broader` → `skos:broader` ; `partOf` → `iso-thes:broaderPartitive` ; `description` → `skos:definition` ; `timestamp` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `inferred:skos:ancestor` → `inferred/required status check.json`
- **[[requirements elicitation]]** : `wikidata entity id: Q838667` → `skos:exactMatch: wd:Q838667` ; `part of` → `iso-thes:broaderPartitive` ; `OmegaWiki Defined Meaning` → `skos:closeMatch`
- **[[requirements engineering]]** : `part of` → `iso-thes:broaderPartitive` ; `subclass of` → `iso-thes:broaderGeneric` ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `wikidata entity id: Q376937` → `skos:exactMatch: wd:Q376937` ; `inferred:skos:ancestor` → `inferred/requirements engineering.json`
- **[[Residual analysis]]** : `inferred:skos:ancestor` → `inferred/Residual analysis.json`
- **[[responsibility assignment matrix]]** : `wikidata entity id: Q1850420` → `skos:exactMatch: wd:Q1850420` ; `instance of` → `iso-thes:broaderInstantial` ; `field of work` → `cache/wikidata.jsonl` (fait sur le monde)
- **[[retraining]]** : `inferred:skos:ancestor` → `inferred/retraining.json`
- **[[retrieval augmented generation]]** : `inferred:skos:ancestor` → `inferred/retrieval augmented generation.json`
- **[[retrieval depth]]** : `inferred:skos:ancestor` → `inferred/retrieval depth.json`
- **[[retriever]]** : `inferred:skos:ancestor` → `inferred/retriever.json`
- **[[retriever orchestration]]** : `inferred:skos:ancestor` → `inferred/retriever orchestration.json`
- **[[rider]]** : `inferred:skos:ancestor` → `inferred/rider.json`
- **[[rights of individuals]]** : `inferred:skos:ancestor` → `inferred/rights of individuals.json`
- **[[risk]]** : `inferred:skos:narrower` → `inferred/risk.json`
- **[[risk management]]** : `wikidata entity id: Q189447` → `skos:exactMatch: wd:Q189447` ; `instance of` → `iso-thes:broaderInstantial` ; `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/risk management.json`
- **[[rollback]]** : `inferred:skos:ancestor` → `inferred/rollback.json`
- **[[rollback capability]]** : `inferred:skos:ancestor` → `inferred/rollback capability.json`
- **[[rule]]** : `wikidata entity id: Q1151067` → `skos:exactMatch: wd:Q1151067` ; `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/rule.json` ; `inferred:skos:narrower` → `inferred/rule.json`
- **[[rules]]** : `rdf:type: Research Note` → `dcterms:type: Concept` (à confirmer : note de recherche) ; `title` → `skos:prefLabel` ; `description` → `skos:definition` ; `timestamp` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `instanceOf` → `iso-thes:broaderInstantial`
- **[[scenario]]** : `inferred:skos:ancestor` → `inferred/scenario.json`
- **[[scenario (computing)]]** : `inferred:skos:ancestor` → `inferred/scenario (computing).json`
- **[[scheduled retraining]]** : `inferred:skos:ancestor` → `inferred/scheduled retraining.json`
- **[[schema design]]** : `inferred:skos:narrower` → `inferred/schema design.json`
- **[[schema-field consumption statistics]]** : `inferred:skos:ancestor` → `inferred/schema-field consumption statistics.json`
- **[[sci-kit Learn]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/sci-kit Learn.json`
- **[[scientific terminology]]** : `has part(s)` → `has part` ; `subclass of` → `iso-thes:broaderGeneric` ; `part of` → `iso-thes:broaderPartitive` ; `instance of` → `iso-thes:broaderInstantial` ; `used by` → `kg:usedBy` ; `wikidata entity id: Q12132640` → `skos:exactMatch: wd:Q12132640` ; `inferred:skos:narrower` → `inferred/scientific terminology.json`
- **[[search]]** : `inferred:skos:narrower` → `inferred/search.json`
- **[[search module]]** : `inferred:skos:ancestor` → `inferred/search module.json`
- **[[SECI model of knowledge dimensions]]** : `wikidata entity id: Q1241796` → `skos:exactMatch: wd:Q1241796` ; `instance of` → `iso-thes:broaderInstantial` ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV)
- **[[selection]]** : `inferred:skos:narrower` → `inferred/selection.json`
- **[[self-supervision]]** : `inferred:skos:ancestor` → `inferred/self-supervision.json`
- **[[semantics]]** : `is the study of` → `cache/wikidata.jsonl` (fait sur le monde) ; `described by source` → `dcterms:isReferencedBy` ; `instance of` → `iso-thes:broaderInstantial` ; `topic has template` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `practiced by` → `cache/wikidata.jsonl` (fait sur le monde) ; `subclass of` → `iso-thes:broaderGeneric` ; `part of` → `iso-thes:broaderPartitive` ; `OmegaWiki Defined Meaning` → `skos:closeMatch` ; `Dewey Decimal Classification` → `dcterms:subject` ; `PhilPapers topic` → **à décider** (hors schéma) ; `image` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `Stack Exchange tag` → `skos:closeMatch` ; `Krugosvet article (archived)` → `skos:closeMatch` ; `MeSH tree code` → `dcterms:subject` ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `wikidata entity id: Q39645` → `skos:exactMatch: wd:Q39645` ; `inferred:skos:narrower` → `inferred/semantics.json`
- **[[semi-structured data]]** : `inferred:skos:ancestor` → `inferred/semi-structured data.json`
- **[[semi-structured interview]]** : `wikidata entity id: Q1477475` → `skos:exactMatch: wd:Q1477475` ; `subclass of` → `iso-thes:broaderGeneric`
- **[[semiotics]]** : `wikidata entity id: Q60195` → `skos:exactMatch: wd:Q60195` ; `is the study of` → `cache/wikidata.jsonl` (fait sur le monde) ; `different from` → `skos:scopeNote` (« différent de … ») ; `instance of` → `iso-thes:broaderInstantial` ; `described by source` → `dcterms:isReferencedBy` ; `topic has template` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `practiced by` → `cache/wikidata.jsonl` (fait sur le monde) ; `Wikimedia outline` → **à décider** (hors schéma) ; `subclass of` → `iso-thes:broaderGeneric` ; `partially coincident with` → `cache/wikidata.jsonl` (fait sur le monde) ; `OmegaWiki Defined Meaning` → `skos:closeMatch` ; `Dewey Decimal Classification` → `dcterms:subject` ; `image` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `Wikimedia import URL` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `Provenio UUID` → **à décider** (hors schéma) ; `Krugosvet article (archived)` → `skos:closeMatch` ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `inferred:skos:narrower` → `inferred/semiotics.json`
- **[[Sensitive Information]]** : `inferred:skos:ancestor` → `inferred/Sensitive Information.json`
- **[[sentence embedding]]** : `wikidata entity id: Q29043221` → `skos:exactMatch: wd:Q29043221` ; `subclass of` → `iso-thes:broaderGeneric` ; `uses` → `kg:uses` ; `inferred:skos:ancestor` → `inferred/sentence embedding.json` ; `inferred:skos:broader` → `inferred/sentence embedding.json`
- **[[sentiment analysis]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/sentiment analysis.json`
- **[[separation of concerns]]** : `wikidata entity id: Q2465506` → `skos:exactMatch: wd:Q2465506` ; `instance of` → `iso-thes:broaderInstantial` ; `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/separation of concerns.json`
- **[[separators-and-dates]]** : `inferred:skos:ancestor` → `inferred/separators-and-dates.json`
- **[[Service-oriented architecture (SOA)]]** : `inferred:skos:ancestor` → `inferred/Service-oriented architecture (SOA).json`
- **[[Session]]** : `inferred:skos:ancestor` → `inferred/Session.json`
- **[[settings.json]]** : `inferred:skos:ancestor` → `inferred/settings.json.json`
- **[[Shadow releasing]]** : `inferred:skos:ancestor` → `inferred/Shadow releasing.json`
- **[[Shapley Additive Explanations (SHAP)]]** : `inferred:skos:ancestor` → `inferred/Shapley Additive Explanations (SHAP).json`
- **[[share]]** : `described by source` → `dcterms:isReferencedBy` ; `subclass of` → `iso-thes:broaderGeneric` ; `wikidata entity id: Q11692` → `skos:exactMatch: wd:Q11692` ; `inferred:skos:narrower` → `inferred/share.json`
- **[[share capital]]** : `described by source` → `dcterms:isReferencedBy` ; `different from` → `skos:scopeNote` (« différent de … ») ; `has part(s)` → `has part` ; `instance of` → `iso-thes:broaderInstantial` ; `part of` → `iso-thes:broaderPartitive` ; `subclass of` → `iso-thes:broaderGeneric` ; `wikidata entity id: Q330601` → `skos:exactMatch: wd:Q330601`
- **[[share purchase agreement]]** : `literal translation` → **à décider** (hors schéma)
- **[[Share transfer clauses]]** : `inferred:skos:ancestor` → `inferred/Share transfer clauses.json`
- **[[Shared computing resources]]** : `inferred:skos:ancestor` → `inferred/Shared computing resources.json`
- **[[shareholder]]** : `different from` → `skos:scopeNote` (« différent de … ») ; `has characteristic` → `cache/wikidata.jsonl` (fait sur le monde) ; `has goal` → **à décider** (hors schéma) ; `instance of` → `iso-thes:broaderInstantial` ; `owner of` → **à décider** (hors schéma) ; `partially coincident with` → `cache/wikidata.jsonl` (fait sur le monde) ; `subclass of` → `iso-thes:broaderGeneric` ; `wikidata entity id: Q381136` → `skos:exactMatch: wd:Q381136` ; `inferred:skos:narrower` → `inferred/shareholder.json`
- **[[Shareholders agreement]]** : `inferred:skos:narrower` → `inferred/Shareholders agreement.json` ; `wikidata entity id: Q3360276` → `skos:exactMatch: wd:Q3360276`
- **[[sheets-api]]** : `inferred:skos:ancestor` → `inferred/sheets-api.json`
- **[[Shifter]]** : `Changes` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Shifter.json`
- **[[Sigmoid function]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Sigmoid function.json`
- **[[Signavio]]** : `wikidata entity id: Q7512866` → `skos:exactMatch: wd:Q7512866` ; `instance of` → `iso-thes:broaderInstantial`
- **[[similarity measure]]** : `inferred:skos:narrower` → `inferred/similarity measure.json`
- **[[Similarity scores]]** : `inferred:skos:ancestor` → `inferred/Similarity scores.json`
- **[[simplicity VS. flexibility]]** : `inferred:skos:ancestor` → `inferred/simplicity VS. flexibility.json`
- **[[single source of truth]]** : `wikidata entity id: Q7523885` → `skos:exactMatch: wd:Q7523885` ; `instance of` → `iso-thes:broaderInstantial` ; `facet of` → `skos:broader` ; `subclass of` → `iso-thes:broaderGeneric` ; `uses` → `kg:uses` ; `inferred:skos:ancestor` → `inferred/single source of truth.json`
- **[[situation]]** : `inferred:skos:narrower` → `inferred/situation.json`
- **[[skills]]** : `partOf` → `iso-thes:broaderPartitive`
- **[[slide deck]]** : `inferred:skos:narrower` → `inferred/slide deck.json`
- **[[slide show]]** : `inferred:skos:ancestor` → `inferred/slide show.json` ; `inferred:skos:broader` → `inferred/slide show.json`
- **[[Smoothing]]** : `inferred:skos:ancestor` → `inferred/Smoothing.json`
- **[[social network analysis]]** : `inferred:skos:ancestor` → `inferred/social network analysis.json`
- **[[société anonyme]]** : `applies to jurisdiction` → **à décider** (hors schéma) ; `instance of` → `iso-thes:broaderInstantial` ; `subclass of` → `iso-thes:broaderGeneric` ; `wikidata entity id: Q18195767` → `skos:exactMatch: wd:Q18195767`
- **[[société par actions simplifiée]]** : `applies to jurisdiction` → **à décider** (hors schéma) ; `different from` → `skos:scopeNote` (« différent de … ») ; `instance of` → `iso-thes:broaderInstantial` ; `part of` → `iso-thes:broaderPartitive` ; `subclass of` → `iso-thes:broaderGeneric` ; `wikidata entity id: Q112176862` → `skos:exactMatch: wd:Q112176862`
- **[[Socrates]]** : `inferred:skos:ancestor` → `inferred/Socrates.json`
- **[[Socratic]]** : `inferred:skos:narrower` → `inferred/Socratic.json`
- **[[software agent]]** : `wikidata entity id: Q2297769` → `skos:exactMatch: wd:Q2297769` ; `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/software agent.json`
- **[[software development kit (SDK)]]** : `inferred:skos:ancestor` → `inferred/software development kit (SDK).json`
- **[[software engineer]]** : `inferred:skos:ancestor` → `inferred/software engineer.json`
- **[[software observability]]** : `wikidata entity id: Q115800581` → `skos:exactMatch: wd:Q115800581`
- **[[source of information]]** : `wikidata entity id: Q3523102` → `skos:exactMatch: wd:Q3523102` ; `inferred:skos:narrower` → `inferred/source of information.json`
- **[[SpaCy]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/SpaCy.json`
- **[[sparkline]]** : `discoverer or inventor` → `cache/wikidata.jsonl` (fait sur le monde) ; `subclass of` → `iso-thes:broaderGeneric` ; `maintained by WikiProject` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `Stack Exchange tag` → `skos:closeMatch` ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `wikidata entity id: Q2307841` → `skos:exactMatch: wd:Q2307841` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/sparkline.json`
- **[[spatial reference system identifier (SRID)]]** : `inferred:skos:narrower` → `inferred/spatial reference system identifier (SRID).json`
- **[[speckit]]** : `inferred:skos:ancestor` → `inferred/speckit.json`
- **[[split data]]** : `inferred:skos:narrower` → `inferred/split data.json`
- **[[spotify story]]** : `inferred:skos:ancestor` → `inferred/spotify story.json`
- **[[spreadsheet]]** : `subclass of` → `iso-thes:broaderGeneric` ; `instance of` → `iso-thes:broaderInstantial` ; `has part(s) of the class` → `cache/wikidata.jsonl` (fait sur le monde) ; `topic has template` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `product or material produced` → `cache/wikidata.jsonl` (fait sur le monde) ; `has part(s)` → `has part` ; `uses` → `kg:uses` ; `Nomenclature for Museum Cataloging` → **à décider** (hors schéma) ; `GitHub topic` → `skos:closeMatch` ; `OmegaWiki Defined Meaning` → `skos:closeMatch` ; `image` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `wikidata entity id: Q183197` → `skos:exactMatch: wd:Q183197` ; `inferred:skos:narrower` → `inferred/spreadsheet.json`
- **[[sprint planning]]** : `inferred:skos:ancestor` → `inferred/sprint planning.json`
- **[[SSH Agent]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/SSH Agent.json`
- **[[SSH Key]]** : `inferred:skos:ancestor` → `inferred/SSH Key.json`
- **[[stability]]** : `inferred:skos:ancestor` → `inferred/stability.json`
- **[[staging area]]** : `inferred:skos:ancestor` → `inferred/staging area.json`
- **[[standard operating procedure]]** : `wikidata entity id: Q702761` → `skos:exactMatch: wd:Q702761` ; `subclass of` → `iso-thes:broaderGeneric` ; `main subject` → `dcterms:subject` ; `facet of` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/standard operating procedure.json`
- **[[standford's design thinking process]]** : `inferred:skos:ancestor` → `inferred/standford's design thinking process.json`
- **[[stash]]** : `inferred:skos:ancestor` → `inferred/stash.json`
- **[[state observer]]** : `inferred:skos:ancestor` → `inferred/state observer.json`
- **[[state-of-the-art]]** : `rdf:type: Research Note` → `dcterms:type: Concept` (à confirmer : note de recherche) ; `title` → `skos:prefLabel` ; `description` → `skos:definition` ; `timestamp` → supprimé (maintenance/média Wikidata ou dérivé de PROV)
- **[[Stateful]]** : `inferred:skos:narrower` → `inferred/Stateful.json`
- **[[Statefulness]]** : `inferred:skos:ancestor` → `inferred/Statefulness.json`
- **[[stateless]]** : `inferred:skos:narrower` → `inferred/stateless.json`
- **[[stateless protocol]]** : `subclass of` → `iso-thes:broaderGeneric` ; `opposite of` → `kg:oppositeOf` ; `has characteristic` → `cache/wikidata.jsonl` (fait sur le monde) ; `wikidata entity id: Q230924` → `skos:exactMatch: wd:Q230924` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/stateless protocol.json`
- **[[statistical graphics]]** : `inferred:skos:narrower` → `inferred/statistical graphics.json`
- **[[statutory auditor]]** : `described by source` → `dcterms:isReferencedBy` ; `different from` → `skos:scopeNote` (« différent de … ») ; `field of this occupation` → **à décider** (hors schéma) ; `instance of` → `iso-thes:broaderInstantial` ; `subclass of` → `iso-thes:broaderGeneric` ; `wikidata entity id: Q1051798` → `skos:exactMatch: wd:Q1051798`
- **[[stochastic processes]]** : `inferred:skos:narrower` → `inferred/stochastic processes.json`
- **[[stretch pants approach]]** : `inferred:skos:ancestor` → `inferred/stretch pants approach.json`
- **[[structured data]]** : `inferred:skos:ancestor` → `inferred/structured data.json`
- **[[structured-references]]** : `inferred:skos:ancestor` → `inferred/structured-references.json`
- **[[study of complex systems]]** : `inferred:skos:ancestor` → `inferred/study of complex systems.json`
- **[[subagent]]** : `inferred:skos:ancestor` → `inferred/subagent.json`
- **[[subdomain]]** : `inferred:skos:ancestor` → `inferred/subdomain.json`
- **[[subject heading]]** : `inferred:skos:ancestor` → `inferred/subject heading.json`
- **[[subject-matter expert]]** : `wikidata entity id: Q4833645` → `skos:exactMatch: wd:Q4833645` ; `instance of` → `iso-thes:broaderInstantial`
- **[[subtext]]** : `inferred:skos:ancestor` → `inferred/subtext.json`
- **[[sum of squared error (SSE)]]** : `inferred:skos:ancestor` → `inferred/sum of squared error (SSE).json`
- **[[supervised finetuning]]** : `inferred:skos:ancestor` → `inferred/supervised finetuning.json`
- **[[supervised learning]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/supervised learning.json` ; `inferred:skos:narrower` → `inferred/supervised learning.json`
- **[[support vector]]** : `inferred:skos:ancestor` → `inferred/support vector.json`
- **[[Support Vector Machine]]** : `foundationalPaper` → `dcterms:isReferencedBy` ; `keyPapers` → `dcterms:isReferencedBy` ; `subclass of` → `iso-thes:broaderGeneric` ; `usedFor` → **à décider** (hors schéma) ; `relatedTo` → `skos:related` ; `inspiredBy` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Support Vector Machine.json`
- **[[swagger]]** : `inferred:skos:ancestor` → `inferred/swagger.json`
- **[[symbolism]]** : `inferred:skos:ancestor` → `inferred/symbolism.json`
- **[[system prompt]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/system prompt.json`
- **[[systematisation]]** : `wikidata entity id: Q56312904` → `skos:exactMatch: wd:Q56312904` ; `instance of` → `iso-thes:broaderInstantial` ; `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/systematisation.json`
- **[[systems engineering]]** : `inferred:skos:narrower` → `inferred/systems engineering.json`
- **[[systems theory]]** : `inferred:skos:narrower` → `inferred/systems theory.json`
- **[[table cell]]** : `inferred:skos:narrower` → `inferred/table cell.json`
- **[[TabPFN]]** : `inferred:skos:ancestor` → `inferred/TabPFN.json`
- **[[tabular data]]** : `inferred:skos:related` → `inferred/tabular data.json`
- **[[tabular foundation model]]** : `inferred:skos:narrower` → `inferred/tabular foundation model.json`
- **[[tacit knowledge]]** : `wikidata entity id: Q743861` → `skos:exactMatch: wd:Q743861` ; `subclass of` → `iso-thes:broaderGeneric` ; `instance of` → `iso-thes:broaderInstantial` ; `opposite of` → `kg:oppositeOf` ; `discoverer or inventor` → `cache/wikidata.jsonl` (fait sur le monde) ; `inferred:skos:ancestor` → `inferred/tacit knowledge.json` ; `inferred:skos:related` → `inferred/tacit knowledge.json`
- **[[tag-along right]]** : `instance of` → `iso-thes:broaderInstantial` ; `part of` → `iso-thes:broaderPartitive` ; `wikidata entity id: Q7675074` → `skos:exactMatch: wd:Q7675074`
- **[[Target]]** : `inferred:skos:related` → `inferred/Target.json`
- **[[Target's pregnancy prediction]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Target's pregnancy prediction.json`
- **[[Task analysis]]** : `inferred:skos:ancestor` → `inferred/Task analysis.json`
- **[[Task flow diagram]]** : `inferred:skos:ancestor` → `inferred/Task flow diagram.json`
- **[[tautology]]** : `subclass of` → `iso-thes:broaderGeneric` ; `opposite of` → `kg:oppositeOf` ; `different from` → `skos:scopeNote` (« différent de … ») ; `notation` → **à décider** (hors schéma) ; `maintained by WikiProject` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `discoverer or inventor` → `cache/wikidata.jsonl` (fait sur le monde) ; `wikidata entity id: Q209555` → `skos:exactMatch: wd:Q209555`
- **[[taxonomy]]** : `inferred:skos:narrower` → `inferred/taxonomy.json`
- **[[Technological privacy]]** : `inferred:skos:ancestor` → `inferred/Technological privacy.json`
- **[[Technology-list]]** : `inferred:skos:ancestor` → `inferred/Technology-list.json`
- **[[templates]]** : `inferred:skos:ancestor` → `inferred/templates.json` ; `inferred:skos:broader` → `inferred/templates.json`
- **[[Tensors]]** : `inferred:skos:ancestor` → `inferred/Tensors.json`
- **[[term sheet]]** : `inferred:skos:ancestor` → `inferred/term sheet.json` ; `wikidata entity id: Q2404777` → `skos:exactMatch: wd:Q2404777`
- **[[Terminal]]** : `inferred:skos:narrower` → `inferred/Terminal.json`
- **[[Test]]** : `inferred:skos:narrower` → `inferred/Test.json`
- **[[Test data set]]** : `inferred:skos:ancestor` → `inferred/Test data set.json`
- **[[Test solution]]** : `inferred:skos:ancestor` → `inferred/Test solution.json`
- **[[testability]]** : `partially coincident with` → `cache/wikidata.jsonl` (fait sur le monde) ; `instance of` → `iso-thes:broaderInstantial` ; `wikidata entity id: Q2149495` → `skos:exactMatch: wd:Q2149495`
- **[[Text2Cypher]]** : `inferred:skos:ancestor` → `inferred/Text2Cypher.json`
- **[[The Book of Why]]** : `author` → **à décider** (hors schéma) ; `main subject` → `dcterms:subject` ; `instance of` → `iso-thes:broaderInstantial` ; `title` → `skos:prefLabel` ; `publication date` → `cache/wikidata.jsonl` (fait sur le monde) ; `wikidata entity id: Q98199430` → `skos:exactMatch: wd:Q98199430`
- **[[The Shift from Models to Compound AI Systems]]** : `inferred:skos:ancestor` → `inferred/The Shift from Models to Compound AI Systems.json`
- **[[theme color]]** : `inferred:skos:ancestor` → `inferred/theme color.json`
- **[[thesaurus]]** : `part of` → `iso-thes:broaderPartitive` ; `has part(s)` → `has part` ; `partially coincident with` → `cache/wikidata.jsonl` (fait sur le monde) ; `different from` → `skos:scopeNote` (« différent de … ») ; `model item` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `has use` → `kg:hasUse` ; `studied by` → `cache/wikidata.jsonl` (fait sur le monde) ; `subclass of` → `iso-thes:broaderGeneric` ; `has goal` → **à décider** (hors schéma) ; `described by source` → `dcterms:isReferencedBy` ; `described at URL` → **à décider** (hors schéma) ; `Dewey Decimal Classification` → `dcterms:subject` ; `name` → **à décider** (hors schéma) ; `wikidata entity id: Q17152639` → `skos:exactMatch: wd:Q17152639` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/thesaurus.json`
- **[[Threshold value]]** : `inferred:skos:narrower` → `inferred/Threshold value.json`
- **[[Théorie du cerveau bayésien]]** : `builtOnTopOf` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Théorie du cerveau bayésien.json`
- **[[Tidy Data]]** : `HeuristicFor` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Tidy Data.json`
- **[[Time-shifted scoring]]** : `rdf:type: skos:Concept` → `dcterms:type: Concept` ; `inferred:skos:ancestor` → `inferred/Time-shifted scoring.json`
- **[[token]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/token.json`
- **[[Tokenizer]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Tokenizer.json`
- **[[Tool arena]]** : `inferred:skos:ancestor` → `inferred/Tool arena.json`
- **[[Tool Assignment Gate]]** : `inferred:skos:ancestor` → `inferred/Tool Assignment Gate.json`
- **[[Toolkits]]** : `related_to` → `skos:related` ; `dependencies` → `kg:dependsOn` ; `components` → `has part` ; `category` → `dcterms:subject` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Toolkits.json` ; `inferred:skos:related` → `inferred/Toolkits.json`
- **[[tools]]** : `inferred:skos:related` → `inferred/tools.json`
- **[[Tooth]]** : `InterlockWith` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Tooth.json`
- **[[Traceable Artifacts]]** : `inferred:skos:ancestor` → `inferred/Traceable Artifacts.json`
- **[[tracing]]** : `wikidata entity id: Q322229` → `skos:exactMatch: wd:Q322229` ; `subclass of` → `iso-thes:broaderGeneric` ; `facet of` → `skos:broader` ; `inferred:skos:related` → `inferred/tracing.json`
- **[[trade-off]]** : `subclass of` → `iso-thes:broaderGeneric` ; `facet of` → `skos:broader` ; `wikidata entity id: Q638123` → `skos:exactMatch: wd:Q638123`
- **[[Train loss]]** : `inferred:skos:ancestor` → `inferred/Train loss.json`
- **[[trainer]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/trainer.json`
- **[[training]]** : `wikidata entity id: Q918385` → `skos:exactMatch: wd:Q918385` ; `instance of` → `iso-thes:broaderInstantial` ; `subclass of` → `iso-thes:broaderGeneric` ; `part of` → `iso-thes:broaderPartitive` ; `practiced by` → `cache/wikidata.jsonl` (fait sur le monde) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/training.json`
- **[[Training algorithm]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Training algorithm.json`
- **[[training data set]]** : `ComplementaryWith` → **à décider** (hors schéma) ; `subclass of` → `iso-thes:broaderGeneric` ; `usedIn` → `kg:usedBy` ; `inferred:skos:ancestor` → `inferred/training data set.json`
- **[[Training pipeline]]** : `inferred:skos:ancestor` → `inferred/Training pipeline.json` ; `inferred:skos:broader` → `inferred/Training pipeline.json`
- **[[TrainingAguments]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/TrainingAguments.json`
- **[[Transfer learning]]** : `foundationalPaper` → `dcterms:isReferencedBy` ; `keyPapers` → `dcterms:isReferencedBy` ; `implements` → **à décider** (hors schéma) ; `usedIn` → `kg:usedBy` ; `benefitFrom` → **à décider** (hors schéma) ; `reducesNeedFor` → **à décider** (hors schéma) ; `accelerates` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Transfer learning.json`
- **[[Transformers]]** : `introducedin` → **à décider** (hors schéma) ; `enablesArchitecture` → **à décider** (hors schéma) ; `uses` → `kg:uses` ; `processes` → **à décider** (hors schéma) ; `foundationFor` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Transformers.json` ; `inferred:skos:narrower` → `inferred/Transformers.json`
- **[[Transparency]]** : `inferred:skos:related` → `inferred/Transparency.json`
- **[[tree depth]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/tree depth.json`
- **[[triage]]** : `inferred:skos:ancestor` → `inferred/triage.json`
- **[[trigger]]** : `partOf` → `iso-thes:broaderPartitive` ; `inferred:skos:related` → `inferred/trigger.json`
- **[[True Negative (TN)]]** : `inferred:skos:ancestor` → `inferred/True Negative (TN).json` ; `inferred:skos:broader` → `inferred/True Negative (TN).json`
- **[[True Positive (TP)]]** : `inferred:skos:ancestor` → `inferred/True Positive (TP).json` ; `inferred:skos:broader` → `inferred/True Positive (TP).json`
- **[[True Positive Rate (Recall)]]** : `inferred:skos:ancestor` → `inferred/True Positive Rate (Recall).json`
- **[[truncation]]** : `partOf` → `iso-thes:broaderPartitive` ; `inferred:skos:ancestor` → `inferred/truncation.json`
- **[[trust]]** : `skos:narrower` → retiré ; chaque cible reçoit `skos:broader: [[trust]]` ; `inferred:skos:related` → `inferred/trust.json`
- **[[turing test]]** : `inferred:skos:ancestor` → `inferred/turing test.json` ; `inferred:skos:broader` → `inferred/turing test.json`
- **[[type of process]]** : `inferred:skos:ancestor` → `inferred/type of process.json`
- **[[Unary operation]]** : `inferred:skos:ancestor` → `inferred/Unary operation.json`
- **[[Underfitting]]** : `inferred:skos:ancestor` → `inferred/Underfitting.json` ; `inferred:skos:broader` → `inferred/Underfitting.json`
- **[[unfinished creative work]]** : `subclass of` → `iso-thes:broaderGeneric` ; `has characteristic` → `cache/wikidata.jsonl` (fait sur le monde) ; `has cause` → `cache/wikidata.jsonl` (fait sur le monde) ; `instance of` → `iso-thes:broaderInstantial` ; `Commons category` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `wikidata entity id: Q2910675` → `skos:exactMatch: wd:Q2910675` ; `inferred:skos:ancestor` → `inferred/unfinished creative work.json` ; `inferred:skos:narrower` → `inferred/unfinished creative work.json`
- **[[union]]** : `wikidata entity id: Q17853087` → `skos:exactMatch: wd:Q17853087` ; `inferred:skos:narrower` → `inferred/union.json`
- **[[Unit tests]]** : `wikidata entity id: Q907375` → `skos:exactMatch: wd:Q907375` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Unit tests.json`
- **[[Unsloth]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Unsloth.json`
- **[[Unstructured data]]** : `inferred:skos:ancestor` → `inferred/Unstructured data.json`
- **[[Unsupervised Learning]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Unsupervised Learning.json`
- **[[updating]]** : `inferred:skos:ancestor` → `inferred/updating.json`
- **[[use case]]** : `facet of` → `skos:broader` ; `has part(s)` → `has part` ; `part of` → `iso-thes:broaderPartitive` ; `subclass of` → `iso-thes:broaderGeneric` ; `OmegaWiki Defined Meaning` → `skos:closeMatch` ; `inception` → `cache/wikidata.jsonl` (fait sur le monde) ; `ACM Classification Code (2012)` → **à décider** (hors schéma) ; `Stack Exchange tag` → `skos:closeMatch` ; `wikidata entity id: Q613417` → `skos:exactMatch: wd:Q613417` ; `inferred:skos:ancestor` → `inferred/use case.json`
- **[[user inputs]]** : `inferred:skos:ancestor` → `inferred/user inputs.json`
- **[[user outputs]]** : `inferred:skos:ancestor` → `inferred/user outputs.json`
- **[[user research]]** : `inferred:skos:narrower` → `inferred/user research.json`
- **[[user support]]** : `inferred:skos:ancestor` → `inferred/user support.json`
- **[[user tests]]** : `inferred:skos:ancestor` → `inferred/user tests.json`
- **[[user training]]** : `inferred:skos:ancestor` → `inferred/user training.json`
- **[[UX Problem Statement]]** : `inferred:skos:ancestor` → `inferred/UX Problem Statement.json`
- **[[Validate data]]** : `inferred:skos:ancestor` → `inferred/Validate data.json` ; `inferred:skos:broader` → `inferred/Validate data.json`
- **[[value judgment]]** : `wikidata entity id: Q1969661` → `skos:exactMatch: wd:Q1969661`
- **[[vanilla RAG design]]** : `articulates` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/vanilla RAG design.json`
- **[[variance]]** : `inferred:skos:ancestor` → `inferred/variance.json` ; `inferred:skos:broader` → `inferred/variance.json`
- **[[Vector]]** : `inferred:skos:narrower` → `inferred/Vector.json`
- **[[vector database]]** : `inferred:skos:narrower` → `inferred/vector database.json`
- **[[vector index]]** : `has part(s)` → `has part` ; `subclass of` → `iso-thes:broaderGeneric` ; `instance of` → `iso-thes:broaderInstantial` ; `part of` → `iso-thes:broaderPartitive` ; `inferred:skos:ancestor` → `inferred/vector index.json` ; `inferred:skos:broader` → `inferred/vector index.json`
- **[[vector length]]** : `inferred:skos:ancestor` → `inferred/vector length.json`
- **[[Vector space]]** : `inferred:skos:narrower` → `inferred/Vector space.json`
- **[[vectorization]]** : `creates` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/vectorization.json`
- **[[venture capital]]** : `instance of` → `iso-thes:broaderInstantial` ; `said to be the same as` → `skos:closeMatch` ; `subclass of` → `iso-thes:broaderGeneric` ; `wikidata entity id: Q219409` → `skos:exactMatch: wd:Q219409`
- **[[Version control]]** : `wikidata entity id: Q189439` → `skos:exactMatch: wd:Q189439` ; `subclass of` → `iso-thes:broaderGeneric` ; `product or material produced` → `cache/wikidata.jsonl` (fait sur le monde) ; `inferred:skos:ancestor` → `inferred/Version control.json` ; `inferred:skos:narrower` → `inferred/Version control.json`
- **[[vertices]]** : `inferred:skos:ancestor` → `inferred/vertices.json`
- **[[Virtual Environment]]** : `firstStepOf` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Virtual Environment.json`
- **[[Virtualization]]** : `inferred:skos:ancestor` → `inferred/Virtualization.json`
- **[[Visibility]]** : `inferred:skos:ancestor` → `inferred/Visibility.json`
- **[[Visual Basic Application]]** : `inferred:skos:ancestor` → `inferred/Visual Basic Application.json`
- **[[vocabulary]]** : `wikidata entity id: Q6499736` → `skos:exactMatch: wd:Q6499736` ; `subclass of` → `iso-thes:broaderGeneric` ; `inferred:skos:ancestor` → `inferred/vocabulary.json` ; `inferred:skos:narrower` → `inferred/vocabulary.json`
- **[[VRAM]]** : `inferred:skos:ancestor` → `inferred/VRAM.json`
- **[[Web worker]]** : `inferred:skos:ancestor` → `inferred/Web worker.json`
- **[[Weights]]** : `partOf` → `iso-thes:broaderPartitive` ; `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Weights.json`
- **[[Well-known text]]** : `inferred:skos:ancestor` → `inferred/Well-known text.json`
- **[[Wizard of Oz prototyping]]** : `inferred:skos:ancestor` → `inferred/Wizard of Oz prototyping.json`
- **[[Word embeddings]]** : `wikidata entity id: Q18395344` → `skos:exactMatch: wd:Q18395344` ; `foundationalPaper` → `dcterms:isReferencedBy` ; `keyPapers` → `dcterms:isReferencedBy` ; `subclass of` → `iso-thes:broaderGeneric` ; `usedIn` → `kg:usedBy` ; `techniques` → **à décider** (hors schéma) ; `properties` → **à décider** (hors schéma) ; `broader` → `skos:broader` ; `uses` → `kg:uses` ; `inferred:skos:ancestor` → `inferred/Word embeddings.json` ; `inferred:skos:related` → `inferred/Word embeddings.json`
- **[[workflow recursion guard]]** : `rdf:type: Concept` → `dcterms:type: Concept` ; `broader` → `skos:broader` ; `description` → `skos:definition` ; `timestamp` → supprimé (maintenance/média Wikidata ou dérivé de PROV) ; `inferred:skos:ancestor` → `inferred/workflow recursion guard.json`
- **[[Working directory]]** : `inferred:skos:ancestor` → `inferred/Working directory.json`
- **[[Wrapper methods]]** : `inferred:skos:ancestor` → `inferred/Wrapper methods.json`
- **[[XHTML]]** : `inferred:skos:ancestor` → `inferred/XHTML.json`
- **[[XML]]** : `inferred:skos:ancestor` → `inferred/XML.json`
- **[[Z-Score normalization]]** : `broader` → `skos:broader` ; `inferred:skos:ancestor` → `inferred/Z-Score normalization.json`
