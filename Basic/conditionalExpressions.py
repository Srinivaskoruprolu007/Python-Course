# sometimes we want to play PUBG on our phone if the day is sunday
# Sometimes we order Icecream online if the day is sunny
# all above decisions are made on the basis of some condition

""" If , else and elif in python"""
# syntax :
# if(condition-1):
#     print(something) or do some task
# elif(condition-2):
#     print(something else) or do some other task
# else:
#     print(some other else) or do some else task
# let's write a program to tell which user input number is greater
num1 = int(input("Enter your first number \n"))
num2 = int(input("Enter your second number \n"))

# let's use conditional statements
if num1 > num2:
    print("The greater number is ", num1)
else:
    print("The greater number is ", num2)