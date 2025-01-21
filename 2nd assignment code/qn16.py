import numpy as np

def newton_forward_difference(x, y, value):
    n = len(x)
    # Create the forward difference table
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y  # First column is y values

    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = diff_table[i + 1][j - 1] - diff_table[i][j - 1]

    # Display the forward difference table
    print("Forward Difference Table:")
    for i in range(n):
        print(diff_table[i, :n - i])

    # Calculate the interpolation result
    h = x[1] - x[0]  # Assuming uniform spacing
    u = (value - x[0]) / h

    result = diff_table[0, 0]
    term = 1
    for i in range(1, n):
        term *= (u - (i - 1)) / i
        result += term * diff_table[0, i]

    return result

# Given data
x = np.array([10, 20, 30, 40, 50])
y = np.array([0.173, 0.342, 0.5, 0.643, 0.766])
value = 15

# Calculate the value of f(x) at x = 15
result = newton_forward_difference(x, y, value)
print(f"The value of f({value}) is approximately {result:.6f}")
