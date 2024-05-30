import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df1 = customers[~customers['id'].isin(orders['customerId'])]['name']
    return pd.DataFrame({'Customers':df1})


# Create the Customers DataFrame
customers = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Joe', 'Henry', 'Sam', 'Max']
})

# Create the Orders DataFrame
orders = pd.DataFrame({
    'id': [1, 2],
    'customerId': [3, 1]
})

print("Customers DataFrame:")
print(customers)
print("\nOrders DataFrame:")
print(orders)

merged = find_customers(customers, orders)
print('\n')
print(merged)