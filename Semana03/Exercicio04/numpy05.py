#Dot product

import numpy as np
l1 = [1, 2,3]
l2 = [4,5,6]
a1 = np.array(l1)
a2 = np.array(l2)

dot = 0

for i in range(len(l1)):
    dot += l1[i] * l2[i]
print(dot)

sum1 = a1*a2
dot = (a1 * a2).sum()
print(dot)

dot = a1 @ a2
print (dot)