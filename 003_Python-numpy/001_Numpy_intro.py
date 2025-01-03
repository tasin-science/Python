#### numpy

import numpy as np

# create a Python list of temperature in degree celcius
print("//Basic of numpy array//")
print("This is the numpy program of temperature converter. here C list contains celcius temperatures")
cvalues = [20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1]
# converting this list into one-dimensional Numpy array
C = np.array(cvalues)
print("C value list: ", cvalues)
print("The type of c value list is: ", type(cvalues), "\n")
print("Celcius numpy array: ", C)
print( "The type of Celcius numpy array is: ", type(C), "\n")
F = C * 9/5 + 32
print("Farenheit numpy array: ", F)
print("\n\n\n")



### Converting numpy array as normal list
print("We want to make farenheit numpy array ", F, " as farenheit temperature list")
Far_list = F.tolist()
print("Farenheit temperature list is: ", Far_list)
print("\n\n\n")



### Matrix/2D list to matrix numpy
print("//Two dimension//")
m_list = [[1,2],[3,4]]
print("Two dimension list is: ", m_list)
M = np.array(m_list)
print("The numpy matrix of that two dimension list is:\n", M)
print("\n\n\n")


### data types of numpy array
print("//data types of numpy array// \n")
B1 = np.array([1, 2, 3, 4])
print("B1 numpy array is: ", B1)
print("Data types of B1 is: ", B1.dtype)
print("\n")
#<>
B2 = np.array([1.0, 2.0, 3.0, 4.0])
print("B2 numpy array is: ", B2)
print("Data types of B2 is: ", B2.dtype)
print("\n")
#<>
B3 = np.array([1+2j, 2+4j, 3+5.6j, 4+11j])
print("B3 numpy array is: ", B3)
print("Data types of B3 is: ", B3.dtype)
print("\n")
#<>
B4 = np.array([True, False, True, True, False, True])
print("B4 numpy array is: ", B4)
print("Data types of B4 is: ", B4.dtype)
print("\n")
#<>
B5 = np.array(['a', 'b', 'c', 'd'])
print("B5 numpy array is: ", B5)
print("Data types of B5 is: ", B5.dtype)
print("\n\n\n")






### data type system using in numpy array
print("//data type system using in numpy array// \n")
A1 = np.array([1, 2, 3, 4])
print("A1 numpy array is: ", A1)
print("data type of A1 is: ", A1.dtype)
print("\n")
#<>
A2 = np.array([1, 2, 3, 4], dtype = np.float64)
print("A2 numpy array is: ", A2)
print("data type of A2 is: ", A2.dtype)
print("\n")
#<>
A3 = np.array([1, 2, 3, 4], dtype = np.complex128)
print("A3 numpy array is: ", A3)
print("data type of A3 is: ", A3.dtype)
print("\n")
#<>
A4 = np.array([1, 2, 3, 4], dtype = np.bool_)
print("A4 numpy array is: ", A4)
print("data type of A4 is: ", A4.dtype)
print("\n")
#<>
A5 = np.array([1, 2, 3, 4], dtype = np.str_)
print("A5 numpy array is: ", A5)
print("data type of A5 is: ", A5.dtype)
