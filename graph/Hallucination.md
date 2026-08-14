---
foundationalPaper: "Neural Text Generation with Unlikelihood Training (Welleck et al., 2020)"
keyPapers: ["Hallucinations in Neural Machine Translation (Lee et al., 2018)", "On Faithfulness and Factuality in Abstractive Summarization (Maynez et al., 2020)", "Survey of Hallucination in Natural Language Generation (Ji et al., 2023)"]
reliéA: "[[Artificial Intelligence (AI)]]"
affecte: ["[[Large Language Model]]", "[[Neural Machine Translation]]", "[[Text Generation]]"]
mitigated_by: ["[[Retrieval Augmented Generation]]", "[[Factual grounding]]", "[[Unlikelihood training]]"]
types: ["[[Intrinsic hallucination]]", "[[Extrinsic hallucination]]"]
broader: "[[Large Language Model]]"
inferred:skos:ancestor: "[[Large Language Model]]"
---

# Hallucination

In AI systems, hallucination refers to generated content that is nonsensical or unfaithful to the provided source content. The term gained prominence with neural language models.

## Original Definition

From Lee et al. (2018) on neural machine translation:
"We define hallucination as the phenomenon where the translation contains information that is not supported by the source sentence."

From Maynez et al. (2020):
"We propose a typology of hallucinations consisting of: intrinsic hallucinations (output that contradicts the source material) and extrinsic hallucinations (output that cannot be verified from the source)."

## Historical Development

1. **Neural Machine Translation (2016+)**: First observations
2. **Abstractive Summarization (2018+)**: Systematic study
3. **Large Language Models (2020+)**: Widespread recognition
4. **Mitigation Research (2021+)**: Active area of study

## Types of Hallucinations

### Intrinsic Hallucinations
From Maynez et al.:
"Generated content that contradicts the source document."
Examples:
- Wrong dates/numbers
- Incorrect named entities
- Contradictory statements

### Extrinsic Hallucinations
"Generated content that cannot be verified from the source."
Examples:
- Added plausible but unverified facts
- Speculation presented as fact
- Unsupported inferences

## Causes

From Ji et al. (2023):
1. **Data-related**:
   - Training on noisy data
   - Knowledge gaps in training data
   - Domain shift

2. **Model-related**:
   - Over-parameterization
   - Exposure bias
   - Decoding strategies

3. **Training-related**:
   - Maximum likelihood objective
   - Teacher forcing
   - Lack of grounding

## Detection Methods

### Automatic Detection
1. **Entailment-based**: Check logical consistency
2. **QA-based**: Generate questions to verify
3. **Knowledge-based**: Cross-reference with knowledge bases
4. **Statistical**: Anomaly detection approaches

### Human Evaluation
1. Faithfulness assessment
2. Factuality verification
3. Coherence checking

## Mitigation Strategies

### Training-time Approaches
From Welleck et al. (2020):
"Unlikelihood training reduces hallucinations by decreasing the probability of unwanted tokens during training."

Other methods:
1. Constrained decoding
2. Knowledge grounding
3. Retrieval augmentation
4. Factual consistency rewards

### Inference-time Approaches
1. Confidence thresholding
2. Multi-model voting
3. Post-processing filters
4. Human-in-the-loop verification

## Impact and Importance

As noted by Ji et al.:
"Hallucinations pose significant challenges for the deployment of AI systems in critical applications such as healthcare, legal, and financial services where factual accuracy is paramount."

## Historical Significance

The study of hallucinations:
- Revealed fundamental limitations of neural language models
- Spurred research into faithful generation
- Led to hybrid approaches combining neural and symbolic methods
- Influenced the development of grounding techniques

## Modern Developments

1. **Retrieval-Augmented Generation (RAG)**: Grounds outputs in retrieved documents
2. **Chain-of-Thought Prompting**: Improves reasoning transparency
3. **Constitutional AI**: Incorporates factuality constraints
4. **Factual Consistency Models**: Specialized models for verification

As LLMs become more prevalent, understanding and mitigating hallucinations remains a critical research area for ensuring AI safety and reliability.
