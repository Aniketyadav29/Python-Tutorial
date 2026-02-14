# 🏛️ Module 13: Object-Oriented Programming (OOPs)

### 📌 Overview
**Object-Oriented Programming (OOPs)** is a programming paradigm that uses "objects" to design software. Instead of writing a list of instructions (procedural), we structure our program into reusable pieces called **Classes**.

---

### 📂 Core Terminology

| Concept | Definition | Analogy |
| :--- | :--- | :--- |
| **Class** | A blueprint for creating objects. | An Architect's Blueprint. |
| **Object** | An instance of a class. | The actual house built from the blueprint. |
| **Attribute** | Characteristics or data associated with an object. | The color, number of rooms, or address. |
| **Method** | Functions/Behaviors associated with an object. | Opening the door or turning on the lights. |

---

### 🛠️ Key Components

#### 1. The Constructor (`__init__`)
The `__init__` method is a special function called automatically when an object is created. It is used to initialize the attributes of that object.
* **The `self` Parameter**: It represents the instance of the object itself and allows you to access variables that belong to the class.

#### 2. Class vs. Instance Attributes
* **Class Attributes**: Data that is the same for every object of the class (e.g., `College Name`).
* **Instance Attributes**: Data that is unique to each specific object (e.g., `Student Name`, `Roll No`).
* **Note**: Instance attributes take precedence over class attributes if they share the same name.

---

### 🌟 The 4 Pillars of OOPs (Expanded)
To build robust software, OOPs relies on these four principles:

1. **Abstraction**: Hiding complex internal details and showing only the necessary features to the user.
2. **Encapsulation**: Wrapping data (attributes) and methods into a single unit (class) to protect it from outside interference.
3. **Inheritance**: Allowing a new class (child) to inherit properties and methods from an existing class (parent).
4. **Polymorphism**: The ability of different classes to be treated as instances of the same general class through the same interface (e.g., a "Shape" class where both "Circle" and "Square" have an `area()` method).

---

### 📊 Practical Implementation
In this module, we demonstrate:
* **Student Management**: Storing names, ages, and calculating pass/fail results.
* **Product Tracking**: Managing customer dress orders and generating automated emails.
* **Automated Logic**: Using loops to filter objects (e.g., finding all students who passed).

---
**Developed with ❤️ by [Aniket Yadav](https://github.com/Aniketyadav29)**
