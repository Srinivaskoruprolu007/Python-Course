""" Set Functions"""
mySet = {1, 9, 7, 44, 78}

# len() Function
print(len(mySet))  # return integer value which represents length

# remove() function
mySet.remove(78)  # it will remove value 78 from the given set
print(mySet)

# pop() function
print(mySet.pop())  # Removes the lowest element from the set and returns the element removed

# clear() function
mySet.clear()  # it empties the set
print(mySet)


s1 = {3, 6, 7, 8, 9}
s2 = {2, 5, 7, 8, 4}

# union() function
print(s1.union(s2))  # union function returns combination of two sets without duplicates

# intersection() function
print(s1.intersection(s2))  # intersection function return common elements of two sets
