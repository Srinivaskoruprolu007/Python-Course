# check the result of a student by user input
marks1 = int(input("Enter the marks for sub 1: "))
marks2 = int(input("Enter the marks for sub 2: "))
marks3 = int(input("Enter the marks for sub 3: "))

overall = ((marks2+marks3+marks1)/3) * 100
# let's check the result by using conditional statements
if overall >= 40:
    if marks2 >= 33 and marks3 >= 33 and marks1 >= 33:
        print("You have passed the exam")
    else:
        print("You have not passed the exam due to one of the subjects")
else:
    print("You have not passed the exam due to overall percentage")

