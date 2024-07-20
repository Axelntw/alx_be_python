class Calculator:
    calculation_type = "Arithmetic Operations"

    def __init__(self):
        print(f"Calculation type: {self.calculation_type}")
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        cls()
        return a * b