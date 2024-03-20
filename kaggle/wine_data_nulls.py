import pandas as pd
import numpy as np

# Create a sample wine data 
data = {
    'Country': ['France', 'Italy', 'Spain', 'France', 'Italy', 'Spain'],
    'Region': ['Bordeaux', 'Tuscany', 'Rioja', 'Burgundy', 'Piedmont','Rioja'],
    'Points': [87, 95, 84, 97, 85, 89],
    'Price': [15, np.NaN, 13, 64, np.NaN, 13],
    'Variety': ['Merlot', 'Sangiovese', 'Tempranillo', 'Pinot Noir', 'Barbera', 
                'Tempranillo'],
    'Reviewer': ['John', 'Emily', 'Michael', 'Sophia', 'William','Michael'],
    'Vintage': [2010, 2012, 2015, 2013, 2011,2015],
    'Description': ['Fra - Bor - Mer', 'Ita - Tus - San', 'Spa - Rio - Tem', 
                    'Fra - Bur - Pin', 'Ita - Pie - Bar', 'Spa - Rio - Tem2']

}

wine_data = pd.DataFrame(data)

# Find rows with null values in the 'Price' column
null_rows = wine_data[wine_data['Price'].isnull()]

# Print the null rows
print(null_rows)
print(f'\nthere are {wine_data['Price'].isnull().sum()} null rows in the dataset')

"""
so far the result looks like:
  Country    Region  Points  Price     Variety Reviewer  Vintage      Description
1   Italy   Tuscany      95    NaN  Sangiovese    Emily     2012  Ita - Tus - San
4   Italy  Piedmont      85    NaN     Barbera  William     2011  Ita - Pie - Bar

there are 2 null rows in the dataset
"""

# replacing all the nulls with value 'Unknown':
print(wine_data.fillna('Unknown'))

"""
it should have this result:
  Country    Region  Points    Price      Variety Reviewer  Vintage       Description
0  France  Bordeaux      87     15.0       Merlot     John     2010   Fra - Bor - Mer
1   Italy   Tuscany      95  Unknown   Sangiovese    Emily     2012   Ita - Tus - San
2   Spain     Rioja      84     13.0  Tempranillo  Michael     2015   Spa - Rio - Tem
3  France  Burgundy      97     64.0   Pinot Noir   Sophia     2013   Fra - Bur - Pin
4   Italy  Piedmont      85  Unknown      Barbera  William     2011   Ita - Pie - Bar
5   Spain     Rioja      89     13.0  Tempranillo  Michael     2015  Spa - Rio - Tem2
"""

print('\n')
# Gotcha: but the original data are not changed:
print(wine_data)
"""
here is the result: (notice that the NaN are still there)
  Country    Region  Points  Price      Variety Reviewer  Vintage       Description
0  France  Bordeaux      87   15.0       Merlot     John     2010   Fra - Bor - Mer
1   Italy   Tuscany      95    NaN   Sangiovese    Emily     2012   Ita - Tus - San
2   Spain     Rioja      84   13.0  Tempranillo  Michael     2015   Spa - Rio - Tem
3  France  Burgundy      97   64.0   Pinot Noir   Sophia     2013   Fra - Bur - Pin
4   Italy  Piedmont      85    NaN      Barbera  William     2011   Ita - Pie - Bar
5   Spain     Rioja      89   13.0  Tempranillo  Michael     2015  Spa - Rio - Tem2
"""

