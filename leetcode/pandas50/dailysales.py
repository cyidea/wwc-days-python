from itertools import count
import pandas as pd

# prepare the dataframe to be used:
# The scenario is a car dealership. 
# There is always a lead who is probably a sales-person, 
# and there is the customer whom they call 'partner'.
# When a car sale is made (each row in the dataset) there is a date and the car,
# there is also the sales-person and the customer.

data = [
    ['2020-12-8', 'toyota', 0, 1],
    ['2020-12-8', 'toyota', 1, 0],
    ['2020-12-8', 'toyota', 1, 2],
    ['2020-12-7', 'toyota', 0, 2],
    ['2020-12-7', 'toyota', 0, 1],
    ['2020-12-8', 'honda', 1, 2],
    ['2020-12-8', 'honda', 2, 1],
    ['2020-12-7', 'honda', 0, 1],
    ['2020-12-7', 'honda', 1, 2],
    ['2020-12-7', 'honda', 2, 1]
]

dailysales = pd.DataFrame(data, columns=['date_id', 'make_name', 'lead_id', 'partner_id'])

print(dailysales)
'''
output:
     date_id make_name  lead_id  partner_id
0  2020-12-8    toyota        0           1
1  2020-12-8    toyota        1           0
2  2020-12-8    toyota        1           2
3  2020-12-7    toyota        0           2
4  2020-12-7    toyota        0           1
5  2020-12-8     honda        1           2
6  2020-12-8     honda        2           1
7  2020-12-7     honda        0           1
8  2020-12-7     honda        1           2
9  2020-12-7     honda        2           1
'''

newcounts = dailysales.drop_duplicates().groupby(['date_id', 'make_name']).agg(
    {'lead_id': (lambda x: len(x.unique())),
     'partner_id': (lambda x: len(x.unique()))
     })

new_columns = ['unique_leads', 'unique_partners']
newcounts.columns = new_columns
print(newcounts.reset_index())