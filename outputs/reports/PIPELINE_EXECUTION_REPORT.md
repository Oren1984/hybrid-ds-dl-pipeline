# Pipeline Execution Report

## Execution Mode
- Script: `src/stage10_run_all.py`
- Mode: Full + Skip-DB tested
- Environment: Local (Conda)

---

## Verified Outputs

### Models
- outputs/models/classical_model.joblib
- outputs/models/dl_model.joblib (or dl_nlp_model.joblib)

### Metrics
- outputs/results/classical_metrics.json
- outputs/results/dl_metrics.json
- outputs/results/final_metrics.json

### Reports
- outputs/reports/comparison_report.md
- outputs/reports/sql_examples.md
- outputs/reports/mongo_schema.md

### Databases
- outputs/results/artifacts.db (SQLite)

---

## Warnings Observed

- sklearn MLP convergence warning (expected for low-iteration demo)
- datetime.utcnow deprecation warnings (non-breaking)

No runtime errors occurred.

---

## Status
 Pipeline executed successfully  
 Artifacts generated as expected  
