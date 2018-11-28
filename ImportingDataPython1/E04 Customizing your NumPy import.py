# Import numpy
import numpy as np

# Assign the filename: file
#file = 'digits_header.txt'
file = '/Volumes/Data/Dropbox/Python3/git/Datacamp/ImportingDataPython1/seaslug.txt'

# Load the data: data
data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0])

# Print data
print(data)
