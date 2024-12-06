#### Numpy Simple Math ####

import numpy as np

a = np.array([[1,2],[3,4]], dtype = np.float64)
b = np.array([[5,6],[7,8]], dtype = np.float64)

### using  arithmetic symbols (+ - * /)
print(a + b, "\n")
print(a - b, "\n")
print(a * b, "\n")
print(a / b, "\n")


#### using arithmetic function
print(np.add(a, b), "\n")
print(np.subtract(a, b), "\n")
print(np.multiply(a, b), "\n")
print(np.divide(a, b), "\n")
