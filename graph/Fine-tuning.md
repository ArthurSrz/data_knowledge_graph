---
foundationalPaper: "How transferable are features in deep neural networks? (Yosinski et al., 2014)"
keyPapers: ["BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (Devlin et al., 2019)", "Universal Language Model Fine-tuning for Text Classification (Howard & Ruder, 2018)", "Parameter-Efficient Transfer Learning for NLP (Houlsby et al., 2019)"]
implementationOf: "[[Transfer learning]]"
appliesTo: ["[[Pre-trained models]]", "[[Large Language Model]]", "[[Neural network models]]"]
techniques: ["[[Full fine-tuning]]", "[[Layer freezing]]", "[[Adapter modules]]", "[[LoRA]]"]
benefits: ["[[Reduced training time]]", "[[Less data required]]", "[[Better performance]]"]
broader: "[[Model tuning]]"
inferred:skos:ancestor: "[[model tuning]]"
inferred:skos:broader: "[[model tuning]]"
inferred:skos:narrower:
  - "[[Instruction dataset]]"
  - "[[Low-Rank Adaptation]]"
  - "[[Unsloth]]"
  - "[[supervised finetuning]]"
---
Fine-tuning is the [[process]] of taking a pre-trained [[model]] and adapting it to a specific task by continuing training on task-specific [[data]].

## Original Definition

From Yosinski et al. (2014):

"Fine-tuning works as follows: first, we train a base network on a base dataset and task, and then we repurpose the learned features, or transfer them, to a second [[target]] network to be trained on a [[target]] dataset and task. This [[process]] tends to work if the features are general, meaning suitable for both base and [[target]] tasks."

From Devlin et al. (2019) on [[BERT]]:
"[[BERT]] is designed to pre-train deep bidirectional representations... As a result, the pre-trained [[BERT]] [[model]] can be fine-tuned with just one additional [[output]] [[layer]] to create state-of-the-art models for a wide range of tasks."

## Historical Development

1. **[[computer vision]] (2012+)**: Fine-tuning CNN features
2. **[[Word Embeddings]] (2013+)**: Fine-tuning word [[vectors]]
3. **ULMFiT (2018)**: Systematic approach for NLP
4. **[[BERT]] Era (2019+)**: Standard practice for [[transformers]]
5. **[[Parameter]]-Efficient (2020+)**: Optimizing fine-tuning

## Fine-tuning [[Process]]

Basic [[algorithm]]:
1. Load pre-trained [[model]] [[weights]]
2. Replace/[[add]] task-specific layers
3. Continue training on task [[data]]
4. Optionally freeze certain layers

## Techniques

### Full Fine-tuning
From Devlin et al.:
"The simplest approach is to initialize all parameters with the pre-trained values and train all parameters end-to-end on the downstream task."

### [[Layer]] Freezing
From Yosinski et al.:
"We can freeze the bottom n layers of the network and only fine-tune the top layers. This preserves the general features learned in the bottom layers."

### [[Learning Rate]] Scheduling
From Howard & Ruder (2018):
"Discriminative fine-tuning: using different learning rates for different layers, typically decreasing from top to bottom layers."

## [[Parameter]]-Efficient Methods

### Adapter Modules (Houlsby et al., 2019)
"Adapters are small bottleneck layers inserted between layers of a pre-trained network. Only these adapter parameters are trained during fine-tuning."

### LoRA (Hu et al., 2021)
"[[Low-Rank Adaptation]] freezes the pre-trained [[model]] [[weights]] and injects trainable rank decomposition matrices into each [[layer]]."

## Mathematical Formulation

Standard fine-tuning:
θ_ft = argmin_θ L_task(f_θ(x), y) + λR(θ - θ_pre)

Where:
- θ_pre are pre-trained parameters
- θ_ft are fine-tuned parameters
- L_task is task-specific loss
- R is [[regularization]] term

## Benefits

From empirical research:
1. **Sample Efficiency**: Better performance with less [[data]]
2. **Faster Convergence**: Builds on learned features
3. **Better Generalization**: Leverages pre-trained [[knowledge]]
4. **Resource Efficiency**: Reduces computational needs

## Challenges

1. **Catastrophic Forgetting**: Losing pre-trained [[knowledge]]
2. **Negative Transfer**: When pre-training hurts performance
3. **Hyperparameter Sensitivity**: Learning rates, freezing strategies
4. **Task Mismatch**: Large [[domain]] gaps

## [[Best]] Practices

From ULMFiT (Howard & Ruder):
1. **Gradual Unfreezing**: Progressively unfreeze layers
2. **Discriminative Learning Rates**: Different rates per [[layer]]
3. **Slanted Triangular Learning Rates**: Warm-up then decay

## Applications

1. **[[computer vision]]**: [[Object]] detection, segmentation
2. **[[Natural Language Processing]]**: Text [[classification]], QA
3. **Speech Recognition**: Accent adaptation
4. **[[Reinforcement Learning]]**: Policy transfer

## Historical Significance

Fine-tuning:
- Enabled practical [[transfer learning]]
- Made large models accessible
- Democratized AI development
- Changed the training paradigm

As Yosinski noted: "Fine-tuning can give significant performance boosts, especially when the [[target]] dataset is small."

## Modern Developments

1. **Prompt Tuning**: Only tune prompt [[embeddings]]
2. **Prefix Tuning**: [[Add]] trainable prefixes
3. **Multi-task Fine-tuning**: Simultaneous task adaptation
4. **Continual Fine-tuning**: Sequential task learning
5. **Few-shot Fine-tuning**: Adaptation with minimal [[data]]

The evolution continues toward more efficient and effective methods for adapting large pre-trained models.
