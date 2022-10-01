"""
--> Core library for scientific computation in python
    -- Data Science, Machine learning, Deep learning
    -- scikit-learn, matplotlib, pandas,....
--> High Performance multidimensional Array ---> Fast!
--> Mathematical operations with arrays
--> A lot of code written in C
"""
import numpy  # it is the way to import the numpy module to your current
import numpy as np  # we can also alias the module with some other term
print(np.__version__)
a = np.array([1, 3, 4, 5])
print(a)
print(a.shape)
print(a.dtype)
print(a.ndim)
print(a.size)
print(a.itemsize)
print(a[0])

# mathematical operations

b = a * np.array([2, 5, 4, 1])
print(b)