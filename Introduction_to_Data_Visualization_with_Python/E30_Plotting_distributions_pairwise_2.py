import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


auto = pd.read_csv('https://assets.datacamp.com/production/course_1761/datasets/auto-mpg.csv',delimiter=',')
print(auto.columns)


# Print the first 5 rows of the DataFrame
print(auto.head())

# Plot the pairwise joint distributions grouped by 'origin' along with regression lines
sns.pairplot(auto.iloc[:,0:5],hue='origin',kind='reg')

# Display the plot
plt.show()
