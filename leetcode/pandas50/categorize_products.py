import pandas as pd

data = [
    ['2020-05-30', 'Headphone'],
    ['2020-06-01', 'Pencil'],
    ['2020-06-02', 'Mask'],
    ['2020-05-30', 'Basketball'],
    ['2020-06-01', 'Bible'],
    ['2020-06-02', 'Mask'],
    ['2020-05-30', 'T-Shirt']
]

columns = ['sell_date', 'product']
activities = pd.DataFrame(data, columns=columns)

print(activities)

# thes = courses.groupby(['class']).student.count()
# newdf = thes.to_frame().reset_index()
# newdff = newdf[newdf['student'] >= 5]
# print(newdff[['class']])

# counts = orders.groupby(['customer_number']).order_number.count().reset_index().sort_values(by=['order_number'], ascending=False)
# print(counts[['customer_number']].head(1))


counts = activities.drop_duplicates().groupby(['sell_date']).product.agg(
    num_sold = "count",
    products = (lambda x: ', '.join(sorted(set(x))))
    ).reset_index()
print(counts)