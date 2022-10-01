# let's check difference between Arrays and list
import numpy as np

l = [1, 3, 5]
a = np.array([1, 3, 5])
l.append(4)
l = l + [4]
l = l * 2
print(l)
# a.append(4)  it's gives you an error
a = a + np.array([4])
a = a * 2
print(a)