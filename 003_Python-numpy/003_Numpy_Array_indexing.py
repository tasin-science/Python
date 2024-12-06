#### Numpy array indexing ####

import numpy as np

### numpy matrix by matrix array
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])



### (row column (rxc) typing show)
b_n_n = a[:,:] # n row and n column
print(b_n_n, "\n")

b_n_1 = a[:,:1] # n row and 1 column
print(b_n_1, "\n")

b_n_2 = a[:,:2] # n row and 2 column
print(b_n_2, "\n")

b_n_3 = a[:,:3] # n row and 3 column
print(b_n_3, "\n")

b_n_4 = a[:,:4] # n row and 4 column
print(b_n_4, "\n")

b_1_n = a[:1,:] # 1 row and n column
print(b_1_n, "\n")

b_1_1 = a[:1,:1] # 1 row and 1 column
print(b_1_1, "\n")

b_1_2 = a[:1,:2] # 1 row and 2 column
print(b_1_2, "\n")

b_1_3 = a[:1,:3] # 1 row and 3 column
print(b_1_3, "\n")

b_1_4 = a[:1,:4] # 1 row and 4 column
print(b_1_4, "\n")

b_2_n = a[:2,:] # 2 row and n column
print(b_2_n, "\n")

b_2_1 = a[:2,:1] # 2 row and 1 column
print(b_2_1, "\n")

b_2_2 = a[:2,:2] # 2 row and 2 column
print(b_2_2, "\n")

b_2_3 = a[:2,:3] # 2 row and 3 column
print(b_2_3, "\n")

b_2_4 = a[:2,:4] # 2 row and 4 column
print(b_2_4, "\n")

b_3_n = a[:3,:] # 3 row and n column
print(b_3_n, "\n")

b_3_1 = a[:3,:1] # 3 row and 1 column
print(b_3_1, "\n")

b_3_2 = a[:3,:2] # 3 row and 2 column
print(b_3_2, "\n")

b_3_3 = a[:3,:3] # 3 row and 3 column
print(b_3_3, "\n")

b_3_4 = a[:3,:4] # 3 row and 4 column
print(b_3_4, "\n")


print("\n")




### element getting
## 'a' matrix has 3 rows and 4 columns. Rows will be counted as 0,1,2. Columns will be counted as 0,1,2,3
print(a[0,0]) # (0,0) element of numpy 'a' matrix
print(a[0,1]) # (0,1) element of numpy 'a' matrix
print(a[0,2]) # (0,2) element of numpy 'a' matrix
print(a[0,3]) # (0,3) element of numpy 'a' matrix
print(a[1,0]) # (1,0) element of numpy 'a' matrix
print(a[1,1]) # (1,1) element of numpy 'a' matrix
print(a[1,2]) # (1,2) element of numpy 'a' matrix
print(a[1,3]) # (1,3) element of numpy 'a' matrix
print(a[2,0]) # (2,0) element of numpy 'a' matrix
print(a[2,1]) # (2,1) element of numpy 'a' matrix
print(a[2,2]) # (2,2) element of numpy 'a' matrix
print(a[2,3]) # (2,3) element of numpy 'a' matrix
print("\n")





### Printing Whole numpy matrix
print(a)
print("\n")



### Boolean array indexing
c = np.array([[1,2],[3,4],[5,6]])
bool_idx = (a>2)
print(bool_idx, "\n")
print(a[bool_idx], "\n")
# we can do this in short as 
print(a[a>2])