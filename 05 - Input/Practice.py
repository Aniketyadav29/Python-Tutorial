# ==========================================================
# 05: USER INPUT & PRACTICE QUESTIONS
# ==========================================================

# --- PART 1: BASICS OF INPUT ---

# Default input (Always returns a String)
name = input("enter your name: ")
print("Welcome", name)

# Demonstrating Typecasting with Input
val_str = input("enter your value: ")
print("Type of default input:", type(val_str))

val_int = int(input("enter your value (int): "))
print("Type after int() conversion:", type(val_int))

val_float = float(input("enter your value (float): "))
print("Type after float() conversion:", type(val_float))

# Combined Input Summary
name = input("enter your name: ")
age = int(input("enter your age: "))
marks = float(input("enter your marks: "))

print("\n--- Summary ---")
print("Welcome:", name, "| Type:", type(name))
print("Age is :", age, "| Type:", type(age))
print("Marks  :", marks, "| Type:", type(marks))


# --- PART 2: INPUT BASED QUESTIONS ---

print("\n--- Question 1: Sum of Two Numbers ---")
num1 = int(input("enter your number 1: "))
num2 = int(input("enter your number 2: "))
sum_result = num1 + num2
print("The sum of the numbers is:", sum_result)

print("\n--- Question 2: Area of a Square ---")
side = int(input("enter your side of square: "))
area = side * side
print("The area of the square is:", area)

print("\n--- Question 3: Average of Floats ---")
f1 = float(input("enter number 1: "))
f2 = float(input("enter number 2: "))
average = (f1 + f2) / 2
print("The average of the numbers:", average)

print("\n--- Question 4: Comparison Logic ---")
a = int(input("enter your number a: "))
b = int(input("enter your number b: "))
print("a is greater than or equal to b:", a >= b)

# ==========================================================
# Practice Session Complete!
# ==========================================================
