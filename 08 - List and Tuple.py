
# List:- List is mutable .

Marks=[23,56.3,56,78,90]
print(Marks)
print(type(Marks))
print(Marks[0])
print(Marks[1])
print(Marks[2])

Student=["Aniket",56,23,"Anupam Lata Yadav"]
print(Student)
print(len(Student))

# List is mutable in python:-

Student[0]="Anshu"
print(Student)

# List Slicing:-
Mark=[23,56.3,56,78,90]
print(Mark[1])
print(Mark[1:4])
print((Mark[:4]))
print(Mark[1:])
print(Marks[-3:-1]) 

# List Methods:-
List=[3,1,2]
 List.sort() # it sorts the list in ascending order
 print(List)
 List.reverse() # it reverses the list
 print(List)
 List.append(4) # it adds an element at the end of the list
 print(List)
List.insert(2,5) # it adds an element at the specified index
 print(List)
 List.remove(5) # it removes the specified element
 print(List)

list=[1,2,3,3,5]
list.remove(3) # it removes the first occurrence of the specified element.
print(list) 
list.pop() # it removes the last element of the list.
print(list)
list.append(6) # it adds an element at the end of the list.
print(list)


# Tuple:- Tuple is immutable in python. it means we cannot change the elements of the tuple.it's a built-in data type in python.

tup=(1,2,3,4,5)
print(type(tup))
print(tup[0])
print(tup[1:4])
print(tup[-3:-1])
# tup[0]=6 # it will give an error because tuple is immutable.

#Tuple Methods:-
tup=(1,2,3,4,5,3)
print(tup.count(3)) # it counts the number of occurrences of the specified element.
print(tup.index(4)) # it returns the index of the first occurrence of the specified element.
print(tup.sort()) # it will give an error because tuple is immutable.
print(tup.reverse()) # it will give an error because tuple is immutable.

# Practice:-
# Question 1:- WAP to ask user to enter his favorite 5 movies and store them in a list.
movies=[]
for i in range(5):
     movie=input("Enter your favorite movie:")
     movies.append(movie)
print("Your favorite movies are:",movies)

# Another Method:-
movies=[]
mov1=input("Enter your favorite movie1:")
mov2=input("Enter your favorite movie2:")
mov3=input("Enter your favorite movie3:")
mov4=input("Enter your favorite movie4:")
mov5=input("Enter your favorite movie5:")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
movies.append(mov4)
movies.append(mov5)
print("Your favorite movies are:",movies)

# Question :- WAP a program to check palindrome or not.
list1=[1,2,1]
list2=[1,2,3]
copy_list1=list1.copy()
list1.reverse()
if (list1==copy_list1):
    print("The list is palindrome")
else:
    print("The list is not palindrome")

# Question :- WAP to count the number of students with "A" grade in the following tuple.
grades=("A","B","C","A","D","A","B")
count=grades.count("A")
print("The number of students with A grade is:",count) 








