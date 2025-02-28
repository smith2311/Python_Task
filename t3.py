employees = []

def add_employee():
    emp_id = input("\nEnter Employee ID: ")
    name = input("Enter Employee Name: ")

    while True:
        try:
            salary = float(input("Enter Salary: "))
            break
        except ValueError:
            print("Invalid salary! Please enter a number.")

    role = input("Enter Role (Manager/Developer): ").strip().title()

    if role == "Manager":
        extra_info = input("Enter Department: ")
    elif role == "Developer":
        extra_info = input("Enter Programming Language: ")
    else:
        print("Invalid role! Employee not added.")
        return

    employee = {
        "ID": emp_id,
        "Name": name,
        "Salary": salary,
        "Role": role,
        "Extra Info": extra_info
    }
    employees.append(employee)
    print("Employee added successfully!")

# Function to display all employees
def show_all_employees():
    if not employees:
        print("\nNo employees found.")
        return

    print("\nAll Employees:")
    for emp in employees:
        print(f"ID: {emp['ID']}, Name: {emp['Name']}, Salary: {emp['Salary']}, Role: {emp['Role']}, Extra: {emp['Extra Info']}")

# Function to filter employees by role
def filter_by_role():
    role = input("Enter role to filter (Manager/Developer): ").strip().title()
    found = False

    print(f"\nEmployees with role '{role}':")
    for emp in employees:
        if emp["Role"] == role:
            print(f"ID: {emp['ID']}, Name: {emp['Name']}, Salary: {emp['Salary']}, Extra: {emp['Extra Info']}")
            found = True

    if not found:
        print(f"No employees found with role: {role}")

# Function to filter employees by salary range
def filter_by_salary():
    try:
        min_salary = float(input("Enter minimum salary: "))
        max_salary = float(input("Enter maximum salary: "))
    except ValueError:
        print("Invalid salary input! Please enter numbers.")
        return

    found = False
    print(f"\nEmployees earning between {min_salary} and {max_salary}:")
    for emp in employees:
        if min_salary <= emp["Salary"] <= max_salary:
            print(f"ID: {emp['ID']}, Name: {emp['Name']}, Salary: {emp['Salary']}, Role: {emp['Role']}")
            found = True

    if not found:
        print("No employees found in this salary range.")

while True:
    print("\nEMPLOYEE MANAGEMENT SYSTEM")
    print("1) Add Employee")
    print("2) Show All Employees")
    print("3) Filter by Role")
    print("4) Filter by Salary Range")
    print("5) Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        show_all_employees()
    elif choice == "3":
        filter_by_role()
    elif choice == "4":
        filter_by_salary()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 5.")
