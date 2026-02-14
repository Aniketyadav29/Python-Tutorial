# ==========================================================
# 13: OBJECT-ORIENTED PROGRAMMING (OOPs) PRACTICE
# ==========================================================

# --- PART 1: BASIC CLASS & OBJECT ---
class Car:
    brand = "Toyota"
    model = "Camry"
    year = 2020
    color = "Red"

car1 = Car()
print("--- Basic Class Attributes ---")
print(f"Car: {car1.brand} {car1.model} ({car1.year})")
print("\n")


# --- PART 2: CONSTRUCTORS (__init__) & ATTRIBUTES ---
class Student:
    college = "BBDU"  # Class Attribute (Shared by all)

    def __init__(self, name, age, marks):
        self.name = name    # Instance Attribute (Unique)
        self.age = age      # Instance Attribute
        self.marks = marks  # Instance Attribute

    def get_result(self):
        if self.marks >= 60:
            return "Pass"
        else:
            return "Fail"

s1 = Student("Aniket Yadav", 26, 85)
s2 = Student("Anupam Lata Yadav", 22, 55)

print("--- Student Info & Results ---")
print(f"Student: {s1.name} | College: {s1.college} | Result: {s1.get_result()}")
print(f"Student: {s2.name} | College: {s2.college} | Result: {s2.get_result()}")
print("\n")


# --- PART 3: METHODS & BEHAVIORS ---
class Dresses:
    def __init__(self, first, last, product, price):
        self.first = first
        self.last = last
        self.product = product
        self.price = price
        self.email = f"{first.lower()}.{last.lower()}@gmail.com"

    def product_details(self):
        return f"{self.first} {self.last} bought {self.product} for ₹{self.price}"

lady_1 = Dresses('Anupam', 'Lata', 'Kurti', 1000)
lady_2 = Dresses('Anushka', 'Singh', 'Saree', 2000)

print("--- Product/Methods Example ---")
print(lady_1.product_details())
print(f"Contact: {lady_2.email}")
print("\n")


# --- PART 4: HANDLING MULTIPLE OBJECTS (LOGIC) ---
# Creating a list of Student objects
classroom = [
    Student("Amit", 20, 80),
    Student("Ravi", 21, 45),
    Student("Neha", 19, 90)
]

print("--- Students who Passed (Marks >= 60) ---")
for student in classroom:
    if student.get_result() == "Pass":
        print(f"Name: {student.name} ({student.marks} marks)")

# ==========================================================
# Practice Session Complete!
# ==========================================================
