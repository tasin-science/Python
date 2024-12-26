#### numpy

import numpy as np

# create a Python list of temperature in degree celcius
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

### Converting numpy array as normal list4
print("We want to make farenheit numpy array ", F, " as farenheit temperature list")
Far_list = list(F)
print("Farenheit temperature list is: ", Far_list)
