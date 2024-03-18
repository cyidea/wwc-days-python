# First, import pandas:
import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Map a function to a column:
df['A_squared'] = df['A'].map(lambda x: x**2)
print(df)

# Map with multiple columns
df['Sum'] = df.apply(lambda x: x['A']+x['B'], axis="columns")
print(df)

# If we want to 'center' the values of a column:
df['A_Centered'] = df['A'].map(lambda x: x-df.A.mean())
print(df)


"""
Here is the result:
   A   B  A_squared
0  1  10          1
1  2  20          4
2  3  30          9
3  4  40         16
4  5  50         25
   A   B  A_squared  Sum
0  1  10          1   11
1  2  20          4   22
2  3  30          9   33
3  4  40         16   44
4  5  50         25   55
   A   B  A_squared  Sum  A_Centered
0  1  10          1   11        -2.0
1  2  20          4   22        -1.0
2  3  30          9   33         0.0
3  4  40         16   44         1.0
4  5  50         25   55         2.0
"""

# # Find the index of the maximum value in column 'A'
# idx = df['A'].idxmax()
# print(idx)

# # give the value of the max on B column:
# idx = df['B'].idxmax()
# val = df.loc[idx, 'B']
# print(val)

# try lambda functions:
# n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
# n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
# descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])