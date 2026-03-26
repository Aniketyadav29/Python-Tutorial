n=("Aniket")
match n:
    case 1:
        print("Yes")
    case 2:
        print("No")

    case _:
    
        print("Other") # if case 1 and case 2 doesn't match with variable's valur , default it prints the value .


#

x = 2

match x:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Other")

# Multiple values in one case :-

x = 3

match x:
    case 1 | 2:
        print("One or Two")
    case 3 | 4:
        print("Three or Four")  

# Variables:- 

data = ("Ani", 21)

match data:
    case (name,age):
        print(name, age)   
    case _:
        print("none")

# Conditional stat.:-

x = 5

match x:
    case 1   if x < 5:
        print("lower than 5")  

    case 2 if x > 5:
        print("5") 
    case _:
        print ("No one ")
    
x = 10

match x:
    case n if n < 5:
        print("Less than 5")
    case n if n > 5:
        print("Greater than 5")
