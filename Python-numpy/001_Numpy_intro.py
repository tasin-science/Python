#### numpy

import numpy as np

# create a Python list of temperature in degree celcius
cvalues = [20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9,
20.1]
# converting this list into one-dimensional Numpy array
C = np.array(cvalues)
print(cvalues)
print(type(cvalues))
print(C)
print(type(C))