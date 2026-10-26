"""
Chronic Disease Risk Dashboard - Data Generator & Cleaner
Generates a realistic 1,000-patient synthetic dataset and produces derived clinical metrics.
"""

import random
import csv

def generate_patient_data(filename="chronic_disease_risk_patients.csv", count=1000):
    random.seed(42)
    rows = []
    headers = [
        "PatientID", "Age", "Gender", "BMI", "BMICategory", "BloodPressure",
        "Cholesterol", "Glucose", "Smoking", "Alcohol", "ExerciseLevel",
        "Fatigue", "ChestPain", "Dizziness", "Disease", "HighRisk", "AgeGroup"
    ]
    rows.append(headers)

    for i in range(1, count + 1):
        pid = f"P{i:04d}"
        age = random.randint(18, 85)

        # Age Group
        if age < 30:
            age_group = "<30"
        elif age <= 44:
            age_group = "30-44"
        elif age <= 59:
            age_group = "45-59"
        else:
            age_group = "60+"

        gender = "Female" if random.random() < 0.49 else "Male"

        # BMI
        base_bmi = 21.0 + (random.random() * 12.0) + ((age - 18) * 0.08)
        bmi = round(min(45.0, max(16.5, base_bmi)), 1)

        if bmi < 18.5:
            bmi_cat = "Underweight"
        elif bmi < 25.0:
            bmi_cat = "Normal"
        elif bmi < 30.0:
            bmi_cat = "Overweight"
        else:
            bmi_cat = "Obese"

        smoking = "Yes" if random.random() < 0.22 else "No"
        
        alc_roll = random.random()
        alcohol = "None" if alc_roll < 0.50 else ("Moderate" if alc_roll < 0.85 else "Heavy")

        ex_roll = random.random()
        exercise = "Low" if ex_roll < 0.35 else ("Moderate" if ex_roll < 0.75 else "High")

        # Clinical vitals
        smoke_bp = 8 if smoking == "Yes" else 0
        bp = int(105 + (age * 0.45) + ((bmi - 22) * 0.8) + smoke_bp + (random.random() * 20 - 10))

        alc_chol = 15 if alcohol == "Heavy" else 0
        chol = int(150 + (age * 0.7) + ((bmi - 22) * 1.2) + alc_chol + (random.random() * 30 - 15))

        ex_gluc = 10 if exercise == "Low" else 0
        glucose = int(75 + (age * 0.5) + ((bmi - 22) * 1.5) + ex_gluc + (random.random() * 25 - 12))

        # Disease modeling
        smoke_risk = 0.2 if smoking == "Yes" else 0.0
        risk_score = ((age - 30) * 0.015) + ((bmi - 24) * 0.02) + ((bp - 120) * 0.01) + ((glucose - 100) * 0.01) + smoke_risk

        disease = "None"
        d_roll = random.random()
        if risk_score > 0.6:
            if d_roll < 0.32:
                disease = "Heart disease"
            elif d_roll < 0.60:
                disease = "Diabetes"
            elif d_roll < 0.78:
                disease = "Stroke"
        elif risk_score > 0.3:
            if d_roll < 0.18:
                disease = "Diabetes"
            elif d_roll < 0.30:
                disease = "Heart disease"
            elif d_roll < 0.38:
                disease = "Stroke"
        else:
            if d_roll < 0.04:
                disease = "Diabetes"
            elif d_roll < 0.07:
                disease = "Heart disease"

        # Symptoms
        fatigue_p = 0.45 if disease != "None" else (0.25 if exercise == "Low" else 0.12)
        chest_p = 0.55 if disease == "Heart disease" else (0.22 if bp > 150 else 0.05)
        dizzy_p = 0.50 if disease == "Stroke" else (0.25 if bp > 150 else 0.08)

        fatigue = "Yes" if random.random() < fatigue_p else "No"
        chest_pain = "Yes" if random.random() < chest_p else "No"
        dizziness = "Yes" if random.random() < dizzy_p else "No"

        # High risk threshold
        is_high_risk = (
            disease != "None" or
            bp >= 140 or
            chol >= 240 or
            glucose >= 140 or
            chest_pain == "Yes"
        )
        high_risk_str = "Yes" if is_high_risk else "No"

        rows.append([
            pid, age, gender, bmi, bmi_cat, bp, chol, glucose,
            smoking, alcohol, exercise, fatigue, chest_pain, dizziness,
            disease, high_risk_str, age_group
        ])

    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"Dataset generated successfully: {filename} ({count} records)")

if __name__ == "__main__":
    generate_patient_data()
