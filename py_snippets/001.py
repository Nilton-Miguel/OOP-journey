class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def present(self):
        print(f"This is {self.name} and it is {self.age} years old")
    
    def speak(self):
        print("I don't know what to say")


class Dog(Pet):
    def speak(self):
        print("Bark :)")

# if the child class needs a different __init__ method than it is better to not overwrite the parent's __init__ and, instead, get the info we need from the parent using super()

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def present(self):
        print(f"This is {self.name} and it is {self.age} years old and {self.color}")

    def speak(self):
        print("Meow :3")

c = Cat("Garu", 5, "Brown")
c.present()
c.speak()

print("")

d = Dog("Duna", 3)
d.present()
d.speak()
