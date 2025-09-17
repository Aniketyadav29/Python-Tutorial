#Type Conversion
#Implicit Type Conversion

a=5
b=2.0
c=a+b
print("The value of c is:",c)# c is float because b is float, so a is converted to float, a = 5.0 and b = 2.0
print("The type of a is:",type(a)) # type of a is int
print("The type of c is:",type(c)) # type of c is float


# Explicit Type Conversion
a="5"
b=4.05
a=int(a) # converting string to int,because a is string
print("The type of a is:",type(a)) # type of a is int
c=a+b
print("The value of c is:",c) # c is float because b is float, so a is converted to float, a = 5.0 and b = 4.05
print("The type of c is:",type(c)) # type of c is float

