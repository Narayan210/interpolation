# Define the function f(x)
def f(x):
    return x**3 - x + 1

# Divided Difference Formula to calculate the approximate value of f(x) at a given point
def divided_difference(x_values, f_values, x):
    n = len(x_values)
    # Create a table to store the divided differences
    diff_table = [f_values]
    
    # Compute the divided differences
    for j in range(1, n):
        diff_row = []
        for i in range(n - j):
            diff_value = (diff_table[j-1][i+1] - diff_table[j-1][i]) / (x_values[i+j] - x_values[i])
            diff_row.append(diff_value)
        diff_table.append(diff_row)
    
    # Calculate the approximation of f(x) using the divided differences
    result = diff_table[0][0]
    product_term = 1
    for j in range(1, n):
        product_term *= (x - x_values[j-1])
        result += product_term * diff_table[j][0]
    
    return result

# Initial points
x1 = 2
x2 = 4
x_values = [x1, x2]
f_values = [f(x1), f(x2)]

# Step size and target point x = 3.8
h = 0.5
x_target = 3.8

# Approximate f(3.8) using the divided difference method
f_approx = divided_difference(x_values, f_values, x_target)

print(f"f(3.8) ≈ {f_approx}")
