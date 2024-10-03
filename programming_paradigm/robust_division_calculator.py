# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Performs division while handling errors for division by zero and non-numeric inputs."""
    try:
        # Convert inputs to float for division
        numerator = float(numerator)
        denominator = float(denominator)

        # Attempt division
        result = numerator / denominator
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
