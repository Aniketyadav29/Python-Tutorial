# 📖 Module 09: Dictionaries and Sets

### 📌 Definitions

#### 1. Dictionary
**Dictionaries** are used to store data values in **Key:Value** pairs. They are:
* **Ordered** (as of Python 3.7+).
* **Mutable**: You can change, add, or remove items after the dictionary is created.
* **Unique Keys**: They do not allow duplicate keys.

#### 2. Sets
**Sets** are collections used to store multiple items in a single variable. They are:
* **Unordered**: Items do not have a defined order.
* **Unindexed**: You cannot access items by index.
* **Unique Elements**: Sets automatically remove all duplicate values.

---

### 🛠️ Key Methods

| Method | Type | Description |
| :--- | :--- | :--- |
| `.keys()` | Dict | Returns a list of all keys in the dictionary. |
| `.values()` | Dict | Returns a list of all values. |
| `.update()` | Dict/Set | Merges another collection into the current one. |
| `.get()` | Dict | Returns the value of a key (safer than `dict[key]`). |
| `.add()` | Set | Adds a single element to a set. |
| `.union()` | Set | Combines two sets (all unique elements). |
| `.intersection()` | Set | Returns only elements present in both sets. |

---

### ⚖️ Real-Life Analogy
* **Dictionary**: Like a **Real Dictionary**—the "Word" is the Key, and the "Meaning" is the Value.
* **Set**: Like a **Guest List**—even if someone tries to sign in twice, their name only appears once on the final list.

---
**Developed by [Aniket Yadav](https://github.com/Aniketyadav29)**
