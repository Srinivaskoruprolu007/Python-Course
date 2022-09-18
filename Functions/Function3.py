# function with parameters


import re


def greeting(name):
    message = name + ", welcome to Python for Everyone"
    return message

print(greeting("Srinivas"))


# function with definite data types as the parameters
def add(num1:int, num2:int) -> int:
    total = num1+num2
    print(total)
add(5,8)
