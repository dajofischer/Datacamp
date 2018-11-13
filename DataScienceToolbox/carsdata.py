import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

cars=pd.read_csv('/Volumes/Data/Dropbox/Python3/git/datacamp/DataScienceToolbox/cars.csv',index_col=0)

print(cars[["cars_per_cap"]])

plt.scatter([0,1,2,3,4,5,6],cars[["cars_per_cap"]], s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=None, edgecolors=None, hold=None, data=None)
plt.show()

plt.plot([1,2,3],[4,3,2])
plt.show()

## test
plot(1,1)
