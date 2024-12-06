#### Numpy Mathematical function ####

import numpy as np
a = np.array([[1,2],[3,4]])

### Sum function
print(np.sum(a)) # compute sum of all elements
print(np.sum(a, axis=0)) # compute sum by column
print(np.sum(a, axis=1)) # compute sum by row