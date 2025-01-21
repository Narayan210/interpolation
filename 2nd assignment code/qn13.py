import numpy as np
from scipy.interpolate import CubicSpline

# Given data points
x_values = np.array([-1, 1, 2, 3])
y_values = np.array([-10, -2, 14, 86])

# Create a cubic spline interpolator
cs = CubicSpline(x_values, y_values)

# Estimate f(0) and f(4) using the cubic spline
f_0 = cs(0)
f_4 = cs(4)

# Output the results
print(f"f(0) ≈ {f_0:.2f}")
print(f"f(4) ≈ {f_4:.2f}")