# ==========================================================
# 11: FUNCTIONS & RECURSION PRACTICE
# ==========================================================

# --- PART 1: BASIC FUNCTIONS ---
def calc_average(num1, num2, num3):
    avg = (num1 + num2 + num3) / 3
    print(f"The average is: {avg}")
    return avg

print("--- Average Calculation ---")
calc_average(10, 20, 30)
print("\n")


# --- PART 2: TYPES OF FUNCTIONS ---

# 1. With Parameters & With Return
def add_numbers(a, b):
    return a + b

# 2. Default Arguments
def calc_product(a=2, b=4):
    result = a * b
    print(f"Product of {a} and {b} is: {result}")
    return result

print("--- Default Arguments ---")
calc_product()      # Uses 2 and 4
calc_product(5)     # Uses 5 and 4
print("\n")


# --- PART 3: RECURSION ---
def show_numbers(n):
    if n == 0: # Base Case
        return
    print(n, end=" ")
    show_numbers(n - 1) # Recursive Call

print("--- Recursion (Countdown) ---")
show_numbers(5)
print("\n")


# --- PART 4: PRACTICE EXERCISES ---

# Exercise: Length of String
def string_length(text):
    print(f"Length of '{text}': {len(text)}")
    return len(text)

# Exercise: Factorial
def calc_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"Factorial of {n} is: {fact}")
    return fact

# Exercise: USD to INR
def convert_usd_to_inr(usd):
    inr = usd * 50.35 # Fixed rate example
    print(f"${usd} USD is approx ₹{inr} INR")
    return inr

print("--- Practice Logic Results ---")
string_length("Aniket Yadav")
calc_factorial(5)
convert_usd_to_inr(100)
print("\n")


# --- PART 5: LOGIC CHALLENGES ---

# Divisible by 3 and 5
print("--- Divisible by 3 and 5 (1-100) ---")
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")
print("\n")

# Count divisible by 4 using Function
def count_divisible_by_4(limit):
    count = 0
    for i in range(1, limit + 1):
        if i % 4 == 0:
            count += 1
    return count

print(f"Numbers divisible by 4 (1-50): {count_divisible_by_4(50)}")

# ==========================================================
# Practice Session Complete!
# ==========================================================
