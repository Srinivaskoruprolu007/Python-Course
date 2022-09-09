# let's check the user is teen or child or adult or dies by entering his age
age = int(input("Dear user Enter your age :\n"))
# let's check the age by using conditional operators
if age in range(0, 13):
    print("You are children ")
elif age in range(13, 20):
    print("You are a teenager")
elif age in range(20, 60):
    print("You are an adult")
elif age in range(60, 101):
    print("You are old enough")
elif age > 100:
    print("You are died")
else:
    print("You are not born yet!")
