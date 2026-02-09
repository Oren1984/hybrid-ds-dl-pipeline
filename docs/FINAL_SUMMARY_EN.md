Hybrid DS + DL Pipeline — Final Summary

Owner: Oren (Oren1984)
Project: hybrid-ds-dl-pipeline
Scope: Applied Hybrid AI (Module 1 + Module 2)

1. Project Goal

This project demonstrates a minimal, end-to-end hybrid AI workflow:

Start with Classical Machine Learning (Module 1)

Establish a strong baseline

Introduce Deep Learning / NLP only where justified (Module 2)

Compare results using a shared metric

Persist results in files and databases

The focus is engineering clarity and decision-making, not model complexity.

2. Design Rationale — Why a Hybrid Approach

This project was intentionally designed as a hybrid DS + DL pipeline, rather than two separate demos.

Why start with Classical Machine Learning

Classical ML models are used first to:

Establish a fast and interpretable baseline

Validate that the problem is solvable without unnecessary complexity

Provide a clear reference point for later comparison

This stage answers the question:
“Can this problem be solved effectively with simpler, explainable models?”

Why introduce Deep Learning / NLP later

Deep Learning is introduced only after baseline performance is measured, in order to:

Learn non-linear feature interactions

Demonstrate an escalation path when classical methods may be insufficient

Evaluate whether added complexity produces measurable value

Why this is a single pipeline

Both approaches operate on the same pipeline and evaluation logic, allowing:

Direct, fair comparison

Clear trade-off analysis

Real-world applied AI decision flow

This reflects how applied AI systems are built in practice:
start simple, measure, then justify complexity.

3. Pipeline Overview

Stages executed (via stage10_run_all.py):

Frame & metadata

Data loading (placeholder)

Quick EDA (placeholder)

Preprocessing contract

Classical ML baseline

Deep Learning / NLP model

Evaluation & comparison

SQLite persistence (optional)

Mongo-style persistence (optional)

4. Models
Classical ML

Model: Logistic Regression

Data: Synthetic tabular (placeholder)

Purpose: Fast, interpretable baseline

Deep Learning

Model: MLPClassifier

Modes:

Numeric tabular DL (default)

NLP pipeline (TF-IDF + MLP) if data/raw/text.csv exists

Purpose: Demonstrate controlled escalation in model complexity

5. Evaluation Strategy

Primary metric: F1-score

Outputs:

classical_metrics.json

dl_metrics.json

final_metrics.json

comparison_report.md

A clear winner is selected programmatically, based on shared metrics.

6. Persistence Layer
SQLite

File: outputs/results/artifacts.db

Stores:

Run metadata

Model metrics

Raw JSON snapshots

Mongo (Optional)

Light schema design

Demonstrated via JSON examples

Actual insertion skipped unless configured

7. Key Engineering Principles

Artifacts-first design

Fully reproducible from a clean environment

No hidden state

Clear separation between:

Code

Data

Outputs

Documentation

8. What This Project Is (and Is Not)

This project is:

An applied AI engineering demo

A hybrid Module 1 + Module 2 implementation

Fully runnable end-to-end

This project is not:

A production system

A platform

An agent-based or RAG system

9. Conclusion

This repository reflects how applied AI projects actually evolve:
start simple, measure results, and justify complexity only when needed.

The pipeline can later be extended with real datasets, advanced models, or production orchestration if required — but those concerns are intentionally out of scope here.
