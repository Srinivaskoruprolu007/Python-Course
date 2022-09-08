# display only unique numbers from the user input numbers
n = int(input("Enter the number of input numbers you want to enter \n"))
s = set()
for i in range(n):
    s.add(int(input("Enter your number = ")))

print(s)