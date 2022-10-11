# Python ByteArray gives a mutable sequence of integers in the range
# 0 to 256

# creating byteArray
a = bytearray((12, 8, 25, 2))
print("Creating Byte array")
print(a)

# accessing elements
print("\nAccessing Elements :", a[1])

# modifying elements
a[1] = 3
print("\nAfter modifying")
print(a)

# appending elements
a.append(30)
print("\nAfter adding elements")
print(a)