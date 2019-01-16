# Import numpy as np
import numpy as np

# Create array using np.linspace: x
x = np.linspace(0,5,100)

# Create array using np.cos: y
y = np.cos(x)

# Add circles at x and y
p.circle(x,y)

# Specify the name of the output file and show the result
output_file('numpy.html')
show(p)
