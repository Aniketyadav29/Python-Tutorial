
# Normal Method :-
n = len("Hello")
if n > 3:
    print(n)

# # Walrus Method :-


if(n:=len("Hello"))>3:
    print(n)


data = input("Enter: ")
while data != "exit":
    print(data)
    data = input("Enter: ")

# # Walrus Methid:

while(data:=input("Enter:")) != "exit":
    print(data)

#walrus Operator:-

numbers = [1, 2, 3, 4, 5]

if (n := len(numbers)) > 3:
    print(f"List is long: {n}")

# normal Way:-

number=[1,2,3,4,5]
m=len(number)
if(m>3):
    print (f"list is long {m}")
