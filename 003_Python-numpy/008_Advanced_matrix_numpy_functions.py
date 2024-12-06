#### Advanced matrix numpy functions ####

import numpy as np


### zeros function
# zeros function creates zero matrix
print("5x5 zero matrix: \n", np.zeros(5), "\n")
print("2x3 zero matrix: \n", np.zeros((2,3)), "\n")


### random.rand function
# this function creates matrix with random values
print("random matrix: \n", np.random.rand(3,4), "\n")


### full function
# this function creates matrix filled with specific value. 
# structure: full((row, column), specific_value)
print("this matrix's all elements are only 8: \n", np.full((3,4), 8), "\n")


### eye function
# this function creates identity matrix
print("this is identity matrix: \n", np.eye(3), "\n")


### arange function 
# this function creates one row matrix with start stop step
# structure: arange(start, stop, step)
print("this is arange matrix with start=1, stop=10, step=2: \n", np.arange(1,10,2), "\n")


### linspace function
# this function creates one row matrix with evenly spaced values between two limits.
# structure: linspace(start, stop, num)
print("This is linspace matrix: \n", np.linspace(0,10,2), "\n")



# now let's fun, think what will happen if we go 0 to 1 by 1000 steps?
print(np.arange(0,1,1000))