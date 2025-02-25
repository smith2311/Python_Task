"""Given a dictionary where employees' names are keys and their monthly sales are values, determine:

The employee with the highest sales.

The top 3 employees sorted in descending order.

employee_sales = {
    "Alice": 5000,
    "Bob": 7500,
    "Charlie": 4200,
    "Diana": 9100,
    "Ethan": 6200
}

# Expected Output:
# Top Performer: Diana
# Top 3 Employees: [('Diana', 9100), ('Bob', 7500), ('Ethan', 6200)]"""

employee_sales = {
    "Alice": 5000,
    "Bob": 7500,
    "Charlie": 4200,
    "Diana": 9100,
    "Ethan": 6200
}
def highest_sales(employee_sales):
    max_sales_by_emp=max(employee_sales,key=employee_sales.get)
    print(f"\n 1) The best-selling product is:",max_sales_by_emp)

def top_3_emp(employee_sales):
    sorted_emp=sorted(employee_sales.items(),key=lambda x:x[1], reverse=True )
    top3=slice(3)
    final_emp=sorted_emp[top3]
    print(f"\n 2) The top 3 employees is: {final_emp}")

highest_sales(employee_sales)
top_3_emp(employee_sales)