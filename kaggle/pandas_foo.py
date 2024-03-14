import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

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