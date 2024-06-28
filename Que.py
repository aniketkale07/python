class Person:
    def __init__(self, name, age) -> None:
        self.name=name
        self.age=age


person1=Person("Aniket", 45)
person2=Person("Vishal", 34)


# Access and print attributes of each instance
print("Person 1:")
print("Name:", person1.name)
print("Age:", person1.age)

print("\nPerson 2:")
print("Name:", person2.name)
print("Age:", person2.age)
