oxford = {"gift": "something willingly given to someone to appreciate", "this": "A keyword in java", "Youtube": "A video sharing platform ", "Instagram": "A picture sharing platform"}

# return a list of (key, value) tuples
print(oxford.items())

# return a list containing dictionary keys
print(oxford.keys())

# return a list containing dictionary values
print(oxford.values())

# update the dictionary with key-value pair
oxford.update({"friend": "vasu"})
print(oxford)
oxford.update({"friend": "vasu", "vasu": "good boy"})
print(oxford)
# let's print values by for loop
for key in oxford.keys():
    print(key)

# let's print keys and values by using for loop
for key, values in oxford.items():
    print(key, "==", values)

# get function will give value of that particular key in the dictionary
print(oxford.get("friend"))

for i in oxford.values():
    print(i)
