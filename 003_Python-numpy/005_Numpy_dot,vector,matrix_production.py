#### Numpy Dot, Vector, Matrix Production ####

import numpy as np
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
c = np.array([9,10])
d = np.array([11,12])
# here a and b are matrix. c and d are vectors


### dot product (vector vector product)
print(c.dot(d), "\n")
print(np.dot(c, d), "\n") # it is as same as print(c.dot(d))

### matrix vector product
print(a.dot(c), "\n")
print(np.dot(a, c), "\n") # it is as same as print(a.dot(c))

### matrix matrix product
print(a.dot(b), "\n")
print(np.dot(a, b), "\n") # it is as same as print(a.dot(b))