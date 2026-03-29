# Normal Method:-
def square():
    n=int(input("Enter Your Number."))
    return n*n
print(square())

# Lemda Function:-

square=lambda x:x*x
print(square(int(input("Enter Your Number ."))))

# Map:-

l=[1,2,3,4,5]
square=lambda x:x*x
sqlist=map(square,l)
print(list(sqlist))

