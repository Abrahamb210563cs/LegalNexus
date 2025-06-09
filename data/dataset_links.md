# 📚 LegalNexus - Indian Legal Datasets

Below is the curated list of top Indian legal datasets used for training and evaluation in LegalNexus. These datasets cover judgments, acts, legal reasoning, NER, and risk clause detection in Indian legal language.

---

### 1. [Law-AI GitHub Repository](https://github.com/Law-AI/)
- **Content**: Experiments, models, and data by researchers working on Indian legal NLP.
- **Use Case**: Foundation for clause analysis, QA, and judgment modeling.
- **Format**: Varies across sub-projects (JSON, CSV).

---

### 2. [Indian Legal Corpus – Sujant Kumar](https://huggingface.co/datasets/sujantkumarkv/indian_legal_corpus)
- **Content**: Raw legal case texts and statutes from multiple Indian courts.
- **Use Case**: Pretraining, summarization, and knowledge extraction.
- **Format**: JSONL files with full legal texts.

---

### 3. [IL-TUR – Exploration Lab](https://huggingface.co/datasets/Exploration-Lab/IL-TUR)
- **Content**: Legal text understanding and retrieval (court docs, legal tasks).
- **Use Case**: Search, retrieval augmentation, and dense embedding training.
- **Format**: Cleaned data, ready for transformer fine-tuning.

---

### 4. [InLegalNER – OpenNyAI](https://huggingface.co/datasets/opennyaiorg/InLegalNER)
- **Content**: Named Entity Recognition dataset for Indian legal texts.
- **Use Case**: Train legal-specific NER models (e.g., Act names, citations, parties).
- **Format**: JSONL with annotated spans.

---

### 5. [LegalBench – OpenReview Paper](https://openreview.net/forum?id=gZhvtIRu7i)
- **Content**: Benchmark datasets for legal reasoning, clause inference, and QA.
- **Use Case**: Evaluate model reasoning, summary quality, contract understanding.
- **Format**: Structured questions, answers, labels.

---

### 6. [LegalBench Arxiv (2022)](https://arxiv.org/abs/2204.00806)
- **Content**: Paper detailing construction and scope of Indian legal tasks.
- **Use Case**: Benchmarking, baseline comparison, QA-focused testing.
- **Format**: Reference for Paper + JSON/CSV data.

---

### 7. [Indian Law Dataset (JSONL) – varma007ut](https://huggingface.co/datasets/varma007ut/Indian_Law_Dataset_JSONL)
- **Content**: Legal provisions + case reasoning formatted for QA.
- **Use Case**: Clause interpretation, summary, question generation.
- **Format**: JSONL, each with `question`, `context`, `answer`.

---

### 8. [Indian Law Dataset – viber1](https://huggingface.co/datasets/viber1/indian-law-dataset)
- **Content**: Contracts, IPC/CrPC sections, and case law.
- **Use Case**: Risk clause detection, regulatory check, citation extraction.
- **Format**: JSON-formatted texts by topic.

---

## 🧠 Recommended Format for Sample
Push 5–10 samples from your custom processed dataset as:
