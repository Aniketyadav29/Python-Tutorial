# OOPs:- object-oriented programming is a programming paradigm that uses "objects" to design software. An object is an instance of a class. A class is a blueprint for creating objects. OOPs is used to structure a program into simple,
#  reusable pieces of code blueprints (usually called classes), which are used to create individual instances of objects. 
# Object:- An object is an instance of a class. It is a real-world entity that has attributes and behavior.
# Class:- A class is a blueprint for creating objects. It is a user-defined data type that contains attributes and methods.
# Attribute:- An attribute is a characteristic of an object. It is a variable that is associated with an object.
# Method:- A method is a function that is associated with an object. It is a behavior of an object. 

# Example No.1:-
#creating a class:-
class student:
    name="Aniket Yadav" # attribute
    age=26  # attribute 

#creating an object:-
s1=student()
print(s1.name) # accessing attribute
print(s1.age)  # accessing attribute

# Example No.2:-
class Car:
    brand="Toyota" # attribute
    model="Camry"  # attribute
    year=2020      # attribute
    color="Red"    # attribute

car1=Car()
print(car1.brand) # accessing attribute
print(car1.model) # accessing attribute
print(car1.year)  # accessing attribute
print(car1.color) # accessing attribute.

#Constructor:- A constructor is a special method that is called when an object is created. It is used to initialize the attributes of the object. In Python, the constructor is defined using the __init__() method.

#Creating a class with constructor

class student:
    def __init__(self): # constructor
        self.name="Full Name" # attribute.

# creating an object
s1=student("Aniket Yadav")
print(s1.name) # accessing attribute.

s2=student("Anupam Lata Yadav")
print(s2.name) # accessing attribute.

# Example No.3:-
class student:
    def __init__(self,name,age): # constructor
        self.name=name  # attribute
        self.age=age    # attribute.

s1=student("Aniket Yadav",26)
print(s1.name) # accessing attribute
print(s1.age)  # accessing attribute.

#Attribute:-
class Student:
    College="Apna College" # class attribute
    def __init__(self,name,age): # constructor
        self.name=name  # instance attribute
        self.age=age    # instance attribute

s1=Student("Aniket Yadav",26)
print(s1.name) # accessing instance attribute
print(s1.age)  # accessing instance attribute
print(s1.College) # accessing class attribute.
s2=Student("Anupam Lata Yadav",22)
print(s2.name) # accessing instance attribute
print(s2.age)  # accessing instance attribute
print(s2.College) # accessing class attribute.

# obj Attributes > class Attributes.#

# Methods:- A method is a function that is associated with an object. It is a behavior of an object. In Python, methods are defined using the def keyword.

# Example:-

class Dresses:
    def __init__(self, first, last, product, price):
        self.first = first
        self.last = last
        self.product = product
        self.price = price
        self.email = f'{first}.{last}@gmail.com'

    def product_details(self):
        return f"{self.first} {self.last} bought {self.product} for {self.price} rupees"
lady_1 = Dresses('Anupam', 'Lata', 'Kurti', 1000)
lady_2 = Dresses('Anushka', 'Singh', 'Saree', 2000)
lady_3 = Dresses('Anu', 'Kushawaha', 'Top', 999)

print(lady_1.product_details())
print(lady_2.email)
print(lady_3.product)






