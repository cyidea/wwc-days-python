import pandas as pd

data = [
    [0, 95, 100, 105],
    [1, 70, None, 80]
]

columns = ['product_id', 'store1', 'store2', 'store3']
products = pd.DataFrame(data, columns=columns)

print(products)

products_new = products.set_index(['product_id']).stack().reset_index()
products_new.columns = ['product_id', 'store', 'price']
print('\n')
print(products_new)
