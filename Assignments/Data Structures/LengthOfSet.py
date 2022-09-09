# find the length of the set after few operations

s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))  # actually  we are adding 3 elements to the set but, it's size is actually 3
# because we're adding same 20 as 20.0 but, there no difference
