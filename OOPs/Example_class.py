# position, name, age, level, salary


software_engineer = ["Software Engineer", "Max", 20, "Junior", 5000]
software_engineer2 = ["Software Engineer", "Lisa", 25, "Junior", 7000]


class SoftwareEngineer:

    def __init__(self, name, age, level, salary):
        # instance Attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary


# instance
software_engineer = SoftwareEngineer(name="vasu", age=24, level=30, salary=70000)
print(software_engineer.name)
