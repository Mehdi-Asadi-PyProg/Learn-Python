# An iterator is an object that can be iterated (looped) over one item at a time.
# It implements two special methods:
#  __iter__() → returns the iterator object itself
#  __next__() → returns the next value (raises StopIteration when finished)

class CountDown:  # Iterator Creation Class
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self          # the object itself is the iterator

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


# Iterator Usage
for num in CountDown(5):
    print(num)

# A generator is a special kind of iterator that produces values one at a time (lazily) 
# instead of creating and storing the entire sequence in memory at once.
"""
You create a generator in two main ways:
    Using a function that contains the "yield" keyword
    Using a generator expression (similar to a list comprehension)
"""

# Using Yield
def countdown(n):  
    print("Starting countdown...")
    while n > 0:
        yield n          # pause here and return the value
        n -= 1
    print("Countdown finished!")

# Create the generator object
gen = countdown(3)

print(next(gen))  # Starting countdown... → 3
print(next(gen))  # 2
print(next(gen))  # 1
# print(next(gen)) → raises StopIteration and prints "Countdown finished!"


# Generator Expression
# List comprehension (creates the whole list in memory)
squares_list = [x**2 for x in range(5)]
print(squares_list)          # [0, 1, 4, 9, 16]

# Generator expression (produces values on demand)
squares_gen = (x**2 for x in range(5))
print(squares_gen)           # <generator object ...>

for num in squares_gen:
    print(num)


# Useful Example: Reading a Large File  --------------------------------
def read_large_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()   # yield one line at a time

# Usage
#for line in read_large_file("big_data.txt"):
#    process(line)   # process one line without loading the whole file


# A decorator is a function that takes another function (or class) as input, adds some extra behavior to it,
# and returns a new function — without permanently modifying the original function.
# Decorators use the @ syntax and are a clean way to wrap functionality around 
# existing code (logging, timing, authentication, caching, etc.).

def my_decorator(func):   # Basic Decorator
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Usage Basic Decorator
say_hello()



def logger(func): # Decorator with Arguments
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

print(add(3, 5))