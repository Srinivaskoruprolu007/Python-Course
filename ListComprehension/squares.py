# code using raw for loop
list1 = []
for i in range(1, 11):
    list1.append(i*i)
print(list1)

# code using list comprehension
list2 = [i*i for i in range(1, 11)]
print(list2)
""" Syntax """
# new_list = [expression for member in iterable]
