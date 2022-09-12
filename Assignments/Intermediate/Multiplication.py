# multiplication table of the number which is inputted by user
num = int(input("Enter the number which you want multiplication table"))

# now we're going to for loop for so many iterations
for i in range(20):
    # now we're using string formation method
    print(f"{num}X{i + 1}={num * (i + 1)}")  # we're using i+1 because I  start from 0


