#A class is a blueprint for creating objects (instances).
#It groups data (attributes) and behavior (methods) together.

#Basic Class + Constructor
class Dog:
    species = "Canis familiaris"          # Class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

# Create objects AFTER the class is fully defined
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

print(Dog.species)      # Canis familiaris  (via the class)
print(dog1.species)     # Canis familiaris  (via the instance)
print(dog2.species)     # Canis familiaris

#   self    refers to the current instance.
# __init__  runs automatically when you create an object.

# Class Attributes vs Instance Attributes
class Dog:
    species = "Canis familiaris"        # Class attribute (shared by all)

    def __init__(self, name):
        self.name = name                # Instance attribute (unique per object)

print(Dog.species)          # Canis familiaris
print(dog1.species)         # Canis familiaris (also accessible via instance)


# Inheritance, allows a new class (called the child or subclass) to reuse and 
# extend the attributes and methods of an existing class (called the parent or superclass).
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):                      # Dog inherits from Animal
    def speak(self):                    # Method overriding
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())   # Buddy says Woof!
print(cat.speak())   # Whiskers says Meow!

# Encapsulation (name mangling / private convention)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance        # "Private" attribute (name mangling)

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())     # 1500
# print(acc.__balance)       # AttributeError (not directly accessible)

# Polymorphism means “many forms”.
# In Python, it means that different objects can respond to the same method name in different ways.
# The most common type of polymorphism in Python is Method Overriding (through inheritance).
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):                # Same method name
        return "Woof!"

class Cat(Animal):
    def speak(self):                # Same method name
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

# Polymorphism in action
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.speak())
    
# Special (Dunder) Methods  ,Dunder is short for “Double Underscore”.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):                  # Used by print() and str()
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):           # Enables + operator
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1)           # Point(1, 2)
print(p1 + p2)      # Point(4, 6)