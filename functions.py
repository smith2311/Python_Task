employees={}

def add_employee(id,name,age,department,salary):
    if id in employees:
        print(f"\t{id} is already registered")
    else:
        employees[id]={'ID':id,'Name':name,'Age':age,'Department':department,'Salary':salary}
        print(f"\n {name} has been added...")

def remove_employee(id):
    if id in employees:
        del employees[id]
        print(f"\n {id} has been removed...")
    else:
        print(f"\n No employee exist with id: {id} ")

def update_employee(id,name,age,department,salary):
    if id in employees:
        if name:
            employees[id]['Name']=name

        if age:
            employees[id]['Age']=age

        if department:
            employees[id]['Department']=department

        if salary:
            employees[id]['Salary']=salary
        print(f"\n {name} has been updated...")
    else:
        print(f"\n No employee exist with id: {id} ")

def search_employee(id):
    if id in employees:
        print(f"\n Employee Found with id: {employees[id]} ")

    else:
        print(f"\n No employee with id: {id} ")

def display_all_employees():
    if not employees:
        print("No employees found")
    else:
        print(f"\n {len(employees)} employees found")
        for emp_id,details in employees.items():
            print(f"\t ID: {emp_id}",
                  f"\t Name: {details['Name']}",
                  f"\t Age: {details['Age']}",
                  f"\t Department: {details['Department']}",
                  f"\t Salary: {details['Salary']}")


def EMS():
    print("\n Welcome to EMS")
    while True:
        print("\n Below are the options:")
        print("\n 1) Add New Employee")
        print("\n 2) Delete an Employee")
        print("\n 3) Update an Employees")
        print("\n 4) Search an Employee")
        print("\n 5) Show All Employee")
        print("\n 6) Exit")

        choice=int(input("\nEnter your choice: "))

        if choice==1:
            emp_id=input("Enter Employee ID: ")
            emp_name=input("Enter Employee Name: ")
            emp_age=input("Enter Employee Age: ")
            emp_department=input("Enter Employee Department: ")
            emp_salary=input("Enter Employee Salary: ")

            add_employee(emp_id,emp_name,emp_age,emp_department,emp_salary)

        elif choice==2:
            emp_id=input("Enter Employee ID: ")

            remove_employee(emp_id)

        elif choice==3:
            emp_id=input("Enter Employee ID: ")
            emp_name=input("Enter Employee Name: ")
            emp_age=int(input("Enter Employee Age in number not in decimal: "))if emp_age else None
            emp_department=input("Enter Employee Department: ")
            emp_salary=float(input("Enter Employee Salary: "))if emp_salary else None

            update_employee(emp_id,emp_name,emp_age,emp_department,emp_salary)

        elif choice==4:
            emp_id=input("Enter Employee ID to be searched: ")
            search_employee(emp_id)

        elif choice==5:
            display_all_employees()

        elif choice==6:
            print("\n Thank you for using EMS.......See you next time!")
            break

        else:
            print("Invalid choice")

if "__name__"=="__main__":
    EMS()