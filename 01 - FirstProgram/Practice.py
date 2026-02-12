# ==========================================
# Python Full Course Practice - Aniket Yadav
# ==========================================

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

# 08 - List and Tuple
print("--- 08 List and Tuple ---")
marks_list = [78, 89, 90]
marks_list.append(100) # List is mutable
print(marks_list)
tup = (1, 2, 3) # Tuple is immutable
print(tup)
print("\n")

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

# 13 - OOPs
print("--- 13 OOPs ---")
class Student:
    def __init__(self, name):
        self.name = name
s1 = Student("Aniket Yadav")
print(s1.name)
