# ==========================================================
# 12: FILE I/O PRACTICE
# ==========================================================
import os

# --- PART 1: WRITING & READING ---
# Example: Creating and Writing
with open("demo.txt", "w") as f:
    f.write("I am Aniket Yadav, a frontend developer.")

# Example: Appending
with open("demo.txt", "a") as f:
    f.write("\nI am learning python programming language.")

# Example: Reading
print("--- Reading File Content ---")
with open("demo.txt", "r") as f:
    content = f.read()
    print(content)
print("\n")


# --- PART 2: THE OS MODULE ---
# Example: Creating a temp file and deleting it
f = open("sample.txt", "w")
f.close()
if os.path.exists("sample.txt"):
    os.remove("sample.txt")
    print("File 'sample.txt' deleted successfully.")


# --- PART 3: PRACTICE CHALLENGES ---

# 1. Create a practice file
print("\n--- Creating practice.txt ---")
with open("practice.txt", "w") as f:
    f.write("hii Everyone\nwelcome to file I/O in python\ni like programming in python")

# 2. Function to find and replace
def replace_word(filename, old_word, new_word):
    with open(filename, "r") as f:
        data = f.read()
    
    new_data = data.replace(old_word, new_word)
    
    with open(filename, "w") as f:
        f.write(new_data)
    print(f"Replaced '{old_word}' with '{new_word}' in {filename}")

replace_word("practice.txt", "python", "java")


# 3. Search for a word
def check_for_word(filename, word):
    with open(filename, "r") as f:
        data = f.read()
    if word in data:
        print(f"Word '{word}' found!")
    else:
        print(f"Word '{word}' not found.")

check_for_word("practice.txt", "programming")


# 4. Find line number of a word
def find_line_of_word(filename, word):
    data = True
    line_no = 1
    with open(filename, "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(f"Found '{word}' at line: {line_no}")
                return line_no
            line_no += 1
    return -1

find_line_of_word("practice.txt", "java")

# 5.
f=open("File.txt")
data=f.read()
print(data)
f.close()


# st="Hey Harry You r amazing"

f=open("myfile.txt","w")
f.write(st)
f.close()

f=open("File.txt")
# lines=f.readlines()
# print(lines, type(lines))

# line0=f.readline()
# print(line0,type(line0))

# line1=f.readline()
# print(line1, type(line1))

# line2=f.readline()
# print(line2, type(line2))

# line3=f.readline()
# print(line3, type(line3))

# line4=f.readline()
# print(line4, type(line4))
line=f.readline()
while(line!=""):
    print(line,type(line))
    line=f.readline()

f.close()

# 6
with open (r"c:\Users\Dell\Desktop\CWH.py\Project -1\main.py","r") as file1:
    content=file1.read()
    print(content)

#7

st="I am a good boy."
with open ("myfile.txt","w") as file1:
    
    file1.write(st)
    print("Done .")



# ==========================================================
# Practice Session Complete!
# ==========================================================
