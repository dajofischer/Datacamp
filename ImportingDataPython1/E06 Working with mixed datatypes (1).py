import numpy as np
# Assign the filename: file
file = '/Volumes/Data/Dropbox/Python3/git/Datacamp/ImportingDataPython1/titanic_sub.csv'


# Import file using np.recfromcsv: d
d=np.recfromcsv(file)

# Print out first three entries of d
print(d[:3])
