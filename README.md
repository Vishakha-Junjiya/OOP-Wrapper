# 🏢 Python OOP Project: Employee Management System

## 📌 1. Project Overview

The **Employee Management System** is a menu-driven Python application developed using Object-Oriented Programming (OOP) concepts. The main purpose of this project is to create and manage the details of different types of people working in an organization.

This project allows users to create a Person, Employee, Manager, and Developer. Users can enter their personal and professional information and display the stored details whenever required.

The project demonstrates important Python concepts such as classes, objects, inheritance, encapsulation, constructors, method overriding, getter and setter methods, and the `super()` and `issubclass()` functions.

This project is designed for learning and understanding the practical implementation of Python OOP concepts.

---

## 🎯 2. Project Objectives

The main objectives of this project are:

* To understand the fundamentals of Object-Oriented Programming in Python.
* To create and manage different types of objects.
* To implement inheritance between related classes.
* To protect sensitive employee information using encapsulation.
* To use constructors for initializing object attributes.
* To implement method overriding in child classes.
* To understand the use of `super()` for accessing parent class methods.
* To use getter and setter methods to access and modify private data.
* To check inheritance relationships using `issubclass()`.
* To develop a menu-driven application using conditional statements and loops.

---

## 🛠️ 3. Technologies Used

| Technology                  | Description               |
| --------------------------- | ------------------------- |
| Python                      | Main programming language |
| Object-Oriented Programming | Application structure     |
| VS Code                     | Code editor               |
| Git                         | Version control           |
| GitHub                      | Source code hosting       |

---

## ⚙️ 4. System Requirements

### Hardware Requirements

* Computer or Laptop
* Minimum 4 GB RAM recommended
* Keyboard and Monitor

### Software Requirements

* Windows, Linux, or macOS
* Python 3.x
* Visual Studio Code or any Python IDE
* Terminal or Command Prompt

---

## ✨ 5. Features of the Project

### 1. Create a Person

Users can enter a person's name and age. The system creates a Person object and stores the information in the program.

### 2. Create an Employee

Users can enter employee details, including:

* Name
* Age
* Employee ID
* Salary

The Employee class inherits the properties and methods of the Person class.

### 3. Create a Manager

Users can create a Manager by entering:

* Name
* Age
* Employee ID
* Salary
* Department

The Manager class inherits from the Employee class and adds department information.

### 4. Create a Developer

Users can create a Developer by entering:

* Name
* Age
* Employee ID
* Salary
* Programming Language

The Developer class inherits from the Employee class and adds programming language information.

### 5. Show Details

Users can choose which type of details they want to display:

* Person Details
* Employee Details
* Manager Details
* Developer Details

The program checks whether the selected object's details are available before displaying them.

### 6. Exit the System

Users can exit the program by selecting the Exit option from the menu.

### 7. Input Validation for Menu Choices

The program includes a basic check for invalid menu and detail choices and displays an appropriate message.

---

## 📚 6. Classes Used in the Project

### A. Person Class

The Person class is the base class of the application.

**Attributes:**

* `name`
* `age`

**Method:**

* `display()` – Displays the person's name and age.

### B. Employee Class

The Employee class inherits from the Person class.

**Attributes:**

* `__emp_id`
* `__salary`

**Methods:**

* `get_emp_id()` – Returns the employee ID.
* `get_salary()` – Returns the salary.
* `set_emp_id()` – Updates the employee ID.
* `set_salary()` – Updates the salary.
* `display()` – Displays personal and employee details.

The employee ID and salary are private attributes, demonstrating encapsulation.

### C. Manager Class

The Manager class inherits from the Employee class.

**Additional Attribute:**

* `department`

**Method:**

* `display()` – Displays personal details, employee details, and department information.

### D. Developer Class

The Developer class also inherits from the Employee class.

**Additional Attribute:**

* `programming_language`

**Method:**

* `display()` – Displays personal details, employee details, and programming language information.

---

## 🧠 7. Object-Oriented Programming Concepts Implemented

### 1. Class

A class is a blueprint used to create objects. This project uses Person, Employee, Manager, and Developer classes.

### 2. Object

An object is an instance of a class. Objects are created to store the details of persons, employees, managers, and developers.

### 3. Constructor (`__init__`)

The constructor initializes the attributes of an object when it is created.

### 4. Inheritance

Inheritance allows a child class to reuse the attributes and methods of a parent class.

The inheritance structure of this project is:

```text
Person
  |
Employee
  |------ Manager
  |
  |------ Developer
```

