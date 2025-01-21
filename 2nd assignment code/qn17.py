import numpy as np
import matplotlib.pyplot as plt

def fit_exponential_curve(x, y):
    # Take the natural logarithm of y
    ln_y = np.log(y)

    # Perform linear regression
    n = len(x)
    sum_x = np.sum(x)
    sum_ln_y = np.sum(ln_y)
    sum_x_ln_y = np.sum(x * ln_y)
    sum_x2 = np.sum(x**2)

    # Calculate coefficients b and ln(a)
    b = (n * sum_x_ln_y - sum_x * sum_ln_y) / (n * sum_x2 - sum_x**2)
    ln_a = (sum_ln_y - b * sum_x) / n

    # Convert ln(a) to a
    a = np.exp(ln_a)

    return a, b

# Given data
x = np.array([1, 2, 3, 4])
y = np.array([1.65, 2.70, 4.50, 7.35])

# Fit the curve
a, b = fit_exponential_curve(x, y)

print(f"The fitted curve is: y = {a:.4f}e^({b:.4f}x)")

# Plot the data and the fitted curve
x_fit = np.linspace(min(x), max(x), 100)
y_fit = a * np.exp(b * x_fit)

plt.scatter(x, y, color='red', label='Data Points')
plt.plot(x_fit, y_fit, label=f'Fitted Curve: y = {a:.4f}e^({b:.4f}x)', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Exponential Curve Fitting')
plt.show()
