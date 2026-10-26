# Chronic Disease Risk Dashboard – Build Spec (for Antigravity)

**Goal:** Use Tableau dashboards to detect high-risk patients early (Heart disease, Diabetes, Stroke), find risk-factor correlations, and support preventive care, clinical decisions and resource allocation. Keep the project **short and simple**; build only what is listed.

## Tools
Tableau Desktop or Tableau Public · data as CSV/Excel (SQL optional) · Python/pandas for cleaning only · Chrome/Edge/Safari. Tableau work is done manually in the app: output exact steps, calculated-field formulas and chart specs for each task.

## Dataset (CSV, one row per patient)
Age, Gender, BMI, BloodPressure, Cholesterol, Glucose, Smoking, Alcohol, ExerciseLevel, Fatigue, ChestPain, Dizziness, Disease (Heart disease / Diabetes / Stroke / None).
Derived: **AgeGroup** (e.g. <30, 30-44, 45-59, 60+), **BMICategory** (Underweight/Normal/Overweight/Obese), **HighRisk** flag (e.g. high BP, cholesterol or glucose plus a disease or symptom).
If no data is provided, generate a realistic synthetic CSV (~1,000 rows).

## Epics & Tasks (8 epics, 14 tasks)

**E1 Data**
1. Get or generate the CSV.
2. Clean (nulls, types, duplicates) and add derived fields.

**E2 Connect**
3. Connect CSV in Tableau; verify data types and roles.

**E3 KPIs**
4. KPI cards: total patients, high-risk %, disease prevalence %, avg BMI, avg BP.

**E4 Disease Prevalence**
5. Prevalence by age group (bar).
6. Prevalence by BMI category (bar/stacked).

**E5 Risk Factors**
7. Heatmap: BP, cholesterol, glucose vs disease.
8. Lifestyle comparison: smoking, alcohol, exercise vs disease (trend/comparative bars).

**E6 Symptoms & Patients**
9. Symptom prevalence: chest pain, fatigue, dizziness.
10. High-risk patient table (sortable).

**E7 Dashboards** (one per persona)
11. **Clinical Risk** (Dr. Michael Carter, Risk Assessment Officer): KPIs, health indicators, high-risk list.
12. **Lifestyle Analysis** (Emily Rodriguez, Data Analyst): trends, heatmaps, lifestyle vs disease.
13. **Population Health** (Dr. Priya Nair, Public Health Researcher): age groups, BMI categories, exercise, symptoms.

**E8 Publish**
14. Add shared filters/actions (age group, BMI, disease), publish to Tableau Public/Cloud, write a half-page insights summary.

## Rules
- Consistent colours (one for high risk), clear titles and labels, interactive filters on every dashboard.
- Every chart must answer a stated goal; drop anything that doesn't.
- Work task by task in order; confirm each before moving on.
- Deliverables: cleaned CSV, `.twbx` workbook, short insights summary.
