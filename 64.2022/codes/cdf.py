import matplotlib.pyplot as plt
import numpy as np

# Define the cumulative distribution function
def F(x):
    if x < 0:
        return (x/4 + 1/2)
    else:
        return 0.5


# Vectorize the function F(x)
vectorized_F = np.vectorize(F)

# Create a range of x values for the plot
x_values = np.linspace(-2, 1, 1000)
y_values = vectorized_F(x_values)

# Plot the probability denstity function (PDF)
plt.plot(x_values, y_values)
plt.text(0, 0.5, s="A")
plt.xlabel('x')
plt.ylabel('F(x)')
plt.title('Probability Density Function (PDF) of X')
plt.grid(True)
plt.savefig('../figs/figure1.png')
plt.show()