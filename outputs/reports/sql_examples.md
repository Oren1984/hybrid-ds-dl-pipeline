# SQL Examples (SQLite)

Database: `outputs/results/artifacts.db`

## Show latest runs
```sql
SELECT id, created_at, winner, classical_f1, dl_f1
FROM run_metrics
ORDER BY id DESC
LIMIT 10;
```

## Show best DL runs
```sql
SELECT id, created_at, dl_model, dl_f1
FROM run_metrics
ORDER BY dl_f1 DESC
LIMIT 10;
```
