# Loops:- Loops are used to execute a block of code repeatedly until a certain condition is met.

# While loop :-
 # While Condition :- 
# Example No.1:- 
count=0 # Iterator Initialization.
while (count<5): # Stopping Condition.
    print("hello world")
    count+=1 # Iterator Update.
print("loop ended")

# secomd example:-
i=1  # Iterator Initialization.
while (i<=10): # Stopping Condition.
    print("hello world",i)
    i+=1 # Iteration Update.
print("Loop Ended")

# Example No.4:- print reverse numbers from 10 to 1.
i=10
while(i>=1): # Stopping Condition.
    print(i)
    i-=1
print("loop ended")

# Example No.5:- print number from 1 to 10.
i=1
while(i<=10): # Stopping Condition.
    print(i)
    i+=1
    print("loop ended")


# practice :- print numbers from 1 to 100
i=1
while(i<=100): # Stopping Condition.
    print(i)
    i+=1
print("Loop Ended")

# practice :- print even numbers from 100 to 1 
i=100
while(i>=1): # Stopping Condition.
    print(i)
    i-=1
print("Loop Ended")

# practice :- print even numbers from 100 to 1 
i=100
while(i>=1): # Stopping Condition.
    print(i)
    i-=1
print("Loop Ended")

# practice :- print a multiplication table of a number n.
n=int(input("Enter your number:"))
i=1
while(i<=10): #Stopping Condition.
    print(n,"x",i,"=",n*i)
    i+=1
print("Loop Ended")

# practice :- print the elements of a list using while loop.
[1,4,9,16,25,36,49,64,81,100]
i=1
while(i<=10):  # Stopping Condition.
    print(i*i)
    i+=1
print("Loop Ended ")

# practice :- print odd numbers from 1 to 100.
i=1 # Iterator Initialization.
while(i<=100):   # Stopping condition.
    print(i) # Print Statement.
    i+=2 # Iterator Update.
print("Loop Ended") # Loop Ended Statement.

# practice :- 
heroes=["Ironman","Captain America","Thor","Hulk","Black Widow","Hawkeye"]
# traverse the list using while loop and print each hero name.
i=0
while i < len(heroes): # Stopping Condition.
    print(heroes[i]) # Print Statement.
    i+=1 # Iterator Update.
print("Loop Ended")

# practice:- Search for a number x in this tuple using while loop.
nums=[1,4,9,16,25,36,49,64,81,100]
x=36
i=1
while(i<=10):
    if (nums[i]==x):
        print("found at index:",i)
        break
    i+=1
print("Loop Ended")

# Break & Continue :- 

# Break:- Break statement is used to terminate the loop when a certain condition is met.
# Continue :- terminates the current iteration of the loop and jumps to the next iteration.

# Example of Break:-
i=1
while(i<=10): # Stopping Condition.
    print(i)
    if (i==5):
        break # it will terminate the loop when i is equal to 5
    i+=1
print("Loop Ended")

# Example No.2 of Break:-

nums=[1,4,9,16,25,36,49,64,81,100]
x=36
i=1
while(i<=10):
     if (nums[i]==x):
         print("found at index:",i)
         break
     i+=1
     print("finding")

#  Example of Continue:-
i=0
while(i<10): # Stopping Condition.
    i+=1
    if (i==5):
        continue # it will skip the iteration when i is equal to 5
    print(i)

# For Loop:- For loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.

veggies=["carrot","broccoli","spinach","potato","onion"]
for value in veggies: # Iteration Variable.
 print(value) # Print Statement.

# Examole No.2:- 
tup=(1,2,3,4,5)
for num in tup: # Iteration Variable.
     print(num) # Print Statement.

# Example No.3:-
str="Aniket Yadav"
for char in str: # Iteration Variable.
    print(char) # Print Statement.

# Example No.4:-
str="Aniket Yadav"
for char in str: # Iteration Variable.
    if(char == "v"):
        print("Found it!")
        break
    print(char) # Print Statement.

# practice :- print the elements from following list using for loop.
nums=[1,4,9,16,25,36,49,64,81,100]
list=[1,4,9,16,25,36,49,64,81,100]
for val in list: # Iteration Variable.
    print(val) # Print Statement.
# Practice :- 
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 100

idx = 0
for el in nums:  # Iteration Variable.
    if (el == x):
        print(f"found it at index: {idx}!")
        break  # Stop the loop once the element is found
    idx += 1  # Increment the index for the *next* element check

# Range Function:- Range function is used to generate a sequence of numbers.Start from 0 by default and increments by 1 (by default) and stops before a specified number.
# Example No.1:-
seq= range(5) # Iteration Variable.
for i in seq: # Iteration Variable.
    print(i) # Print Statement.

Range(start?,stop,step?):-
seq= range(5) # Iteration Variable. # range(stop)
for i in seq: # Iteration Variable.
    print(i) # Print Statement.

seq1= range(2,10) # Iteration Variable. # range(start,stop)
for i in seq1: # Iteration Variable.
    print(i) # Print Statement.

seq2= range(1,10,2) # Iteration Variable. # range(start,stop,step)
for i in seq2: # Iteration Variable.
    print(i) # Print Statement.

# Example No.2:-
for i in range(2,100,2): # Iteration Variable.
    print(i) # Print Statement.

# Practice :-
for i in range(1,101,1): # Iteration Variable.
    print(i) # Print Statement.

# Practice :-
for i in range(101,0,-1): # Iteration Variable.
    print(i) # Print Statement.


# Practice :-
n=int(input("Enter your number:"))
for i in range(1,11): # Iteration Variable.
    print(n,"x",i,"=",n*i) # Print Statement.
 
# Practice:-WAP a program to find the sum of first n numbers using while loop.

n=int(input("Enter your number:"))
sum=0
for i in range(1,n+1): # Iteration Variable.
    
    sum=sum+i # Print Statement.
print("The sum of first n numbers is:",sum)

# using while loop
n=int(input("Enter your Number:"))
sum=0
i=1
while(i<=n): # Stopping Condition.
    sum=sum+i # Print Statement.
    i+=1
print("The sum of first n numbers is:",sum)

# practice:- WAP to find the factorial of a number using for loop.
n=int(input("Enter your number:"))
factorial=1
for i in range(1,n+1): # Iteration Variable.
    factorial=factorial*i # Print Statement.  
print("The factorial of the number is:",factorial)

# using while loop
n=int(input("Enter your number:"))
factorial=1
i=1
while(i<=n): # Stopping Condition.
    factorial=factorial*i # Print Statement.
    i+=1













