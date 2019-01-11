import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://assets.datacamp.com/production/course_1761/datasets/percent-bachelors-degrees-women-usa.csv',delimiter=',')
print(df.loc[:,'Year'])

year=df.loc[:,'Year'].values
computer_science=df.loc[:,'Computer Science'].values
physical_sciences=df.loc[:,'Physical Sciences'].values

print(type(year))

# Create plot axes for the first line plot
plt.axes([.05, 0.05, 0.425, 0.9])

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')

# Create plot axes for the second line plot
plt.axes([.525, .05, .425, .9])

# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')

# Display the plot
plt.show()
