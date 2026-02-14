# 📂 Module 12: File Input/Output (I/O) Mastery

### 📌 Overview
File Handling is a core part of any programming language. In Python, File I/O allows you to create, read, update, and delete files stored on the local file system. This module covers everything from basic reading to advanced file manipulation using the `os` module.

---

### 📁 1. Understanding File Types
Before working with files, it is important to know the two main types:
1. **Text Files (.txt, .py, .csv)**: Store data in a human-readable format (characters and strings).
2. **Binary Files (.png, .jpg, .mp4, .exe)**: Store data in bytes. These require special modes like `rb` or `wb`.

---

### 🛠️ 2. File Opening Modes (The Deep Dive)
Python provides several modes to control how you interact with a file:

| Mode | Technical Purpose | Pointer Position | Effect on Existing Data |
| :--- | :--- | :--- | :--- |
| **`'r'`** | **Read Only** | Start of file | None (Safe) |
| **`'w'`** | **Write Only** | Start of file | **Overwrites** (Deletes old content) |
| **`'a'`** | **Append Only** | End of file | Keeps old data, adds to the end |
| **`'r+'`** | **Read & Write** | Start of file | Can overwrite from the start |
| **`'w+'`** | **Write & Read** | Start of file | Overwrites, then allows reading |
| **`'rb'`** | **Read Binary** | Start of file | For non-text files (images/PDFs) |

---

### 🔍 3. Common Reading Methods
* **`f.read()`**: Reads the **entire** file as a single string. Use with caution on very large files.
* **`f.readline()`**: Reads only **one line** at a time. Perfect for memory-efficient processing.
* **`f.readlines()`**: Reads all lines and returns them as a **List** of strings.

---

### 🛡️ 4. Best Practice: The `with` Statement
Manually using `f.close()` is risky because if an error occurs before that line, the file stays open in memory, potentially causing data corruption.

**The "with" syntax** (Context Manager) is the industry standard:
```python
with open("data.txt", "r") as f:
    content = f.read()
# File is automatically closed here, even if the code crashes!
