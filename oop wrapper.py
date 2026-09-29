
print("--- Python OOP Project: Employee Management System ---")

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class employee(person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.__emp_id = emp_id
        self.__salary = salary

    # Getter Methods
    def get_emp_id(self):
        return self.__emp_id

    def get_salary(self):
        return self.__salary

    # Setter Methods
    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    def set_salary(self, salary):
        self.__salary = salary

    def display(self):
        super().display()
        print("Employee ID:", self.get_emp_id())
        print("Salary:", self.get_salary())


class manager(employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)


class developer(employee):
    def __init__(self, name, age, emp_id, salary, programming_language):
        super().__init__(name, age, emp_id, salary)
        self.programming_language = programming_language

    def display(self):
        super().display()
        print("Programming Language:", self.programming_language)


# Check Inheritance using issubclass()
print("Is Manager a subclass of Employee?", issubclass(manager, employee))
print("Is Developer a subclass of Employee?", issubclass(developer, employee))


person_obj = None
employee_obj = None
manager_obj = None
developer_obj = None

while True:

    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4.Create a Developer")
    print("5. Show details")
    print("6. Exit")
   

    choice = int(input("Enter your choice: "))
    

    if choice == 1:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        person_obj = person(name, age)
        print("Person created with name:", name, "and age:", age)
        print("\n--- Choose another operation ---")

    elif choice == 2:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = int(input("Enter Employee ID: "))
        salary = float(input("Enter Salary: "))
        employee_obj = employee(name, age, emp_id, salary)
        print("Employee created with name:", name, ", age:", age,
              ", ID:", emp_id, ", and salary: $", salary)
        print("\n--- Choose another operation ---")

    elif choice == 3:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = int(input("Enter Employee ID: "))
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")
        manager_obj = manager(name, age, emp_id, salary, department)
        print("Manager created with name:", name, ", age:", age,
              ", ID:", emp_id, ", salary:", salary,
              ", and department:", department)
        print("\n--- Choose another operation ---")

    elif choice == 4:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        emp_id = int(input("Enter Employee ID: "))
        salary = float(input("Enter Salary: "))
        programming_language = input("Enter Programming Language: ")
        developer_obj = developer(
            name, age, emp_id, salary, programming_language
        )
        print("Developer created with name:", name, ", age:", age,
              ", ID:", emp_id, ", salary:", salary,
              ", and Programming Language:", programming_language)
        print("\n--- Choose another operation ---")

    elif choice == 5:
        print("Choose details to show:")
        print("1.Person")
        print("2.Employee")
        print("3.Manager")
        print("4.Developer")
        detail = int(input("Enter your choice: "))

        if detail == 1:
            if person_obj is not None:
                print("Person Details:")
                person_obj.display()
            else:
                print("Person details are not available!")

        elif detail == 2:
            if employee_obj is not None:
                print("Employee Details:")
                employee_obj.display()
            else:
                print("Employee details are not available!")

        elif detail == 3:
            if manager_obj is not None:
                print("Manager Details:")
                manager_obj.display()
            else:
                print("Manager details are not available!")

        elif detail == 4:
            if developer_obj is not None:
                print("Developer Details:")
                developer_obj.display()
            else:
                print("Developer details are not available!")

        else:
            print("Invalid detail choice!")
        print("\n--- Choose another operation ---")

    elif choice == 6:
        print("Exiting the system. All resources have been freed")
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")