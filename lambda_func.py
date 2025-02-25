sales_data = {
    "Store_A": {
        "Laptop": 15,
        "Phone": 30,
        "Tablet": 10
    },
    "Store_B": {
        "Laptop": 25,
        "Phone": 20,
        "Tablet": 15
    },
    "Store_C": {
        "Laptop": 10,
        "Phone": 35,
        "Tablet": 5}
}

# 1) Total sales for each product across all stores
def total_sales(sales_data):
    total_dict = {}
    for data in sales_data.values():
        for key, value in data.items():
            total_dict[key] = value
    return total_dict

# 2) Identify the store with the highest total sales
def best_sales(sales_data):
    total_sales_per_store = {store: sum(products.values()) for store, products in sales_data.items()}
    highest_sales_store = max(total_sales_per_store, key=total_sales_per_store.get)
    highest_sales_value = total_sales_per_store[highest_sales_store]
    print("\n2) The store with the highest sales is:", highest_sales_store, "with", highest_sales_value,"sales")

# 3) Find the best-selling product
def best_sold_product(total_sales_dict):
    best_selling_product = max(total_sales_dict, key=total_sales_dict.get)
    print("\n3) The best-selling product is:", best_selling_product)

# 4) Sort stores based on total sales in descending order
def sorting(sales_data):
    total_sales_per_store = {store: sum(products.values()) for store, products in sales_data.items()}
    sorted_stores = sorted(total_sales_per_store.items(), key=lambda item: item[1], reverse=True)
    print("\n4) Stores after sorting are as follows:")
    for store, sales in sorted_stores:
        print(f"\t{store}: {sales}")

# Execute functions
total_sales_vals = total_sales(sales_data)
print("\n1) Total sales for each product:", total_sales_vals)
best_sales(sales_data)
best_sold_product(total_sales_vals)
sorting(sales_data)
