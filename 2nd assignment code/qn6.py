def divided_difference_table(x_values, y_values):
    """
    Compute the divided difference table.

    Parameters:
    x_values: list of x-coordinates (data points)
    y_values: list of y-coordinates (corresponding data points)

    Returns:
    Divided difference table as a 2D list.
    """
    n = len(x_values)
    table = [[0] * n for _ in range(n)]

    # Initialize the first column with y_values
    for i in range(n):
        table[i][0] = y_values[i]

    # Fill the divided difference table
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x_values[i + j] - x_values[i])

    return table

def newton_polynomial(x_values, table, x):
    """
    Estimate f(x) using Newton's divided difference method.

    Parameters:
    x_values: list of x-coordinates (data points)
    table: divided difference table
    x: the x-coordinate at which to interpolate

    Returns:
    Estimated value of f(x).
    """
    n = len(x_values)
    result = table[0][0]
    product = 1

    for i in range(1, n):
        product *= (x - x_values[i - 1])
        result += table[0][i] * product

    return result

# Given data points
x_values = [3.2, 2.7, 1.0, 4.8, 5.6]
y_values = [22.0, 17.8, 14.2, 38.3, 51.7]

# Compute the divided difference table
diff_table = divided_difference_table(x_values, y_values)

# Print the divided difference table
print("Divided Difference Table:")
for row in diff_table:
    print([round(value, 4) for value in row if value != 0])

# Estimate f(x) at x = 2 and x = 5
x_to_estimate = [2, 5]
for x in x_to_estimate:
    f_x = newton_polynomial(x_values, diff_table, x)
    print(f"The estimated value of f({x}) is {round(f_x, 4)}")
