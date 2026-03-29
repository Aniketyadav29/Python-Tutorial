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
# 

l=[1,2,3,4,5]
def square(x):
    return x*x
print(list(map(square,l)))

# Filter :-
l=[1,2,3,4,5]
result=filter(lambda x:x%2==0,l)
print(list(result))


from functools import reduce
l=[1,2,3,4,5]
result=reduce(lambda x,y:x+y,l)
print(result)

