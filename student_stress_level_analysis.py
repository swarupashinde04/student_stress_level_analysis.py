def calculate_stress(study_hours, sleep_hours, assignments_per_week, exam_days_left):
    """
    Calculates student stress level based on academic and lifestyle factors
    """

    stress_score = 0

    # Study hours impact
    if study_hours > 8:
        stress_score += 30
    elif study_hours > 5:
        stress_score += 20
    else:
        stress_score += 10

    # Sleep hours impact
    if sleep_hours < 6:
        stress_score += 30
    elif sleep_hours < 8:
        stress_score += 20
    else:
        stress_score += 10

    # Assignment load impact
    if assignments_per_week >= 5:
        stress_score += 25
    elif assignments_per_week >= 3:
        stress_score += 15
    else:
        stress_score += 5

    # Exam proximity impact
    if exam_days_left <= 7:
        stress_score += 25
    elif exam_days_left <= 15:
        stress_score += 15
    else:
        stress_score += 5

    # Risk classification
    if stress_score >= 80:
        risk = "HIGH STRESS"
        advice = "Immediate rest, better time management, and reduced workload recommended."
    elif stress_score >= 50:
        risk = "MODERATE STRESS"
        advice = "Balance study with rest and monitor workload."
    else:
        risk = "LOW STRESS"
        advice = "Stress levels are manageable. Maintain current routine."

    return stress_score, risk, advice


# -------- USER INPUT --------
study_hours = int(input("Enter daily study hours: "))
sleep_hours = int(input("Enter daily sleep hours: "))
assignments = int(input("Assignments per week: "))
exam_days = int(input("Days left for next exam: "))

score, risk_level, recommendation = calculate_stress(
    study_hours, sleep_hours, assignments, exam_days
)

print("\n--- Student Stress Analysis Report ---")
print(f"Stress Score      : {score}")
print(f"Stress Level      : {risk_level}")
print(f"Recommendation    : {recommendation}")
