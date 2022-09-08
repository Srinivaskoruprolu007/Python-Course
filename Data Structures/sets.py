""" Sets in python"""
# Sets is a collection of non-repetitive elements
s = set()  # No repetitive elements
s.add(1)
s.add(2)
print(s)

""" Properties of sets"""
# 1. Sets are unordered
# 2. Sets are un-indexed
# 3. There is no way to change items in sets
# 4. Sets can't contain duplicate elements

mySet = {1, 5, 2, 6, 7}
# add operation is used add more items to the set
mySet.add(9)
print(len(mySet))  # it returns the length of the set

# if we tried to add string the given set it will add as a string itself
mySet.add("1")
print(mySet)