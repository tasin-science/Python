#### Broadcasting ####

import numpy as np

x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
v = np.array([1,0,1])
# Here we want that we will add vector v to each row of matrix x.



### Using empty_like function
y = np.empty_like(x)
print("empty_like(x) is: \n", y, "\n")
for i in range(4):
    y[i, :] = x[i, :] + v
print("in empty_like manner: \n", y, "\n")
print("\n")

### Using tile function
z = np.tile(v, (4,1))
print("tile(v, (4,1)) is: \n", z, "\n")
q = x + z
print("in tile manner: \n", q, "\n")
print("\n")


### Using Broadcasting
p = x + v
print("in Broadcast manner: \n", p, "\n")