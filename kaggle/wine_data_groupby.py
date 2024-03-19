import pandas as pd

''' Here we are practicing groupby.
    Some of the groupby functionality can be achieved by value_counts.
'''

# Create a sample wine data
data = {
    'Country': ['France', 'Italy', 'Spain', 'France', 'Italy'],
    'Region': ['Bordeaux', 'Tuscany', 'Rioja', 'Burgundy', 'Piedmont'],
    'Points': [87, 95, 84, 97, 85],
    'Price': [15, 65, 13, 64, 14],
    'Variety': ['Merlot', 'Sangiovese', 'Tempranillo', 'Pinot Noir', 'Barbera'],
    'Reviewer': ['John', 'Emily', 'Michael', 'Sophia', 'John'],
}

wine_data = pd.DataFrame(data)

# create a series that is similar to what value_count does. 
# That is, give out the number of reviews each Reviewer has done 
# and put it in a Series.
# Remember that a Series takes the values and then the index names
reviewer_counts = wine_data.groupby('Reviewer').Reviewer.count()
sr = pd.Series(reviewer_counts.values, index=reviewer_counts.index)
print(sr)

'''
Here is what the result look like:

Reviewer
Emily      1
John       2
Michael    1
Sophia     1
dtype: int64
'''

