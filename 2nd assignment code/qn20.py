import numpy as np

# Given data points
x_values = np.array([5, 6, 9, 11])
y_values = np.array([12, 13, 14, 16])

# Function to compute the Lagrange polynomial at a given x
def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)
    result = 0.0
    
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    return result

# Estimate y(10) using the Lagrange interpolation polynomial
x_to_estimate = 10
y_at_10 = lagrange_interpolation(x_values, y_values, x_to_estimate)

print(f"The value of y at x = {x_to_estimate} is: {y_at_10:.4f}")
