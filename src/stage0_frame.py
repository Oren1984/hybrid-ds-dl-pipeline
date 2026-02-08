# src/stage0_frame.py
# This script sets up the initial frame for the project, including

import json
from datetime import datetime

# Project metadata to be saved in outputs/results/metadata.json
PROJECT_METADATA = {
    "project": "hybrid-ds-dl-pipeline",
    "owner": "Oren (Oren1984)",
    "stage": "Stage 0 - Frame",
    "created_at": datetime.utcnow().isoformat(),
    "description": "Hybrid project combining Classical ML and Deep Learning",
    "primary_metric": "F1-score"
}

# In a real implementation, you might include more detailed metadata such as:
# - Data sources
# - Model architectures
# - Training parameters
def main():
    with open("outputs/results/metadata.json", "w") as f:
        json.dump(PROJECT_METADATA, f, indent=2)

    print("Stage 0 completed: metadata.json created")

if __name__ == "__main__":
    main()
