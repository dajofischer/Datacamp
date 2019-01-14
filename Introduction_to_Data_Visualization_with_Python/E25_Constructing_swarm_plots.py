import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


auto = pd.read_csv('https://assets.datacamp.com/production/course_1761/datasets/auto-mpg.csv',delimiter=',')
print(auto.columns)

# Make a strip plot of 'hp' grouped by 'cyl'
plt.subplot(2,1,1)
sns.swarmplot(x='cyl', y='hp', data=auto, hue='cyl')

# Make the strip plot again using jitter and a smaller point size
plt.subplot(2,1,2)
sns.swarmplot(x='hp', y='cyl', data=auto, hue='origin',orient='h')

# Display the plot
plt.show()
