import pandas as pd

# Create a sample wine data
data = {
    'Country': ['France', 'Italy', 'Spain', 'France', 'Italy'],
    'Region': ['Bordeaux', 'Tuscany', 'Rioja', 'Burgundy', 'Piedmont'],
    'Points': [87, 95, 84, 97, 85],
    'Price': [15, 65, 13, 64, 14],
    'Variety': ['Merlot', 'Sangiovese', 'Tempranillo', 'Pinot Noir', 'Barbera']
}

wine_data = pd.DataFrame(data)

# example 1: Define a custom function to calculate the "best bargain"
def quality_to_cost_ratio(row):
    return row['Points'] / row['Price']

# Apply the custom function to create a new column 'quality_to_cost'
wine_data['quality_to_cost'] = wine_data.apply(quality_to_cost_ratio, axis=1)

# Print the updated dataframe
print(wine_data)
print('\n')

# Getting the best bargain wine's variety:
best_quality_to_cost_index = wine_data['quality_to_cost'].idxmax()
print(wine_data.loc[best_quality_to_cost_index, 'Variety'])
print('\n')

# example 2: Define a custom function to calculate the rating (1, 2, 3)
#            based on the country and points
def cal_wine_rating(row):
    rating = 1
    if row['Country'] == 'France' or row['Points'] >= 95:
        rating = 3
    elif row['Points'] >= 85:
        rating = 2

    return rating

wine_data['rating'] = wine_data.apply(cal_wine_rating, axis=1)
print(wine_data)

"""
result will be like:

  Country    Region  Points  Price      Variety  quality_to_cost
0  France  Bordeaux      87     15       Merlot         5.800000
1   Italy   Tuscany      95     65   Sangiovese         1.461538
2   Spain     Rioja      84     13  Tempranillo         6.461538
3  France  Burgundy      97     64   Pinot Noir         1.515625
4   Italy  Piedmont      85     14      Barbera         6.071429

Tempranillo

  Country    Region  Points  Price      Variety  quality_to_cost  rating
0  France  Bordeaux      87     15       Merlot         5.800000       3
1   Italy   Tuscany      95     65   Sangiovese         1.461538       3
2   Spain     Rioja      84     13  Tempranillo         6.461538       1
3  France  Burgundy      97     64   Pinot Noir         1.515625       3
4   Italy  Piedmont      85     14      Barbera         6.071429       2

"""
print('\n')

# filtering using lambda:
high_rating_wines = wine_data[wine_data.apply(lambda row: row['rating'] > 2, axis=1)]

# keeping only three columns (to demonstrate keeping specific columns):
print(high_rating_wines[['Country', 'Variety', 'rating']])

'''
result:
  Country     Variety  rating
0  France      Merlot       3
1   Italy  Sangiovese       3
3  France  Pinot Noir       3
'''

# for simple filtering you don't need lambda:
high_rating_wines_2 = wine_data[wine_data['rating'] > 2]

print('\nhigh_rating_wines_2:')
# keeping only three columns (to demonstrate keeping specific columns):
print(high_rating_wines_2[['Country', 'Variety', 'rating']])

# special things with dealing with string types:
# it appears you have to create a seperate column to store 
# the intermediary results
# to only display the wines that Variety starts with letter M:
wine_data['variety_M'] = wine_data['Variety'].str.startswith('M')
print(wine_data[wine_data['Variety'].str.startswith('M')])

# and you can't do this:
wine_data[wine_data.apply(lambda row: row['Variety'].str.startswith('M'), axis=1)]

#here is the error you will get:
'''
AttributeError: 'str' object has no attribute 'str'
'''


# empty df case
df = pd.DataFrame(columns=['A', 'B', 'C'])

# Define the filtering conditions using a lambda function
condition = lambda row: row['A'] > 10 and row['B'] > 3

# Filter the DataFrame, select columns A and C
filtered_df = df[df.apply(condition, axis=1)]

# Check if the filtered DataFrame is empty
if filtered_df.empty:
    print("The filtered DataFrame is empty.")
else:
    print(filtered_df)