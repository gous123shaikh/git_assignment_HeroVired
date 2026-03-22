import math

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def square_root(self, x):
        return math.sqrt(x)

calculator = Calculator()

print(calculator.add(10,5))
print(calculator.subtract(10,5))
print(calculator.multiply(10,5))
print(calculator.divide(10,5))
print(calculator.square_root(25))

Updated calculator with sqrt and bug fix
