# Hybrid DS + DL Pipeline  Final Summary

**Owner:** Oren (Oren1984)  
**Project:** hybrid-ds-dl-pipeline  
**Scope:** Applied Hybrid AI (Module 1 + Module 2)

---

## 1. Project Goal

This project demonstrates a **minimal, end-to-end hybrid AI workflow**:

- Start with **Classical Machine Learning** (Module 1)
- Establish a strong baseline
- Introduce **Deep Learning / NLP** only where justified (Module 2)
- Compare results using a shared metric
- Persist results in files and databases

The focus is **engineering clarity**, not model complexity.

---

## 2. Pipeline Overview

Stages executed (via `stage10_run_all.py`):

0. Frame & metadata  
1. Data loading (placeholder)  
2. Quick EDA (placeholder)  
3. Preprocessing contract  
4. Classical ML baseline  
5. Deep Learning / NLP model  
6. Evaluation & comparison  
7. SQLite persistence (optional)  
8. Mongo-style persistence (optional)

---

## 3. Models

### Classical ML
- Model: Logistic Regression
- Data: Synthetic tabular (placeholder)
- Purpose: Fast, interpretable baseline

### Deep Learning
- Model: MLPClassifier
- Modes:
  - Numeric tabular DL (default)
  - NLP pipeline (TF-IDF + MLP) if `data/raw/text.csv` exists
- Purpose: Demonstrate escalation path

---

## 4. Evaluation Strategy

- Primary metric: **F1-score**
- Outputs:
  - `classical_metrics.json`
  - `dl_metrics.json`
  - `final_metrics.json`
  - `comparison_report.md`

A clear winner is selected programmatically.

---

## 5. Persistence Layer

### SQLite
- File: `outputs/results/artifacts.db`
- Stores:
  - Run metadata
  - Model metrics
  - Raw JSON snapshot

### Mongo (Optional)
- Light schema design
- Demonstrated via JSON examples
- Actual insertion skipped unless configured

---

## 6. Key Engineering Principles

- Artifacts-first design
- Reproducible from clean environment
- No hidden state
- Clear separation between:
  - Code
  - Data
  - Outputs
  - Documentation

---

## 7. What This Project Is (and Is Not)

 Applied engineering demo  
 Hybrid Module 1 + Module 2  
 Runnable end-to-end  

 Not a production system  
 Not a platform  
 Not agent-based / RAG

---

## 8. Conclusion

This repository reflects **how applied AI projects actually evolve**:
start simple, measure, then justify complexity.

The pipeline can later be extended with real datasets,
advanced models, or production orchestration if needed.
