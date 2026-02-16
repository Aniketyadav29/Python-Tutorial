# ==========================================================
# 09: DICTIONARIES & SETS PRACTICE
# ==========================================================

# --- PART 1: DICTIONARY BASICS ---
student = {
    "Name": "Aniket Yadav",
    "Class": "CS-3C",
    "College": "BBDU", #
    "City": "Lucknow"
}
print("--- Dictionary Basics ---")
student["Branch"] = "CSE"
student.update({"Marks": 90})
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("\n")

# --- PART 2: NESTED DICTIONARY ---
students = {
    "st1": {"Name": "Aniket", "Age": 20},
    "st2": {"Name": "Anupam", "Age": 22}
}
print("--- Nested Dictionary ---")
print("Student 1 Info:", students.get("st1"))
print("\n")

# --- PART 3: SET BASICS ---
collection = {1, 2, 3, 4, 5, 5, 5} # Duplicates will be removed
print("--- Set Operations ---")
print("Set Collection:", collection)
print("Length (Unique):", len(collection))

# Creating an empty set
null_set = set() 
print("Empty Set Type:", type(null_set))
print("\n")

# --- PART 4: SET METHODS & MATH ---
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print("Union:", s1.union(s2))         # {1, 2, 3, 4, 5}
print("Intersection:", s1.intersection(s2)) # {3}
print("\n")

# --- PART 5: PRACTICE QUESTIONS ---

# Question 3: Count unique subjects
print("--- Question 3: Unique Subjects ---")
subjects = {
    "python", "java", "c++", "python", "javascript", "java",
    "python", "java", "C++", "c"
}
print("Unique subjects count:", len(subjects))

# Question 5: Dictionary Input
print("\n--- Question 5: Marks Entry ---")
marks_dict = {}
phy = int(input("Enter Physics Marks: "))
marks_dict.update({"physics": phy})
math = int(input("Enter Math Marks: "))
marks_dict.update({"math": math})
print("Marks Dictionary:", marks_dict)

# Question 6: Storing 9 and 9.0 separately
print("\n--- Question 6: Separate 9 and 9.0 ---")
# Method 1: Using Tuples to distinguish type
values_tup = {("float", 9.0), ("int", 9)}
# Method 2: Using String for one
values_str = {"9.0", 9}
print("Set 1:", values_tup)
print("Set 2:", values_str)

#Write a program to store seven friuts in list entered by the user 

a=str(input("Enter your First Fruits:"))
b=str(input("Enter your second Fruits:"))
d=str(input("Enter your Fourth Fruits:"))
e=str(input("Enter your Fifth Fruits:"))
f=str(input("Enter your sixth Fruits:"))
g=str(input("Enter your seventh Fruits:"))
list=[a,b,d,e,f,g]
print(list)
list.append("Aniket")
print(list)

# Write a program to print to marks of a student and desplay it into sorted maner.
 Write a program to print to marks of a student and desplay it into sorted maner.
# m=(input("Enter your NO. :"))
# s=(input("Enter your NO. :"))
# z=(input("Enter your NO. :"))
# b=(input("Enter your NO. :"))
# d=(input("Enter your NO. :"))
# p=(input("Enter your NO. :"))
# list=[m,s,z,b,d,p]
# print(list)
# list.sort()
# print(list) 
 write a program that tuple type can not be changed .
# f=(23,45,78,90,"Aniket","Anupam",23.9,0.2)
# print(type(f))

# Write a program to sum a list with 4 numbers.
# a=int(input("Enter your first number"))
# b=int(input("Enter your Second number"))
# c=int(input("Enter your Third number"))
# d=int(input("Enter your four number"))
# list=[a,b,c,d]
# # sum=(a+b+c+d)
# print(list)
# print(sum(list))
 write a program that tuple type can not be changed .
# f=(23,45,78,90,"Aniket","Anupam",23.9,0.2)
# print(type(f))

Write a program to sum a list with 4 numbers.
a=int(input("Enter your first number"))
b=int(input("Enter your Second number"))
c=int(input("Enter your Third number"))
d=int(input("Enter your four number"))
list=[a,b,c,d]
# sum=(a+b+c+d)
print(list)
print(sum(list))


# write a program that tuple type ca

# write a program that tuple type ca

# ==========================================================
# Practice Session Complete!
# ==========================================================
