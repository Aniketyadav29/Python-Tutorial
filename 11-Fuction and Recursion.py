
# Function:- Function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

a=4
b=3

sum=a+b 
print(sum) #print("This is addition function")

#Example 1:-
   
# A.
def add_numbers(a,b): # Function Definition.
    sum=a+b
    print("The sum is:",sum) # Print Statement.
# Function Call.
add_numbers(4,3)
# B.
def print_even(n):
    for i in range(1,n+1):
        print(i*2)
print_even(5)

# C.
def power(base,exp):
    return base**exp
print(power(3,3))

# Example No.2:-
def calc_area(Length,Breadth):
    area=Length*Breadth
    print("The area of the rectangle is:",area)
    return area
calc_area(5,10)

# Example No.3:-
def print_hello():
    print("Hello World")
print_hello()
print_hello()   
print_hello()
print_hello()
print_hello()

# Example No.4:-
#Calculate the average of 3 numbers.
def calc_average(num1,num2,num3):
    average=(num1+num2+num3)/3
    print("the averageof the numbers is :", average)
    return average
calc_average(10,20,30)

# Example No.5:-
a=num1=int(input("Enter your first number:"))
b=num2=int(input("Enter your second number:"))
c=num3=int(input("Enter your third number:"))
Average=(a+b+c)/3
print("the average of the numbers is :",Average)
calc_average(a,b,c)

# types of function:-
# 1. Function without parameters and without return type.
# 2. Function with parameters and without return type.
# 3. Function without parameters and with return type.
# 4. Function with parameters and with return type.

# 1. Function without parameters and without return type.
def greet():
    print("Hello, Welcome to Python Programming")   
greet()
# 2. Function with parameters and without return type.
def greet_user(name):
    print("Hello",name,"Welcome to Python Programming")
greet_user("Aniket Yadav")
greet_user("Anupam Lata Yadav")
# 3. Function without parameters and with return type.
def get_greeting():
    return "Hello, Welcome to Python Programming"
message=get_greeting()
print(message)
# 4. Function with parameters and with return type.
def add_numbers(a,b):
    return a+b
sum=add_numbers(5,10)
print("The sum of a and b is:",sum)
sum=add_numbers(20,30)
print("The sum of a and b is:",sum)# Default Arguments:- Default arguments are the arguments that are passed to the function when no value is provided for that argument.
def calc_product(a=2,b=4):
    product=a*b
    print("The product of a and b is:",product)
    return product
calc_product() # it will use the default values of a and b
calc_product(5) # it will use the default value of b

#Exercise:-
# WAF to print the length of the string.
def string_length(a):
    length=len(a)
    print("The length of the string is:",length)
    return length
string_length("Aniket Yadav")
string_length("Apna College")
#WAF to print the element of a list in a single line . (list is a parameter )
def print_list_elements(lst):
    for element in lst:
        print(element, end=' ')
    print()  # for newline after printing all elements

print_list_elements([1, 2, 3, 4, 5])
# WAF to find the factorial of a number n.
def calc_factorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
    print("The factorial of the number is:",factorial)
    return factorial    
calc_factorial(5)
calc_factorial(7)
#WAF to convert USD to INR.
def convert_usd_to_inr(usd):
    inr=usd*50.35
    print(inr)
    return inr
convert_usd_to_inr(100)

# Recursion:- Recursion is a process in which a function calls itself directly or indirectly. 
#The main idea of recursion is to break a complex problem into smaller sub-problems that are easier to solve.
# Recursive Function:-
def show(n):
    if(n==0): # Base Case.
        return
    print(n)
    show(n-1)   
show(5)

# how will you print all numbers between 1 and 100 which are divisible by 3 and 5 ?
for i in range(1,100):
    if i%3==0 and i%5==0:
        print(i)

# print age category of a person based on age
def age_catagory(age):
    if age>60:
        print("senior")
    else:
        print("junior")
age_catagory(65)








