# Chronic Disease Risk Dashboard Project

> 🌐 **Live Interactive Demo:** [https://bhayresejal-ux.github.io/Moviesproject/](https://bhayresejal-ux.github.io/Moviesproject/)

An end-to-end Healthcare Analytics and Tableau Business Intelligence project designed to detect high-risk patients early (Heart Disease, Diabetes, Stroke), uncover clinical risk-factor correlations, and support preventive care, clinical decision-making, and resource allocation.

---

## 📊 Project Overview

- **Goal:** Provide clinical decision support, population health insights, and lifestyle risk evaluation using interactive Tableau dashboards.
- **Dataset:** 1,000 patient records encompassing demographic vitals, clinical biomarkers, lifestyle factors, and diagnosed chronic conditions.
- **Target Personas:**
  1. **Dr. Michael Carter** (Risk Assessment Officer): Clinical triage, KPI monitoring, and high-risk patient registries.
  2. **Emily Rodriguez** (Data Analyst): Lifestyle determinants, exercise correlations, and risk heatmap distributions.
  3. **Dr. Priya Nair** (Public Health Researcher): Population stratification, age/BMI epidemiology, and healthcare resource planning.

---

## 📁 Repository Structure

```
├── HealthRisk_Tableau.md               # Build specification & task requirements
├── TABLEAU_GUIDE.md                    # Complete Tableau implementation manual (all 8 epics & 14 tasks)
├── INSIGHTS_SUMMARY.md                 # Executive half-page clinical insights report
├── chronic_disease_risk_patients.csv   # Cleaned 1,000-row patient dataset with derived fields
├── generate_dataset.py                 # Python script to reproduce/regenerate synthetic clinical data
└── README.md                           # Project documentation & execution guide
```

---

## 📈 Dataset Schema & Data Dictionary

| Column | Type | Description | Values / Range |
| :--- | :--- | :--- | :--- |
| `PatientID` | String | Unique patient identifier | `P0001` - `P1000` |
| `Age` | Integer | Patient age in years | `18` - `85` |
| `AgeGroup` | String | Stratified age cohort | `<30`, `30-44`, `45-59`, `60+` |
| `Gender` | String | Biological sex | `Male`, `Female` |
| `BMI` | Float | Body Mass Index ($kg/m^2$) | `16.5` - `45.0` |
| `BMICategory`| String | WHO BMI classification | `Underweight`, `Normal`, `Overweight`, `Obese` |
| `BloodPressure` | Integer | Resting Systolic BP (mmHg) | `95` - `188` |
| `Cholesterol` | Integer | Total serum cholesterol (mg/dL) | `130` - `305` |
| `Glucose` | Integer | Fasting blood glucose (mg/dL) | `70` - `235` |
| `Smoking` | String | Active tobacco user | `Yes`, `No` |
| `Alcohol` | String | Alcohol consumption frequency | `None`, `Moderate`, `Heavy` |
| `ExerciseLevel` | String | Physical activity level | `Low`, `Moderate`, `High` |
| `Fatigue` | String | Recurring fatigue symptom | `Yes`, `No` |
| `ChestPain` | String | Reported chest angina / discomfort| `Yes`, `No` |
| `Dizziness` | String | Reported vertigo / dizziness | `Yes`, `No` |
| `Disease` | String | Diagnosed primary condition | `None`, `Heart disease`, `Diabetes`, `Stroke` |
| `HighRisk` | String | Clinical risk threshold flag | `Yes`, `No` |

---

## 🚀 Tableau Quick Start

1. Open **Tableau Desktop** or **Tableau Public**.
2. Connect to [chronic_disease_risk_patients.csv](file:///chronic_disease_risk_patients.csv).
3. Follow the detailed calculated fields and sheet creation instructions in [TABLEAU_GUIDE.md](file:///TABLEAU_GUIDE.md).
4. Review key epidemiological findings in [INSIGHTS_SUMMARY.md](file:///INSIGHTS_SUMMARY.md).

---

## 🔬 Key Insights Summary
- **44.8%** of the cohort is categorized as **High Clinical Risk**, primarily driven by synergistic elevations in Blood Pressure ($\ge 140$ mmHg) and Glucose ($\ge 140$ mg/dL).
- Disease prevalence accelerates from **6.5%** in patients $<30$ to **58.4%** in patients aged $60+$.
- Obese patients face a **2.8x higher risk** of diabetes compared to normal-BMI counterparts.
