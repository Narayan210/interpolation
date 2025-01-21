import numpy as np

# Given data points
x_values = np.array([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
y_values = np.array([2.7, 4.0, 5.8, 8.3, 11.2, 15.0, 19.0])

# Calculate the necessary sums for the normal equations
n = len(x_values)

sum_x2 = np.sum(x_values**2)
sum_x3 = np.sum(x_values**3)
sum_x4 = np.sum(x_values**4)
sum_x = np.sum(x_values)
sum_y = np.sum(y_values)
sum_yx = np.sum(y_values * x_values)
sum_yx2 = np.sum(y_values * x_values**2)

# Create the coefficient matrix and the right-hand side vector
A = np.array([[sum_x4, sum_x3, sum_x2],
              [sum_x3, sum_x2, sum_x],
              [sum_x2, sum_x, n]])

B = np.array([sum_yx2, sum_yx, sum_y])

# Solve for the coefficients a, b, and c
coefficients = np.linalg.solve(A, B)

# Output the result
a, b, c = coefficients
print(f"The quadratic function is: y = {a:.2f}x^2 + {b:.2f}x + {c:.2f}")
