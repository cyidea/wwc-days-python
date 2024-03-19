import pandas as pd

# Create a sample wine data 
data = {
    'Country': ['France', 'Italy', 'Spain', 'France', 'Italy', 'Spain'],
    'Region': ['Bordeaux', 'Tuscany', 'Rioja', 'Burgundy', 'Piedmont','Rioja'],
    'Points': [87, 95, 84, 97, 85, 89],
    'Price': [15, 65, 13, 64, 14, 13],
    'Variety': ['Merlot', 'Sangiovese', 'Tempranillo', 'Pinot Noir', 'Barbera', 
                'Tempranillo'],
    'Reviewer': ['John', 'Emily', 'Michael', 'Sophia', 'William','Michael'],
    'Vintage': [2010, 2012, 2015, 2013, 2011,2015],
    'Description': ['Fra - Bor - Mer', 'Ita - Tus - San', 'Spa - Rio - Tem', 
                    'Fra - Bur - Pin', 'Ita - Pie - Bar', 'Spa - Rio - Tem2']

}

wine_data = pd.DataFrame(data)

# Calculate the average price per country and region using groupby and mean
average_price=wine_data.groupby(['Country', 'Region']).Price.mean()

# Print the average price per country and region
print(average_price)

"""
result:

Country  Region  
France   Bordeaux    15.0
         Burgundy    64.0
Italy    Piedmont    14.0
         Tuscany     65.0
Spain    Rioja       13.0
Name: Price, dtype: float64

"""

# what is the best wine I can buy for a given amount of money?
# create a series whose index is wine prices and whose values is
# the maximum number of points a wine costing that much was given 
# in a review.
best_wines_for_price = wine_data.groupby(['Price']).Points.max()
print(best_wines_for_price)

"""
Price
13    89
14    85
15    87
64    97
65    95
Name: Points, dtype: int64
"""

# What are the minimum and maximum prices for each variety of wine? 
# Create a DataFrame whose index is the variety category 
# from the dataset and whose values are the min and max values thereof.
variety_prices = wine_data.groupby(['Variety']).Price.agg(['min', 'max'])
print(variety_prices)

"""
             min  max
Variety              
Barbera       14   14
Merlot        15   15
Pinot Noir    64   64
Sangiovese    65   65
Tempranillo   13   13
"""

# What are the most expensive wine varieties? 
# Create a variable sorted_varieties where varieties 
# are sorted in descending order based on minimum price, 
# then on maximum price (to break ties).
sorted_varieties = variety_prices.sort_values(['min', 'max'], ascending=False)
print(sorted_varieties)

"""
result:
Variety              
Sangiovese    65   65
Pinot Noir    64   64
Merlot        15   15
Barbera       14   14
Tempranillo   13   13
"""

# Create a `Series` whose index is reviewers and whose values is 
# the average review score given out by that reviewer. 

reviewer_mean_ratings = wine_data.groupby('Reviewer').Points.mean()
print(reviewer_mean_ratings)

"""
result:
Reviewer
Emily      95.0
John       87.0
Michael    86.5
Sophia     97.0
William    85.0
Name: Points, dtype: float64
"""
