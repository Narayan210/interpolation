import numpy as np

# Given data points
x_values = np.array([1, 3, 4, 5, 6])
y_values = np.array([2, 7, 8, 7, 5])

# Fit a quadratic curve (degree 2 polynomial)
coefficients = np.polyfit(x_values, y_values, 2)

# Create the quadratic equation using the coefficients
# coefficients = [a, b, c] for the equation y = ax^2 + bx + c
a, b, c = coefficients

# Estimate the value of f(x) at x = 2
x_target = 2
y_estimate = a * x_target**2 + b * x_target + c

# Output the result
print(f"The quadratic curve is: y = {a:.2f}x^2 + {b:.2f}x + {c:.2f}")
print(f"Estimated f(2) = {y_estimate:.2f}")
