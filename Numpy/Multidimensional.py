import numpy as np

a = np.array([[1, 2, 6],
              [3, 4, 8],
              [2, 5, 6]])
print(a)
print(a.shape)  # it will give the number of rows and columns

print(a[0][0])
# slicing
print(a[:, 0])


# transpose
print(a.T)

# inverse
print(np.linalg.inv(a))  # to use this method our matrix should be sqr matrix

# determinant
print(np.linalg.det(a))

# diagonal elements
print(np.diag(a))
