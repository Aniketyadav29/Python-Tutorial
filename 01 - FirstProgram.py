
# My Python journey start from here ......


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


# String and Conditional statements.
Str1="my name is aniket yadav "
Str2='this is aniket yadav'
Str3="""" my name is banku """
print(Str1)


#why we use :-

" This is apna college's tutorial."
#Escape Sequence Character :-

 Str4= "this is string.\n we are using it in python."
 print(Str4)

# Basic Operation on String:-

#concatination:-

 print(Str1+Str2)
 print(Str1+""+Str2)

#Length of String:-

 len1=len(Str1)
 print(len1)

 len2=len(Str1)
 print(len2)

#Indexing in python :-

print(Str1[1])

print(Str1[4])

print(Str2[5])

print(Str2[9])

# Slicing :-

 print(Str1[1:4])
print(Str2[1:7])
 print(Str3[4:])  #[4:length(Str3)]
 print(Str2[:7])  #[0:7]

# Slicing in Negative Index :-

 Str="apple"
 print(Str[-3:-2])
 print(Str[-5:-2])


# String Function:-

 str="this is apna college and i am learning python"
 print(str.endswith("thon")) # it checks whether the string ends with the specified value, returns true or false
 print(str.capitalize()) # it converts the first character to upper case
 print(str.find("apna")) # it finds the first occurrence of the specified value, returns the index of the first occurrence
 print(str.replace("apna","our")) # it replaces the specified value with the specified value
 print(str.count("is")) # it counts the number of occurrences of the specified value

# Practice :-

# Question 1:-  WAP to input user name and print the length of the name.
 name=(input("Enter your name:"))
 print("the length of your name is :" ,len(name)) 

# Question 2:- WAP to find occurrence of $ in a string.

str=input("Enter your string:")
print("the occurrence of $ in the string is :",str.count('$'))

 Conditional Statements in pyton:-

# if statement

 age=23
 if (age>=18):
     print("you are eligible for vote" )
     print("I am always executed")

# if elif statement
 light="red"
 if (light=="red"):
     print("you should stop")
 elif (light=="yellow"):
     print("you should get ready")
 elif (light=="green"):
     print("you can go")
   
 print("end of the program")

 difference between if and elif:-

# if statement:- if statement is used to execute a block of code if a specified condition is true. if the condition is false, the block of code is skipped.
 num=5
 if (num>2):
     print("num is greater than 2")
 if (num>4):
     print("num is greater than 4")
  # elif statement:- elif statement is used to execute a block of code if the previous condition is false and the specified condition is true. if the condition is false, the block of code is skipped. 
num=5
if (num>2):
    print("num is greater than 2")
elif (num>4):
    print("num is greater than 4")  
# else statement:- else statement is used to execute a block of code if the previous condition is false. if the condition is true, the block of code is skipped.
light="pink"
if (light=="red"):
    print("you should stop") # indented block
elif (light=="yellow"):
    print("you should get ready") #indentation block
elif (light=="green"):
    print("you can go") 
else:
    print("invalid color") # indented block 

# Practice:-

age=28
if (age<18):
    print("you are a minor") #indented block
else: 
    print("you are an adult") 


# Question 1:- WAP to assign grades to students based on their marks.
marks=int(input("enter your marks:"))
if(marks>=90):
    print("A grade")
elif(90>marks>=80):
    print("B grade")
elif(80>marks>=70):
    print("C grade")
else:
    print("D grade") 
print("grade of student->", marks)

# Nested if-else statement:-

age=25
if(age>=18):
    if(age>=29):
        print("you are eligible for voting")
    else:
        print("you are not eligible for voting")
else:
    print("you are not eligible for vote")    


# Practice:-WAP if the number is entered by the user is even or odd.
num=int(input("Enter Your Number"))
if (num%2==0):
    print("The Number is Even")
else:
    print("the Number is Odd")

# Question 2:- WAP to find the greatest number among three numbers.
num1=int(input("Enter your number1:"))
num2=int(input("Enter your number2:"))
num3=int(input("Enter your number3:"))
if (num1>=num2) and (num1>=num3):
    print("num1 is the greatest number:",num1) 
elif (num2>=num1) and (num2>=num3):
    print("num2 is the greatest number:",num2)
else:
    print("num3 is the greatest number:",num3) 

# Question 3:- WAP to check whether the entered number is multiple by 7 or not

num=int(input("Enter your number:"))
if(num%7==0):
    print("The Number is Multiple by 7")
else:
    print("The Number is not Multiple by 7")

# List:-

Marks=[23,56.3,56,78,90]
print(Marks)
print(type(Marks))
print(Marks[0])
print(Marks[1])
print(Marks[2])

Student=["Aniket",56,23,"Anupam Lata Yadav"]
print(Student)
print(len(Student))

# List is mutable in python:-

Student[0]="Anshu"
print(Student)

# List Slicing:-
Mark=[23,56.3,56,78,90]
print(Mark[1])
print(Mark[1:4])
print((Mark[:4]))
print(Mark[1:])
print(Mark[-3:-1]) 

# List Methods:-
List=[3,1,2]
List.sort() # it sorts the list in ascending order
print(List)
List.reverse() # it reverses the list
print(List)
List.append(4) # it adds an element at the end of the list
print(List)
List.insert(2,5) # it adds an element at the specified index
print(List)
List.remove(5) # it removes the specified element
print(List)

# List Methods:-
list=[1,2,3,3,5]
list.remove(3) # it removes the first occurrence of the specified element
print(list) 

list.pop() # it removes the last element of the list
print(list)

list.append(6) # it adds an element at the end of the list
print(list)

#Tuple:- Tuple is immutable in python. it means we cannot change the elements of the tuple.it's a built-in data type in python.

tup=(1,2,3,4,5)
print(type(tup))
print(tup[0])
print(tup[1:4])
print(tup[-3:-1])
tup[0]=6 # it will give an error because tuple is immutable

tup1=(1)
print(type(tup1)) # it will give type 'int' because it's not a tuple, it's an integer
tup2=("Aniket")
print(type(tup2)) # it will give type 'str' because it's not a tuple, it's a string
tup3=(1,2,3,4,5)
print(type(tup3))# it will give type 'tuple' because it's a tuple

# Tuple Methods:-
tup=(1,2,3,4,5,3)
print(tup.count(3)) # it counts the number of occurrences of the specified element
print(tup.index(4)) # it returns the index of the first occurrence of the specified element
print(tup.sort()) # it will give an error because tuple is immutable
print(tup.reverse()) # it will give an error because tuple is immutable

# practice:-
# Question 1:- WAP to ask user to enter his favorite 5 movies and store them in a list.
movies=[]
for i in range(5):
    movie=input("Enter your favorite movie:")
    movies.append(movie)
print("Your favorite movies are:",movies)
# Methos :- 2
movies=[]
mov1=input("Enter your favorite movie1:")
mov2=input("Enter your favorite movie2:")
mov3=input("Enter your favorite movie3:")
mov4=input("Enter your favorite movie4:")
mov5=input("Enter your favorite movie5:")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
movies.append(mov4)
movies.append(mov5)
print("Your favorite movies are:",movies)

# Question 2:- WAP a program to check palindrome or not.
list1=[1,2,1]
list2=[1,2,3]
copy_list1=list1.copy()
list1.reverse()
if (list1==copy_list1):
    print("The list is palindrome")
else:
    print("The list is not palindrome")



 





































