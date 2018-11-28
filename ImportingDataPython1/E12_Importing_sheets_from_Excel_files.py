import pandas as pd

file = '/Volumes/Data/Dropbox/Python3/git/Datacamp/ImportingDataPython1/'
file = file+'battledeath.xlsx'

xl = pd.ExcelFile(file)


# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('2004')

# Print the head of the DataFrame df1
print(df1.head())

# Load a sheet into a DataFrame by index: df2
df2 = xl.parse('2002')

# Print the head of the DataFrame df2
print(df2.head())