### 5. Encapsulation

Encapsulation is implemented by declaring employee ID and salary as private attributes using double underscores.

### 6. Getter Methods

Getter methods are used to retrieve private attribute values.

### 7. Setter Methods

Setter methods are used to update private attribute values.

### 8. Method Overriding

The Manager and Developer classes override the `display()` method to display their additional information.

### 9. `super()` Function

The `super()` function is used to call the parent class constructor and display method without rewriting the same code.

### 10. `issubclass()` Function

The `issubclass()` function checks whether Manager and Developer are subclasses of Employee.

---

## 🔄 8. Working of the Project

The project follows a simple menu-driven process:

1. The program displays the project title.
2. It checks the inheritance relationships between the classes.
3. The main menu is displayed.
4. The user selects an operation.
5. The program asks for the required information.
6. An object of the selected class is created.
7. The user can select the Show Details option.
8. The program displays the selected object's details if available.
9. The menu continues until the user selects Exit.

---

## ▶️ 9. How to Install and Run the Project

### Step 1: Install Python

Download and install Python 3.x from the official website:

https://www.python.org/downloads/

### Step 2: Download the Project

Download or clone the project repository to your computer.

### Step 3: Open the Project Folder

Open the project folder in Visual Studio Code or another Python editor.

### Step 4: Open the Terminal

Open the terminal inside the project folder.

### Step 5: Run the Python File

Use the following command, replacing `main.py` with your actual Python filename:

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

### Step 6: Use the Menu

Select an option from the displayed menu and enter the requested information.

---

## 💻 10. Sample Program Menu

```text
--- Python OOP Project: Employee Management System ---

Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Create a Developer
5. Show details
6. Exit

Enter your choice:
```

---

## 📋 11. Sample Output

### Creating an Employee

```text
Enter your choice: 2
Enter Name: Vishakha
Enter Age: 20
Enter Employee ID: 101
Enter Salary: 25000

Employee created with name: Vishakha,
age: 20, ID: 101, and salary: $ 25000.0
```

### Displaying Employee Details

```text
Employee Details:
Name: Vishakha
Age: 20
Employee ID: 101
Salary: 25000.0
```

### Creating a Manager

```text
Enter your choice: 3
Enter Name: Rahul
Enter Age: 30
Enter Employee ID: 102
Enter Salary: 45000
Enter Department: IT

Manager created with name: Rahul,
age: 30, ID: 102, salary: 45000.0,
and department: IT
```

### Displaying Manager Details

```text
Manager Details:
Name: Rahul
Age: 30
Employee ID: 102
Salary: 45000.0
Department: IT
```

*Note: These are illustrative sample inputs and outputs.*

---

## 📁 12. Project Structure

```text
Employee-Management-System/
│
├── main.py
└── README.md
```

**Note:** Replace `main.py` with the actual name of your Python file. If your project contains additional files, include them in the structure.

---

## ⚠️ 13. Limitations

* The program stores information only while it is running.
* Data is not saved permanently in a database or file.
* The system manages one current object for each category.
* The program uses basic menu-choice validation.
* The current implementation is intended for learning and demonstration purposes.

---

## 🚀 14. Future Enhancements

The project can be improved in the future by adding:

* Permanent data storage using files or a database.
* Multiple employee records.
* Search employee by ID or name.
* Update employee details through the menu.
* Delete employee records.
* More detailed input validation.
* A graphical user interface (GUI).
* Login and authentication features.
* Report generation for employee information.

---

## 🎓 15. Learning Outcomes

After completing this project, the developer gains practical experience in:

* Writing Python classes and creating objects.
* Implementing single and multilevel inheritance.
* Using private attributes and encapsulation.
* Working with constructors and parent class methods.
* Applying method overriding.
* Creating getter and setter methods.
* Using loops and conditional statements.
* Developing a menu-driven application.
* Organizing Python code into reusable components.

---

## 📝 16. Conclusion

The Python OOP Employee Management System is a simple educational project that demonstrates the practical use of Object-Oriented Programming concepts. It provides separate classes for Person, Employee, Manager, and Developer, allowing users to create objects and display their details through a menu-driven interface.

This project helps build a strong foundation in Python programming and prepares the developer for more advanced projects involving data management, databases, and software development.

---

## 👩‍💻 17. Developed By

**Name:** Vishakha Junjiya

**Project Title:** Python OOP Project – Employee Management System

**Purpose:** Academic Learning and Python OOP Practice

**Programming Language:** Python
