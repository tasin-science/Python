#### Numpy Simple Math ####

import numpy as np

a = np.array([[1,2],[3,4]], dtype = np.float64)
b = np.array([[5,6],[7,8]], dtype = np.float64)
c = np.array([[4,9],[16,25]])

### using  arithmetic symbols (+ - * /)
print("Using arithmetic symbols (+ - * /)")
print(a + b, "\n")
print(a - b, "\n")
print(a * b, "\n")
print(a / b, "\n")
print("\n")

#### using arithmetic function
print("Using arithmetic function")
print(np.add(a, b), "\n")
print(np.subtract(a, b), "\n")
print(np.multiply(a, b), "\n")
print(np.divide(a, b), "\n")
print("\n")

### square root function
print("square root of c")
print(np.sqrt(c), "\n")