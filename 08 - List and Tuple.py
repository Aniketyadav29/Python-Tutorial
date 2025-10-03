
# List:-

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

#List Methods:-
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
list.remove(3) # it removes the first occurrence of the specified element
print(list) 
list.pop() # it removes the last element of the list
print(list)
