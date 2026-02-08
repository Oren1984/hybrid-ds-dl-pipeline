# src/stage7_persist_sql.py
# This stage takes the final metrics from Stage 6 and persists them into a SQLite database.
# It also generates a simple markdown file with SQL query examples to retrieve the stored metrics.

import json
import sqlite3
from pathlib import Path
from datetime import datetime

# In a real implementation, you would load the final metrics from Stage 6 and persist them into a database here, for example:
DB_PATH = Path("outputs/results/artifacts.db")
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

# In a real implementation, you would also generate a markdown file with SQL query examples to retrieve the stored metrics here, for example:
FINAL_METRICS_PATH = Path("outputs/results/final_metrics.json")
SQL_DOC_PATH = Path("outputs/reports/sql_examples.md")
SQL_DOC_PATH.parent.mkdir(parents=True, exist_ok=True)

# Utility function to load JSON metrics
def main():
    if not FINAL_METRICS_PATH.exists():
        raise FileNotFoundError("Missing outputs/results/final_metrics.json (run Stage 6 first)")
    
    # Load the final metrics from Stage 6
    with open(FINAL_METRICS_PATH, "r") as f:
        final = json.load(f)

    # Persist the final metrics into a SQLite database
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Create a table to store the metrics if it doesn't exist
    cur.execute("""
    CREATE TABLE IF NOT EXISTS run_metrics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TEXT NOT NULL,
        winner TEXT NOT NULL,
        classical_model TEXT,
        classical_f1 REAL,
        dl_model TEXT,
        dl_f1 REAL,
        raw_json TEXT NOT NULL
    )
    """)

    # Extract relevant fields from the final metrics for insertion into the database
    created_at = final.get("created_at", datetime.utcnow().isoformat())
    winner = final.get("winner", "unknown")
    classical_model = final.get("classical", {}).get("model")
    classical_f1 = float(final.get("classical", {}).get("f1_score", 0.0))
    dl_model = final.get("deep_learning", {}).get("model")
    dl_f1 = float(final.get("deep_learning", {}).get("f1_score", 0.0))

    # Insert the metrics into the database
    cur.execute("""
    INSERT INTO run_metrics(created_at, winner, classical_model, classical_f1, dl_model, dl_f1, raw_json)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (created_at, winner, classical_model, classical_f1, dl_model, dl_f1, json.dumps(final)))

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

    # Generate a markdown file with SQL query examples to retrieve the stored metrics
    SQL_DOC_PATH.write_text(
        "# SQL Examples (SQLite)\n\n"
        "Database: `outputs/results/artifacts.db`\n\n"
        "## Show latest runs\n"
        "```sql\n"
        "SELECT id, created_at, winner, classical_f1, dl_f1\n"
        "FROM run_metrics\n"
        "ORDER BY id DESC\n"
        "LIMIT 10;\n"
        "```\n\n"
        "## Show best DL runs\n"
        "```sql\n"
        "SELECT id, created_at, dl_model, dl_f1\n"
        "FROM run_metrics\n"
        "ORDER BY dl_f1 DESC\n"
        "LIMIT 10;\n"
        "```\n",
        encoding="utf-8"
    )

    print("Stage 7 completed:")
    print("- outputs/results/artifacts.db")
    print("- outputs/reports/sql_examples.md")


if __name__ == "__main__":
    main()
