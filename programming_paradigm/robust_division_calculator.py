def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to float
        num = float(numerator)
        denom = float(denominator)

        # Perform division
        result = num / denom
        print("Division successful")
        return result

    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

    except ValueError:
        return "Error: Non-numeric input detected."
