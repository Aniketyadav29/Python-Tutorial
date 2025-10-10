# Dictionary and Sets in Python:-

# Dictionary :- Dictionary are used to store data value in keys ; value = pair.
# they are unorderd ,Mutable,can't accept duplicate keys.

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

# Sets:- Sets are used to store multiple items in a single variable.
# they are unordered, unindexed, immutable, can't accept duplicate values.  
collection={1,2,3,4,5,5,5,5}
print(collection)
print(type(collection))
print(len(collection)) # it returns the number of items in the set.
# Sets:- Sets are used to store multiple items in a single variable.

# Null sets:-

collection1= set() # it is used to create an empty set ; Syntax: set()
print(collection1)
print(type(collection1)) # it will give type 'set' because it's a set





    

