import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


auto = pd.read_csv('https://assets.datacamp.com/production/course_1761/datasets/auto-mpg.csv',delimiter=',')
print(auto.columns)


# Generate a violin plot of 'hp' grouped horizontally by 'cyl'
plt.subplot(2,1,1)
sns.violinplot(x='cyl', y='hp', data=auto)

# Generate the same violin plot again with a color of 'lightgray' and without inner annotations
plt.subplot(2,1,2)
sns.violinplot(x='cyl', y='hp', data=auto,inner=None,color='lightgray')


# Overlay a strip plot on the violin plot
sns.stripplot(x='cyl', y='hp', data=auto, jitter=True,size=1.5)

plt.style.use('ggplot')
# Display the plot
plt.show()
