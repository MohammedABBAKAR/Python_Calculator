# Simple OOP Calculator
# Create methods for the Calculator class that can do the following:

# Add two numbers.
# Subtract two numbers.
# Multiply two numbers.
# Divide two numbers.
# Examples
# calculator = Calculator()

# calculator.add(10, 5) ➞ 15

# calculator.subtract(10, 5) ➞ 5

# calculator.multiply(10, 5) ➞ 50

# calculator.divide(10, 5) ➞ 2
# Notes
# The methods should return the result of the calculation.
# Don't worry about needing to handle division by zero errors.
# See the Resources tab for some helpful tutorials on Python classes.

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

# Example usage:
calculator = Calculator(10, 5)
print(calculator.add())        # Output: 15
print(calculator.subtract())   # Output: 5
print(calculator.multiply())   # Output: 50
print(calculator.divide())     # Output: 2.0
