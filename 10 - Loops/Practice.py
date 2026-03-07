# ==========================================================
# 10: LOOPS (WHILE & FOR) PRACTICE
# ==========================================================

# --- PART 1: WHILE LOOP BASICS ---
print("--- Reverse Numbers 10 to 1 ---")
i = 10
while i >= 1:
    print(i, end=" ")
    i -= 1
print("\nLoop Ended\n")


# --- PART 2: BREAK & CONTINUE ---
print("--- Break Example (Stop at 5) ---")
i = 1
while i <= 10:
    if i == 5:
        break
    print(i, end=" ")
    i += 1
print("\n")

print("--- Continue Example (Skip 5) ---")
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i, end=" ")
print("\n")


# --- PART 3: FOR LOOP & RANGE ---
print("--- Iterating over a String ---")
name = "Aniket Yadav"
for char in name:
    if char == " ": continue
    print(char, end="-")
print("\n")

print("--- Range Function (Start, Stop, Step) ---")
# Even numbers from 2 to 10
for i in range(2, 11, 2):
    print(i, end=" ")
print("\n")


# --- PART 4: PRACTICE QUESTIONS ---

# Question: Multiplication Table
print("--- Question: Multiplication Table ---")
n = int(input("Enter number for table: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

# Question: Sum of first N numbers
print("\n--- Question: Sum of N numbers ---")
num = int(input("Enter N: "))
total_sum = 0
for i in range(1, num + 1):
    total_sum += i
print(f"The sum of first {num} numbers is: {total_sum}")

#Question:-write a program to print the name start with s in the list.
l=["Harry","Sohan","Suraj","Rahul"]
for name in l:
    if(name.startswith("S")):
        print(f" Hello {name} ")

#Question:-  Do problem print table with while Loop.
n=int(input("Enter your Number :"))
i=1
while(i<11):
    print(f"{n} X {i} = {n*i} ")
    i=i+1


# Question:- Write a program to find the number is prime or not .
n=int(input("Enter Your Number :"))
for i in range(2,n):
    if((n%i)==0):
      print("Number is not prime ")
      break
else:
   print("Number is prime")

# Question: Factorial
print("\n--- Question: Factorial ---")
f_num = int(input("Enter number for Factorial: "))
fact = 1
for i in range(1, f_num + 1):
    fact *= i
print(f"The factorial of {f_num} is: {fact}")

# Question: List Traversal
print("\n--- Question: Traversing Heroes ---")
heroes = ["Ironman", "Captain America", "Thor", "Hulk"]
for hero in heroes:
    print("Hero Name:", hero)

# Question.5:- Write a program to find the sum of first n naturals numbers using while loop .
n=int(input("Enter your Number."))
i=1
sum=0
while(i<=n):
    sum+=i
    i=i+1
print(sum)

# Question.6:- Write a program to find the factorial of the given number using for loop.
n=int(input("Enter Your Number."))
product=1
for i in range(1,n+1):
    product=product*i
print(f"The factorial of {n} is {product}")


# Question.7:- Write a program to print star pattern
For n=3
 *
***
***** 

n=int(input("Enter your Number."))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("")

# Question.8:- Write a program to print the following star pattern .
n=int(input("Enter Your Number."))
for i in range(1,n+1):
    print("*"*i,end="")
    print("")

 # Question.9:-  write a program to print the following star pattern.
 # * * *
 # *   *
 # * * * for n=3
n=int(input("Enter Your Number."))
for i in range(1,n+1):
    if (i==1 or i==n ):
       print("*"*n)
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
        print("")

# ==========================================================
# Practice Session Complete!
# ==========================================================
