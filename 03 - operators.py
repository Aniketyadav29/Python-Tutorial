# Operators in Python :- In Python, an operator is a symbol or keyword used to perform operations on values or variables.

# Arithmetic Operators:- Arithmetic operators are used to perform mathematical calculations like addition, subtraction, multiplication, etc.
a=45
b=65
print("The value of a+b is",a+b)
print("The value of a-b is",a-b)
print("The value of a*b is",a*b)
print("The value of a/b is",a/b)
print("The value of a%b is",a%b)
print("The value of a//b is",a//b)

# Relational Operators:- These operators are used to compare two values or expressions, and the result is always a Boolean value — either True or False.
a=50
b=20
print("The value of a==b is",a==b) # equality operator ,'False' because 50 is not equal to 20

print("the value of a!=b is:",a!=b) # not equal to operator, 'True' because 50 is not equal to 20

print("the value of a>=b is:",a>=b) # greater than or equal to operator, 'True' because 50 is greater than 20

print("the value of a<=b is:",a<=b)  # less than or equal to operator, 'False' because 50 is not less than 20

print("the value of a>b is:",a>b) # greater than operator, 'True' because 50 is greater than 20

print("the value of a<b is:",a<b)   # less than operator, 'False' because 50 is not less than 20

# Assignment Operators:- Assignment operators are used to assign values to variables, and sometimes update them at the same time.
num=5
num+=5
print("num is:",num)

num=5
num-=5
print("num is:",num)
num=5
num*=5
print("num is:",num)

num=5
num/=5
print("num is:",num)

num=5
num%=5
print("num is:",num)

num=5
num **= 5
print("num is:",num)

# Logical Operators:-they are used to combine conditional statements and return either True or False.

a=True
b=False
print("The value of a and b is:",a and b) # and operator, 'False' because both a and b are not true
print("The value of a or b is:",a or b) # or operator, 'True' because at least one of a or b is true
print("The value of not a is:",not a) # not operator, 'False'
print("The value of not b is:",not b) # not operator, 'True'
