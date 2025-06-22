
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def present(self):
        print(f"This is {self.name} and it is {self.age} years old")
    
    def speak(self):
        print("I don´t know what to say")

# child inherets methods and attributes from parent, but overwrites it if more specific versions are given

class Dog(Pet):
    def speak(self):
        print("Bark :)")

class Cat(Pet):
    def speak(self):
        print("Meow :3")

class Fish(Pet):
    pass

c = Cat("Garu", 5)
c.present()
c.speak()

print("")

d = Dog("Duna", 3)
d.present()
d.speak()

print("")

f = Fish("Tim", 1)
f.present()
f.speak()
