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


    

