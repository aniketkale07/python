
class Animal:
    def __init__(self, name) -> None:
        self.name=name
    
    def speak(self):
        print(f"{self.name} says somethings..")
    
class Dog(Animal):
    def bark(self):
        print(f"{self.name} Barks Loudly..")
        

my_dog =Dog("Sweety")

my_dog.speak()
my_dog.bark()