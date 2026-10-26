# Tableau Implementation Guide: Chronic Disease Risk Dashboard

This guide provides step-by-step instructions, calculated field formulas, and visual specifications across all 8 Epics and 14 Tasks defined in the project build spec.

---

## Epic 1 & 2: Data Import & Field Configuration

### 1. Data Connection
1. Launch **Tableau Desktop** or **Tableau Public**.
2. Under **Connect** > **To a File**, select **Text file**.
3. Select `chronic_disease_risk_patients.csv`.

### 2. Verify Data Types & Roles
Ensure fields are assigned appropriate types:
- **Dimensions (Categorical / Discrete):**
  - `PatientID` (String)
  - `Gender` (String)
  - `BMICategory` (String: Underweight, Normal, Overweight, Obese)
  - `AgeGroup` (String: <30, 30-44, 45-59, 60+)
  - `Smoking` (String: Yes / No)
  - `Alcohol` (String: None, Moderate, Heavy)
  - `ExerciseLevel` (String: Low, Moderate, High)
  - `Fatigue`, `ChestPain`, `Dizziness` (String: Yes / No)
  - `Disease` (String: None, Heart disease, Diabetes, Stroke)
  - `HighRisk` (String: Yes / No)
- **Measures (Continuous / Quantitative):**
  - `Age` (Number Whole)
  - `BMI` (Number Decimal)
  - `BloodPressure` (Number Whole)
  - `Cholesterol` (Number Whole)
  - `Glucose` (Number Whole)

---

## Epic 3: Calculated Fields & KPI Cards

Create the following calculated fields (**Analysis** > **Create Calculated Field...**):

### Calculated Field Formulas

1. **`[Total Patients]`**
   ```tableau
   COUNTD([PatientID])
   ```

2. **`[High Risk Patient Count]`**
   ```tableau
   COUNTD(IF [HighRisk] = 'Yes' THEN [PatientID] END)
   ```

3. **`[High Risk %]`**
   ```tableau
   [High Risk Patient Count] / [Total Patients]
   ```
   *(Right-click field > Default Properties > Number Format > Percentage, 1 decimal)*

4. **`[Disease Patient Count]`**
   ```tableau
   COUNTD(IF [Disease] != 'None' THEN [PatientID] END)
   ```

5. **`[Disease Prevalence %]`**
   ```tableau
   [Disease Patient Count] / [Total Patients]
   ```
   *(Format as Percentage, 1 decimal)*

6. **`[Avg BMI]`**
   ```tableau
   AVG([BMI])
   ```
   *(Format as Number, 1 decimal)*

7. **`[Avg Blood Pressure]`**
   ```tableau
   AVG([BloodPressure])
   ```
   *(Format as Number, 0 decimals, unit: mmHg)*

### Sheet 1: KPI Summary Cards
- Drag **Measure Values** to **Text** on Marks Card.
- Keep only: `[Total Patients]`, `[High Risk %]`, `[Disease Prevalence %]`, `[Avg BMI]`, `[Avg Blood Pressure]`.
- Place **Measure Names** on **Columns**.
- Format Marks as Large Bold KPI cards (Font Size 20pt for numbers, 10pt grey for labels).

---

## Epic 4: Disease Prevalence

### Sheet 2: Disease Prevalence by Age Group
- **Rows:** `[AgeGroup]` (Sort order: `<30`, `30-44`, `45-59`, `60+`)
- **Columns:** `[Disease Prevalence %]` (or `COUNTD([PatientID])`)
- **Color:** `[Disease]`
  - Palette: Heart Disease (Dark Red / Crimson), Diabetes (Amber / Orange), Stroke (Purple), None (Muted Grey).
- **Marks:** Horizontal Stacked Bar Chart.
- **Labels:** Check "Show mark labels" (Percentage of Total).

### Sheet 3: Disease Prevalence by BMI Category
- **Columns:** `[BMICategory]` (Sort: `Underweight`, `Normal`, `Overweight`, `Obese`)
- **Rows:** `[Disease Prevalence %]`
- **Color:** `[Disease]`
- **Marks:** Stacked Column Bar Chart.
- **Tooltip:** Include Patient Count, Category %, and Avg Glucose.

---

## Epic 5: Risk Factor Analysis

