"""Task 3

Given a dictionary where complaint types are keys and their occurrence counts are values, determine:

The most common complaint type.
The percentage share of each complaint type

complaints = {
    "Late Delivery": 120,
    "Damaged Product": 95,
    "Wrong Item": 60,
    "Customer Service": 75,
    "Billing Issues": 50
}

# Expected Output:

# Most Common Complaint: Late Delivery
# Complaint Percentage Distribution:
# {'Late Delivery': 32%, 'Damaged Product': 25%, 'Wrong Item': 16%, 'Customer Service': 20%, 'Billing Issues': 7%}"""

complaints = {
    "Late Delivery": 120,
    "Damaged Product": 95,
    "Wrong Item": 60,
    "Customer Service": 75,
    "Billing Issues": 50
}

#Most common complaint
def common_complaints(complaints):
    max_com=max(complaints,key=complaints.get)
    print(f"1) The most common complaint from the dictionary is {max_com}.")

#The percentage share of each complaint type
def complaints_percentage_ratio(complaints):
    total_complaints=sum(complaints.values())
    for comp, count in complaints.items():
        percentage=(count/total_complaints)*100
        print(f"\t{comp} : {percentage:.2f}%.")


common_complaints(complaints)

print(f"\n2) The percentage of all complaints complaints is:")
complaints_percentage_ratio(complaints)


