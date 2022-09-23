# list comprehension with if conditions
""" Syntax"""
# list_1 = [expression for member in iterable (if condition)]
# let's print the even numbers by using list comprehension
even = [i for i in range(21) if i % 2 == 0]
print(even)