### Sheet 4: Clinical Vitals Heatmap (BP, Cholesterol, Glucose vs Disease)
- **Rows:** `[Disease]`
- **Columns:** `Measure Names` (Filtered to: `AVG(BloodPressure)`, `AVG(Cholesterol)`, `AVG(Glucose)`)
- **Marks:** Square.
- **Color:** `Measure Values` with **Use Separate Legends** enabled:
  - Avg BP: Sequential Orange-Red (Normal ~120 to High ~155)
  - Avg Cholesterol: Sequential Red (Normal ~180 to High ~230)
  - Avg Glucose: Sequential Red (Normal ~90 to High ~145)
- **Label:** `Measure Values` centered inside each square.

### Sheet 5: Lifestyle Determinants Comparison
- **Rows:** `[Disease]`
- **Columns:** `[ExerciseLevel]` (or `[Smoking]`, `[Alcohol]`)
- **Marks:** Side-by-side Bar chart comparing patient distribution.
- **Filter/Dimension:** Add parameter or container toggle for Lifestyle Factor.

---

## Epic 6: Symptoms & Patient Clinical Table

### Sheet 7: Symptom Prevalence
- Create calculated fields for symptom counts:
  - `Chest Pain %`: `COUNTD(IF [ChestPain] = 'Yes' THEN [PatientID] END) / [Total Patients]`
  - `Fatigue %`: `COUNTD(IF [Fatigue] = 'Yes' THEN [PatientID] END) / [Total Patients]`
  - `Dizziness %`: `COUNTD(IF [Dizziness] = 'Yes' THEN [PatientID] END) / [Total Patients]`
- **Rows:** Measure Names
- **Columns:** Measure Values
- **Marks:** Bar chart with highlight color on High-Risk segments.

### Sheet 8: High-Risk Patient Registry (Sortable Table)
- **Rows:** `[PatientID]`, `[Age]`, `[Gender]`, `[BMI]`, `[BloodPressure]`, `[Cholesterol]`, `[Glucose]`, `[Disease]`, `[HighRisk]`
- **Filter:** `[HighRisk]` = `Yes`
- **Color Mark:** Flag red icon or red text on `[BloodPressure] >= 140` or `[Glucose] >= 140`.
- **Sorting:** Default descending by `[BloodPressure]` or `[Age]`.

---

## Epic 7: Persona-Driven Dashboards

### Dashboard 1: Clinical Risk Officer (Dr. Michael Carter)
*Focus: Immediate risk detection, critical vitals, patient triage.*
- **Top:** 5 KPI Cards (`Total Patients`, `High Risk %`, `Disease Prevalence %`, `Avg BP`, `Avg BMI`).
- **Middle Left:** High-Risk Patient Registry (Sortable, actionable list).
- **Middle Right:** Clinical Vitals Heatmap (BP, Cholesterol, Glucose by Disease).
- **Filters (Top Bar):** `Disease`, `AgeGroup`, `BMICategory`.

### Dashboard 2: Lifestyle Analysis (Emily Rodriguez)
*Focus: Behavioral risk factors, preventive health patterns.*
- **Top:** Lifestyle KPI split (Smoking %, Sedentary %, Alcohol distribution).
- **Main Left:** Lifestyle Factor vs Disease Prevalence bars.
- **Main Right:** Exercise Level vs Glucose and BP correlation scatter/bars.
- **Bottom:** Symptoms by Lifestyle habits.

### Dashboard 3: Population Health (Dr. Priya Nair)
*Focus: Demographic stratification, resource planning, epidemiology.*
- **Top:** Population Overview and Age-stratified Prevalence.
- **Left:** Disease Prevalence by Age Group (`<30` to `60+`).
- **Right:** BMI Distribution vs Chronic Disease onset.
- **Bottom:** Symptom cluster radar / bar breakdown.

---

## Epic 8: Shared Filters, Actions & Publishing

### 1. Interactive Dashboard Actions
1. **Filter Action (Cross-filtering):**
   - Click **Dashboard** > **Actions** > **Add Action** > **Filter**.
   - Source: Disease Prevalence chart.
   - Target: All other sheets on dashboard.
   - Run on: **Select**. Clearing selection shows all values.
2. **Highlight Action:**
   - Highlight patients across charts when an Age Group or BMI category is clicked.

### 2. Publishing to Tableau Public / Cloud
1. Click **Server** > **Tableau Public** > **Save to Tableau Public...**
2. Sign in with your Tableau Public credentials.
3. Workbook name: `Chronic_Disease_Risk_Dashboard`.
4. Ensure **Allow access to data source** is checked.
5. Copy public URL and paste into the project repository README.
