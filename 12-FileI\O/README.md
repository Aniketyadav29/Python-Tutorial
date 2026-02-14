# 📂 Module 12: File Input/Output (I/O)

### 📌 Definition
**File I/O** is used to read data from and write data to files on your system. Python uses the built-in `open()` function to interact with files.

---

### 📁 Types of Files
1. **Text File (.txt)**: Contains plain text (characters).
2. **Binary File (.bin)**: Contains data in binary format (e.g., images, videos).

---

### 🛠️ File Opening Modes

| Mode | Name | Description |
| :--- | :--- | :--- |
| **'r'** | Read | Opens a file for reading (default). Error if file doesn't exist. |
| **'w'** | Write | Opens for writing. Overwrites existing content or creates a new file. |
| **'a'** | Append | Opens for writing at the end of the file. Creates file if missing. |
| **'r+'** | Read+Write | Opens for both reading and writing. |
| **'b'** | Binary | Opens file in binary mode (used as `rb` or `wb`). |

---

### 🛡️ The `with` Syntax
Using the `with` statement is the best practice for file handling because it **automatically closes the file** for you, even if an error occurs.

### 🗑️ Deleting Files
To delete a file, Python requires the `os` module:
```python
import os
os.remove("filename.txt")
