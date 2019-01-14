import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


auto = pd.read_csv('https://assets.datacamp.com/production/course_1761/datasets/auto-mpg.csv',delimiter=',')
print(auto.columns)

# Generate a joint plot of 'hp' and 'mpg'
sns.jointplot(x='hp',y='mpg',data=auto)

# Display the plot
plt.show()
