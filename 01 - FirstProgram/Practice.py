# Python Full Course Practice -

# 01 - Comments
# This is a single-line comment
'''
This is a multi-line comment
covering several lines
'''
print("--- 01 Comments ---")
print("Check the code for comment examples")
print("\n")

# 02 - Variables and Data Types
print("--- 02 Variables and Data Types ---")
name = "Aniket Yadav"
age = 20
cgpa = 9.1
is_student = True
print(name)
print(age)
print(type(name))
print("\n")

# 03 - Operators
print("--- 03 Operators ---")
a = 23
b = 34
print("Sum:", a + b)
print("Is a > b:", a > b)
print("Logical check:", True and False)
print("\n")

# 04 & 05 - Type Conversion and Input
print("--- 04 & 05 Conversion and Input ---")
val = "100"
val = int(val) # Explicit conversion
print("Converted Value:", val)
# name = input("Enter your name: ")
print("\n")

# 06 - Strings
print("--- 06 Strings ---")
str1 = "python mastery"
print(str1.capitalize())
print(str1[0:6]) # Slicing
print("\n")

# 07 - Conditional Statements
print("--- 07 Conditional Statements ---")
marks = 85
if(marks >= 90):
    print("Grade A")
elif(marks >= 80):
    print("Grade B")
else:
    print("Grade C")
print("\n")

 # write a program to find out whether a student has passed or failed if it required a total 40% and atleast 33% in each subject to pass . assume 3 subject and total marks as an input from user.
a=int(input("Enter your 1st Subject marks : "))
b=int(input("enter your 2nd subject marks : "))
c=int(input("Enter your 3rd subject Marks : "))
d=((a+b+c)*100)/300
if (d>=40 and a>=33 and b>=33 and c>=33):
    print("Student Passed in the exam .", d)
else:
    print("Student has failed in the exam ." ,d)


# Write a program to detect the spam words .
p1="Make a lot of money ."
p2="buy now ."
p3="Subscribe now ."
p4="Click this ."
message=input("Enter your Message : ")
if((p1 in message)or(p2 in message)or(p3 in message)or (p4 in message)):
    print ("This is spam message.")

else :
    print("This is not a spam message .")
#Write a program to find wether a given username contains 10 caracters or not.
a=(input("Enter Your Name : "))
b=len(a)
if((b>10)):
    print("The name has 10 letters.")
else:
    print("The name has not 10 letters.")

# Write a program to find out whether a given name is present in list or not.
list=["Aniket", 23, "suraj", "Anupam", "Anushka ", "Aryan"]
Name=input("Enter Your Name : ")
if (Name in list):
    print("The Name is in the list .")
else :
    print("The name is not in the list .")

# Write a program to check the in the post.
post=input("Enter your Post : ")
# post="hey Aniket bhai is good  aniket is very good and harry is also good  "
if ("Aniket".lower() in post.lower()):
    print ("yes")
else:
    print("NO")
# enter tour number to check whether it is divisible 2 or not .
a=int(input("Enter your number:"))
# if statement No.1
if(a%2==0):
    print("Number is divisible by 2")
  #  if statement No.2
if(a%2==3):
    print("number is not divisible by 2 :")
else:
    print("None")

# write program to calculate the grade of a student from his marks from the following scheme.
marks=int(input("Enter your Markes : "))
if(marks<=100 and marks>90):
    print("The Student got : EX ")
elif (marks<=90 and marks>80):
    print("The Student got : A ")
elif(marks<=80 and marks>70):
    print("The Student got : B ")
elif(marks<=70 and marks>60):
    print("The Student got : C ")
elif(marks<=60 and marks>50):
    print("The Student got : D ")
else:
    print("The Student Has Failed .")



# 08 - List and Tuple
print("--- 08 List and Tuple ---")
marks_list = [78, 89, 90]
marks_list.append(100) # List is mutable
print(marks_list)
tup = (1, 2, 3) # Tuple is immutable
print(tup)
print("\n")

# a :-
# Write a program to store seven friuts in list entered by the user 

