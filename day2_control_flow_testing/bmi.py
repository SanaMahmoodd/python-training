def bmi_calculator(height: float, weight: float) -> float:
    """
    Calculate BMI using metric units.
    height: meters
    weight: kilograms
    """
    if isinstance(height, bool) or isinstance(weight, bool):
        raise TypeError("Bool is not a valid input")

    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a number")

    if not isinstance(weight, (int, float)):
        raise TypeError("Weight must be a number")

    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be positive")

    bmi = weight / (height ** 2)
    return round(bmi, 2)
