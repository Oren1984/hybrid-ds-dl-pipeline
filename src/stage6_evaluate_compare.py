# src/stage6_evaluate_compare.py
# This script compares the results from the classical ML baseline and the deep learning NLP model.
# It loads the metrics from both stages, decides a winner based on a chosen metric (e

import json
from pathlib import Path
from datetime import datetime

# In a real implementation, you would load the metrics from both stages, compare them, and save a final report here, for example:
OUTPUT_DIR = Path("outputs")
(OUTPUT_DIR / "results").mkdir(parents=True, exist_ok=True)
(OUTPUT_DIR / "reports").mkdir(parents=True, exist_ok=True)

# Define paths to the metrics files from both stages
CLASSICAL_METRICS = OUTPUT_DIR / "results/classical_metrics.json"
DL_METRICS = OUTPUT_DIR / "results/dl_metrics.json"

# Utility function to load JSON metrics
def load_json(path: Path):
    if not path.exists():
        raise FileNotFoundError(f"Missing required file: {path}")
    with open(path, "r") as f:
        return json.load(f)

# Main function to compare metrics and save final report
def main():
    classical = load_json(CLASSICAL_METRICS)
    dl = load_json(DL_METRICS)

    # Decide winner by f1_score (same key in both)
    c_f1 = float(classical.get("f1_score", 0.0))
    d_f1 = float(dl.get("f1_score", 0.0))

    # In case of a tie, we can also compare accuracy or declare a tie. For simplicity, we'll just pick the one with higher f1_score.
    winner = "deep_learning" if d_f1 >= c_f1 else "classical_ml"

    # Save final comparison results
    final = {
        "created_at": datetime.utcnow().isoformat(),
        "comparison_metric": "f1_score",
        "winner": winner,
        "classical": classical,
        "deep_learning": dl,
    }

    # Save final metrics to JSON
    with open(OUTPUT_DIR / "results/final_metrics.json", "w") as f:
        json.dump(final, f, indent=2)

    # Generate a markdown report summarizing the comparison
    report = []
    report.append("# Model Comparison Report\n")
    report.append(f"- Metric used: **f1_score**\n")
    report.append(f"- Winner: **{winner}**\n\n")

    # Add details from both models
    report.append("## Classical ML\n")
    report.append(f"- Model: `{classical.get('model')}`\n")
    report.append(f"- Accuracy: `{classical.get('accuracy')}`\n")
    report.append(f"- F1: `{classical.get('f1_score')}`\n")
    report.append(f"- Note: {classical.get('note')}\n\n")

    # Add details from the deep learning model
    report.append("## Deep Learning / NLP\n")
    report.append(f"- Model: `{dl.get('model')}`\n")
    report.append(f"- Task: `{dl.get('task')}`\n")
    report.append(f"- Accuracy: `{dl.get('accuracy')}`\n")
    report.append(f"- F1: `{dl.get('f1_score')}`\n")
    report.append(f"- Note: {dl.get('note')}\n\n")

    # Add a summary
    report.append("## Summary\n")
    report.append("This project demonstrates a minimal end-to-end hybrid flow:\n")
    report.append("Classical ML baseline  Deep Learning model  Results comparison.\n")

    # Save the markdown report
    (OUTPUT_DIR / "reports/comparison_report.md").write_text("".join(report), encoding="utf-8")

    print("Stage 6 completed:")
    print("- outputs/results/final_metrics.json")
    print("- outputs/reports/comparison_report.md")


if __name__ == "__main__":
    main()
