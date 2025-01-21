import numpy as np
from scipy.interpolate import CubicSpline

# Given data points
x_values = np.array([5, 6, 9, 11])
y_values = np.array([12, 13, 14, 16])

# Create the cubic spline interpolation
cs = CubicSpline(x_values, y_values)

# Estimate y(1.5) using the cubic spline interpolation
y_at_1_5 = cs(1.5)

# Estimate y'(2) using the cubic spline derivative
y_prime_at_2 = cs.derivative()(2)

print(f"The value of y at x = 1.5 is: {y_at_1_5:.4f}")
print(f"The value of y' at x = 2 is: {y_prime_at_2:.4f}")
