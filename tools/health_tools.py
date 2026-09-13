from agents import function_tool


@function_tool
def calculate_bmi(weight_kg: float, height_m: float) -> str:
    """
    Calculate BMI from weight in kilograms and height in meters.
    """

    if weight_kg <= 0:
        return "Weight must be greater than 0."

    if height_m <= 0:
        return "Height must be greater than 0."

    bmi = weight_kg / (height_m ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obesity"

    return f"BMI: {bmi:.2f}. Category: {category}."


@function_tool
def log_symptom(
    symptom: str,
    severity: int,
    duration: str,
) -> str:
    """
    Record a symptom provided by the user.
    """

    if severity < 1 or severity > 10:
        return "Severity must be between 1 and 10."

    return (
        f"Symptom recorded: {symptom}. "
        f"Severity: {severity}/10. "
        f"Duration: {duration}."
    )