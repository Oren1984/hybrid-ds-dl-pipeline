# src/stage5_dl_nlp.py
# This script is responsible for training a deep learning model.
# For now, it trains a simple MLPClassifier on synthetic data or text data if available

import json
from pathlib import Path

import pandas as pd
from joblib import dump

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score

from sklearn.neural_network import MLPClassifier

# NLP path (optional)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline

# plotting (optional but recommended)
import matplotlib.pyplot as plt

# In a real implementation, you would train your model on the preprocessed dataset here, for example:
# def train_nlp_mlp(texts, labels):
# def train_numeric_mlp():
OUTPUT_DIR = Path("outputs")
(OUTPUT_DIR / "models").mkdir(parents=True, exist_ok=True)
(OUTPUT_DIR / "results").mkdir(parents=True, exist_ok=True)
(OUTPUT_DIR / "figures").mkdir(parents=True, exist_ok=True)

# Check for text.csv in data/raw/ to determine if we should run NLP or numeric path
RAW_TEXT_PATH = Path("data/raw/text.csv")

# Train a simple MLPClassifier on synthetic data or text data if available
def train_nlp_mlp(texts, labels):
    pipe = Pipeline(
        steps=[
            ("tfidf", TfidfVectorizer(max_features=5000, ngram_range=(1, 2))),
            ("mlp", MLPClassifier(hidden_layer_sizes=(128, 64), max_iter=20, random_state=42)),
        ]
    )
    X_train, X_test, y_train, y_test = train_test_split(
        texts, labels, test_size=0.2, random_state=42, stratify=labels
    )
    pipe.fit(X_train, y_train)
    preds = pipe.predict(X_test)

    # Evaluate metrics
    metrics = {
        "task": "text_classification",
        "model": "TFIDF + MLPClassifier",
        "accuracy": float(accuracy_score(y_test, preds)),
        "f1_score": float(f1_score(y_test, preds, average="weighted")),
        "note": "NLP path (text.csv present)"
    }
    return pipe, metrics

# Train a simple MLPClassifier on synthetic numeric data as a baseline
def train_numeric_mlp():
    X, y = make_classification(
        n_samples=800,
        n_features=20,
        n_informative=8,
        random_state=42
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Train a simple MLPClassifier
    model = MLPClassifier(
        hidden_layer_sizes=(64, 32),
        max_iter=50,
        random_state=42
    )
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    # Evaluate metrics
    metrics = {
        "task": "tabular_classification",
        "model": "MLPClassifier",
        "accuracy": float(accuracy_score(y_test, preds)),
        "f1_score": float(f1_score(y_test, preds)),
        "note": "Numeric synthetic data (no text.csv found)"
    }

    # Plot loss curve if available
    if hasattr(model, "loss_curve_") and model.loss_curve_:
        plt.figure()
        plt.plot(model.loss_curve_)
        plt.title("Training Loss Curve (MLP)")
        plt.xlabel("Iteration")
        plt.ylabel("Loss")
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / "figures/dl_training_loss_curve.png", dpi=150)
        plt.close()

    return model, metrics

# Main function to determine which path to run and save artifacts
def main():
    if RAW_TEXT_PATH.exists():
        df = pd.read_csv(RAW_TEXT_PATH)
        if not {"text", "label"}.issubset(df.columns):
            raise ValueError("data/raw/text.csv must contain columns: text,label")

        # Train NLP MLPClassifier
        model, metrics = train_nlp_mlp(df["text"].astype(str), df["label"])
        dump(model, OUTPUT_DIR / "models/dl_nlp_model.joblib")
        metrics["artifact"] = "outputs/models/dl_nlp_model.joblib"
    else:
        model, metrics = train_numeric_mlp()
        dump(model, OUTPUT_DIR / "models/dl_model.joblib")
        metrics["artifact"] = "outputs/models/dl_model.joblib"

        # Ensure figure path appears in results even if plot wasn't created
        fig_path = OUTPUT_DIR / "figures/dl_training_loss_curve.png"
        metrics["training_curve_figure"] = str(fig_path) if fig_path.exists() else None

    # Save metrics
    with open(OUTPUT_DIR / "results/dl_metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    print("Stage 5 completed:")
    print("- outputs/models/*dl*.joblib")
    print("- outputs/results/dl_metrics.json")


if __name__ == "__main__":
    main()
