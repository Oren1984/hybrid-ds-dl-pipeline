# MongoDB Schema (Light)

Collection: `experiment_runs`

## Document example
- type: `experiment_run`
- created_at: ISO timestamp
- winner: `classical_ml` or `deep_learning`
- classical: {model, f1_score, accuracy}
- deep_learning: {model, task, f1_score, accuracy}
- raw: full JSON snapshot (optional)

## Notes
- This project keeps Mongo optional to avoid heavy setup.
