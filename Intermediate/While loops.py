# basic example regarding loops
a = 0
# while loop
while a < 10:   # while loops are used when you've no idea how many times to loop
    print(a)
    a += 1

# in while loop it iterates only when the statement is true

"""Quick Quiz"""
# write a program ro print 1 to 50 using a while loop
print("\n")  # it is not mandatory
num = 1
while num <= 50:
    print(num)
    num += 1

# let's discuss infinite loop
#  is nothing but a loop which iterates repeatedly
# let's create
# num1 = 1
# while num1 <= 5:
#     print(num1)

# let's print items in the list
list1 = [1, 3, 4, 5, "banana"]
i = 0
while i < len(list1):
    print(list1[i])
    i += 1