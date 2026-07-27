# Arithmathic Operation
a = 17
b = 5

add_result = a + b          # Addition
sub_result = a - b          # Subtraction
Mult_result = a * b         # Multiplication
div_result = a / b          # Devision
print(f"Divesion Operation {div_result}")
floor_div_Result = a // b   # Floor Devision
print(f"Floor Devision Operation {floor_div_Result}")
modulus_Result = a % b      # Modulus
print(f"Modulus Operation {modulus_Result}")
exponent_result = a ** b
print(f"Exponent Operation {exponent_result}")

# Comarssion Operators
a = 10
b = 10
print("-" * 50)
print(f"{a} == {b} ",a == b)
num1 = 36
num2 = 27
print(f"{num1} != {num2} ", num1 != num2)
print(f"{num1} <= {num2} ",num1 <= num2)
print(f"{num1} > {num2} ",num1 > num2)

str1 = "Hello"
str2 = "Bye"
print(f"{str1} == {str2}",str1 == str2)

# Logical Operations  AND OR NOT
print("-" * 50)

x = True
y = False

print(f"{x} and {y}", x and y)
print(f"{x} or {y} ",x or y)
print(f"not {y} ",not y)

# IF Statment
print("-" * 50)

age = 17
if age < 13 :
    print("You Are a Child")
elif age < 18:
    print("You Are a Teenager")
else:
    print("You Are Adult")

# For Loops
print("-" * 50)
for i in range (10,1,-1):
    print(i)

str = "Hello World I'M New In Programming"
for i in str :
    print(i)

# While Loops
count = 0
while count < 5 :
    print(count)
    count = count+1

# Loop Control Statements

# break  ----> the break statement exits the loop permanently
# continue --> the continue statement skips the current iteration and continues with next round of current loop
# pass   ----> the pass statement is a null operator and does nothing