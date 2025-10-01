
# String and Conditional statements.:-

Str1="my name is aniket yadav "
Str2='this is aniket yadav'
Str3="""" my name is banku """

# Why it is used:-
"this is apnacillege's tutorial"

# Escape Sequence Character :-

 Str4= "this is string.\n we are using it in python."
 print(Str4)

# Basic Operation on String

# Concatination

print(Str1+Str2)

# Length of String:-

len1=len(Str1)
print(len1)

len2=len(Str1)
print(len2)

# Indexing in python :-

print(Str1[1])

print(Str1[4])

print(Str2[5])

print(Str2[9])

# Slicing :-

 print(Str1[1:4])
 print(Str2[1:7])
 print(Str3[4:])  #[4:length(Str3)]
 print(Str2[:7])  #[0:7]

# Slicing in Negative Index :-

 Str="apple"
 print(Str[-3:-2])
 print(Str[-5:-2])

# String Function:-

 str="this is apna college and i am learning python"
 print(str.endswith("thon")) # it checks whether the string ends with the specified value, returns true or false
 print(str.capitalize()) # it converts the first character to upper case
 print(str.find("apna")) # it finds the first occurrence of the specified value, returns the index of the first occurrence
 print(str.replace("apna","our")) # it replaces the specified value with the specified value
 print(str.count("is")) # it counts the number of occurrences of the specified value

# Practice :- 

# Question 1:-  WAP to input user name and print the length of the name.
 name=(input("Enter your name:"))
 print("the length of your name is :" ,len(name))

# Question 2:- WAP to find occurrence of $ in a string.

str=input("Enter your string:")
print("the occurrence of $ in the string is :",str.count('$'))

