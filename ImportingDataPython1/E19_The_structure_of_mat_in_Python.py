import scipy.io
import matplotlib.pyplot as plt
import numpy as np


file = '/Volumes/Data/Dropbox/Python3/git/Datacamp/ImportingDataPython1/'
file = file+'ja_data2.mat'
mat = scipy.io.loadmat(file)

# Print the keys of the MATLAB dictionary
print(mat.keys())
# Print the type of the value corresponding to the key 'CYratioCyt'
print(type(mat['CYratioCyt']))

# Print the shape of the value corresponding to the key 'CYratioCyt'
print(np.shape(mat['CYratioCyt']))

# Subset the array and plot it
data = mat['CYratioCyt'][25, 5:]
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')
plt.show()
