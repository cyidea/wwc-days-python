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

# Define a custom function to calculate the "best bargain"
def bargain_or_not(row):
    return row['Points'] / row['Price']

# Apply the custom function to create a new column 'bargain_rating'
wine_data['bargain_rating'] = wine_data.apply(bargain_or_not, axis=1)

# Print the updated dataframe
print(wine_data)

# Getting the best bargain wine's variety:
index_of_best_bargain = wine_data['bargain_rating'].idxmax()
print(wine_data.loc[index_of_best_bargain, 'Variety'])

"""
result will be like:

  Country    Region  Points  Price      Variety  bargain_rating
0  France  Bordeaux      87     15       Merlot        5.800000
1   Italy   Tuscany      95     65   Sangiovese        1.461538
2   Spain     Rioja      84     13  Tempranillo        6.461538
3  France  Burgundy      97     64   Pinot Noir        1.515625
4   Italy  Piedmont      85     14      Barbera        6.071429
Tempranillo
"""

