import time
import numpy as np

a = np.random.randn(1000)
b = np.random.randn(1000)

A = list(a)
B = list(b)
T = 1000


def dot1():
    dot = 0
    for i in range(len(A)):
        dot += A[i]*B[i]
    return dot


def dot2():
    return np.dot(a, b)


st = time.time()
for t in range(T):
    dot1()
en = time.time()
t1 = en-st


st1 = time.time()
for t in range(T):
    dot2()
end = time.time()
t2 = end-st1

print("The time taken by normal dot product is ", t1)
print("The time taken by module dot product is ", t2)
print("The numpy dot product is ", t1/t2, "times faster than normal dot product")