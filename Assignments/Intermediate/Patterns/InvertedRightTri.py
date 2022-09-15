rows = int(input("Enter the number of rows \n"))
# * * * * *
# * * * *
# * * *
# * *
# *
for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print("*", end=" ")
    print(" ")

# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5
b = 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i+1):
        print(b, end=" ")
    print(" ")

# 5 5 5 5 5
# 5 5 5 5
# 5 5 5
# 5 5
# 5
num = 5
for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print(num, end=" ")
    print(" ")

# reverse number pattern
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
for i in range(rows, 0, -1):
    num = i
    for j in range(0, i):
        print(num, end=' ')
    print("\r")
