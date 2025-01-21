import numpy as np

# Given data points
x_values = np.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4])
y_values = np.array([2.0, 2.6, 3.9, 6.0, 9.3, 15.0, 20.6, 30.4])

# Calculate the necessary sums for the normal equations
n = len(x_values)

sum_x = np.sum(x_values)
sum_y = np.sum(y_values)
sum_xx = np.sum(x_values**2)
sum_xy = np.sum(x_values * y_values)

# Create the coefficient matrix and the right-hand side vector
A = np.array([[sum_xx, sum_x],
              [sum_x, n]])

B = np.array([sum_xy, sum_y])

# Solve for the coefficients m (slope) and c (intercept)
coefficients = np.linalg.solve(A, B)

# Output the result
m, c = coefficients
print(f"The linear function is: y = {m:.2f}x + {c:.2f}")
