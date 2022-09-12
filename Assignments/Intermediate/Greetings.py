# Let's greet everyone whose names are started with S in the list
names = ["Shivam", "Soham", "Harry", "Sanjana"]
for name in names:
    if name.startswith("S"):
        print(f"Good morning {name}")

# let's do the same problem with while loop
i = 0
while i < len(names):
    if names[i].startswith("S"):
        print(f"Good Morning {names[i]}")
    i += 1