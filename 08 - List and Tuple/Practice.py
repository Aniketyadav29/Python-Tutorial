# ==========================================================
# 08: LISTS & TUPLES PRACTICE
# ==========================================================
#Example :-
l1=[2,4,3,6,7,9,5,]
l1.sort()
print(l1)
l1.insert(2,333)
print(l1) 
l1.pop(2)
l1.append("87")
print(l1)
l1.remove(9)
print(l1)
l1.reverse()
print(l1)


# --- PART 1: LIST BASICS & MUTABILITY ---
fruits = ["apple", "banana", "orange", "grape", "kiwi", 90, 67, 45, 23, 12]
fruits.insert(2, "Watermelon")
fruits.remove("banana")
fruits[0] = "Pineapple"  # Proving mutability
print("--- Updated Fruits List ---")
print(fruits)
print("\n")

# --- PART 2: LIST SLICING ---
marks = [23, 56.3, 56, 78, 90]
print("--- List Slicing ---")
print("Full List:    ", marks)
print("Slice [1:4]:  ", marks[1:4])
print("Negative [-3:-1]:", marks[-3:-1])
print("\n")

# --- PART 3: TUPLE BASICS & IMMUTABILITY ---
# a:-
tup = (1, 2, 3, 4, 5, 3)
print("--- Tuple Operations ---")
print("Type: ", type(tup))
print("Count of 3:", tup.count(3))
print("Index of 4:", tup.index(4))
# tup[0] = 6  # This would raise a TypeError
print("\n")

# b:-
a=(1,2,3,4 ,False,"Rohan","Shivam")
print(type(a))
print(a)
b=(1)
print(b)

no=a.count(45)
print(no)
c=a.index(3)
print(c)
print(len(a))



# --- PART 4: PRACTICE QUESTIONS ---

# Question 1: Palindrome Check
print("--- Question: Palindrome Check ---")
list1 = [1, 2, 1]
copy_list1 = list1.copy()
list1.reverse()
if list1 == copy_list1:
    print("The list is palindrome")
else:
    print("The list is not palindrome")

# Question 2: Grade Counting
print("\n--- Question: Grade Counting ---")
grades = ("A", "B", "C", "A", "D", "A", "B")
print("Total 'A' Grades:", grades.count("A"))

# Question 3: Summing a List
print("\n--- Question: Sum of 4 Numbers ---")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
num_list = [a, b, c, d]
print("List:", num_list)
print("Total Sum:", sum(num_list))

# Question 4: Count Zeros in Tuple
print("\n--- Question: Count Zeros ---")
zeros_tup = (0, 3, 0, 4, 0, 5, 0, 62, 0, 9)
print("Number of zeros:", zeros_tup.count(0))

# ==========================================================
# Practice Session Complete!
# ==========================================================
