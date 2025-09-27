# Conditional Statements in pyton:-

# if statement

age=23
if(age>=18):
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

# difference between if and elif:-

#if statement:- if statement is used to execute a block of code if a specified condition is true. if the condition is false, the block of code is skipped.
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
