# Dictionary and Sets in Python:-

# Dictionary :- Dictionary are used to store data value in keys ; value = pair.
# they are unorderd ,Mutable,can't accept duplicate keys.
# Example :-1 
Student={
    "Name":"Aniket Yadav",
    "Class":"CS-3C",
    "College":"BBDU",
    "City":"Lucknow"
}
print(Student)
print(type(Student))
Student["Branch"]="CSE"
print(Student) 
rint(Student.keys())
print(Student.values())
key=list(Student.keys())
print(key[0])
Student.update({"Marks":90})
print(Student)
#Example :-2
info ={
    "key" : "value",
    "Name":"Aniket Yadav",
    "Age":"26",
    "Section":"2C",
    "Subject":"Math,Science,Java,Chemistry,Python",
    "Topic":"Dictionary and Sets"
}

print(info)
print(type(info)) 
print(info["Name"])
print(info["Age"])
print(info["Section"])
print(info["Subject"])
print(info["Topic"])
info["Name"]="Anshu Yadav" # it will change the value of the specified key
print(info["Name"])
info["Roll No"]=56 # it will add a new key-value pair to the dictionary
print(info)

# Null value in dictionary:-
null_dict={}
print(null_dict)
print(type(null_dict))

# Nested Dictionary:-
student={
    "student1":{
        "Name":"Aniket Yadav",
        "Age":26,
        "Section":"2C"
    },
    "student2":{
        "Name":"Anupam Lata Yadav",
        "Age":22,
        "Section":"3B"
    },
    "student3":{
        "Name":"Banku Yadav",
        "Age":20,
        "Section":"1A"
    }

}

# Dictionary Methods:-
print(student.keys()) # it returns the keys of the dictionary
print(student.values()) # it returns the values of the dictionary
print(student.items()) # it returns the key-value pairs of the dictionary
print(student.get("student1")) # it returns the value of the specified key
student.pop("student2") # it removes the specified key-value pair from the dictionary
print(student)
student.update({"student4":{"Name":"Anjali Yadav","Age":18,"Section":"2B"}}) # it adds a new key-value pair to the dictionary
print(student)

# Sets:- Sets are used to store multiple items in a single variable. they are unordered, unindexed, immutable, can't accept duplicate values.  
collection={1,2,3,4,5,5,5,5}
print(collection)
print(type(collection))
print(len(collection)) # it returns the number of items in the set.
# Sets:- Sets are used to store multiple items in a single variable.

# Null sets:-

collection1= set() # it is used to create an empty set ; Syntax: set()
print(collection1)
print(type(collection1)) # it will give type 'set' because it's a set

# Sets Methods:-
collection2={1,2,3}
collection2.add(4) # it adds an element to the set
print(collection2)
collection2.remove(2) # it removes the specified element from the set
print(collection2)
collection2.pop() # it removes a random element from the set
print(collection2)
collection3={3,4,5}
collection2.update(collection3) # it adds the elements of the specified set to the set
print(collection2)
collection2.clear() # it removes all the elements from the set
print(collection2)

#set1={1,2,3,4,5}
#set2={4,5,6,7,8}
print(set1.union(set2)) # it returns a set that contains all the elements from both sets, without duplicates
print(set1.intersection(set2)) # it returns a set that contains only the elements that are present in both sets.

# Practice:-
dictionary={
    "Name":"Aniket Yadav",
    "Age":26,
    "Section":"2C",
    "Subject":["Math,Science,Java,Chemistry,Python"]
}
print(dictionary)

# Practice 2 :-

dictionary = {
    "cat": "A small domesticated carnivorous mammal",
    "table": ["A piece of furniture with a flat top and one or more legs","list of facts and figure"],
}
print (dictionary)

# practice 3:- 

subjects={
    "python","java","c++","python","javascript","java",
    "python","java","C++","c",
}
print(subjects)
print(len(subjects))

practice 4:-
Mark={}
Marks1=int(input("Enter your Marks1:"))
Mark.update({"Marks1":Marks1})
Marks2=input("Enter your Marks2:")
Mark.update({"Marks2":Marks2})
Marks3=input("Enter your Marks3:")
Mark.update({"Marks3":Marks3})

print(Mark)

# Practice 5:-
marks={}
Phy=int(input("Enter your Physics Marks:"))
marks.update({"physics":Phy})
chem=int(input("Enter your Chemistry Marks:"))
marks.update({chem:chem})
math=int(input("Enter your math marks:"))
marks.update({"math": math})

print(marks)

# practice 6:- Figure out a way to store 9 and 9.0 as seprate values in the set .

values={
    ("float",9.0),
    ("int",9)   

}
print(values)

# Solution 2:- 
values={"9.0",9}
print(values)









    

