import numpy as np
import random
import matplotlib.pyplot as plt

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y

test=np.random.random(size=100)
print(ecdf(data=test))
x,y=ecdf(test)

plt.scatter(x,y)
plt.show()
