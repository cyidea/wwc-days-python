import pandas as pd

data = [
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 3]
]

columns = ['order_number', 'customer_number']
orders = pd.DataFrame(data, columns=columns)

print(orders)

print('\n')

# thes = courses.groupby(['class']).student.count()
# newdf = thes.to_frame().reset_index()
# newdff = newdf[newdf['student'] >= 5]
# print(newdff[['class']])

counts = orders.groupby(['customer_number']).order_number.count().reset_index().sort_values(by=['order_number'], ascending=False)
print(counts[['customer_number']].head(1))