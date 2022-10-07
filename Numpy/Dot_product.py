import numpy as np
l1 = [1, 3, 5]
l2 = [4, 6, 8]
a1 = np.array(l1)
a2 = np.array(l2)

# dot product
dot = 0
for i in range(len(l1)):
    dot += l1[i]*l2[i]
print(dot)
dot = np.dot(l1, l2)
print(dot)

sum1 = a1 * a2
dot = (a1 * a2).total()
print(dot)

# simple_method
dot = a1 @ a2
print(dot)
