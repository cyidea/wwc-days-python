import pandas as pd

SalesPerson = pd.DataFrame({
    'sales_id': [1, 2, 3, 4, 5],
    'name': ['John', 'Amy', 'Mark', 'Pam', 'Alex'],
    'salary': [100000, 12000, 65000, 25000, 5000],
    'commission_rate': [6, 5, 12, 25, 10],
    'hire_date': ['4/1/2006', '5/1/2010', '12/25/2008', '1/1/2005', '2/3/2007']
})

# Company DataFrame
Company = pd.DataFrame({
    'com_id': [1, 2, 3, 4],
    'name': ['RED', 'ORANGE', 'YELLOW', 'GREEN'],
    'city': ['Boston', 'New York', 'Boston', 'Austin']
})

# Orders DataFrame
Orders = pd.DataFrame({
    'order_id': [1, 2, 3, 4],
    'order_date': ['1/1/2014', '2/1/2014', '3/1/2014', '4/1/2014'],
    'com_id': [3, 4, 1, 1],
    'sales_id': [4, 5, 1, 4],
    'amount': [10000, 5000, 50000, 25000]
})

orders_for_red = Orders.merge(right=Company, on='com_id')

print(orders_for_red)

result = SalesPerson[~SalesPerson['sales_id'].isin(orders_for_red.query('name == "RED"')['sales_id'])]
print(result[['name']])