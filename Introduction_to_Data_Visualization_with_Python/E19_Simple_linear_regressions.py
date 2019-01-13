import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

sns.lmplot(x='total_bill',y='tip',data=tips)

plt.show()



df = pd.read_csv('https://assets.datacamp.com/production/course_1761/datasets/auto-mpg.csv',delimiter=',')
print(df.columns)

weight=df.loc[:,'weight'].values
hp=df.loc[:,'hp'].values

sns.lmplot(x='weight', y='hp', data=df)

# Display the plot
plt.show()
