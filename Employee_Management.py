class Employee:
    def __init__(self, emp_id, name, department):
        self.emp_id = emp_id
        self.name = name
        self.department = department

    def display(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Department: {self.department}")


employees = [
    Employee(101, "Manju", "Trainee"),
    Employee(102, "Anusha", "Trainee"),
]

def create_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        employees.append(Employee(emp_id, name, department))
        print("Employee added successfully.")
    except ValueError:
        print("Invalid input.")

def read_employees():
    if not employees:
        print("No employees found.")
    else:
        print("All Employees (Sorted by Name):")
        for emp in sorted(employees, key=lambda e: e.name.lower()):
            emp.display()

def update_employee():
    try:
        emp_id = int(input("Enter Employee ID to update: "))
        for emp in employees:
            if emp.emp_id == emp_id:
                name = input("Enter new name (leave blank to keep current): ")
                department = input("Enter new department (leave blank to keep current): ")
                if name:
                    emp.name = name
                if department:
                    emp.department = department
                print("Employee updated successfully.")
                return
        print("Employee not found.")
    except ValueError:
        print("Invalid input.")

def delete_employee():
    try:
        emp_id = int(input("Enter Employee ID to delete: "))
        for i, emp in enumerate(employees):
            if emp.emp_id == emp_id:
                del employees[i]
                print("Employee deleted successfully.")
                return
        print("Employee not found.")
    except ValueError:
        print("Invalid input.")

def main_menu():
    while True:
        print("\n-----------------------")
        print("1. Create Employee")
        print("2. Display All Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        print("-----------------------")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            create_employee()
        elif choice == '2':
            read_employees()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

main_menu()
