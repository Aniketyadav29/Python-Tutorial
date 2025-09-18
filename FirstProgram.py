print("Hello World")
print ("my name is Aniket Yadav ")
print ("I am learning Python")
print ("I am enjoying it")  
print(23+34)
print(23*34)
print(23/34)  
name="Aniket Yadav"
age=20
cgpa=9.1
age2=age
print (name)
print (age)
print (cgpa)  
print (age2)

print(type(name))
print(type(age))
print(type(cgpa))
age=23
old = False
a= None 
print(type(age))
print(type(old))   
print(type(a))
# print sum/sub/mul/div of two numbers
a=23
b=35
sum=a+b
print("The sum of a and b is",sum)
sub=a-b
print("The sub of a and b is",sub)
mul=a*b
print("The mul of a and b is",mul)
div=a/b
print("the div of a and div;",div)


# comment
# this is a single line comment
'''
this is a multi line comment
line 1  
line 2
line 3
line 4
'''
"""this is also a multi line comment
line 1
line 2
line 3
line 4
"""
# Operators in Python
# Arithmetic Operators
a=23
b=34
print("The value of a+b is",a+b)
print("The value of a-b is",a-b)
print("The value of a*b is",a*b)
print("The value of a/b is",a/b)
print("The value of a%b is",a%b)
print("The value of a//b is",a//b)

# Relational Operators
a=50
b=20
print("The value of a==b is",a==b) # equality operator ,'False' because 50 is not equal to 20

print("the value of a!=b is:",a!=b) # not equal to operator, 'True' because 50 is not equal to 20

print("the value of a>=b is:",a>=b) # greater than or equal to operator, 'True' because 50 is greater than 20

print("the value of a<=b is:",a<=b)  # less than or equal to operator, 'False' because 50 is not less than 20

print("the value of a>b is:",a>b) # greater than operator, 'True' because 50 is greater than 20

print("the value of a<b is:",a<b)   # less than operator, 'False' because 50 is not less than 20

# Assignment Operators
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

# Logical Operators
a=True
b=False
print("The value of a and b is:",a and b) # and operator, 'False' because both a and b are not true
print("The value of a or b is:",a or b) # or operator, 'True' because at least one of a or b is true
print("The value of not a is:",not a) # not operator, 'False'
print("The value of not b is:",not b) # not operator, 'True'

#Type Conversion
#Implicit Type Conversion

a=5
b=2.0
c=a+b
print("The value of c is:",c)# c is float because b is float, so a is converted to float, a = 5.0 and b = 2.0
print("The type of a is:",type(a)) # type of a is int
print("The type of c is:",type(c)) # type of c is float

<br>
 # Explicit Type Conversion
a="5"
b=4.05
a=int(a) # converting string to int,because a is string
print("The type of a is:",type(a)) # type of a is int
c=a+b
print("The value of c is:",c) # c is float because b is float, so a is converted to float, a = 5.0 and b = 4.05
print("The type of c is:",type(c)) # type of c is float

<br>
#Input in Python

name=input("enter your name:")
print("Welcome",name)


name=input("enter your age:")
print("Your age is:",name)

value=input("enter your value:")
print(type(value))

value=int(input("enter your value:"))
print(type(value))

value=float(input("enter your value:"))
print(type(value))

name=input("enter your name:")
age=int(input("enter your age:"))
marks=float(input("enter your marks:"))

print("Welcome",name)
print("age is :",age)
print("your marks:",marks)
print(type(name))
print(type(age))
print(type(marks))

<br>
#Question 1: Write a program to add two numbers and display the sum.

num1=int(input("enter your number:"))
num2=int(input("enter your number"))
sum=num1+num2
print ("The sum of the numbers is :",sum)


<br>

# Question 2: Write a program to calculate the area of a square.

side=int(input("enter your side of square:"))
area =side*side
print("The area of the square is :",area)







