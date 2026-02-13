# ==========================================================
# 06: STRINGS & MANIPULATION PRACTICE
# ==========================================================

# --- PART 1: DEFINITIONS & ESCAPE CHARACTERS ---
str1 = "my name is aniket yadav "
str2 = 'this is aniket yadav'
str3 = """ my name is banku """

# Using Escape Sequences
str4 = "This is string.\nwe are using it in python."
print("--- Escape Sequence ---")
print(str4)
print("\n")


# --- PART 2: BASIC OPERATIONS ---
print("--- Concatenation & Length ---")
print("Joined String:", str1 + str2)
print("Length of str1:", len(str1))
print("\n")


# --- PART 3: INDEXING & SLICING ---
print("--- Indexing ---")
print("Index 1 of str1:", str1[1])
print("Index 5 of str2:", str2[5])

print("\n--- Slicing ---")
print("Slice [1:4] str1:", str1[1:4])
print("Slice [:7] str2: ", str2[:7])  # Starts from 0
print("Slice [4:] str3: ", str3[4:])  # Goes to end

print("\n--- Negative Slicing ---")
word = "apple"
print("Slice [-3:-2] apple:", word[-3:-2])
print("Slice [-5:-2] apple:", word[-5:-2])
print("\n")


# --- PART 4: STRING FUNCTIONS ---
text = "this is apna college and i am learning python"
print("--- String Functions ---")
print("Ends with 'thon'?:", text.endswith("thon"))
print("Capitalized:     ", text.capitalize())
print("Find 'apna':     ", text.find("apna"))
print("Replace 'apna':  ", text.replace("apna", "our"))
print("Count 'is':      ", text.count("is"))
print("\n")


# --- PART 5: PRACTICE QUESTIONS ---

# Question 1: Input name and print length
print("--- Question 1 ---")
user_name = input("Enter your name: ")
print("The length of your name is:", len(user_name))

# Question 2: Find occurrence of $
print("\n--- Question 2 ---")
dollar_str = input("Enter your string: ")
print("The occurrence of $ in the string is:", dollar_str.count('$'))

# ==========================================================
# Practice Session Complete!
# ==========================================================
