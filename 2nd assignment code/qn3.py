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
x_values = [1, 5, 7, 9]
y_values = [80, 95, 105, 125]

# Values of x at which we want to find y
x_values_to_find = [13, 15]

# Calculate and print the interpolated y values
for x in x_values_to_find:
    y_at_x = lagrange_interpolation(x_values, y_values, x)
    print(f"The interpolated value of y (height) at age {x} is {y_at_x} cm")
