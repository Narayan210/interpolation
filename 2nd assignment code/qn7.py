def forward_difference_table(x_values, y_values):
    """
    Compute the forward difference table.

    Parameters:
    x_values: list of x-coordinates (data points)
    y_values: list of y-coordinates (corresponding data points)

    Returns:
    Forward difference table as a 2D list.
    """
    n = len(y_values)
    table = [y_values]

    for i in range(1, n):
        differences = [table[i - 1][j + 1] - table[i - 1][j] for j in range(n - i)]
        table.append(differences)

    return table

def newton_forward_interpolation(x_values, y_values, x):
    """
    Estimate f(x) using Newton's Forward Difference Formula.

    Parameters:
    x_values: list of x-coordinates (data points)
    y_values: list of y-coordinates (corresponding data points)
    x: the x-coordinate at which to interpolate

    Returns:
    Estimated value of f(x).
    """
    table = forward_difference_table(x_values, y_values)
    h = x_values[1] - x_values[0]
    u = (x - x_values[0]) / h

    result = y_values[0]
    u_term = 1

    for i in range(1, len(table)):
        u_term *= (u - (i - 1))
        result += (u_term * table[i][0]) / factorial(i)

    return result

def newton_backward_interpolation(x_values, y_values, x):
    """
    Estimate f(x) using Newton's Backward Difference Formula.

    Parameters:
    x_values: list of x-coordinates (data points)
    y_values: list of y-coordinates (corresponding data points)
    x: the x-coordinate at which to interpolate

    Returns:
    Estimated value of f(x).
    """
    table = forward_difference_table(x_values, y_values)
    h = x_values[1] - x_values[0]
    u = (x - x_values[-1]) / h

    result = y_values[-1]
    u_term = 1

    for i in range(1, len(table)):
        u_term *= (u + (i - 1))
        result += (u_term * table[i][-1]) / factorial(i)

    return result

def factorial(n):
    """Calculate factorial of n."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Given data points
x_values = [1891, 1901, 1911, 1921, 1931]
y_values = [46, 66, 81, 93, 101]

# Estimate f(x) at x = 1895 and x = 1935
x_to_estimate = [1895, 1935]

for x in x_to_estimate:
    if x < x_values[len(x_values) // 2]:
        # Use forward interpolation for values closer to the start
        f_x = newton_forward_interpolation(x_values, y_values, x)
        print(f"Using Forward Difference Formula, the estimated value of f({x}) is {round(f_x, 4)}")
    else:
        # Use backward interpolation for values closer to the end
        f_x = newton_backward_interpolation(x_values, y_values, x)
        print(f"Using Backward Difference Formula, the estimated value of f({x}) is {round(f_x, 4)}")
