print(10 / 0) # program crash 


# with Handling :-

try:
    print(10 / 0)
except:
    print("Error handled")


v=int(input("Enter Your Number :"))
print("w") # make a error (str)

try:
    v=int(input("Enter Your Number :"))
    print("w") # make a error (str)

except:
  print("None")

print("Thank You.")

# Finally :-
try:
   print(10/0)
except:
   print("yes")
finally:
  print("I am Aniket Yadav .") # it always print the value either the try block run or not run .

# Global Variable :-
a=45

def func():
   a=23
   print(a)

func()
print(a)

# Enumerate fuc():-

l=[3,4,5,7,8]
for index ,item in enumerate(l):
   print(index,item)

# List comprehension :-
mylist=[1,2,3,4,6,7]
squaredlist=[]
for item in mylist:
   squaredlist.append (item*item)
print(squaredlist)

# OR

squarelist=[item*item for item in mylist]
print(squarelist)

# Practice:-
try:
   with open("2.txt","r")as f:
    print(f.read())
except:
  print("Exception as e .")
try:
   with open("2.txt","r")as f:
    print(f.read())
except:
  print("Exception is not in the file 2")
try:
   with open("3.txt","r")as f:
    print(f.read())

except:
  print("Exception not in the filr 3.")


#

l=[1,2,3,4,5,6,7,8,9]
for i , item in enumerate(l):
  if i==1 or i==2 or i==4 or i==6:
    print(list[item])

l=int(input("Enter Your Number."))
mylist=[]
for i in range(1,11):
  mylist.append(i*l)
print(mylist)

#list Comprehension :


l=int(input("Enter Your Number."))
mylist=[i*l for i in range(1,11)]
print(mylist)

#

try:
    a=int(input("Enter your Number."))
    b=int(input("Enter Your Number"))
    print(a/b)
except ZeroDivisionError :
    print("infinite")

with open("Table.txt","w") as f:
   n=int(input("enter your Number."))
   result=[i*n for i in range(1,11)]
   f.write(str(result) + "\n")
