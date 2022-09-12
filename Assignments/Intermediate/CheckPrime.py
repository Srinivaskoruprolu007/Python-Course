# num = int(input("Enter the num which you want to check >>\n"))
# # let's check prime using for loop
# for i in range(2, num):
#     if num % i == 0:
#         print("Not prime number")
#         break
# else:
#     print("This is prime number")

# let's print the prime numbers in range
low = int(input("Enter the low range number >>"))
high = int(input("Enter the high range number >>"))
for i in range(low, high+1):
    count = 0
    for j in range(2, (i//2 + 1)):
        if i % j == 0:
            count += 1
            break
    if count == 0 and i != 1:
        print(i)