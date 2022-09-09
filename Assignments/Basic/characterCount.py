# let's check the username's characters are less than 10 or not
userName = input("Enter the username \n")
count = len(userName)

if count < 10:
    print("Yes")
else:
    print("No")