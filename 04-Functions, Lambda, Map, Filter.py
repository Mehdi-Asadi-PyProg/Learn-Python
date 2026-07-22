# function is a block of codes that performs a specific task. functions help to organize, reuse and improve readabilty of code.
def even_or_odd(num):
    """
    This function check num and print if it is Even pr Odd
    """
    if num%2==0 :
        print("The Number is Even!")
    else:
        print("The Number Is Odd! ")

def print_Times(name, n = 1):
    """
    print n Times name that you Entered!
    """
    for i in range(n):
        print(name)
    return 0


# if we don't know argumenats list or want to be not prefefined we use this keyword *args
def mul(*args):
    """
    multiply list of numbers if you entred a number also work properly
    """
    res = 1
    for i in args:
        res *= i
    return res

#if  our inpute is a deictionary instrad of *args we use **kwargs
def area (**kwargs):
    """
    using **kwargs for counting Area of a shape
    """
    return kwargs['length'] * kwargs['width']

def print_details(*args,**kwargs):
    """
    using *args to show a list of numbers and **kwargs for show a dictionary key:value pairs
    """
    for val in args:
        print(f"Positional arument :{val}")
    for key, value in kwargs.items():
        print(f"{key}:{value}")

def is_strong_password(password):
    """
    This Function Checks how is strong the password that user intered
    """
    if len(password) < 8 :
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in "!@#$%^&*()_+" for char in password):
        return False
    return True

# Lambda Function is a small anonymous function defined using the "lambda" keyword and its syntax is as below 
# lambda arguments : expression , only one expression will be used

def addition(a,b):
    return a+b

sum = lambda a,b : a+b # this is equal to addition() function
even = lambda num: num%2 == 0


# Map() function apply a given function to all items in an input list and returned map object
numbers = [1,2,3,4,5,6]
squared_list = list (map(lambda x : x**2, numbers))

# Filter() function constructs an iterator from elements of an iterable for wi=hich a fuction returns True. useful on lists

# This filter numbers and returns Float Numbers!!!
a = [5,6.2,3.14,6,3,8,4.3,11.2,0.7,0.564,14]
get_Floaf_List = list(filter(lambda x : x!=int(x),a))


# call and test functions
even_or_odd(20)    
print_Times("Mehdi",5)
print(mul(3,4,5,6))
print(area(length = 7, width= 6))
print_details(1,2,3,4,5,name="Mehdi",age = "40", country="Iran")
print(is_strong_password("IiuKJUU#23d00"))

# call lambda function
print(sum(5,6))
print(even(13))

# Using Map on Lambda
print(squared_list)

# Using Filter On Lambda
print(get_Floaf_List)