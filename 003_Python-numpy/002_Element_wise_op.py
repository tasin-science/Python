#### Element wise operation

import numpy as np

A = np.array([[1,2,3],[4,5,6]])
print(A)
print(A.shape)
B = np.array([[7,8,9],[10,11,12]])
print(B)
print(B.shape)
C = A + B
print(C)
print(C.shape)