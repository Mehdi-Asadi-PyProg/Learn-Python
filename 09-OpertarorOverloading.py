
#Operator overloading lets you redefine how operators (+, -, *, ==, etc.) work with objects of your own classes. 
# You do this by implementing special methods (also called magic methods or dunder methods).

""" 
    + __add__(self, other)a + b
    - __sub__(self, other)a - b
    * __mul__(self, other)a * b
    == __eq__(self, other)a == b
    < __lt__(self, other)a < b
    str() __str__(self) print(a)
    repr() __repr__(self)repr(a)
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(1, 4)

print(v1 + v2)      # Vector(3, 7)
print(v1 - v2)      # Vector(1, -1)
print(v1 == v2)     # False
print(v1 == Vector(2, 3))  # True


class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __mul__(self, number):
        return Money(self.amount * number)

    def __str__(self):
        return f"${self.amount}"


m1 = Money(50)
m2 = Money(30)

print(m1 + m2)      # $80
print(m1 * 3)       # $150