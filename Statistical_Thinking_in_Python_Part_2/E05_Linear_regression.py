import numpy as np
import matplotlib.pyplot as plt

illiteracy = np.random.random(100)*100
fertility = np.random.random(100)

# Plot the illiteracy rate versus fertility
_ = plt.plot(illiteracy, fertility, marker='.', linestyle='none')
plt.margins(0.02)
_ = plt.xlabel('percent illiterate')
_ = plt.ylabel('fertility')

# Perform a linear regression using np.polyfit(): a, b
a, b = np.polyfit(illiteracy,fertility,1)

# Print the results to the screen
print('slope =', a, 'children per woman / percent illiterate')
print('intercept =', b, 'children per woman')

# Make theoretical line to plot
x = np.array([0,100])
y = x * a + b

# Add regression line to your plot
_ = plt.plot(x, y)

# Draw the plot
plt.show()
