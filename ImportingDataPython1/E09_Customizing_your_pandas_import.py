# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import pandas as pd
# Assign filename: file
file = 'titanic_corrupt.txt'
file = '/Volumes/Data/Dropbox/Python3/git/Datacamp/ImportingDataPython1/titanic_sub.csv'

# Import file: data
data = pd.read_csv(file, sep='\t', comment='#', na_values='Nothing')

# Print the head of the DataFrame
print(data.head())

# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()
