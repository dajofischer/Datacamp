import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('https://assets.datacamp.com/production/course_1761/datasets/auto-mpg.csv',delimiter=',')
print(df.columns)

# Import plotting modules


# Generate a green residual plot of the regression between 'hp' and 'mpg'
sns.residplot(x='hp', y='mpg', data=df, color='green')

# Display the plot
plt.show()
