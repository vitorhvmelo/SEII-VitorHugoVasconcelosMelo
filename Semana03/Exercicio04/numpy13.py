#Data types

import numpy as np
x = np.array([1, 2])
print(x.dtype)
x = np.array([1.0, 2.0])
print(x.dtype)

x = np.array([1, 2], dtype=np.int64)
print(x.dtype)
x = np.array([1, 2], dtype=np.float32)