
#Write a Python program to demonstrate polymorphism where two different classes have the same method name, and a common function calls those methods

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

animal_sound(dog)  
animal_sound(cat)  

# Create a base class Vehicle with a method speed(). Then, create a derived class Car that overrides the speed() method.

class Vehicle:
    def speed(self):
        return "Vehicle speed"

class Car(Vehicle):
    def speed(self):
        return "Car speed"

vehicle = Vehicle()
car = Car()

print(vehicle.speed()) 
print(car.speed()) 

#Create a class Box that overloads the + operator to add the volume of two boxes

class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def add(self, other):
        return self.volume() + other.volume()

b=Box(1,2,3)
c=Box(2,3,4)

b.volume()

c.volume()

c.add(b)