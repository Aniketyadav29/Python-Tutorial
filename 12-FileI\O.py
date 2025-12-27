# File I\O :- File I\O is used to read and write data to a file. In Python, we can use the built-in open() function to open a file. The open() function takes two parameters: the name of the file and the mode in which the file is opened.

# Types of files:-
# 1. Text File:- Text files are files that contain plain text. They are usually created using a text editor. Text files have the extension .txt.
# 2. Binary File:- Binary files are files that contain binary data. They are usually created using a binary editor. Binary files have the extension .bin.

# File Modes:-
# 1. 'r' - Read Mode: This mode is used to read data from a file. The file must exist, otherwise an error will be raised.
# 2. 'w' - Write Mode: This mode is used to write data to a file. If the file already exists, it will be overwritten. If the file does not exist, a new file will be created.
# 3. 'a' - Append Mode: This mode is used to append data to a file. If the file already exists, the new data will be added to the end of the file. If the file does not exist, a new file will be created.
# 4. 'b' - Binary Mode: This mode is used to read and write binary data to a file. It can be used in combination with other modes (e.g., 'rb' for read binary, 'wb' for write binary).
# # Example No.1:-
# # Writing to a file
file=open("example.txt","w") # Open the file in write mode
file.write("Hello, Welcome to Python Programming") # Write data to the file

#example No.2:-
f=open("demo.txt","r")
content=f.read()
print(content)
print(type(content))
f.close() # Close the file.

# Example No.3:-

f=open("demo.txt","r") # Open the file in read mode.
line1=f.readline() 
print(line1)
print(type(line1))
line2=f.readline()
print(line2)    
print(type(line2))
line3=f.readline()
print(line3)
print(type(line3))
f.close() # Close the file

#Example No.4:-

f=open("demo.txt","w")
content=f.write("I am aniket yadav , a frontend developer.")
f.close()

#Example No.5:-
f=open("demo.txt","a")
content=f.write("\nI am learning python programming language.")
f.close()

# Example No.6:-
f=open("sample.txt","w")
f.close()

# Example No.7:-
f=open("demo.txt","r+")
content=f.read()
print(content)
f.write("I love coding.")
f.close()

#with Syntax:-
with open("demo.txt","r") as f:
    content=f.read()
    print(content)

#Example No.2:-
with open("demo.txt","r") as f:
    data = f.read()
    print(data)


# Deleting files:- using os module

#module is a file containing Python code. It can define functions, classes, and variables. A module can also include runnable code.

import os
os.remove("sample.txt")

# Example No.2:- create a file with name of "pratice.txt" and then add following data 
# hii Everyone
# welcome to file I\O in python
# i like programming in python
f=open("practice.txt","w")
data=f.write("hii Everyone\n welcome to file I\O in python\n i like programming python")
f.close()

# WAF that replace of all occurance of python with java in the file "practice.txt"
f=open("practice.txt", "r")
data = f.read()
new_data=data.replace("java","python")
print(new_data)
f=open("practice.txt","w")
f.write(new_data)
f.close()

# search for a word "learning" in the file "practice.txt" .
f=open("practice.txt","r")
data=f.read()
if"learning" in data:
    print("word found")
else:
    print("word not found")
f.close()

# another Example:- 

f=open("practice.txt","r")

data=f.read()
if "programming" in data:
    print("word found")
else:
    print("word not found")
    f.close()





