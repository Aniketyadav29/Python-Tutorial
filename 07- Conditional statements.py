# Conditional Statements in pyton:-

# if statement :-

age=23
if(age>=18):
    print("you are eligible for vote" )
    print("I am always executed")

# if elif statement:-
light="red"
if (light=="red"):
     print("you should stop")
elif (light=="yellow"):
     print("you should get ready")
elif (light=="green"):
     print("you can go")
   
print("end of the program")

# Difference between if and elif:-

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

#else statement:- else statement is used to execute a block of code if the previous condition is false. if the condition is true, the block of code is skipped.
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


#Question 1:- WAP to assign grades to students based on their marks.
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

# Question 1 :-WAP if the number is entered by the user is even or odd.
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

