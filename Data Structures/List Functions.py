# list Slicing
List1 = [7, 5, 'sri']
print(List1[0:2])
# the whole process of list slicing same as string slicing
# let's check the type after list is sliced
print(type(List1[0:2]))
# we can conclude that after sling a string or list it will remain string or list
print(List1[0:44])
print(List1[0:3])
print(List1[0:4])

l1 = [1, 2, 7, 5, 6, 8]
# list sort
l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.append(22)  # it will add at end of the list
print(l1)
l1.insert(3, 8)  # it will insert a value at particular index
print(l1)
print(l1.pop(2))  # it will delete and return the value at index 2
l1.remove(22)  # It will remove 22 from the list
print(l1)