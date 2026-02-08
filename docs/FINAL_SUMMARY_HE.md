# Hybrid DS + DL Pipeline — צינור עבודה היברידי (DS + DL)

**יוצר:** אורן (Oren1984)  
**פרויקט:** hybrid-ds-dl-pipeline  
**היקף:** בינה מלאכותית יישומית — שילוב מודול 1 (Data Science) ומודול 2 (Deep Learning & NLP)

---

## סקירה כללית

ריפוזיטורי זה מדגים תהליך **מקצה לקצה** של בינה מלאכותית היברידית,
בדומה לאופן שבו פרויקטים עובדים בעולם האמיתי:

1. התחלה עם **למידת מכונה קלאסית** ליצירת Baseline ברור  
2. מעבר ל־**Deep Learning / NLP** רק כאשר יש הצדקה מדידה  
3. השוואת מודלים באמצעות מטריקה אחידה  
4. שמירת תוצרים בצורה שחזורית וברורה  

המיקוד הוא **בהנדסה, קבלת החלטות וזרימת עבודה** — לא במורכבות מיותרת של מודלים.

---

## מבנה הפרויקט

hybrid-ds-dl-pipeline/
├─ src/ # שלבי Pipeline להרצה (דטרמיניסטיים)
├─ notebooks/ # מחברת סקירה (קריאה בלבד)
├─ outputs/
│ ├─ models/ # ארטיפקטים של מודלים מאומנים
│ ├─ results/ # מטריקות ומטא־דאטה (JSON, DB)
│ ├─ reports/ # דוחות קריאים (Markdown)
│ └─ figures/ # גרפים (אופציונלי)
├─ docs/ # תיעוד ברמת פרויקט
├─ requirements.txt
├─ validate_env.py
└─ README.md


---

## שלבי ה־Pipeline

ה־Pipeline מורץ באמצעות סקריפטים (לא דרך Notebook):

- **שלב 0** — הגדרת מסגרת ומטא־דאטה  
- **שלב 1** — טעינת נתונים (Placeholder)  
- **שלב 2** — EDA ראשוני (Placeholder)  
- **שלב 3** — חוזה קדם־עיבוד  
- **שלב 4** — מודל קלאסי (Baseline)  
- **שלב 5** — מודל Deep Learning / NLP  
- **שלב 6** — הערכה והשוואה  
- **שלב 7** — שמירה ל־SQLite (אופציונלי)  
- **שלב 8** — שמירה בסגנון Mongo (אופציונלי)  

קיים סקריפט נוחות להרצה מלאה לצורכי דמו.

---

## הרצה מהירה (Run Fast)

### 1. סביבה
pip install -r requirements.txt
python validate_env.py

2. הרצה מלאה (דמו)
python src/stage10_run_all.py

3. דילוג על מסדי נתונים (אופציונלי)
python src/stage10_run_all.py --skip-db

תוצרים (Single Source of Truth)
כל התוצאות נכתבות תחת outputs/.

### מודלים
outputs/models/classical_model.joblib

outputs/models/dl_model.joblib (או גרסת NLP)


### מטריקות
- outputs/results/classical_metrics.json

- outputs/results/dl_metrics.json

- outputs/results/final_metrics.json


### דוחות
- outputs/reports/comparison_report.md

- outputs/reports/PIPELINE_EXECUTION_REPORT.md


### מסד נתונים
outputs/results/artifacts.db (SQLite)


### מדיניות Notebook
המחברת תחת notebooks/:

- אינה מאמנת מודלים

- טוענת ומפרשת תוצרים קיימים בלבד

- מיועדת לסקירה, הצגה והסבר

- כל הלוגיקה הקריטית נמצאת בסקריפטים תחת src/.


### תיעוד
- אנגלית (מקור אמת):

docs/FINAL_SUMMARY_EN.md

- עברית (משלים):

docs/FINAL_SUMMARY_HE.md

דוחות הרצה זמינים תחת outputs/reports/.


### עקרונות הנדסיים
תכנון מבוסס תוצרים (Artifacts-first)

שחזור מלא מסביבה נקייה

ללא State סמוי


### הפרדה ברורה בין:

- קוד

- נתונים

- תוצרים

- תיעוד

מה הפרויקט הזה כן ומה לא
✔ הדגמת הנדסת AI יישומית
✔ שילוב מודול 1 + מודול 2
✔ ניתן להרצה ושחזור מלא

✖ לא מערכת פרודקשן
✖ לא פלטפורמה
✖ לא מבוסס Agents / RAG

