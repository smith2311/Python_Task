"""Task 1:
Given a dictionary of sales data and another dictionary of product prices, calculate total revenue for each store.

Identify which store generated the highest revenue.

sales_data = {
    "Store_A": {"Laptop": 15, "Phone": 30, "Tablet": 10},
    "Store_B": {"Laptop": 25, "Phone": 20, "Tablet": 15},
    "Store_C": {"Laptop": 10, "Phone": 35, "Tablet": 5}
}

product_prices = {
    "Laptop": 1000,
    "Phone": 500,
    "Tablet": 300
}

# Expected Output:
# Revenue per store: {'Store_A': 34500, 'Store_B': 37500, 'Store_C': 30500}
# Most profitable store: Store_B"""

sales_data = {
    "Store_A": {"Laptop": 15, "Phone": 30, "Tablet": 10},
    "Store_B": {"Laptop": 25, "Phone": 20, "Tablet": 15},
    "Store_C": {"Laptop": 10, "Phone": 35, "Tablet": 5}
}

product_prices = {
    "Laptop": 1000,
    "Phone": 500,
    "Tablet": 300
}

#total revenue for each store.
def total_revenue(sales_data,product_prices):
    total_rev={}
    for store,product in sales_data.items():
        total=0
        for product,qty in product.items():
            total += (product_prices.get(product)*qty)
        total_rev[store]=total
    return total_rev

def highest_revenue(sales_data,product_prices):
    revenues=total_revenue(sales_data,product_prices)
    highest_store = max(revenues, key=revenues.get)
    return highest_store, revenues[highest_store]

final_revenue=total_revenue(sales_data,product_prices)
max_revenue=highest_revenue(sales_data,product_prices)

print("1) The total revenue for each store is:", final_revenue)
print("2) Store with highest revenue is:", max_revenue)

