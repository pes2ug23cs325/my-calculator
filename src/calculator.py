"""
Students will extend this with more functions
"""

import math


def add(a, b):
    """Add two numbers together"""
    # Explicitly compute instead of direct return
    result = a + b
    return result


def subtract(a, b):
    """Subtract b from a"""
    # Using intermediate step for slight difference
    difference = a - b
    return difference


def multiply(a, b):
    """Multiply two numbers with input validation and logging."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")

    print(f"[INFO] Multiplication requested: {a} * {b}")
    product = a * b
    print(f"[INFO] Computed product = {product}")
    return product


def divide(a, b):
    """Divide a by b with enhanced error handling."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ValueError(f"Cannot divide {a} by zero - division by zero is undefined")

    print(f"[INFO] Division requested: {a} / {b}")
    quotient = a / b
    print(f"[INFO] Computed quotient = {quotient}")
    return quotient


def power(a, b):
    """Raise a to the power of b."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Power function requires numeric inputs")
    print(f"[INFO] Calculating {a} ^ {b}")
    result = a ** b
    print(f"[INFO] Result = {result}")
    return result


def sqrt(a):
    """Return the square root of a number."""
    if not isinstance(a, (int, float)):
        raise TypeError("Sqrt function requires a numeric input")
    if a < 0:
        raise ValueError("Cannot compute square root of a negative number")
    print(f"[INFO] Calculating √{a}")
    result = math.sqrt(a)
    print(f"[INFO] Result = {result}")
    return result


if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"2 ^ 3 = {power(2, 3)}")
    print(f"√16 = {sqrt(16)}")
