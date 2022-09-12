# *
# * *
# * * *
# * * * *
# * * * * *

rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print(" ")

# let's try above program with number instead of stars
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print(" ")

# let's try above program by printing Alphabets
# A
# B B
# C C C
# D D D D
# E E E E E
# in addition, we have to add ASCII VALUE
ascii_value = 65
for i in range(rows):
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet, end="")
    ascii_value += 1
    print(" ")

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
for i in range(rows):
    for j in range(i):
        print(i, end=" ")
    print(" ")