a = [1, 2, 3, 4, 5, 6, 7, 8]

for item in a:
    print(item)
    if item == 4:
        break
print("We have finished this loop")

# let's do the same thing with continue statement
for num in a:
    print(num)
    if num == 4:
        continue

print("We have skipped the iteration at num is equals to 4")