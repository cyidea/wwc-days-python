from itertools import count
import pandas as pd

# prepare the dataframe to be used:
# The scenario is a car dealership. 
# There is a lead who is probably a sales-person, 
# and there is the customer whom they call 'partner'.
# When a car sale is made (each row in the dataset) there is sale date and the car,
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
     date_id   make_name  lead_id  partner_id
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

# Now we are going to solve the problem of finding on a daily bases,
# for each kind of car, how many unique sales-person have made a deal,
# and how many unique customer bought the car.

# the chained-commands below is to (sequentially) do the following:
# get rid of duplicates, group by a double-column, 
# use agg to create two new columns (using dictionary).
# explanation of the agg:
# create two new columns based on the two existing columns 'lead_id' and 'partner_id'
# the lambda functions each deal with x which represents those columns' data.
# pay attention how the 'unique' is called on each of the x, it gets rid of the 
# duplicates in the columns' data themselves (pretty neat!)
newcounts = dailysales.drop_duplicates().groupby(['date_id', 'make_name']).agg(
    {'lead_id': (lambda x: len(x.unique())),
     'partner_id': (lambda x: len(x.unique()))
     })

# this following bit is to turn the double-column index back to default indexing.
# first we need to create the new column names for each of the columns in the agg
# then we call reset_index magic.
new_columns = ['unique_leads', 'unique_partners']
newcounts.columns = new_columns
print(newcounts.reset_index())

'''
result:
    date_id     make_name  unique_leads  unique_partners
0  2020-12-7     honda             3                2
1  2020-12-7    toyota             1                2
2  2020-12-8     honda             2                2
3  2020-12-8    toyota             2                3
'''