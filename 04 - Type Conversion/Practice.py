# 04 & 05: TYPE CONVERSION PRACTICE
# ==========================================

# 1: IMPLICIT TYPE CONVERSION :-
# Automatically converts data types without loss of info.

a = 5
b = 2.0
c = a + b

print("--- Implicit Conversion ---")
print("The value of c is:", c)      # Result is 7.0 (float)
print("The type of a is:", type(a)) # type is int
print("The type of c is:", type(c)) # type is float
print("\n")


# 2: EXPLICIT TYPE CONVERSION :-
# Manually converting types using int(), float(), str(), etc.

a = "5"
b = 4.05

# Converting string to int manually
a = int(a) 

print("--- Explicit Conversion ---")
print("The type of a is:", type(a)) # type is now int
c = a + b
print("The value of c is:", c)      # Result is 9.05
print("The type of c is:", type(c)) # type is float

# ==========================================
# Practice Session Complete!
# ==========================================
