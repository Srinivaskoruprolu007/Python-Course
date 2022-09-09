# let's find the given name is present int the list or not
listOfNames = ["Srinivas", "Vasu", "Ananth", "Dhakshi"]
name = input("Enter your name : \n").capitalize()
if name in listOfNames:
    print("yes your name is exists ")
else:
    print("No your name is not exists")
