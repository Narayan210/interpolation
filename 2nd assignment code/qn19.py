import numpy as np

# Given data points
x_values = np.array([1, 3, 5, 7, 9])
y_values = np.array([1.0, 0.891, 0.563, 0.447, 0.355])

# Take the natural logarithm of y values
log_y_values = np.log(y_values)

# Perform linear regression on x and log(y)
# The regression model is log(y) = A + Bx
n = len(x_values)

sum_x = np.sum(x_values)
sum_log_y = np.sum(log_y_values)
sum_xx = np.sum(x_values**2)
sum_x_log_y = np.sum(x_values * log_y_values)

# Create the coefficient matrix and right-hand side vector
A_matrix = np.array([[sum_xx, sum_x],
                     [sum_x, n]])

B_vector = np.array([sum_x_log_y, sum_log_y])

# Solve for the coefficients A and B
coefficients = np.linalg.solve(A_matrix, B_vector)

# Extract A and B
A, B = coefficients

# Transform A back to get 'a'
a = np.exp(A)

# Output the result
print(f"The fitted curve is: y = {a:.4f} * e^({B:.4f} * x)")