a=str(input("Enter your First Fruits:"))
b=str(input("Enter your second Fruits:"))
d=str(input("Enter your Fourth Fruits:"))
e=str(input("Enter your Fifth Fruits:"))
f=str(input("Enter your sixth Fruits:"))
g=str(input("Enter your seventh Fruits:"))
list=[a,b,d,e,f,g]
print(list)
list.append("Aniket")
print(list)
# b:-
# Write a program to print to marks of a student and desplay it into sorted maner.
m=(input("Enter your NO. :"))
s=(input("Enter your NO. :"))
z=(input("Enter your NO. :"))
b=(input("Enter your NO. :"))
d=(input("Enter your NO. :"))
p=(input("Enter your NO. :"))
list=[m,s,z,b,d,p]
print(list)
list.sort()
print(list) 

# c:-Write a program to sum a list with 4 numbers.
a=int(input("Enter your first number"))
b=int(input("Enter your Second number"))
c=int(input("Enter your Third number"))
d=int(input("Enter your four number"))
list=[a,b,c,d]
sum=(a+b+c+d)
print(list)
print(sum(list)


# 09 - Dictionary and Sets
print("--- 09 Dictionary and Sets ---")
info = {
    "name": "Aniket",
    "course": "Python"
}
print(info["name"])
collection = {1, 2, 2, 3} # Set removes duplicates
print(collection)
print("\n")

# 10 - Loops
print("--- 10 Loops ---")
# For loop
for i in range(1, 6):
    print(i)
# While loop
count = 1
while(count <= 3):
    print("Hello")
    count += 1
print("\n")
# Break Statements:-
for i in range(100):
    if(i==35):
        break  # Exit from the loop .
    print(i)

# Continue :-

#Example:-

for i in range(100):
    if(i==35):
        continue # skip this iteration.
    print(i)

# Example :-

for i in range (4):
    print("Printing")
    if i==2:
        continue
    print(i)

# Example :-
for i in range(645):
    pass
i=0
while(i<47):
    print(i)
    i=i+1

#     Quiz -----
#Que.1:-  Write a progarm to print multiplication table of given number.
n=int(input("Enter Your Number :"))
for i in range(1,11,):
    print(f" {n} X {i} = {n*i}" )

#Que.2:-  write a program to print the name start with s in the list.
l=["Harry","Sohan","Suraj","Rahul"]
for name in l:
    if(name.startswith("S")):
        print(f" Hello {name} ")


#Que.3:-  Do problem No.1 with while Loop.
n=int(input("Enter your Number :"))
i=1
while(i<11):
    print(f"{n} X {i} = {n*i} ")
    i=i+1
# Que.4:- Write a program to find the number is prime or not .
n=int(input("Enter Your Number :"))
for i in range(2,n):
    if((n%i)==0):
      print("Number is not prime ")
      break
else:
   print("Number is prime")

# 11 - Function and Recursion

print("--- 11 Function ---")
def my_func(name):
    print("Hello " + name)
my_func("Aniket")
print("\n")

# 12 - File I/O
print("--- 12 File I/O ---")
f = open("demo.txt", "w")
f.write("I am learning Python")
f.close()
print("File written successfully")
print("\n")
# program for read a file .
f=open("File.txt")
data=f.read()
print(data)
f.close()
# Program for write in file.
st="Hey Harry You r amazing"

f=open("myfile.txt","w")
f.write(st)
f.close()

# Program for read all the line using (Readlines(),Readline()).

f=open("File.txt")
lines=f.readlines()
print(lines, type(lines))

line0=f.readline()
print(line0,type(line0))

line1=f.readline()
print(line1, type(line1))

line2=f.readline()
print(line2, type(line2))

line3=f.readline()
print(line3, type(line3))

line4=f.readline()
print(line4, type(line4))
# Another Method to write this Program.

# line=f.readline()
# while(line!=""):
#     print(line,type(line))
#     line=f.readline()

f.close()

# 13 - OOPs
print("--- 13 OOPs ---")
class Student:
    def __init__(self, name):
        self.name = name
s1 = Student("Aniket Yadav")
print(s1.name)

# Advance Python:-

# MathCase:-
n=("Aniket")
match n:
    case 1:
        print("Yes")
    case 2:
        print("No")

    case _:
    
        print("Other") # if case 1 and case 2 doesn't match with variable's valur , default it prints the value .


#

x = 2

match x:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Other")

# Multiple values in one case :-

x = 3

match x:
    case 1 | 2:
        print("One or Two")
    case 3 | 4:
        print("Three or Four")  

# Variables:- 

data = ("Ani", 21)

match data:
    case (name,age):
        print(name, age)   
    case _:
        print("none")

# Conditional stat.:-

x = 5

match x:
    case 1   if x < 5:
        print("lower than 5")  

    case 2 if x > 5:
        print("5") 
    case _:
        print ("No one ")
    
x = 10

match x:
    case n if n < 5:
        print("Less than 5")
    case n if n > 5:
        print("Greater than 5")

# Merge Dictionary:-

# Union:-

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

result = d1 | d2
print(result)

# update :-
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

d1.update(d2)
print(d1)

# Wallrus Method :-

# Normal Method :-
n = len("Hello")
if n > 3:
    print(n)

# Walrus Method :-


if(n:=len("Hello"))>3:
    print(n)


data = input("Enter: ")
while (data != "exit"):
    print(data)
    # data = input("Enter: ")

# Walrus Method:

while(data:=input("Enter:")) != "exit":
    print(data)

# walrus Operator:-

numbers = [1, 2, 3, 4, 5]

if (n := len(numbers)) > 3:
    print(f"List is long: {n}")

# normal Way:-

number=[1,2,3,4,5]
m=len(number)
if(m>3):
    print (f"list is long {m}")

# Jion :-
a=["Aniket","Anupam","Anshu"]
final="::".join(a)
print(final)

# Format
a="{} is a good {}".format("Aniket","boy")
print(a)

# Lemda Function:-
# Normal Method:-
def square():
    n=int(input("Enter Your Number."))
    return n*n
print(square())

#Using Lembda Function:-
square=lambda x:x*x
print(square(int(input("Enter Your Number ."))))

# Map:-

l=[1,2,3,4,5]
square=lambda x:x*x
sqlist=map(square,l)
print(list(sqlist))

#example:-

l=[1,2,3,4,5]
def square(x):
    return x*x
print(list(map(square,l)))

# Filter :-
l=[1,2,3,4,5]
result=filter(lambda x:x%2==0,l)
print(list(result))


from functools import reduce
l=[1,2,3,4,5]
result=reduce(lambda x,y:x+y,l)
print(result)

# Mini Project :-
import random
'''
1 for snake
-1 for water
0 for gun
'''
computer=random.choice([1,-1,0])
youstr=input(" Enter Your Choice. ")      
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}
you=youDict[youstr]
print(f" You choose {reverseDict[you]}\n Computer choose {reverseDict[computer]} ")
if(computer==you):
    print("It's a Draw!")
else:
    if(computer== -1 and you== 1):
        print("You Win!.")

    elif(computer== -1 and you== 0):
        print("You Win!.")

    elif(computer== 1 and you== -1):
        print("You Loose!.")

    elif(computer== 1 and you== 0):
        print("You Loose!.")

    elif(computer== 0 and you== -1):
        print("You Loose!.")

    elif(computer== 0 and you== 1):
        print("You Win!.")

    else:
        print("somthing Went Wrong.")

# Asychronous programming :-
# // Normal Method Programming//
import time

def task(name):
    print(f"Start {name}")
    time.sleep(2)   # blocks execution
    print(f"End {name}")

task("A")
task("B")

# Output:-
# Start A
# End A
# Start B
# End B

# // Asynchronous programming //

import asyncio

async def task(name):
    print(f"Start {name}")
    await asyncio.sleep(2)   # non-blocking wait
    print(f"End {name}")

async def main():
    await asyncio.gather(
        task("A"),
        task("B")
    )

asyncio.run(main())









