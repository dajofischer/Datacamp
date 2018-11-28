import pandas as pd
import numpy as np
# Assign the filename: file
file = 'digits.csv'
file = '/Volumes/Data/Dropbox/Python3/git/Datacamp/ImportingDataPython1/titanic_sub.csv'

# Read the first 5 rows of the file into a DataFrame: data
data = pd.read_csv(file,nrows=5,header=None)

# Build a numpy array from the DataFrame: data_array
data_array = np.array(data)

# Print the datatype of data_array to the shell
print(type(data_array))
