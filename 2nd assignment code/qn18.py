import numpy as np

# Given data points
x_values = np.array([-1, 1.2, 2, 2.7, 3.6, 4])
y_values = np.array([1, 20, 27, 33, 41, 45])

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

# Solve for the coefficients b (slope) and a (intercept)
coefficients = np.linalg.solve(A, B)

# Output the result
b, a = coefficients
print(f"The linear function is: y = {a:.2f} + {b:.2f}x")
