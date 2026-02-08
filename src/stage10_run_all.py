# src/stage10_run_all.py
# This script runs all stages in sequence, from Stage 0 to Stage 8.
# It also measures the execution time of each stage and prints a summary at the end.

import argparse
import subprocess
import sys
from pathlib import Path
from datetime import datetime

# Note: In a real implementation, you might want to add error handling, logging, and more sophisticated time measurement here. This is a simplified version for demonstration purposes.
STAGES = [
    ("Stage 0", "src/stage0_frame.py"),
    ("Stage 1", "src/stage1_load.py"),
    ("Stage 2", "src/stage2_eda.py"),
    ("Stage 3", "src/stage3_preprocess.py"),
    ("Stage 4", "src/stage4_classical_ml.py"),
    ("Stage 5", "src/stage5_dl_nlp.py"),
    ("Stage 6", "src/stage6_evaluate_compare.py"),
    ("Stage 7", "src/stage7_persist_sql.py"),
    ("Stage 8", "src/stage8_persist_mongo.py"),
]

# Utility function to run a script and measure its execution time
def run_script(label: str, script_path: str, python_exe: str):
    print(f"\n=== {label} | {script_path} ===")
    start = datetime.utcnow()
    result = subprocess.run([python_exe, script_path], capture_output=True, text=True)
    end = datetime.utcnow()

    # Print the output and error streams from the script
    if result.stdout:
        print(result.stdout.rstrip())
    if result.stderr:
        print(result.stderr.rstrip(), file=sys.stderr)

    # Check if the script executed successfully
    if result.returncode != 0:
        raise RuntimeError(f"{label} failed with exit code {result.returncode}")

    # Calculate and print the duration
    dur_ms = int((end - start).total_seconds() * 1000)
    print(f"--- {label} done in {dur_ms} ms ---")

# Utility function to ensure key output directories exist
def ensure_dirs():
    # ensure key folders exist even if user forgot to create them
    Path("outputs/results").mkdir(parents=True, exist_ok=True)
    Path("outputs/models").mkdir(parents=True, exist_ok=True)
    Path("outputs/reports").mkdir(parents=True, exist_ok=True)
    Path("outputs/figures").mkdir(parents=True, exist_ok=True)

# Main function to run all stages
def main():
    parser = argparse.ArgumentParser(description="Run all stages for the hybrid DS+DL pipeline project.")
    parser.add_argument("--python", default=sys.executable, help="Python executable to use (default: current).")
    parser.add_argument("--skip-db", action="store_true", help="Skip DB persistence stages (Stage 7 + 8).")
    args = parser.parse_args()

    # Ensure output directories exist
    ensure_dirs()

    # Determine which stages to run based on the --skip-db flag
    stages = STAGES
    if args.skip_db:
        stages = [s for s in STAGES if s[0] not in ("Stage 7", "Stage 8")]

    # quick existence check
    missing = [p for _, p in stages if not Path(p).exists()]
    if missing:
        print("Missing scripts:", missing, file=sys.stderr)
        sys.exit(2)

    print("Running stages:", " -> ".join([s[0] for s in stages]))
    for label, path in stages:
        run_script(label, path, args.python)

    print("\n Run-all completed successfully.")

if __name__ == "__main__":
    main()
