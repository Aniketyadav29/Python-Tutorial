# ==========================================================
# 07: CONDITIONAL STATEMENTS PRACTICE
# ==========================================================

# --- PART 1: BASIC IF-ELIF-ELSE ---
light = "pink"

print("--- Traffic Light Logic ---")
if light == "red":
    print("you should stop")
elif light == "yellow":
    print("you should get ready")
elif light == "green":
    print("you can go")
else:
    print("invalid color")
print("\n")


# --- PART 2: IF VS ELIF (The Difference) ---
num = 5
print("--- Multiple 'if' Blocks (Checks both) ---")
if num > 2:
    print("num is greater than 2")
if num > 4:
    print("num is greater than 4")

print("\n--- 'if-elif' Chain (Checks until True) ---")
if num > 2:
    print("num is greater than 2")
elif num > 4:
    print("num is greater than 4") # This will not print
print("\n")


# --- PART 3: NESTED IF-ELSE ---
print("--- Nested Logic Check ---")
age = 25
if age >= 18:
    if age >= 29:
        print("you are eligible for voting")
    else:
        print("you are not eligible for voting yet")
else:
    print("you are a minor")
print("\n")


# --- PART 4: PRACTICE QUESTIONS ---

# Question 1: Student Grades
print("--- Question 1: Grading System ---")
marks = int(input("enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D")

# Question 2: Even or Odd
print("\n--- Question 2: Even or Odd ---")
x = int(input("Enter Your Number: "))
if x % 2 == 0:
    print("The Number is Even")
else:
    print("the Number is Odd")

# Question 3: Greatest of Three
print("\n--- Question 3: Greatest Number ---")
n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))

if n1 >= n2 and n1 >= n3:
    print("Greatest is n1:", n1)
elif n2 >= n1 and n2 >= n3:
    print("Greatest is n2:", n2)
else:
    print("Greatest is n3:", n3)

# Question 4: Multiple of 7
print("\n--- Question 4: Multiple of 7 ---")
m = int(input("Enter your number: "))
if m % 7 == 0:
    print("The Number is Multiple by 7")
else:
    print("The Number is not Multiple by 7")

# ==========================================================
# Practice Session Complete!
# ==========================================================
