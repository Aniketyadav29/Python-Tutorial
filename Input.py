# Input in Python

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


#input based question 


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

<br>

# Question 3: Write a program to input 2 floating points number & print their Average 

num1=float(input("enter number 1:"))
num2=float(input("enter number 2:"))
average=(num1+num2)/2
print("the average of the numbers :",average)

#Question 4: WAP to input of 2 number a & b print true if a is greater than or equal to b otherwise false.
a=int(input("enter your number a:"))
b=int (input("enter your number b:"))
print("a is greater than or equal to b:",a>=b)


