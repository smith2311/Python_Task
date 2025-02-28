#Task 1

import xlwt

sale_data = [
    {'category': 'Toys', 'item': 'Doll', 'price': 185, 'quantity': 8},
    {'category': 'Clothing', 'item': 'Jeans', 'price': 386, 'quantity': 10},
    {'category': 'Books', 'item': 'Novel', 'price': 212, 'quantity': 4},
    {'category': 'Clothing', 'item': 'Hat', 'price': 951, 'quantity': 1},
    {'category': 'Books', 'item': 'Novel', 'price': 397, 'quantity': 9},
    {'category': 'Electronics', 'item': 'Smartwatch', 'price': 601, 'quantity': 9},
    {'category': 'Toys', 'item': 'Action Figure', 'price': 753, 'quantity': 5},
    {'category': 'Clothing', 'item': 'Jeans', 'price': 312, 'quantity': 9},
    {'category': 'Sports', 'item': 'Football', 'price': 382, 'quantity': 8},
    {'category': 'Books', 'item': 'Comic Book', 'price': 512, 'quantity': 1},
    {'category': 'Sports', 'item': 'Gym Bag', 'price': 17, 'quantity': 1},
    {'category': 'Electronics', 'item': 'Phone', 'price': 909, 'quantity': 4},
    {'category': 'Home & Kitchen', 'item': 'Toaster', 'price': 577, 'quantity': 10},
    {'category': 'Toys', 'item': 'Doll', 'price': 209, 'quantity': 6},
    {'category': 'Clothing', 'item': 'Hat', 'price': 812, 'quantity': 10},
    {'category': 'Electronics', 'item': 'Laptop', 'price': 161, 'quantity': 5},
    {'category': 'Toys', 'item': 'Puzzle', 'price': 627, 'quantity': 2},
    {'category': 'Sports', 'item': 'Basketball', 'price': 902, 'quantity': 9},
    {'category': 'Electronics', 'item': 'Phone', 'price': 919, 'quantity': 4},
    {'category': 'Home & Kitchen', 'item': 'Microwave', 'price': 404, 'quantity': 10},
    {'category': 'Electronics', 'item': 'Headphones', 'price': 165, 'quantity': 7},
    {'category': 'Clothing', 'item': 'T-Shirt', 'price': 782, 'quantity': 1},
    {'category': 'Home & Kitchen', 'item': 'Toaster', 'price': 898, 'quantity': 4},
    {'category': 'Toys', 'item': 'Doll', 'price': 932, 'quantity': 8},
    {'category': 'Clothing', 'item': 'Shoes', 'price': 213, 'quantity': 6},
    {'category': 'Books', 'item': 'Notebook', 'price': 868, 'quantity': 2},
    {'category': 'Toys', 'item': 'Doll', 'price': 464, 'quantity': 4},
    {'category': 'Home & Kitchen', 'item': 'Microwave', 'price': 764, 'quantity': 6},
    {'category': 'Toys', 'item': 'Remote Car', 'price': 531, 'quantity': 9},
    {'category': 'Clothing', 'item': 'Hat', 'price': 610, 'quantity': 5}
]

file = xlwt.Workbook()
sheets = file.add_sheet('Sales Data')

header_style = xlwt.easyxf('font: bold 1')

headers = ['category', 'item', 'price', 'quantity']
for column_num, header in enumerate(headers):
    sheets.write(0, column_num, header, header_style)

for row_num, data in enumerate(sale_data, start=1):
    sheets.write(row_num, 0, data['category'])
    sheets.write(row_num, 1, data['item'])
    sheets.write(row_num, 2, data['price'])
    sheets.write(row_num, 3, data['quantity'])

output= file.save('sales_data.xls')

if output == 0:
    print('File created successfully')