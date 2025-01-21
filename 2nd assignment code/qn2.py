def lagrange_interpolation(x_values, y_values, x):
    """
    Perform Lagrange interpolation to find the value of y at a given x.

    Parameters:
    x_values: list of x-coordinates (data points)
    y_values: list of y-coordinates (corresponding data points)
    x: the x-coordinate at which to interpolate

    Returns:
    Interpolated y value at x
    """
    n = len(x_values)
    result = 0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result

# Given data points
x_values = [-2, 1, 3, 7]
y_values = [5, 7, 11, 34]

# Value of x at which we want to find y
x = 0

# Calculate the interpolated y value
y_at_x = lagrange_interpolation(x_values, y_values, x)
print(f"The interpolated value of y at x={x} is {y_at_x}")
