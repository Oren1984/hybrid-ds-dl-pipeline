# src/stage8_persist_mongo.py
# This stage takes the final metrics from Stage 6 and persists them into a MongoDB collection (if MONGO_URI is set).
# It also generates a sample JSON document and a markdown file

import json
import os
from pathlib import Path
from datetime import datetime

# In a real implementation, you would load the final metrics from Stage 6 and persist them into a MongoDB collection here, for example:
FINAL_METRICS_PATH = Path("outputs/results/final_metrics.json")
OUT_DOCS = Path("outputs/results/sample_documents.json")
OUT_SCHEMA = Path("outputs/reports/mongo_schema.md")
OUT_DOCS.parent.mkdir(parents=True, exist_ok=True)
OUT_SCHEMA.parent.mkdir(parents=True, exist_ok=True)

# In a real implementation, you would also generate a markdown file with the MongoDB schema and example document here, for example:
def main():
    if not FINAL_METRICS_PATH.exists():
        raise FileNotFoundError("Missing outputs/results/final_metrics.json (run Stage 6 first)")

    # Load the final metrics from Stage 6
    with open(FINAL_METRICS_PATH, "r") as f:
        final = json.load(f)

    # Prepare a document to insert into MongoDB (lightweight schema)
    doc = {
        "type": "experiment_run",
        "created_at": final.get("created_at", datetime.utcnow().isoformat()),
        "winner": final.get("winner"),
        "comparison_metric": final.get("comparison_metric", "f1_score"),
        "classical": {
            "model": final.get("classical", {}).get("model"),
            "f1_score": final.get("classical", {}).get("f1_score"),
            "accuracy": final.get("classical", {}).get("accuracy"),
        },
        "deep_learning": {
            "model": final.get("deep_learning", {}).get("model"),
            "task": final.get("deep_learning", {}).get("task"),
            "f1_score": final.get("deep_learning", {}).get("f1_score"),
            "accuracy": final.get("deep_learning", {}).get("accuracy"),
        },
        "raw": final
    }

    # Save a sample document to JSON for reference
    OUT_DOCS.write_text(json.dumps([doc], indent=2), encoding="utf-8")

    # Generate a markdown file with the MongoDB schema and example document
    OUT_SCHEMA.write_text(
        "# MongoDB Schema (Light)\n\n"
        "Collection: `experiment_runs`\n\n"
        "## Document example\n"
        "- type: `experiment_run`\n"
        "- created_at: ISO timestamp\n"
        "- winner: `classical_ml` or `deep_learning`\n"
        "- classical: {model, f1_score, accuracy}\n"
        "- deep_learning: {model, task, f1_score, accuracy}\n"
        "- raw: full JSON snapshot (optional)\n\n"
        "## Notes\n"
        "- This project keeps Mongo optional to avoid heavy setup.\n",
        encoding="utf-8"
    )

    # Insert the document into MongoDB if MONGO_URI is set
    mongo_uri = os.getenv("MONGO_URI")
    if mongo_uri:
        try:
            from pymongo import MongoClient  # optional dependency
            client = MongoClient(mongo_uri)
            db = client.get_default_database() or client["hybrid_db"]
            col = db["experiment_runs"]
            res = col.insert_one(doc)
            print(f"Inserted document to MongoDB, _id={res.inserted_id}")
        except Exception as e:
            print("Mongo insert skipped/failed (optional). Reason:", str(e))
    else:
        print("MONGO_URI not set. Mongo insert skipped (optional).")

    print("Stage 8 completed:")
    print("- outputs/results/sample_documents.json")
    print("- outputs/reports/mongo_schema.md")


if __name__ == "__main__":
    main()
