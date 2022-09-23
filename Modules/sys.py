""" The sys module in Python provides various functions and variables that are used to manipulate different parts of
the Python runtime environment? """
# let's check the version of python interpreter
import sys
print(sys.version)

# let's use sys for input the data from command line
for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    print(f'Input : {line}')
print("Exit")