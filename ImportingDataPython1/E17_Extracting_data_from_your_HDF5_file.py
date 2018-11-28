# Import packages
import numpy as np
import h5py
import matplotlib.pyplot as plt
# Assign filename: file
file = 'LIGO_data.hdf5'
file = '/Volumes/Data/Dropbox/Python3/git/Datacamp/ImportingDataPython1/'
file = file+'L-L1_LOSC_4_V1-1126259446-32.hdf5'
# Load file: data
data = h5py.File(file, 'r')

# Get the HDF5 group: group
group = data['strain']

# Check out keys of group
for key in group.keys():
    print(key)

# Set variable equal to time series data: strain
strain = group['Strain'].value

# Set number of time points to sample: num_samples
num_samples = 10000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()
