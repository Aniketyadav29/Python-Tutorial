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
f.close() # Close the file
