# Magic methods (also called dunder methods) are special methods that start and end with double underscores (__). Python calls them automatically in specific situations. You rarely call them directly — instead, you implement them to control how your class behaves.

# __init__ — The Constructor Called when an object is created.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)
print(p.name)  # Alice

# __str__ and __repr__ — Object Representation
# __str__ → Human-readable output (used by print() and str())
# __repr__ → Official/developer representation (used by repr())

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

p = Person("Sarah", 25)
print(p)          # Sarah, 25 years old
print(repr(p))    # Person('Sarah', 25)

# Arithmetic and Comparison Operators
# MethodOperator__add__+__sub__-__mul__*__truediv__/__eq__==__lt__<
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(1, 4)
print(v1 + v2)  # (3, 7)
# __len__ — Length of an Object Called by len().
class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

t = Team(["Alice", "Bob", "Charlie"])
print(len(t))  # 3

# __getitem__ and __setitem__ — Indexing Makes objects behave like lists or dictionaries.
class MyList:
    def __init__(self):
        self.data = []

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def append(self, value):
        self.data.append(value)

ml = MyList()
ml.append(10)
ml.append(20)
print(ml[0])   # 10
ml[1] = 99
print(ml[1])   # 99
# __call__ — Making Objects Callable Allows an instance to be called like a function.
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor

double = Multiplier(2)
print(double(5))  # 10

# Context Managers (with statement) Implemented with __enter__ and __exit__.
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with FileManager("SampleFiles/test.txt") as f:
    f.write("Hello Python!")