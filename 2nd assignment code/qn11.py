import math

# Given data points
x_values = [10, 20, 30, 40, 50]
f_values = [0.985, 0.934, 0.866, 0.766, 0.643]

# Function to calculate backward differences
def backward_differences(x_values, f_values):
    n = len(f_values)
    diff_table = [f_values]
    
    # Create the backward difference table
    for i in range(1, n):
        new_diff_row = []
        for j in range(n - i):
            diff_value = diff_table[i - 1][j] - diff_table[i - 1][j + 1]
            new_diff_row.append(diff_value)
        diff_table.append(new_diff_row)
    
    return diff_table

# Newton's backward difference formula
def newtons_backward_interpolation(x_values, f_values, x_target):
    n = len(f_values)
    diff_table = backward_differences(x_values, f_values)
    
    # h is the difference between consecutive x-values
    h = x_values[1] - x_values[0]
    
    # Find the index of x_target in the x_values list
    x_n = x_values[-1]
    index = n - 1
    
    # Calculate the difference (x - x_n) / h
    term = (x_target - x_n) / h
    result = f_values[-1]
    
    # Use the backward differences to calculate the interpolation value
    for i in range(1, n):
        term *= (x_target - x_values[-(i + 1)]) / h
        result += term * diff_table[i][0] / math.factorial(i)
    
    return result

# Target point x = 45
x_target = 45

# Approximate f(45) using Newton's backward interpolation
f_approx = newtons_backward_interpolation(x_values, f_values, x_target)

# Print the result
print(f"f(45) ≈ {f_approx}")
