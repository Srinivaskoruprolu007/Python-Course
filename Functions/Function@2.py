# function with returning value

from itertools import tee
import re


def generate_full_name():
    first_name = "srinivas"
    second_name = "Koruprolu"
    space = " "
    full_name = first_name+space+second_name
    return full_name

print(generate_full_name())



# function with integer as return value
def add():
    num1 = 5
    num2 = 5
    total = num1+num2
    return total

print(add())