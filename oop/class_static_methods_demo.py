class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Returns the sum of a and b."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        cls.calculation_type = "Multiplication"
        print(f"Calculation type: {cls.calculation_type}")
        """Returns the product of a and b."""
        return a * b
