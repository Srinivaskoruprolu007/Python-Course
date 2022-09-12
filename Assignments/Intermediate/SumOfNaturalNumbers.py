# let's perform summation of natural numbers unto n numbers
N = int(input("Enter the number which you want the sum >>"))
# let's initiate sum with 0
Sum = 0
for i in range(1, N + 1):
    Sum += i

print(Sum)

# let's do the same problem with while loop
i = 1
while i <= N:
    Sum += i
    i += 1
print(Sum)