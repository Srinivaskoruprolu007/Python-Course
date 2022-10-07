number = int(input("Enter your number ="))
total = 0
temp = number
while temp > 0:
    digit = temp % 10
    total += digit ** 3
    temp //= 10
if number == total:
    print(number, "is a Armstrong number")
else:
    print(number, "not a Armstrong number")



