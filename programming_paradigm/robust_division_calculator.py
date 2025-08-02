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
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
