# Hybrid DS + DL Pipeline

**Owner:** Oren (Oren1984)  
**Scope:** Applied AI  Module 1 (Data Science & Classical ML) + Module 2 (Deep Learning & NLP)

---

## Overview

This repository demonstrates a **minimal, end-to-end hybrid AI pipeline** that reflects
real-world applied machine learning workflows:

1. Start with **Classical Machine Learning** to establish a strong baseline  
2. Introduce **Deep Learning / NLP** only when justified  
3. Compare models using a shared metric  
4. Persist results as reproducible artifacts  

The focus is **engineering clarity and decision-making**, not model complexity.

---

## Project Structure

hybrid-ds-dl-pipeline/
 src/ # Executable pipeline stages (deterministic)
 notebooks/ # Read-only overview notebook
 outputs/
  models/ # Trained model artifacts
  results/ # Metrics & metadata (JSON, DB)
  reports/ # Human-readable reports (MD)
  figures/ # Optional plots
 docs/ # Project-level documentation
 requirements.txt
 validate_env.py
 README.md


---

## Pipeline Stages

The pipeline is executed via scripts (not notebooks):

- **Stage 0**  Frame & metadata
- **Stage 1**  Data loading (placeholder)
- **Stage 2**  Quick EDA (placeholder)
- **Stage 3**  Preprocessing contract
- **Stage 4**  Classical ML baseline
- **Stage 5**  Deep Learning / NLP model
- **Stage 6**  Evaluation & comparison
- **Stage 7**  SQLite persistence (optional)
- **Stage 8**  Mongo-style persistence (optional)

A convenience script exists for demo purposes.

---

## Run Fast

### 1. Environment
pip install -r requirements.txt
python validate_env.py

### 2. Full pipeline (demo)
python src/stage10_run_all.py

### 3. Skip databases (optional)
python src/stage10_run_all.py --skip-db


### Outputs (Single Source of Truth)

All results are written under outputs/:

* Models

- outputs/models/classical_model.joblib

- outputs/models/dl_model.joblib (or NLP variant)
  

* Metrics

- outputs/results/classical_metrics.json

- outputs/results/dl_metrics.json

- outputs/results/final_metrics.json


* Reports

- outputs/reports/comparison_report.md

- outputs/reports/PIPELINE_EXECUTION_REPORT.md


* Database

- outputs/results/artifacts.db (SQLite)


### Notebook Policy

The notebook under notebooks/:

- Does not train models

- Only loads and interprets existing outputs

- Exists for review, presentation, and explanation

All critical logic lives in scripts under src/.


### Documentation

* English (source of truth):

- docs/FINAL_SUMMARY_EN.md

* Hebrew (supporting):

- docs/FINAL_SUMMARY_HE.md
  

### Execution reports are available under outputs/reports/.

* Engineering Principles

* Artifacts-first design

* Reproducible from a clean environment

* No hidden state

* Clear separation between:

- Code

- Data

- Outputs

- Documentation
  

### What This Project Is (and Is Not)

 ✔ Applied AI engineering demo
 ✔ Hybrid Module 1 + Module 2
 ✔ Fully reproducible

 ✖ Not a production system
 ✖ Not a platform
 ✖ Not agent-based / RAG


### Final Note

This repository reflects how applied AI projects actually evolve:
start simple, measure, then justify complexity.

Further extensions (real datasets, advanced models, production infra)
are intentionally out of scope.
