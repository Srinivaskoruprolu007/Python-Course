# For loop is used to iterate through a sequence like list, tuple, strings, etc..
# syntax
list1 = [1, 5, 7, "vasu", True]
for item in list1:
    print(item)

# for loop range function : the range function is used to iterate for some range
for item in range(1, 4):  # here 1 is inclusive and 4 is exclusive
    print(item)

# let's do with skip value in range function
for i in range(0, 4, 2):
    print(i)

list2 = [1, 3, 9, 0, 54]
# for loop with else
for num in list2:
    print(num)
else:
    print("Done")  # else will execute only when for loop completes the iteration

# pass statement
# pass is a null statement in python it instructs to "Do nothing"
for i in list2:
    pass