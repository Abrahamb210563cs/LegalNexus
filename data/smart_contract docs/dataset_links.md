# 📦 Smart Contract Datasets for LegalNexus

This folder contains curated and preprocessed smart contract datasets used to train LegalNexus on **Solidity code auditing**, focused on vulnerability detection and risk clause identification.

---

## 🔍 Purpose

Smart contracts, written mostly in Solidity, often contain subtle security flaws that lead to millions in losses. LegalNexus aims to:

- Understand Solidity syntax and structure
- Detect and explain common vulnerabilities (e.g., reentrancy, overflow)
- Act as a multilingual code compliance advisor for Web3 legal-tech

---

## 📚 Included Datasets

### ✅ 1. Slither-Audited Smart Contracts  
**Source:** [HuggingFace](https://huggingface.co/datasets/mwritescode/slither-audited-smart-contracts)  
- 113K contracts with **multi-label vulnerability annotations**
- Labels auto-generated using [Slither](https://github.com/crytic/slither) – a leading Solidity static analyzer
- Format: JSONL with `source_code` and `slither` tags

### ✅ 2. Messi-Q Vulnerability Dataset  
**GitHub:** [Messi-Q/Smart-Contract-Dataset](https://github.com/Messi-Q/Smart-Contract-Dataset)  
- Human-labeled contracts (~12K)
- Target vulnerabilities:
  - Reentrancy
  - Timestamp dependence
  - Integer overflows/underflows
  - Dangerous delegate calls

### ✅ 3. Aggregated Smart Contract Corpus  
**Reference:** [Awesome Smart Contract Datasets](https://github.com/acorn421/awesome-smart-contract-datasets)  
- A list of 30+ academic-grade datasets:
  - SmartBugs
  - SC-Bench
  - EtherScan Scrapes
  - SmartWild
- We use select samples from this list for few-shot generalization.

---

## 🛠️ Preprocessing

We convert all datasets to a common instruction-style format (`sample_contracts.jsonl`) for fine-tuning LLaMA:

```json
{
  "instruction": "audit",
  "input": "<Solidity Code>",
  "output": "Identified risks: reentrancy, overflow, ..."
}
