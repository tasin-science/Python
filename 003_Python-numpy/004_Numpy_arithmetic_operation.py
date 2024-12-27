#### Numpy Arithmetic Operation ####

import numpy as np

a = np.array([[1,2],[3,4]], dtype = np.float64)
b = np.array([[5,6],[7,8]], dtype = np.float64)
c = np.array([[4,9],[16,25]])

print("Matrix a is: \n", a, "\n")
print("Matrix b is: \n", b, "\n")
print("Matrix c is: \n", c, "\n")
print("\n\n")


### using  arithmetic symbols (+ - * /)
print("Using arithmetic symbols (+ - * /) \n")
print("a + b: \n", a + b, "\n") # matrix a + matrix b 
print("a - b: \n", a - b, "\n") # matrix a - matrix b
print("a * b: \n", a * b, "\n") # matrix a * matrix b
print("a / b: \n", a / b, "\n") # matrix a / matrix b
print("\n\n")



#### using arithmetic function
print("Using arithmetic function \n")
print("add(a, b) = a + b \n", np.add(a, b), "\n")  
print("subtract(a, b) = a - b \n", np.subtract(a, b), "\n")  
print("multiply(a, b) = a * b \n", np.multiply(a, b), "\n")  
print("divide(a, b) = a / b \n", np.divide(a, b), "\n") 
print("\n")


### square root function
print("square root of c: \n")
print(np.sqrt(c), "\n")