# Import package
import numpy as np
from matplotlib import pyplot as plt
# Assign filename to variable: file
file = '/Volumes/Data/Dropbox/Python3/git/Datacamp/ImportingDataPython1/mnist_kaggle_some_rows.csv'

# Load file as array: digits
digits = np.loadtxt(file, delimiter=',')

# Print datatype of digits
print(type(digits))

# Select and reshape a row
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))

# Plot reshaped data (matplotlib.pyplot already loaded as plt)
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()
