"""  Arithmetic Operators"""
# 1. Addition
print(5 + 6)

# we can use addition operator for concat two strings
print("Srinivas" + "Rao")

# 2. Subtraction
print(44 - 2)
# we can't use subtract to strings
# print("Srinivas"-"sri")  # it gives Type error

# 3. Multiplication
print(3 * 5)
# we can use this operand on strings to prints as many times as we want
print("sri " * 4)

# 4. Division
print(5 / 4)
# the result of division is always float value

# 5. Modulo operator
print(31 % 10)
# Modulo operand gives the remainder of that division

# Assignment Operator
""" It is used to Assign a value to variable"""
num1 = 15
print("Num1 :", num1)

# Compound Operators
num1 += 5  # num1 = num1+5
print("Num1 :", num1)
num1 -= 5  # num1 = num1-5
print("Num1 :", num1)
num1 *= 5  # num1 = num1 * 5
print("Num1 :", num1)
num1 /= 5  # num1 = num1/5
print("Num1 :", num1)

""" Comparison Operator """
# Equals to Operator
x = 5
y = 5
print(x == y)  # Its results either True or False

# Not Equals to Operator
print(x != y)

# Less than or equals to Operator
print(x <= y)

# Greater than or equals to Operator
print(x >= y)

""" Logical Operators"""
# AND operator
print(x > 3 > x)  # it results True when both conditions are True

# OR Operator
print(x > 3 or x < 3)  # it results True when any of the condition is true

""" Identity Operator"""
# is Operator
fruits = ["Apple", "Mango", "Grapes"]
pandlu = ["Apple", "Mango", "Grapes"]
z = fruits
print(z is fruits)
